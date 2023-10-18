#include "vector3D.hpp"

#include <cmath>
#include <gtest/gtest.h>

TEST(Vector3DTest, AdditionVector) {
    Vector3D v1(1.0, 2.0, 3.0);
    Vector3D v2(4.0, 5.0, 6.0);
    Vector3D result = v1 + v2;
    EXPECT_EQ(result.x, 5.0);
    EXPECT_EQ(result.y, 7.0);
    EXPECT_EQ(result.z, 9.0);
}

TEST(Vector3DTest, AdditionScalar) {
    Vector3D v(1.0, 2.0, 3.0);
    Vector3D result = v + 1.0;
    EXPECT_EQ(result.x, 2.0);
    EXPECT_EQ(result.y, 3.0);
    EXPECT_EQ(result.z, 4.0);
}

TEST(Vector3DTest, SubtractionVector) {
    Vector3D v1(4.0, 5.0, 6.0);
    Vector3D v2(1.0, 2.0, 3.0);
    Vector3D result = v1 - v2;
    EXPECT_EQ(result.x, 3.0);
    EXPECT_EQ(result.y, 3.0);
    EXPECT_EQ(result.z, 3.0);
}

TEST(Vector3DTest, SubtractionScalar) {
    Vector3D v(4.0, 5.0, 6.0);
    Vector3D result = v - 1.0;
    EXPECT_EQ(result.x, 3.0);
    EXPECT_EQ(result.y, 4.0);
    EXPECT_EQ(result.z, 5.0);
}

TEST(Vector3DTest, MultiplicationVector) {
    Vector3D v1(1.0, -7.0, 1.0);
    Vector3D v2(5.0, 2.0, -2.0);
    Vector3D result = v1 * v2;
    EXPECT_EQ(result.x, 12.0);
    EXPECT_EQ(result.y, 7.0);
    EXPECT_EQ(result.z, 37.0);
}

TEST(Vector3DTest, MultiplicationScalar) {
    Vector3D v(1.0, -7.0, 1.0);
    Vector3D result = v * 2;
    EXPECT_EQ(result.x, 2.0);
    EXPECT_EQ(result.y, -14.0);
    EXPECT_EQ(result.z, 2.0);
}

TEST(Vector3DTest, DotProduct) {
    Vector3D v1(1.0, -7.0, 1.);
    Vector3D v2(5., 2., -2.);
    double result = v1 % v2;
    EXPECT_DOUBLE_EQ(result,-11.);
}

TEST(Vector3DTest,Magnitude){
   Vector3D v(1.,-7.,1.);
   double result = &v;
   EXPECT_DOUBLE_EQ(result,std::sqrt(51));
}