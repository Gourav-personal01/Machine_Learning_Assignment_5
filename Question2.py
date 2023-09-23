# Q2. What is nominal encoding? Provide an example of how you would use it in a real-world scenario.

# Answer - 
# Nominal encoding is used to convert the categorical data to numberical data without any order such that our machine learning models can use that.

# Example -

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({
    'color' : ['red','blue','green','green','red','blue']
})

print(df)

# Create an instance of one hot encoder

encoder = OneHotEncoder()

# fit the encoder to the dataframe and transform the categorical variable 
encoded = encoder.fit_transform(df[['color']])

print(encoded)