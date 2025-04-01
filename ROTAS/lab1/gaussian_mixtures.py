from matplotlib.colors import LogNorm
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

if __name__ == '__main__':
    X1, y1 = make_blobs(n_samples=1000, centers=((4, -4), (0, 0)), random_state=42)
    X1 = X1.dot(np.array([[0.374, 0.95], [0.732, 0.598]]))
    X2, y2 = make_blobs(n_samples=250, centers=1, random_state=42)
    X2 = X2 + [6, -8]
    X = np.r_[X1, X2]

    plt.scatter(X[:, 0], X[:, 1], s=10)
    plt.show()

    gm = GaussianMixture(n_components=3, n_init=10)
    gm.fit(X)
    print(gm.weights_)
    print(gm.means_)

    res = gm.sample(100)

    plt.scatter(X[:, 0], X[:, 1], s=10)
    plt.scatter(res[0][:, 0], res[0][:, 1], s=100, marker='x')
    plt.show()