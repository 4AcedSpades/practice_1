movies = [ 
    ("The Matrix", 1999), 
    ("Avatar", 2009), 
    ("Jurassic Park", 1993), 
    ("Avengers: Endgame", 2019), 
    ("Inception", 2010), 
    ("Titanic", 1997) 
]

sorted_movies = sorted(movies, key = lambda s: s[1], reverse=True)

print(list(sorted_movies))