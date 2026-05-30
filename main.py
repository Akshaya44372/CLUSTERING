from src.data_preprocessing import load_and_preprocess_data
from src.clustering import (
    find_optimal_clusters,
    perform_clustering
)
from src.pca_analysis import apply_pca
from src.visualization import (
    plot_customer_clusters,
    plot_pca_clusters
)
from src.rfm_analysis import create_cluster_report


def main():

    print("Project Started...")

    file_path = "dataset/Mall_Customers.csv"

    # Load data
    df, scaled_data = load_and_preprocess_data(file_path)

    print("Data Loaded Successfully")

    # Elbow Method
    find_optimal_clusters(scaled_data)

    # Clustering
    clusters = perform_clustering(scaled_data)

    df["Cluster"] = clusters

    # PCA
    pca_result = apply_pca(scaled_data)

    # Visualization
    plot_customer_clusters(df)
    plot_pca_clusters(pca_result, clusters)

    # Report
    report = create_cluster_report(df)

    report.to_csv(
        "outputs/cluster_report.csv",
        index=True
    )

    print("Project Executed Successfully!")


if __name__ == "__main__":
    main()