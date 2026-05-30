import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def find_optimal_clusters(data):

    os.makedirs("outputs", exist_ok=True)

    inertia = []
    K = range(1, 11)

    for k in K:
        kmeans = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        kmeans.fit(data)
        inertia.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(K, inertia, marker="o")

    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.title("Elbow Method")

    plt.savefig("./outputs/elbow_method.png")

    plt.close()


def perform_clustering(data):

    kmeans = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(data)

    return clusters