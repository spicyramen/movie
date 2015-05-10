import media
import fresh_tomatoes

"""Movie definition
   media.Movie contains Title, Story Line, Poster Image,Trailer in Youtube
   From Movie class: (movie_title, movie_storyline,
   poster_image,trailer_youtube)"""

godfather = media.Movie('The Godfather',
                        'American mafia is born',
                        'http://bit.ly/1u2LOBu',
                        'https://www.youtube.com/watch?v=vjPmaneLadQ')

avatar = media.Movie('Avatar',
                     'A marine on alien planet',
                     'http://bit.ly/1F6nt8g',
                     'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

trainspotting = media.Movie('Trainspotting',
                            'Crazy life',
                            'http://bit.ly/1Jzbujd',
                            'https://www.youtube.com/watch?v=Sl6O7sad9hI')

amelie = media.Movie('Amelie',
                     'Le fabuleux destin d Amelie Poulain',
                     'http://bit.ly/1xMfTfw',
                     'https://www.youtube.com/watch?v=B-uxeZaM-VM')

# We create an array of movies
movies = [godfather, avatar, trainspotting, amelie]

# Pass Movies array so it will be display in our web page by fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
