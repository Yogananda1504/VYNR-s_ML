# Why Split Before Scaling

Separating data into training and testing sets first prevents information leakage. If the scaler is fitted on the entire dataset, statistical measures (e.g., mean, standard deviation) would include information from the test set, biasing performance estimates. By splitting first, each dataset is processed only with the statistics derived from the training set, keeping future data unseen and ensuring a fair model evaluation.

# Feature Scaling Explained

Scaling adjusts the range of your features, often by standardizing or normalizing them. This helps many algorithms converge faster and avoid giving undue importance to larger-valued features.

### Simple Example

1. Suppose you have a feature with values [0, 1, 2, 3] in your training set.  
2. The mean is 1.5 and the standard deviation is about 1.118.  
3. Standardizing:  
    - For the value 3:  
      (3 - 1.5) / 1.118 ≈ 1.34  

Applying the same scaler to the test data prevents data snooping and maintains consistency.
