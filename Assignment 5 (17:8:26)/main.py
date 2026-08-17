def find_lcs(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ""

    if str1[-1] == str2[-1]:
        return find_lcs(str1[:-1], str2[:-1]) + str1[-1]

    remove_first = find_lcs(str1[:-1], str2)
    remove_second = find_lcs(str1, str2[:-1])

    if len(remove_first) >= len(remove_second):
        return remove_first

    return remove_second


first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")

result = find_lcs(first_word, second_word)

print("Longest Common Subsequence:", result)
print("LCS Length:", len(result))