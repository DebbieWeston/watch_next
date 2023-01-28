# T38 Compulsory Task 2 - watch_next.py

import spacy

nlp = spacy.load('en_core_web_md')

def get_available_movies():

    # Initialize variables, keyed by movie name.

    """ Set filepath to get inventory.txt.
    Using vs code, filepath uses explicit path.
    Using PyCharm, directory not required.
    """
    # filepath = "./T38/movies.txt"
    filepath = "movies.txt"

    # Make dictionary of movies, keyed by movie name.
    available_movies = {}

    # Read in values from movies.txt and populate available_movies dictionary.
    try:
        with open(filepath, "r") as movies:
            for content in (movies):
                content = content.strip("\n")
                content = (content.split(" :"))
                available_movies[content[0]] = content[1]               
    except IOError:
        print("No movies.txt file found") 
    return(available_movies) 

def compare_to_current_viewing(model_description, available_movies):

    best_similarity = 0
    best_match = ""
    for movie in available_movies:
        similarity = nlp(available_movies[movie]).similarity(model_description)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = movie

    return(best_match)


all_available_movies = get_available_movies()

current_viewing = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

model_description = nlp(current_viewing)

print(f"""Best matching movie is {compare_to_current_viewing(model_description, 
        all_available_movies)}""")
