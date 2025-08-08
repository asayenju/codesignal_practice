"""
String Pattern Matching:

You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Your task is to calculate the number of substrings of source that match pattern. 

We'll say that a substring source[l..r] matches pattern if the following three conditions are met:
The pattern and substring are equal in length.
Where there is a 0 in the pattern, there is a vowel in the substring. 
Where there is a 1 in the pattern, there is a consonant in the substring. 

Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.
"""
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
def string_pattern_matching(source, pattern):
    n, m = len(source), len(pattern)
    if n < m:
        return 0

    count = 0
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            is_vowel = source[i + j] in vowels
            if (pattern[j] == '0' and not is_vowel) or (pattern[j] == '1' and is_vowel):
                match = False
                break
        if match:
            count += 1
    return count

print(string_pattern_matching("amazing", "010"))  # Output: 2
            