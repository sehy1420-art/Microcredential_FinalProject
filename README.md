# Customer Segmentation using K-Means Clustering

## Overview

This project explores the relationship between raw customer behavior (purchase frequency and basket size) and overall customer value. We use the K-Means Clustering algorithm to see if it can naturally identify high-value customers without being explicitly told their total spend.

## Hypothesis

"In retail customer segmentation, the K-means algorithm will naturally group customers into clusters that correlate with their 'Total Spend', even if the algorithm is only provided with behavioral features like frequency and average basket size."

## Dataset

We use the UCI Online Retail Dataset, which contains transactional data from a UK-based online retailer.

- Size: ~541,000 rows.
- Key Features Used: InvoiceNo, Quantity, UnitPrice, and CustomerID.

"In retail customer segmentation, the K-means algorithm will naturally group customers into clusters that correlate with their 'Value Score' (Total Spend), even if the algorithm is only provided with raw behavioral data like purchase frequency and average basket size."

To test this, we use the Online Retail Dataset (available via the UCI Machine Learning Repository). It contains transactional data for a UK-based non-store online retail company.

- Key Features: Quantity, UnitPrice, CustomerID, and InvoiceDate.
- Goal: Engineer features for Frequency, Recency, and Monetary value (RFM) to see how K-means clusters them.
