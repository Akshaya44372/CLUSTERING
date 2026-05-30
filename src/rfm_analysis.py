import pandas as pd


def create_cluster_report(df):
    report = df.groupby("Cluster").mean()

    return report