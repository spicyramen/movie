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
                                'http://bit.ly/1u2LOBu',
                                'https://www.youtube.com/watch?v=vjPmaneLadQ')

    """

    def __init__(self, title, storyline, poster_image, trailer_video):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_video

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
