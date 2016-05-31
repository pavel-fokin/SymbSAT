#ifndef GB_H
#define GB_H

#include "poly.h"

std::vector<Poly> autoreduce(const std::vector<Poly>&);
std::vector<Poly> buchberger(const std::vector<Poly>&, const int);

#endif // GB_H
