#include "vector3D.hpp"
#include <iostream>

int main() {

    Vector3D a(1, 2, 3), b(4, 5, 6), c(7, 8, 9), r;
    double s;

    s = &a;
    std::cout << s << std::endl;

    return 0;
}