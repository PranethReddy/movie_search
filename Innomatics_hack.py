#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data1=pd.read_csv('Downloads/movie_data/movies.csv')


# In[4]:


print(data1.shape)


# In[5]:


data2=pd.read_csv('Downloads/movie_data/ratings.csv')


# In[6]:


print(data2.shape)


# In[8]:


unique_user_ids = data2['userId'].nunique()
print(unique_user_ids)


# In[11]:


ratings_count = data2['movieId'].value_counts()
max_mo_rat = ratings_count.idxmax()
max_rat_titl = data1[data1['movieId'] == max_mo_rat]['title'].values[0]
print(max_rat_titl)


# In[13]:


data3 = pd.read_csv('Downloads/movie_data/tags.csv')

matrix_movie_id = data1[data1['title'] == "Matrix, The (1999)"]['movieId'].values[0]
matrix_tags = data3[data3['movieId'] == matrix_movie_id]['tag'].unique()
print(matrix_tags)


# In[14]:


terminator_movie_id = data1[data1['title'] == "Terminator 2: Judgment Day (1991)"]['movieId'].values[0]
terminator_avg_rating = data2[data2['movieId'] == terminator_movie_id]['rating'].mean()
print(terminator_avg_rating)


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


fight_club_movie_id = data1[data1['title'] == "Fight Club (1999)"]['movieId'].values[0]
fight_club_ratings = data2[data2['movieId'] == fight_club_movie_id]['rating']
plt.hist(fight_club_ratings, bins=10, edgecolor='black')
plt.title("Distribution of User Ratings for 'Fight Club (1999)'")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()


# In[18]:


import pandas as pd



grouped_ratings = data2.groupby('movieId').agg(count=('rating', 'count'), mean=('rating', 'mean')).reset_index()

print(grouped_ratings.head())


# In[19]:


merged_df = pd.merge(data1, grouped_ratings, on='movieId', how='inner')

print(merged_df.head())


# In[20]:


filtered_df = merged_df[merged_df['count'] > 50]

print(filtered_df.head())


# In[21]:


mpv = filtered_df.loc[filtered_df['mean'].idxmax()]

print(mpv)


# In[22]:


top_5_movies = filtered_df.sort_values(by='count', ascending=False).head(5)

print(top_5_movies[['title', 'count']])


# In[23]:


sci_fi = filtered_df[filtered_df['genres'].str.contains('Sci-Fi')]

tmp = sci_fi.sort_values(by='count', ascending=False).iloc[2]

print(tmp)


# In[25]:


data4 = pd.read_csv('Downloads/movie_data/links.csv')

fil_link = pd.merge(filtered_df, data4, on='movieId', how='inner')

print(fil_link.head())


# In[27]:


movies = pd.read_csv('Downloads/movie_data/movies.csv')
ratings = pd.read_csv('Downloads/movie_data/ratings.csv')
ratings_scrapped = pd.read_csv('ratingscrapped.csv')

movies_ratings = pd.merge(movies, ratings_scrapped, on='movieId')

ratings_count = ratings.groupby('movieId').size().reset_index(name='count')

popular_movies = pd.merge(movies_ratings, ratings_count, on='movieId')
popular_movies = popular_movies[popular_movies['count'] > 50]

highest_imdb_movie = popular_movies.loc[popular_movies['Imdb_ratings'].idxmax()]

sci_fi_movies = popular_movies[popular_movies['genres'].str.contains('Sci-Fi', na=False)]
highest_imdb_sci_fi_movie = sci_fi_movies.loc[sci_fi_movies['Imdb_ratings'].idxmax()]

print("Movie with the highest IMDB rating:")
print(highest_imdb_movie[['movieId', 'title', 'Imdb_ratings']])

print("\nSci-Fi movie with the highest IMDB rating:")
print(highest_imdb_sci_fi_movie[['movieId', 'title', 'Imdb_ratings']])


# In[ ]:




