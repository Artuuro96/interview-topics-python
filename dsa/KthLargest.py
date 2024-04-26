"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4    [3]   [2,3]   [2,3,3]  [1,2,3,3]   [1,2,3,3,]
Output: 4

3
si peek > new_value
    push new value
else
    peek = stack.peek()
    while peek < new_value


"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top
        self.size += 1

    def print_stack(self):
        while self.top is not None:
            print(self.top.value)
            self.top = self.top.next

    def pop(self):
        if self.top is None:
            raise Exception("Empty stack")
        top_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return top_value

    def peek(self):
        if self.top is None:
            raise Exception("Empty stack")
        return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False


def find_kth_largest(nums, k):
    sorted_stack = Stack()
    stack = Stack()
    if len(nums) == 1:

        return nums[0]
    for num in nums:
        stack.push(num)

    while not stack.is_empty():
        tmp = stack.pop()
        while not sorted_stack.is_empty() and tmp > sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(tmp)

    i = 0
    value = None
    while not sorted_stack.is_empty():
        sorted_stack.top = sorted_stack.top.next
        i += 1
        if i == sorted_stack.size - k:
            print(f"{i} == {sorted_stack.size - k} value: {sorted_stack.top.value}")
            value = sorted_stack.top.value

    return value


print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
