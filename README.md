# Market & Customer Segmentation using Machine Learning

## Project Overview

This project performs **Market & Customer Segmentation** using **Machine Learning (K-Means Clustering)** on the **Mall Customers Dataset**.

The goal of this project is to group customers based on their:

* Gender
* Age
* Annual Income
* Spending Score

This helps businesses understand customer behavior and create **targeted marketing strategies**.

---

## Features

* Data preprocessing
* Customer segmentation using **K-Means Clustering**
* **Elbow Method** to find optimal clusters
* **PCA (Principal Component Analysis)** for dimensionality reduction
* Cluster visualization using graphs
* Customer cluster profiling report

---

## Project Structure

```text
Market_Customer_Segmentation/
│
├── dataset/
│   └── Mall_Customers.csv
│
├── outputs/
│   ├── elbow_method.png
│   ├── customer_clusters.png
│   ├── pca_clusters.png
│   └── cluster_report.csv
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── rfm_analysis.py
│   ├── pca_analysis.py
│   ├── clustering.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* PCA
* K-Means Clustering

---

## Dataset

Dataset contains customer information:

| Column Name            | Description             |
| ---------------------- | ----------------------- |
| CustomerID             | Unique customer ID      |
| Gender                 | Male/Female             |
| Age                    | Customer age            |
| Annual Income (k$)     | Yearly income           |
| Spending Score (1-100) | Customer spending score |

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 2. Navigate to project folder

```bash
cd Market_Customer_Segmentation
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

---

## Run the Project

Run the following command:

```bash
python main.py
```

Successful execution message:

```text
Project Started...
Data Loaded Successfully
Project Executed Successfully!
```

---

## Output Files

After running the project, the following files are generated inside the `outputs/` folder:

### 1. Elbow Method Graph

**File:** `elbow_method.png`

Used to determine the optimal number of customer clusters.

---

### 2. Customer Cluster Visualization

**File:** `customer_clusters.png`

Shows customer groups based on:

* Annual Income
* Spending Score

Different colors represent different customer segments.

---

### 3. PCA Cluster Visualization

**File:** `pca_clusters.png`

Visualizes customer segments using **Principal Component Analysis (PCA)**.

---

### 4. Cluster Report

**File:** `cluster_report.csv`

Contains average values of each customer segment.

Example:

| Cluster | Age | Income | Spending Score |
| ------- | --- | ------ | -------------- |
| 0       | 28  | 60     | 75             |
| 1       | 45  | 30     | 20             |

---

## Machine Learning Concepts Used

### K-Means Clustering

Used to group customers into similar segments.

### Elbow Method

Used to find the best number of clusters.

### PCA (Principal Component Analysis)

Used for dimensionality reduction and visualization.

---

## Future Improvements

* Add Streamlit Web App
* Better customer profiling
* Real-time dashboard
* Interactive visualizations
* Advanced customer recommendation system

---

## Author

**Sushma Munagala**

Machine Learning & Software Development Enthusiast
