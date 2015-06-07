Movie Trailer Website:
This project renders a dynamically generated html page with movie posters and hyperlinks to their trailers on youtube.
Currently, there are three movies - "How to train your dragon", "Ratatouille", "Ice Age"

To run this project:
Install Python. (Preferably 3.4)
Navigate in to the movie_website directory.
Run python .\entertainment_center.py

Implementation details:
The python class "Movies" implemented in media.py file stores the movie title, poster URL, storyline and a YouTube link to the movie trailer.
Multiple instances of this Python Class are created in entertainment_center.py to represent three movies.
These instances are put into a list called "movies" and passed to the fresh_tomatoes.open_movies_page() method
In fresh_tomatoes.py there is a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all the movies