"""
1455 = "one hundred fifty five"
45 = "forty five"
"""
import math

basic_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def number_to_string_number(number):
    if number == 0:
        return "zero"

    result = ""

    if math.floor(number / 1000) > 0:
        result += number_to_string_number(math.floor(number / 1000)) + " thousand "
        number %= 1000

    if math.floor(number / 100) > 0:
        result += basic_digits[math.floor(number / 100)] + " hundred "
        number %= 100

    if number > 0:
        if 10 < number < 19:
            result += teens[number % 10]
        else:
            result += tens[math.floor(number / 10)]
            if number % 10 != 0:
                result += " " + basic_digits[number % 10]

    return result


print(number_to_string_number(400000))
