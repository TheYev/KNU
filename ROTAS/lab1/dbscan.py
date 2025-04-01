import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

if __name__ == '__main__':
    dataset = make_moons(n_samples=200, noise=0.06, random_state=0)
    plt.scatter([data[0] for data in dataset[0]], [data[1] for data in dataset[0]])
    plt.show()

    dbscan = DBSCAN(eps=0.1, min_samples=5)
    dbscan.fit(dataset[0])
    y_dbscan = dbscan.labels_
    plt.scatter([data[0] for data in dataset[0]], [data[1] for data in dataset[0]], c=y_dbscan, s=50, cmap='viridis')
    plt.show()

    dbscan = DBSCAN(eps=0.2, min_samples=2)
    dbscan.fit(dataset[0])
    y_dbscan = dbscan.labels_
    plt.scatter([data[0] for data in dataset[0]], [data[1] for data in dataset[0]], c=y_dbscan, s=50, cmap='viridis')
    plt.show()