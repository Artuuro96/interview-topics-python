"""
Given an array arr[] of size n and an integer X. Find if there’s a triplet in the array which sums up to the given integer X.

Examples:
Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
Output: 12, 3, 9
Explanation: There is a triplet (12, 3 and 9) present
in the array whose sum is 24.

Input: array = {1, 2, 3, 4, 5}, sum = 9
Output: 5, 3, 1
Explanation: There is a triplet (5, 3 and 1) present
in the array whose sum is 9.
[9,2,5,6] target = 7

9 + x = 7 => x = 7 - 9 = -2
             x = 7 - 2 = 5
             x = 7 - 5 = 2
"""

def sum_three(nums, sum):
    result = []
    complements = dict()
    for i in range(len(nums)):
        complement = sum - nums[i]
        if nums[i] not in complements:
            complements.update({complement: i})
        else:
            result.append(complement)
            result.append(nums[i])

    return result


sum_three([9,2,5, 21, 9,2,7,6], 28)


