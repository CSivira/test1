struct Vector3D {
    Vector3D();

    Vector3D(int _x, int _y, int _z);

    Vector3D(float _x, float _y, float _z);

    Vector3D(double _x, double _y, double _z);
    
    Vector3D operator+(Vector3D const& v);

    Vector3D operator+(double const& v);

    Vector3D operator-(Vector3D const& v);

    Vector3D operator-(double const& v);

    Vector3D operator*(Vector3D const& v);

    Vector3D operator*(double const& v);
    
    double operator%(Vector3D const& v);
    
    double operator&();

    void print();
    

    ~Vector3D();

    double x, y, z;
};