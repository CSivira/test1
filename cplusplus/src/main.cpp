#include "vector3D.hpp"
#include <iostream>

int main() {

    Vector3D a(1, 2, 3), b(4, 5, 6), c(7, 8, 9), r;
    double s;

    r = b + c;
    std::cout << "b + c = ";
    r.print();
    r = a * b + c;
    std::cout << "a * b + c = "; 
    r.print();
    r = (b + b) * (c - a);
    std::cout << "(b + b) * (c - a) = ";  
    r.print();
    r = b + 3;
    std::cout << "b + 3 = "; 
    r.print();
    r = a * 3.0 + &b;
    std::cout << "a * 3.0 + &b = "; 
    r.print();
    r = (b + b) * (c % a);
    std::cout << "(b + b) * (c % a) = ";
    r.print();

    return 0;
}