#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef unsigned long long ull;

int nqueens(ull i, ull n);
ull factorial(ull n);

int main(int argc, char* argv[]) {
    ull i = 0, n = 0, total = 0;
    double start_time, end_time;

    if (argc != 2) {
        printf("Invalid number of command line arguments.\nFormat should be ./nqueens <n>\n\n");
        return 1;
    }

    n = atoi(argv[1]);
    start_time = clock();

    ull max = factorial(n);
    for (i = 0; i < max; i++) {
        total += nqueens(i, n);
    }

    end_time = clock();

    printf("The execution time is %g sec\n", (end_time - start_time) / CLOCKS_PER_SEC);
    printf("Total number of solutions found: %llu\n\n", total);
    return 0;
}

int nqueens(ull i, ull n) {
    int a, b = 0;
    int* fact = (int*)calloc(n, sizeof(int));
    int* perm = (int*)calloc(n, sizeof(int));

    fact[b] = 1;
    while (++b < (int)n) {
        fact[b] = fact[b - 1] * b;
    }

    for (b = 0; b < (int)n; ++b) {
        perm[b] = i / fact[n - 1 - b];
        i = i % fact[n - 1 - b];
    }

    for (b = n - 1; b > 0; --b) {
        for (a = b - 1; a >= 0; --a) {
            if (perm[a] <= perm[b]) {
                perm[b]++;
            }
        }
    }
    free(fact);

    for (ull j = 0; j < n; j++) {
        int val = perm[j];

        for (int k = j + 1, dist = 1; k < (int)n; k++, dist++) {
            if (val - dist == perm[k] || val + dist == perm[k]) {
                free(perm);
                return 0;
            }
        }

        for (int k = j - 1, dist = 1; k >= 0; k--, dist++) {
            if (val - dist == perm[k] || val + dist == perm[k]) {
                free(perm);
                return 0;
            }
        }
    }

    free(perm);
    return 1;
}

ull factorial(ull n) {
    return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}
