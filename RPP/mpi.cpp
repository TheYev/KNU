#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

typedef unsigned long long ull;

int nqueens(int proc, ull i, ull n);
ull factorial(ull n);

int main(int argc, char* argv[]) {
    int rnk, sze;
    ull i = 0, n = 0, total = 0, subtot = 0;
    double elapsed_time;

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rnk);
    MPI_Comm_size(MPI_COMM_WORLD, &sze);

    MPI_Barrier(MPI_COMM_WORLD);
    elapsed_time = -MPI_Wtime();

    if (argc != 2) {
        if (rnk == 0)
            printf("Invalid number of command line arguments.\nFormat should be ./nqueens <n>\n\n");
    }
    else {
        n = atoi(argv[1]);

        ull max = factorial(n);

        for (i = rnk; i < max; i += sze) {
            subtot += nqueens(rnk, i, n);
        }

        MPI_Reduce(&subtot, &total, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    }

    MPI_Barrier(MPI_COMM_WORLD);
    elapsed_time += MPI_Wtime();

    if (0 == rnk) {
        printf("Program executed in %g sec\n", elapsed_time);
        printf("Total number of solutions found: %llu\n\n", total);
        fflush(stdout);
    }

    MPI_Finalize();
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
