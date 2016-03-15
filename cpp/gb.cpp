#include "gb.h"

std::vector<Poly> autoreduce(std::vector<Poly>& F) {
    std::vector<Poly> G(F);
    std::vector<Poly> P;

    while (!G.empty()) {
        Poly h = G.back();
        G.pop_back();
        h = normalform(h, P);
        if (!h.isZero()) {
            for (auto& q: P) {
                if (q.lm().isdivisible(h.lm())) {
                    G.push_back(q);
                    // P.erase(q);
                }
            }
        }
    }

    return G;
}

std::vector<Poly> buchberger(std::vector<Poly>& F) {
    std::vector<Poly> G {F};
    std::vector<std::tuple<int, int>> pairs;

    // std::cout << std::endl;
    int num_vars{4};

    int k = G.size();
    for (int i=-num_vars; i<k; ++i) 
        for (int j=0; j<k; ++j) 
            if (i<j) {
                // std::cout << i  << " " << j << std::endl;
                pairs.push_back(std::make_tuple(i, j));
            }

    std::reverse(pairs.begin(), pairs.end());

    std::cout << std::endl;
    while (!pairs.empty()) {
        Poly s, h;
        int i, j;

        std::tie(i, j) = pairs.back();
        pairs.pop_back();
        std::cout << i  << " " << j << std::endl;

        if (i<0) {
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
    
    return G;
}