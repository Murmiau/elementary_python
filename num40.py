import pandas as pd

df = pd.read_csv('/content/sample_data/california_housing_train.csv')

df.head()

df.dtypes

df.isnull().sum()

print(df[df['population'] < 500]['median_house_value'].mean())
print(round(df[df['population'] < 500]['median_house_value'].mean()))
print(df[df['population'] == df['population'].min()]['households'].max())
