"""
20. Valid Parentheses
Dado un String que solamente contiene los caracteres '(', ')', '{', '}', '[' y ']',
implementa un algoritmo para determinar si es válido.

Ejemplo 1:
Input: "([]){}"
Output: true

Ejemplo 2:
Input: "({)}"
Output: false
 """

from Stack import Stack


def push_closed_char(stack, char):
    if char == "(":
        return stack.push(")")

    if char == "[":
        return stack.push("]")

    if char == "{":
        return stack.push("}")


def is_valid_char_sequence(char_seq):
    stack = Stack()
    closed_chars = {")", "]", "}"}
    for char in char_seq:
        if char in closed_chars:
            if stack.pop() != char:
                return False
        else:
            push_closed_char(stack, char)
    if not stack.is_empty():
        return False
    return True


print(is_valid_char_sequence("([]){}"))
print(is_valid_char_sequence("({})[]{"))
print(is_valid_char_sequence("([{}])"))
