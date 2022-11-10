import numpy as np
import pandas as pd

df = pd.read_csv('articles.csv')

index = df['index']

q_articles = index.sort_values('index', ascending=False)
output = q_articles[['index']].head(20).values.tolist()