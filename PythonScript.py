import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load Real Dataset
# Note: You can also use a local path if you downloaded 'Online Retail.xlsx'
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
df_raw = pd.read_excel(url)

# 2. Data Cleaning (Essential for K-Means)
# Remove rows without CustomerID and filter out returns (negative quantities)
df_clean = df_raw.dropna(subset=['CustomerID'])
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]

# 3. Feature Engineering: Group by Customer to create Behavioral Data
# We calculate Frequency and Average Basket Size per customer
customer_df = df_clean.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',           # Frequency: Number of unique visits
    'Quantity': 'sum',                # Total items bought
    'UnitPrice': 'mean'               # Average price of items (Basket Size proxy)
}).reset_index()

customer_df.columns = ['CustomerID', 'Frequency', 'AvgBasket', 'TotalItems']
# Calculate TotalSpend for evaluation (the 'hidden' truth)
customer_df['TotalSpend'] = df_clean.groupby('CustomerID').apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum()).values

# 4. Preprocessing for K-Means
features = ['Frequency', 'AvgBasket']
X = customer_df[features]

# K-means is distance-based; scaling is mandatory
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. K-Means Clustering (k=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
customer_df['Cluster'] = kmeans.fit_predict(X_scaled)

# 6. Evaluation against Total Spend
summary = customer_df.groupby('Cluster')['TotalSpend'].agg(['mean', 'count']).sort_values(by='mean')
print("Cluster Analysis against Real Total Spend:")
print(summary)

# 7. Visualization
plt.figure(figsize=(10, 6))
for i in range(3):
    clustered_data = customer_df[customer_df['Cluster'] == i]
    plt.scatter(clustered_data['Frequency'], clustered_data['AvgBasket'], alpha=0.6, label=f'Cluster {i}')

plt.title('K-Means on Real Online Retail Data')
plt.xlabel('Frequency (Total Visits)')
plt.ylabel('Avg Basket Price ($)')
plt.legend()
plt.show()

