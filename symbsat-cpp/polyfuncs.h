#pragma once

template <typename PolyType>
PolyType spoly(const PolyType &f, const PolyType &g) {
    auto f_lm = f.lm();
    auto g_lm = g.lm();
    auto lcm = f_lm*g_lm;

    PolyType spoly;
    spoly = f*(lcm/f_lm) + g*(lcm/g_lm);

    return spoly;
}

template <typename PolyType>
PolyType normalform(const PolyType &f, const std::vector<PolyType> &F) {
    PolyType p(f), r;

    if (F.empty()) {
        return p;
    }

    while (!p.isZero()) {
        unsigned int i {0};
        bool divisionoccured {false};
        auto p_lm = p.lm();
        while (i < F.size() && !divisionoccured) {
            auto fi_lm = F[i].lm();
            if (p_lm.isdivisible(fi_lm)) {
                p = p + F[i]*(p_lm/fi_lm);
                divisionoccured = true;
            } else {
                i++;
            }
            //std::cout << p << "\n";
        }
        if (!divisionoccured) {
            r = r + PolyType(p_lm);
            p = p + PolyType(p_lm);
        }
    }
    return r;
}
