__author__ = 'gogasca'

import media
import fresh_tomatoes

the_godfather = media.Movie('The Godfather',
                        'American mafia is born',
                        'http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg',
                        'https://www.youtube.com/watch?v=vjPmaneLadQ')

avatar = media.Movie('Avatar',
                     'A marine on alien planet',
                     'http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

trainspotting = media.Movie('Trainspotting',
                            'Crazy life',
                            'http://upload.wikimedia.org/wikipedia/en/7/71/Trainspotting_ver2.jpg',
                            'https://www.youtube.com/watch?v=Sl6O7sad9hI')
amelie = media.Movie('Amelie',
                     'Le fabuleux destin d Amelie Poulain',
                     'http://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg',
                     'https://www.youtube.com/watch?v=B-uxeZaM-VM')

movies = [the_godfather,avatar,trainspotting,amelie]
fresh_tomatoes.open_movies_page(movies)
