import pandas as pd

df = pd.read_csv('../data/sample_data.csv')

# Simple transformation
df['performance'] = df['score'].apply(lambda x: 'Good' if x > 75 else 'Needs Improvement')

df.to_csv('../data/processed_data.csv', index=False)

print("Data processed successfully")
