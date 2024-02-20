max_rating = -float('inf')
min_rating = float('inf')

max_rating_movie = ''
min_rating_movie = ''

total_ratings = 0
numbers_of_movies = int(input())

for _ in range(numbers_of_movies):
    movie_name = input()
    movie_rating = float(input())
    total_ratings += movie_rating

    if movie_rating > max_rating:
        max_rating = movie_rating
        max_rating_movie = movie_name

    if movie_rating < min_rating:
        min_rating = movie_rating
        min_rating_movie = movie_name

average_rating = total_ratings / numbers_of_movies

print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")





