import numpy as np

A = np.array([[0.45, 0.3, 0.2], [0.2, 0.25, 0.4], [0.3, 0.35, 0.3]])

B = np.linalg.inv(np.eye(3) - A)

SUM = np.eye(3)
A_N = np.eye(3)

i = 0

while True:
    i += 1
    A_N = A_N @ A
    SUM += A_N
    if np.max(np.abs(SUM-B)) < 1e-2:
        print(f"Converged on step {i}")
        break