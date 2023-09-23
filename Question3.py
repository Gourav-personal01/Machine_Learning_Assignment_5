# Q3. In what situations is nominal encoding preferred over one-hot encoding? Provide a practical example.

# Answer - 

# Nominal encoding (label encoding) is preferred over one-hot encoding when dealing with categorical features with a large number of unique categories. 
# It helps reduce the dimensionality of the dataset, making it more manageable and efficient.

# Example: When encoding "Country" in a dataset with hundreds of unique countries, nominal encoding assigns a unique integer to 
# each country (e.g., USA: 1, Canada: 2), while one-hot encoding would create hundreds of binary columns, 
# leading to a high-dimensional dataset.