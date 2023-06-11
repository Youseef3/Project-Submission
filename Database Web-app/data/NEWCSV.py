import pandas as pd

#We extract the attributes that we want to work with
df = pd.read_csv('countries-of-the-world.csv')

columns_to_keep = ['Country', 'Population', 'GDP ($ per capita)', ]
df = df[columns_to_keep]

df.to_csv('modified_data.csv', index=False)
