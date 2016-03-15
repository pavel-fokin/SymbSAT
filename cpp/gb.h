#ifndef GB_H
#define GB_H

#include "poly.h"

std::vector<Poly> autoreduce(std::vector<Poly>&);
std::vector<Poly> buchberger(std::vector<Poly>&);

#endif // GB_H
