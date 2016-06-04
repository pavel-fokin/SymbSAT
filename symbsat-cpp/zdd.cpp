#include "zdd.h"

// TODO need to review for correctness
bool ZDD::operator==(const ZDD& rhs) const {

    if (this == &rhs) {
        return true;
    }

    MonomConstIterator it1(*this), it2(rhs);

    while (!it1 || !it2) {
        if ( !(it1.monom() == it2.monom()) ) {
            return false;
        }
        ++it1;
        ++it2;
    }

    // TODO should be used || or ^ ?
    if (!it1 ^ !it2) {
        return false;
    }

    return true;
}

const ZDD::Node* ZDD::add(const Node* i, const Node* j) {
    if ( i->isZero() ) {
        return copy(j);
    } else if ( j->isZero() ) {
        return copy(i);
    // } else if (i == j) {
    } else if (ZDD::Node::isEqual(i, j)) {
        // return 0
        return mZero;
    } else if ( i->isOne() ) {
        return create_node(
            j->mVar, copy(j->mMul),
            add(j->mAdd, mOne)
        );
    } else if ( j->isOne() ) {
        return create_node(
            i->mVar, copy(i->mMul),
            add(i->mAdd, mOne)
        );
    } else {
        if (i->mVar < j->mVar) {
            return create_node(
                i->mVar, copy(i->mMul), add(i->mAdd, j)
            );
        } else if (i->mVar > j->mVar) {
            return create_node(
                // j->mVar, copy(j->mMul), add(j->mAdd, i)
                j->mVar, j->mMul, add(i, j->mAdd)
            );
        } else {
            auto m = add(i->mMul, j->mMul);
            auto a = add(i->mAdd, j->mAdd);

            if (m->isZero()) {
                return a;
            }

            return create_node(i->mVar, m, a);
        }
    }
}

const ZDD::Node* ZDD::mul(const Node* i, const Node* j) {
    if ( i->isOne() ) {
        return copy(j);
    } else if ( i->isZero() || j->isZero() ) {
        // return 0
        return mZero;
    // } else if ( j->isOne() || i == j ) {
    } else if ( j->isOne() || ZDD::Node::isEqual(i, j) ) {
        return copy(i);
    } else {
        if (i->mVar < j->mVar) {
            auto m = mul(i->mMul, j);
            auto a = mul(i->mAdd, j);

            if (m->isZero()) {
                return a;
            }

            return create_node(i->mVar, m, a);
        } else if (i->mVar > j->mVar) {
            auto m = mul(j->mMul, i);
            auto a = mul(j->mAdd, i);

            if (m->isZero()) {
                return a;
            }

            return create_node(j->mVar, m, a);
        } else {
            auto m1 = mul(i->mAdd, j->mMul);
            auto m2 = mul(i->mMul, j->mMul);
            auto m3 = mul(i->mMul, j->mAdd);
            auto m = add(m1, add(m2, m3));

            if (m->isZero()) {
                return mul(i->mAdd, j->mAdd);
            }

            return create_node(
                i->mVar, m,
                mul(i->mAdd, j->mAdd)
            );
        }
    }
}

ZDD ZDD::operator+(const ZDD& rhs) const {
    ZDD tmp(*this);
    tmp.mRoot = tmp.add(mRoot, rhs.mRoot);
    return tmp;
}

ZDD ZDD::operator*(const ZDD& rhs) const {
    ZDD tmp(*this);
    tmp.mRoot = tmp.mul(mRoot, rhs.mRoot);
    return tmp;
}

void ZDD::MonomConstIterator::operator++() {
    while(!mPath.empty() && (mPath.top()->mAdd->isZero())) {
        mPath.pop();
        mMonom.erase(std::begin(mMonom));
    }
    if (!mPath.empty()) {
        const Node *i=mPath.top()->mAdd;
        mPath.pop();
        mMonom.erase(std::begin(mMonom));
        for ( ; !i->isOne(); i = i->mMul) {
            mPath.push(i);
            mMonom.push_back(i->mVar);
        }
    }
}

std::ostream& operator<<(std::ostream& out, const ZDD::Node* a) {
    if (a->isZero()) {
        out << "_zero";
    } else if (a->isOne()) {
        out << "_one";
    } else {
        out << a->mVar << " -> {" << a->mMul << "} {" << a->mAdd << "} ";
    }

    return out;
}

std::ostream& operator<<(std::ostream& out, const ZDD &a) {
    ZDD::MonomConstIterator it(a);

    if (a.isZero()) {
        out << "0";
    } else if (a.isOne()) {
        out << "1";
    } else {
        while(!it) {
            out << it.monom() << " ";
            ++it;
        }
    }
    return out;
}
