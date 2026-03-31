# $K$-Means Clustering Algorithm in Graph Machine Learning

The topic of this project of the Research Data Foundations Camp final project is related to graph machine learning, specifically known as the $K$-means clustering algorithm. The $K$-means clustering algorithm is an unsupervised machine learning algorithm that partitions a dataset into $K$ distinct, non-overlapping clusters. It is an iterative algorithm that assigns data points to the nearest centroid (mean) and updating centroids to minimize within-cluster sum of squared errors (distance). Namely, the algorithm steps are as follows:

* Step 1 (Initialization): choose $K$ initial centroids (means) of the sample randomly;
* Step 2 (Assigning): Assign each data point to the closest centroid with respect to the Euclidean distance;
* Step 3 (Update): Calculate the new centroid for each cluster;
* Step 4 (Iteration): Iterate Step 2 and 3 ultil centroids no longer change (convergence).
