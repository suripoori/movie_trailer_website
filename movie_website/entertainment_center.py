__author__ = 'Suraj'

# Import the media file which contains the Movies class
import media
# Import the fresh_tomatoes file which implements the open_movies_page method
import fresh_tomatoes

# Create a movies list which are going to be present on the web page
movies = []

# Add "How to train your dragon" to the list of movies
movies.append(media.Movie("How to train your dragon", "Story of a viking who trains dragons",
                    "http://upload.wikimedia.org/wikipedia/en/a/af/How_to_Train_Your_Dragon_2_poster.jpg",
                    "https://www.youtube.com/watch?v=oKiYuIsPxYk"))

# Add "Ratatouille" to the list of movies
movies.append(media.Movie("Ratatouille", "Story of a mouse who wants to be a chef",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk"))

# Add "Ice Age" to the list of movies
movies.append(media.Movie("Ice Age", "Story of a mammoth, a sabertooth, and a sloth during the ice age",
                          "http://upload.wikimedia.org/wikipedia/en/a/a9/Ice_Age.jpg",
                          "https://www.youtube.com/watch?v=cMfeWyVBidk"))

# Render a movies page with the list of movies which were created above.
# The open_movies_page method calls the create_movie_tiles_content method which generates the html page
# It then opens the page in a web browser.
fresh_tomatoes.open_movies_page(movies)


