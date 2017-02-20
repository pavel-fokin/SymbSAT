template <typename PolyType>
PolyType spoly(const PolyType &f, const PolyType &g) {
    auto f_lm = f.lm();
    auto g_lm = g.lm();
    auto lcm = f_lm*g_lm;

    PolyType spoly;
    spoly = f*(lcm/f_lm) + g*(lcm/g_lm);

    return spoly;
}
