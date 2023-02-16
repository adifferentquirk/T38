# Import Libraries
import spacy
nlp = spacy.load('en_core_web_md')

# Planet Hulk Description
description = """
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk 
into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on
the planet Sakaar where he is sold into slavery and trained as a gladiator."""

description = nlp(description)

# Opens movie.txt files
with open("movies.txt","r") as movies:
    # Sets initial values
    similarity = 0
    recommended_movie = ""

    movies = movies.readlines()
    # Makes text file readable
    for movie in movies:
        movie = movie.strip()
        # Splits into Movie Name and Description
        movie = movie.split(":")
        # Compares description to Planet Hulk Description
        movie_comparison = nlp(movie[1])
        movie_similarity = description.similarity(movie_comparison)
        # Keeps track of which film has the highest similarity
        if movie_similarity > similarity:
            similarity = movie_similarity
            recommended_movie = movie[0]

    # Displays the most recommended film
    print(f"Your next recommended movie is {recommended_movie}")
