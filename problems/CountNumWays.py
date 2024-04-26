"""
Amazon is working on a new hashing approach that takes in the original string and a seed number.

Engineers decided that the seed can be generated from the same input string by counting the number of times
a reverse of a substring of length k makes the new string lexicographically smaller.
You are deployed with the task of developing a service that takes in a string s and an integer k,
and returns the number of ways to reverse any substring of length k such that the resulting string is lexicographically
smaller than the original string.
Notes:
    • A substring is a contiguous sequence of characters within a string. For example, the string "zon" is a substring of "amazon", "zone", etc. but is not a substring of "zoin", "zozo", etc.
    • A string a is lexicographically smaller than string b if a[i]f < b[i]l at the first index where a and b differ. For example, "amazon" is lexicographically smaller than amozan".
Example
S= "amazon" k=3
"""


def is_lex_smaller(s, substr):
    return substr > s


def count_num_ways(s, k):
    count = 0
    for i in range(len(s) - k + 1):
        substring = s[i: k + i]
        substr_reversed = substring[::-1]
        new_string = s[:i] + substr_reversed + s[k + i:]
        if is_lex_smaller(s, new_string):
            count += 1
    return count


print(count_num_ways("amazon", 3))
