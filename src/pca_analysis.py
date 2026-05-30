from sklearn.decomposition import PCA


def apply_pca(data):
    pca = PCA(n_components=2)

    pca_result = pca.fit_transform(data)

    return pca_result