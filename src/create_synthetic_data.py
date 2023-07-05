import pandas as pd
import numpy as np
from faker import Faker

# Initialize a Faker object
fake = Faker()

# Set a random seed for reproducibility
np.random.seed(123)

# List of specific words
specific_words = ["groceries", "rent", "refund", "reimbursement", "dining", "shopping", "credit", "debit"]

# Generate random transaction descriptions
transaction_descriptions = []
for _ in range(100):
    sentence = fake.sentence(nb_words=5).split()
    if np.random.rand() < 0.5:  # 50% chance to inject a specific word
        position = np.random.randint(len(sentence))  # choose a random position
        sentence[position] = np.random.choice(specific_words)  # replace a word at this position
    transaction_descriptions.append(' '.join(sentence))

# Remove the period at the end of each description
transaction_descriptions = [desc.rstrip('.') for desc in transaction_descriptions]

# Generate random transaction amounts
transaction_amounts = np.random.choice(
    [45, 50, 23.45, 78.12, 56.78, 12.34, 89.56, 34.12],
    size=100
)

# Combine descriptions and amounts into a DataFrame
transactions = pd.DataFrame({
    "Description": transaction_descriptions,
    "Amount": transaction_amounts
})

# Output the DataFrame to a CSV file
transactions.to_csv('./data/transactions.csv', index=False)
