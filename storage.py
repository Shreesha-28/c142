import csv

all_movies= []

with open ('final.csv', 'r', encoding = 'utf-8') as f:
    reader_data = csv.reader (f)
    data = list (reader_data)
    all_movies=data[1:]

liked_movies = []
unliked_movies = []
did_not_watch = []
