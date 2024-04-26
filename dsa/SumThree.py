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
"""


def sum_three(nums, target):
    for i in range(len(nums)):
        complements = dict()
        result = []
        rest = target - nums[i]
        for j in range(len(nums) - 1):
            complement = rest - nums[j + 1]
            if nums[j + 1] in complements:
                result.append(nums[i])
                result.append(nums[j + 1])
                result.append(nums[complements.get(nums[j + 1])])
                return result
            else:
                complements.update({complement: (j + 1)})


print(sum_three([12, 3, 4, 1, 6, 9], 24))
print(sum_three([1, 2, 3, 4, 5], 9))
