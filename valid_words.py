"""
Count Valid Words from String
Given a string and a list of valid letters, count how many words in the string can be formed using the letters in the valid letters list. For the input string, words are split using spaces. Punctuation and numbers are always considered valid letters. Both uppercase and lowercase are invalid for letters not present in the input list.

Example:

Input:
String: "Hello, I am h2ere!"
Letters: "heloiar"
Output: 3
Explanation:
Valid words: "Hello,", "I", "h2ere!".
Invalid word: "am" (as 'm' is not present in the list of valid letters).
"""
def valid_words(string, letters):
    lists = string.split(" ")
    count = 0
    for n in lists:
        flag = True
        for l in n:
            if (l>="a" and l<="z") or (l>="A" and l<="Z"):
                if l.lower() not in letters:
                    flag = False
                    break
        if flag:
            count+=1
    return count

print(valid_words("Hello, I am h2ere!", "heloiar"))