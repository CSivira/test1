#include "rotate.h"

char* rotar(char* w, int k) {
    int l = strlen(w);
    if (l == 0 || k == 0) return w;

    char* r = malloc((l + 1) * sizeof(char));
    if (!r) return "";

    for (int i = 0; i < l; i++) r[i] = w[(k + i) % l];

    r[l] = '\0';
    return r;
}