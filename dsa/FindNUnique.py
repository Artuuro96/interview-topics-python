"""
1304. Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input: n = 3
Output: [-1,0,1]

Example 3:

Input: n = 1
Output: [0]

"""
import math


def sum_zero(n):
    result = []
    if n == 1:
        result.append(0)
        return result

    if n % 2 != 0:
        result.append(0)

    for i in range(math.floor(n / 2)):
        result.append(i+1)
        result.append(-i-1)

    return result



