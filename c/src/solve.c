#include "solve.h"
#include "rotate.h"
#include "matrix.h"

#include <time.h>

void p1b1() {
    printf("I. Calcular la rotación de k posiciones de una cadena w \n");

    char* w = "hola mundo!";
    int k = 10;

    printf("\nw = %s\n", w);
    printf("k = [0,...,%d)\n\n", k);

    char* test;
    for (int i = 0; i < k; i++) {
        test = rotar(w, i);
        printf("rotar(\"%s\", %i) = \"%s\"\n", w, i, test);
        if (test != w) free(test);
    }
}

void p1b2() {
    printf("II. Dada una matriz cuadrada A, calcular el producto A x A_t \n");

    srand(time(NULL));

    int n = 10;
    int** A = malloc(n * sizeof(int*));
    int** R = malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        A[i] = malloc(n * sizeof(int));
        R[i] = malloc(n * sizeof(int));
    }

    // Generate random A
    printf("\nn = %d\nA = \n", n);
    printMatrix(n, A, 0, 1);

    // Show A_t
    printf("\nA_t = \n", n);
    printMatrix(n, A, 1, 0);

    mMult(n, A, R); 

    // Show R
    printf("\n A x A_t = \n");
    printMatrix(n, R, 0, 0);

    free(A);
    free(R);
}