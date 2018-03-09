class Movie():
    def __init__(self, movie_title, movie_poster, trailer_link):
        # the movie title
        self.title = movie_title
        # the URL for the movie's poster image
        self.poster_image_url = movie_poster
        # the URL for the movie's YouTube trailer
        self.trailer_youtube_url = trailer_link
