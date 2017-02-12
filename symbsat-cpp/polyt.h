#pragma once

#include <algorithm>
#include <initializer_list>
#include <unordered_set>
#include <vector>

#include "monomt.h"

namespace symbsat {

template <typename MonomT> class Poly {
  std::vector<MonomT> mMonoms;

public:
  Poly() = default;
  ~Poly() = default;
  explicit Poly(MonomT &m) : mMonoms{m} {}
  explicit Poly(std::initializer_list<MonomT> monoms) : mMonoms(monoms) {
    std::sort(mMonoms.begin(), mMonoms.end());
  }
  explicit Poly(std::vector<MonomT> &monoms) : mMonoms(monoms) {
    std::sort(mMonoms.begin(), mMonoms.end());
  }
  Poly(const Poly &other) : mMonoms(other.mMonoms) {}
  Poly &operator=(const Poly &other) {
    if (this != &other) {
      mMonoms = other.mMonoms;
    }
    return *this;
  }
  Poly(const Poly &&other) noexcept : mMonoms(std::move(other.mMonoms)) {}
  Poly &operator=(Poly &&other) noexcept {
    if (this != &other) {
      mMonoms = std::move(other.mMonoms);
    }
    return *this;
  }

  bool isZero() const { return mMonoms.empty(); }
  bool isOne() const { return mMonoms.size() == 1 && mMonoms[0].isOne(); }

  MonomT lm() const {
    if (isZero()) {
      return MonomT();
    }
    return mMonoms.back();
  };

  Poly &operator+=(const Poly &b) {
    std::vector<MonomT> monoms;
    std::set_symmetric_difference(mMonoms.begin(), mMonoms.end(),
                                  b.mMonoms.begin(), b.mMonoms.end(),
                                  std::back_inserter(monoms));

    mMonoms = monoms;
    return *this;
  }
  friend Poly operator+(Poly lhs, const Poly &rhs) {
    lhs += rhs;
    return lhs;
  }

  Poly &operator*=(const Poly &b) {
    if (isZero() || b.isZero()) {
      mMonoms.clear();
      return *this;
    }
    std::unordered_set<MonomT, typename MonomT::hash> monoms_set;

    for (auto &m1 : mMonoms) {
      for (auto &m2 : b.mMonoms) {
        MonomT tmp(m1 * m2);
        if (monoms_set.find(tmp) == monoms_set.end()) {
          monoms_set.insert(tmp);
        } else {
          monoms_set.erase(tmp);
        }
      }
    }

    std::vector<MonomT> monoms_vec(std::begin(monoms_set),
                                   std::end(monoms_set));

    mMonoms = monoms_vec;
    std::sort(mMonoms.begin(), mMonoms.end());

    return *this;
  }
  friend Poly operator*(Poly lhs, const Poly &rhs) {
    lhs *= rhs;
    return lhs;
  }
  Poly &operator*=(const MonomT &b) {
    if (isZero() || b.isZero()) {
      mMonoms.clear();
      return *this;
    }
    std::unordered_set<MonomT, typename MonomT::hash> monoms_set;

    for (auto& m: mMonoms) {
        MonomT tmp(m*b);

        if (monoms_set.find(tmp) == monoms_set.end()) {
            monoms_set.insert(tmp);
        } else {
            monoms_set.erase(tmp);
        }
    }

    std::vector<MonomT> monoms_vec(std::begin(monoms_set),
                                   std::end(monoms_set));

    mMonoms = monoms_vec;
    std::sort(mMonoms.begin(), mMonoms.end());

    return *this;
  }
  friend Poly operator*(Poly lhs, const MonomT &rhs) {
    lhs *= rhs;
    return lhs;
  }

  friend std::ostream &operator<<(std::ostream &out, const Poly &a) {
    if (a.isZero()) {
      out << "0";
    } else if (a.isOne()) {
      out << "1";
    } else {
      auto monoms(a.mMonoms);
      std::reverse(monoms.begin(), monoms.end());
      for (auto &m : monoms) {
        out << m << " ";
      }
    }
    return out;
  }
  std::string toStr() const {
    std::ostringstream s;
    s << *this;
    return s.str();
  }
};

}; // namespace symbsat
