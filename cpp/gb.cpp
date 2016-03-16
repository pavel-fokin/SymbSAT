#include "gb.h"

std::vector<Poly> autoreduce(const std::vector<Poly>& F) {
    std::vector<Poly> G(F);
    std::vector<Poly> P;

    while (!G.empty()) {
        Poly h = G.back();
        G.pop_back();
        h = normalform(h, P);
        if (!h.isZero()) {
            auto itP = P.begin();
            while ( itP != P.end() ) {
                if ((*itP).lm().isdivisible(h.lm())) {
                    G.push_back(*itP);
                    P.erase(itP);
                } else {
                    ++itP;
                }
            }
            P.push_back(h);
        }
    }

    int PSize = P.size();
    for (int i=0; i<PSize; ++i) {
        Poly h = P.front();
        P.erase(P.begin());
        h = normalform(h, P);
        if (h.isZero()) {
            --PSize;
        } else {
            P.push_back(h);
        }
    }
    G = std::move(P);
    return G;
}

std::vector<Poly> buchberger(const std::vector<Poly>& F, const int num_vars) {
    std::vector<Poly> G;
    std::vector<std::tuple<int, int>> pairs;

    G = autoreduce(F);

    int k = G.size();
    for (int i=-num_vars; i<k; ++i)
        for (int j=0; j<k; ++j)
            if (i<j) {
                pairs.push_back(std::make_tuple(i, j));
            }

    // std::cout << std::endl;
    while (!pairs.empty()) {
        Poly s, h;
        int i, j;

        std::tie(i, j) = pairs.front();
        pairs.erase(pairs.begin());
        // std::cout << i  << " " << j << std::endl;

        if (i < 0) {
            Monom Gj_lm = G[j].lm(), xi(std::abs(i));
            if (Gj_lm.isrelativelyprime(xi))
                continue;
            s = G[j]*xi;
        } else {
            Poly p = G[i], q = G[j];
            if (p.lm().isrelativelyprime(q.lm()))
                continue;
            s = spoly(p, q);
        }

        h = normalform(s, G);
        if (!h.isZero()) {
            G.push_back(h);
            ++k;
            for (int i=-num_vars; i<k-1; ++i) {
                pairs.push_back(std::make_tuple(i, k-1));
            }
        }
    }

    G = autoreduce(G);

    return G;
}
