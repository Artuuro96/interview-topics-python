"""
Input: words = ["saco", "arresto", "programa", "rastreo", "caso"].
Output: [["saco", "caso"], ["arresto", "rastreo"], ["programa"]].

"""

words = ["saco", "arresto", "programa", "rastreo", "caso"]


def group_anagram(words):
    anagram_dic = {}
    for word in words:
        hash_sorted = "".join(sorted(word))
        if hash_sorted not in anagram_dic:
            anagram_dic.update({hash_sorted: []})
        anagram_dic.get(hash_sorted).append(word)

    return anagram_dic.values()


result = []
for anagrams in group_anagram(words):
    result.append(anagrams)

print(result)


def group_anagram_optimized(words):
    anagram_dict = {}
    for word in words:
        hash = generate_hash(word)
        if hash not in anagram_dict:
            anagram_dict.update({hash: [word]})
        else:
            anagram_dict[hash].append(word)
    return anagram_dict.values()


def generate_hash(word):
    size = 26
    hash = [0] * size
    for letter in word:
        hash[ord(letter) - ord("a")] = + 1

    return str(hash)


result = []
for anagrams in group_anagram_optimized(words):
    result.append(anagrams)

print("Result Optimized", result)
