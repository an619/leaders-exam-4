def longest_unique_substring(s):
    unique_seq_list = [0]
    unique = ""
    for char in s:
        if char not in unique:
            unique += char
        else:
            unique_seq_list.append(len(unique))
            unique = ""
    return max(unique_seq_list)


print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbbb"))
print(longest_unique_substring(""))
print(longest_unique_substring("pwwkew"))