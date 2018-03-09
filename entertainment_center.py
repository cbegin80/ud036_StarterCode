import fresh_tomatoes
import media

# create a list of movies with titles, posters, and trailer video links

fellowship_of_the_ring = media.Movie("The Lord of the Rings: Fellowship of "
    "the Ring",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=Pki6jbSbXIY")

two_towers = media.Movie("The Lord of the Rings: The Two Towers",
    "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",  # noqa
    "https://www.youtube.com/watch?v=2dlRvAjU_RI")

return_of_the_king = media.Movie("The Lord of the Rings: The Return of the "
    "King",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",  # noqa
    "https://www.youtube.com/watch?v=WIrRJ8bCZYQ")

star_trek_2009 = media.Movie("Star Trek (2009)",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
    "https://www.youtube.com/watch?v=SyJszxnJydA")

shawshank_redemption = media.Movie("The Shawshank Redemption",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

o_brother = media.Movie("The Greatest Showman",
    "https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png",  # noqa
    "https://www.youtube.com/watch?v=AXCTMGYUg9A")

movies = [fellowship_of_the_ring, two_towers, return_of_the_king,
    star_trek_2009, shawshank_redemption, o_brother]

# build and display web page using Fresh Tomatoes

fresh_tomatoes.open_movies_page(movies)
