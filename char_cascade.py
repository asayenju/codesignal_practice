"""
Character Cascade from String Array
You are given an array of strings arr. Your task is to construct a string from the words in arr, starting with the 0th character from each word (in the order they appear in arr), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word. Return the resulting string.

Example: For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".
"""
from collections import defaultdict
def char_cascade(arr):
    hashmap = defaultdict(str)
    for words in arr:
        for i in range(len(words)):
            hashmap[i] += words[i]
    s = ""
    for key in hashmap:
        s+=hashmap[key]
    return s

print(char_cascade(["Daisy", "Rose", "Hyacinth", "Poppy"]))