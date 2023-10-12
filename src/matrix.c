#include "matrix.h"

void mMult(int n, int** A, int** R) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            R[i][j] = 0;
            for (int k = 0; k < n; k++) R[i][j] += A[i][k] * A[j][k];
            R[j][i] = R[i][j];
        }
    }
}

void printMatrix(int n, int** M, int t, int g) {
    for (int i = 0; i < n; i++) {
        printf("    ");
        for (int j = 0; j < n; j++) {
            if (g == 1) M[i][j] = rand() % 9;
            if (t == 1) printf("%d ", M[j][i]);
            else  printf("%d ", M[i][j]);
        }
        printf("\n");
    }
}