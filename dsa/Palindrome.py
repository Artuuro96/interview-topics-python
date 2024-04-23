def is_palindrome(word):
    word = "".join(word.split())
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("logracasillasallisacargol"))
print(is_palindrome("anportaa"))
print(is_palindrome("arroz a la zorra"))
