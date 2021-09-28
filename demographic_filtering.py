import pandas as pd
import numpy as np

df = pd.read_csv ('final.csv')
C=df2['vote_average'].mean()
print(C)

m=df2['vote_count'].quantile(0.9)
print(m)

q_movies=df2.copy().loc[df2['vote_count']>=m]
print(q_movies.shape)

def weighted_rating(x,m=m,C=C):
  v=x['vote_count']
  R=x['vote_average']
  return (v/(v+m)*R) + (m/(v+m)*C)
q_movies['score'] = q_movies.apply(weighted_rating, axis = 1)

q_movies = q_movies.sort_values('score', ascending = False)
output = q_movies[['original_title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(10).values.tolist()

