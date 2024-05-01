"""
 1.Two Sum
 Dado un array de números enteros y un target, retorna los índices de dos
 números para los que la suma de ambos sea igual al target.

 Puedes asumir que hay solamente una solución.

 Ejemplo 1:
 Input: nums = [9,2,5,6], target = 7
 Output: [1,2]
 Explicación: nums[1] + nums[2] == 7, devolvemos [1, 2].

 Ejemplo 2:
 Input: nums = [9,2,5,6], target = 100
 Output: null

 Algorithm:
 1. Iterate the array and take the first number.
 2. While the result is different from 7, try the different sum of combinations of the array elements in search of
 one equal to 7
 3. If there is no sum of two items that is equal to 7, return false.
"""


def sum_two(nums, target):
    result = []
    complements = dict()
    for index in range(len(nums)):
        complement = target - nums[index]
        print("complement", complement, complements)
        if nums[index] not in complements:
            complements.update({complement: index})
        else:
            result.append(complements.get(nums[index]))
            result.append(index)

    return result


print(sum_two([9, 2, 5, 6], 7))
