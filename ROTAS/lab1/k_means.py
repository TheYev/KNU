import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


def generate_data():
    dataset = []
    for i in range(30):
        dataset.append([random.randint(20, 30), random.randint(40, 60)])
    for i in range(30):
        dataset.append([random.randint(50, 70), random.randint(10, 20)])
    for i in range(30):
        dataset.append([random.randint(35, 45), random.randint(55, 65)])
    for i in range(50):
        dataset.append([random.randint(30, 50), random.randint(30, 40)])
    return dataset


if __name__ == '__main__':
    dataset = generate_data()
    plt.scatter([data[0] for data in dataset], [data[1] for data in dataset])
    plt.show()

    scores = []
    for i in range(2, 7):
        kmeans = KMeans(n_clusters=i, n_init=10)
        kmeans.fit(dataset)
        y_kmeans = kmeans.predict(dataset)
        scores.append(kmeans.score(dataset))

    plt.plot(range(2, 7), scores)
    plt.xticks(range(2, 7))
    plt.show()

    kmeans = KMeans(n_clusters=4, n_init=10)
    kmeans.fit(dataset)
    y_kmeans = kmeans.predict(dataset)
    plt.scatter([data[0] for data in dataset], [data[1] for data in dataset], c=y_kmeans, s=50, cmap='viridis')
    plt.show()