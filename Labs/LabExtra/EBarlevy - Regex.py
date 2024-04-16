import re

with open('reviews.txt', 'r') as file:
    for line in file:
        print("release year: " + re.search(r'[1-2][0-9][0-9][0-9]', line).group(0), end="")
        print("    rating: " + re.search(r'[1][0][\/][1][0]|[0-9][\/][1][0]|[0-9] out of [1][0]|[1][0]out of [1][0]', line).group(0), end="")
        print("    reviewer: " + re.search(r'Reviewer: \w+\W+\w+|- \w+\W+\w+$|by \w+\W+\w+|by: \w+\W+\w+', line).group(0), end="") # this should be parsed but i dont care
        print("    movie: " + re.search(r'\b\w*[A-Z]+\w*(?=\s*\()|\b\w*[A-Z]+\w*(?=\s*\,)', line).group(0), end="") # i got one of the words
        print()
