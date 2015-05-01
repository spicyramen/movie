__author__ = 'gogasca'
import webbrowser

class Movie():
    """This class creates a Movie instance and provides a way to save Movie information"""
    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self,movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Will play movie using Youtube trailer property
    def show_trailer(self):
        if self.trailer_youtube_url != None:
            webbrowser.open(self.trailer_youtube_url,new=2)
        else:
            return "Trailer property not defined"

    # Return story line text
    def __str__(self):
        if self.storyline != None:
            return self.storyline
        else:
            return "Storyline property not defined"
    