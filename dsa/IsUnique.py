def is_unique(word):
    str_set = set()
    for char in word:
        if char in str_set:
            return False
        str_set.add(char)

    return True


print(is_unique("abcdef"))
