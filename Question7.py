# Q7.You are working on a project that involves predicting customer churn for a telecommunications
# company. You have a dataset with 5 features, including the customer's gender, age, contract type,
# monthly charges, and tenure. Which encoding technique(s) would you use to transform the categorical
# data into numerical data? Provide a step-by-step explanation of how you would implement the encoding.

# Answer - 

# Here are the steps:

# Perform label encoding for the "gender" column, which will replace "Male" with 0 and "Female" with 1.

# Apply one-hot encoding to the "contract type" column, creating three binary columns, one for each contract type (e.g., "Month-to-Month," "One Year," "Two Year"). The binary columns will have values of 0 or 1, indicating the contract type for each customer.

# After these encoding steps, your dataset will con