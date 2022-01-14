#include <fstream>
#include <iostream>
#include <sstream>

#include "monom.h"
#include "order.h"
#include "poly.h"
#include "zdd.h"
#include "gb.h"

using namespace symbsat;

typedef Monom<32, DegRevLex> Monom32;
typedef Poly<Monom32> PolyN;
typedef std::unordered_map<std::string, PolyN> Vars;

PolyN parseMonom(const Vars V, std::string monom) {
    PolyN m; m.setOne();

    std::stack<std::string> tokens;

    for (std::string::size_type i = 0; i < monom.size(); i++) {
        if (monom[i] == '*') {
            continue;
        } else if (monom[i] == 'x') {
            std::string var;
            while (monom[i] != '+' && monom[i] != '*' && i < monom.length()) {
                var += monom[i];
                i++;
            }
            tokens.push(var);
            i--;
        }
    }

    while (!tokens.empty()) {
        std::string var = tokens.top();
        tokens.pop();
        m *= V.at(var);
    }

    return m;
}

int main (int argc, char *argv[]) {
    std::ifstream cnf(argv[1]);

    std::cout << "gnv-file - '" << argv[1] << "'" << std::endl;

    std::string vars;
    std::getline(cnf, vars);
    vars.erase(std::find(vars.begin(), vars.end(), ';'));

    std::istringstream buf;
    buf.str(vars);

    Vars V;

    std::string var;
    int count = 0;
    while (getline(buf, var, ',')) {
        V[var] = PolyN(count);
        count++;
    }

    std::string polys;
    getline(cnf, polys, ';');
    polys.erase(std::find(polys.begin(), polys.end(), ';'));

    std::istringstream buf2;
    buf2.str(polys);

    std::vector<PolyN> P;

    std::string poly;
    while (getline(buf2, poly, ',')) {

        PolyN p;

        std::istringstream buf3;
        buf3.str(poly);

        std::string monom;
        while (getline(buf3, monom, '+')) {
            PolyN m = parseMonom(V, monom);
            p += m;
        }

        P.push_back(p);
    }

    cnf.close();

    for (auto&& p: P) {
        std::cout << p << std::endl;
    }

    auto G = buchberger(P, V.size());

    std::cout << std::endl;
    for (auto&& p: G) {
        std::cout << p << std::endl;
    }
}
