#include "vector3D.hpp"

#include <cmath>
#include <iostream>

Vector3D::Vector3D() { }

Vector3D::Vector3D(int _x, int _y, int _z) { x = _x; y = _y; z = _z; }

Vector3D::Vector3D(float _x, float _y, float _z) { x = _x; y = _y; z = _z; }

Vector3D::Vector3D(double _x, double _y, double _z) { x = _x; y = _y; z = _z; }

Vector3D Vector3D::operator+(Vector3D const& v) { 
    return Vector3D(x + v.x, y + v.y, z + v.z); 
}

Vector3D Vector3D::operator+(double const& s) { 
    return Vector3D(x + s, y + s, z + s); 
}

Vector3D Vector3D::operator-(Vector3D const& v) { 
    return Vector3D(x - v.x, y - v.y, z - v.z); 
}

Vector3D Vector3D::operator-(double const& s) { 
    return Vector3D(x - s, y - s, z - s); 
}

Vector3D Vector3D::operator*(Vector3D const& v) { 
    return Vector3D(y * v.z - z * v.y,
                    z * v.x - x * v.z,
                    x * v.y - y * v.x); 
}

Vector3D Vector3D::operator*(double const& s) { 
    return Vector3D(x * s, y * s, z * s); 
}

double Vector3D::operator%(Vector3D const& v) { 
    return x * v.x + y * v.y + z * v.z; 
}

double Vector3D::operator&() { 
    return std::sqrt(std::pow(x, 2) + std::pow(y, 2) + std::pow(z, 2));
}

void Vector3D::print() {
    std::cout << "(" << x << ", " << y << ", " << z << ")" << std::endl;
}

Vector3D::~Vector3D() {};