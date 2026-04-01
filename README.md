# $K$-Means Clustering Algorithm in Graph Machine Learning

The topic of this project of the Research Data Foundations Camp final project is related to graph machine learning, specifically known as the $K$-means clustering algorithm. The $K$-means clustering algorithm is an unsupervised machine learning algorithm that partitions a dataset into $K$ distinct, non-overlapping clusters. It is an iterative algorithm that assigns data points to the nearest centroid (mean) and updating centroids to minimize within-cluster sum of squared errors (distance). Namely, the algorithm steps are as follows:

1. **Initialization:** choose $K$ initial centroids (means) of the sample randomly;
2. **Assigning:** Assign each data point to the closest centroid with respect to the Euclidean distance;
3. **Update:** Calculate the new centroid for each cluster;
4. **Iteration:** Iterate 2 and 3 ultil centroids no longer change (convergence).

# 1. Question and Hypothesis

Typical $K$-means clustering deals with the set of "points", but we could go and ask the following question: "what if we have a set of "networks", or "graphs" instead of points? Formally, a graph is a tuple $G=(V,E)$, consisting of a set $V$ of nodes (entities) and a set $E$ of edges (relationship). Graphs are commonly used in data modelling because they intuitively represent complex, highly connected real-world relationships, unlike tabulated data. Both nodes and edges in a graph enable fast, efficient interpretation of real-world data.

Suppose we have graphs $G_1, G_2,\cdots, G_N$, then typical distances, such as Euclidean distance or $L^p$-distance, does not measure how close two graphs are in the $K$-means clustering. Therefore, we need a notion of distance between graphs to determine how close two graphs are in the $K$-means clustering. There are several graph distances proposed in the past literature, but I will focus on using the Wasserstein metric in my project.

Measuring a distance between graphs is extremely difficult, because there is no "intituive" way of forming such a distance. For example, if the Euclidean distance between nodes in two graphs is large, does it mean two graphs are far away from each other?
