import numpy as np;
import pandas as pd;
from sklearn.feature_extraction.text import CountVectorizer;
from sklearn.metrics.pairwise import cosine_similarity;

df = pd.read_csv('articles.csv')

count = CountVectorizer(stop_words = 'english')
count_matrix = count.fit_transform(df['title'])

similarity = cosine_similarity(count_matrix, count_matrix)

df = df.reset_index()

indices = pd.Series(df.index, index = df['contentId'])

print(indices)

def get_recommendations(title, cosine_sim):
    index = indices[title]
    sim_scores = list(enumerate(cosine_sim[index]))
    sim_scores = sorted(sim_scores, key = lambda x:x[1], reverse = True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[article_indices]