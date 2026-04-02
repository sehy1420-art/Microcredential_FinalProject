import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load Dataset (Simulated snippet of UCI Online Retail data)
# For a real run, use: data = pd.read_csv('OnlineRetail.csv', encoding='ISO-8859-1')
np.random.seed(42)
data_size = 500
df = pd.DataFrame({
    'CustomerID': range(1, data_size + 1),
    'Frequency': np.random.poisson(5, data_size), # Number of purchases
    'AvgBasket': np.random.uniform(10, 500, data_size), # Avg spent per visit
})
df['TotalSpend'] = df['Frequency'] * df['AvgBasket']

# 2. Preprocessing
# We only give K-means 'Frequency' and 'AvgBasket' (Not TotalSpend)
features = ['Frequency', 'AvgBasket']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. K-Means Clustering (k=3 for Low, Medium, High value)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 4. Evaluation: Compare Clusters against the hidden 'TotalSpend'
summary = df.groupby('Cluster')['TotalSpend'].agg(['mean', 'std', 'min', 'max']).sort_values(by='mean')
print("Cluster Analysis against Total Spend:")
print(summary)

# 5. Visualization
plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green']
for i in range(3):
    clustered_data = df[df['Cluster'] == i]
    plt.scatter(clustered_data['Frequency'], clustered_data['AvgBasket'], 
                label=f'Cluster {i} (Avg Spend: ${clustered_data["TotalSpend"].mean():.2f})')

plt.title('K-Means Clustering: Purchase Frequency vs Avg Basket Size')
plt.xlabel('Frequency (Number of Purchases)')
plt.ylabel('Average Basket Size ($)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
