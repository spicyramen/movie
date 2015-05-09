import webbrowser

# Class Movie will store the information for each movie created in
# entertainment center


class Movie():
    """This class creates a Movie instance and provides a way to save Movie information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """ We initialize class with title, storyline, image and youtube trailer URL
     Example:
     the_godfather = media.Movie('The Godfather',
                                'American mafia is born',
                                'http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg',
                                'https://www.youtube.com/watch?v=vjPmaneLadQ')

    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Will play movie using Youtube trailer property in web page
    def show_trailer(self):
        if self.trailer_youtube_url is not None:
            webbrowser.open(self.trailer_youtube_url, new=2)
        else:
            return "Trailer property not defined"

    # Return story line as text
    def __str__(self):
        if self.storyline is not None:
            return self.storyline
        else:
            return "Storyline property not defined"
