"""
A coach of a school chess club wants to start a mentoring program for newer players. Each player has an integer rating
representing skill level. The coach would like to pair up students whose ratings differ by no less than a given minimum.
What is the maximum number of pairs that can be formed?

Example
n = 6
rating = [1,2,3,4,5,6]
min_diff = 4

There are n = 6 players. Two pairs of players have a difference of 4 or more: those with ratings (1,5) and (2,6)
Function Description
Complete the function max_pairs in the editor bellow. The function must return an integer that represents the maximum
number of pairs that the coach can form
max_pairs has the following parameters:
    -rating: an array of integers denoting the ratings of the players
    -min_diff: the minimum difference in skill levels of the players in a pair
"""


def max_pairs(rating, min_diff):
    complements = set(rating)
    pairs = []
    for rate in rating:
        complement = rate - min_diff
        if complement in complements:
            pairs.append([complement, rate])

    return pairs


print(max_pairs([1, 2, 3, 4, 5, 6], 4))
