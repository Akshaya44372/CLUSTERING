import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_and_preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Convert Gender to numerical
    encoder = LabelEncoder()
    df["Gender"] = encoder.fit_transform(df["Gender"])

    # Select features
    features = df[
        ["Gender", "Age",
         "Annual Income (k$)",
         "Spending Score (1-100)"]
    ]

    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    return df, scaled_features