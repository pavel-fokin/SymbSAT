#pragma once

#include <algorithm>
// #include <iostream>
#include <iterator>
#include <memory>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <stack>

#include "monom.h"


class ZDD {

    struct Node {
        int mVar;
        const Node* mMul; // and
        const Node* mAdd; // xor

        Node () =delete;
        Node (const Node& n) =delete;
        Node (const Node&& n) =delete;
        Node& operator=(const Node&) =delete;
        Node& operator=(const Node&&) =delete;

        Node (int var, const Node* mul, const Node* add):
            mVar(var), mMul(mul), mAdd(add) {}

        inline bool isZero() const {
            return mVar == -2;
        }
        inline bool isOne() const {
            return mVar == -1;
        }

        static bool isEqual(const Node* a, const Node* b) {
            if (a->mVar != b->mVar) {
                return false;
            } else if (a->isZero() && b->isZero()) {
                return true;
            } else if (a->isOne() && b->isOne()) {
                return true;
            } else {
                return isEqual(a->mAdd, b->mAdd) && isEqual(a->mMul, b->mMul);
            }
        }
    };

    const Node* mRoot;
    std::vector<Node*> mNodes;

    const Node* mOne = create_node(-1, nullptr, nullptr);
    const Node* mZero = create_node(-2, nullptr, nullptr);

    inline const Node* create_node(int var, const Node* mul, const Node* add) {
        Node* tmp = new Node(var, mul, add);
        mNodes.push_back(tmp);
        return tmp;
    }

    const Node* copy(const Node* n) {
        if (n->mVar < 0) {
            return n;
        } else {
            return create_node(n->mVar, copy(n->mMul), copy(n->mAdd));
        }
    }

    friend std::ostream& operator<<(std::ostream& out, const Node *a);

    const Node* add(const Node* a, const Node* b);
    const Node* mul(const Node* a, const Node* b);

public:

    ZDD() {
        // mRoot = create_node(-2, nullptr, nullptr); // zero
        mRoot = mZero;
    }
    ZDD(const ZDD& z) {
        mRoot = copy(z.mRoot);
    }
    ZDD(const ZDD&& z) {
        mRoot = copy(z.mRoot);
    }
    ZDD& operator=(const ZDD& other) {
        if (this != &other) {
            mRoot = copy(other.mRoot);
        }
        return *this;
    }
    ZDD& operator=(const ZDD&& other) {
        if (this != &other) {
            mRoot = copy(other.mRoot);
        }
        return *this;
    }
    ~ZDD() {
        std::for_each(
            std::begin(mNodes), std::end(mNodes),
            [](Node* n) {
                delete n;
            }
        );
    }

    explicit ZDD(int var) {
        mRoot = create_node(var, mOne, mZero);
    }
    explicit ZDD(const Monom& m);

    inline bool isZero() const {
        return mRoot->isZero();
    }
    inline bool isOne() const {
        return mRoot->isOne();
    }
    inline void setZero() {
        mRoot = mZero;
    }
    inline void setOne() {
        mRoot = mOne;
    }

    Monom lm() const;

    bool operator==(const ZDD& rhs) const;

    ZDD operator+(const ZDD& rhs) const;
    ZDD operator+(const Monom& rhs) const;

    ZDD operator*(const ZDD& rhs) const;
    ZDD operator*(const Monom& rhs) const;

    class MonomConstIterator {
        std::vector<int> mMonom;
        std::stack<const Node*> mPath;
    public:
        explicit MonomConstIterator(const ZDD& z) {
            for (const Node* i=z.mRoot; i->mVar >= 0; i = i->mMul) {
                mPath.push(i);
                mMonom.push_back(i->mVar);
            }
        };
        ~MonomConstIterator () =default;

        const Monom monom() const {
            Monom tmp;
            for (auto& i: mMonom) {
                // zero-bit indicates 0/1
                tmp.setVar(i+1);
            }
            return tmp;
        }

        operator bool () const {
            return mPath.empty();
        }
        void operator++();
    };

    friend std::ostream& operator<<(std::ostream& out, const ZDD &a);
};

ZDD spoly(const ZDD&, const ZDD&);
ZDD normalform(const ZDD&, const std::vector<ZDD>&);
