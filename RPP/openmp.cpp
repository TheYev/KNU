#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#include <omp.h>

typedef unsigned long long ull;

int nqueens(int proc, ull i, ull n);
ull factorial(ull n);


int main(int argc, char* argv[]) {

    ull i = 0, n = 0, total = 0;
    double start_time, end_time;
    int num_workers;

    start_time = omp_get_wtime();

    if (argc != 3) {
        printf("Invalid number of command line arguments.\nFormat should be ./nqueens <n>\n\n");
    }
    else {
        n = atoi(argv[1]);
        num_workers = atoi(argv[2]);
        omp_set_num_threads(num_workers);

        ull max = factorial(n);

#pragma omp parallel for
        for (i = 0; i < max; i++) {
            int res = nqueens(0, i, n);
#pragma omp atomic
            total += res;
        }
    }

    end_time = omp_get_wtime();

    printf("The execution time is %g sec\n", end_time - start_time);
    printf("Total number of solutions found: %llu\n\n", total);
    fflush(stdout);
    return 0;
}

int nqueens(int proc, ull i, ull n) {
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
