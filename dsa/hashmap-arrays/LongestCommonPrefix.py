"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string
Example 1:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Example 2:
Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    result = strs[0]
    for i in range(len(strs) - 1):
        if result == "":
            break
        substr = ""
        length = min(len(result), len(strs[i + 1]))
        for j in range(length):
            if result[j] != strs[i + 1][j]:
                break
            substr += result[j]
        result = substr
    return result


print(longest_common_prefix(["flower", "flow", "flight", "fat"]))
print(longest_common_prefix(["a", "aca", "accb", "b"]))
