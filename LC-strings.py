#
# # 242. Valid Anagram
#
# def is_anagram(s, t):
#     sorted_t = sorted(t)
#     sorted_s = sorted(s)
#     if sorted_t == sorted_s:
#         return True
#     else:
#         return False
#
# # MORE EFFICIENT
# def is_anagram(s: str, t: str) -> bool:
#     return sorted(s) == sorted(t)
#
#
# # EX.1
# s = "anagram"
# t = "nagaram"
#
# # EX.2
# # s = "rat"
# # t = "car"
#
# print(is_anagram(s, t))


#344 Reverse String – Problem

#
# def reverse_string(s):
#     l, r = 0, len(s) - 1
#     while l < r:
#         s[l], s[r] = s[r], s[l]
#         l += 1
#         r -= 1
#     return s
#
# s = ["h","e","l","l","o"]
# # s = ["H","a","n","n","a","h"]
# print(reverse_string(s))
#
# def find_first_unique_character(s):
#     char_hashmap = {}
#
#     # First pass: Build a hashmap with character frequencies
#     for char in s:
#         if char in char_hashmap:
#             char_hashmap[char] += 1
#         else:
#             char_hashmap[char] = 1
#
#     # Second pass: Find the index of the first unique character
#     for i, char in enumerate(s):
#         if char_hashmap[char] == 1:
#             return i
#
#     # If no unique character is found, return -1
#     return -1
#
#
# s = "leetcode"
# # s = "loveleetcode"
# # s = "aabb"
#
# print(find_first_unique_character(s))
#
#
#
# # 28. Find the Index of the First Occurrence in a String
#
# def find_index_of_first_occurance(needle, haystack):
#     length_hay = len(haystack)
#     length_needle = len(needle)
#     # 1ST CHECK IF NEEDLE IS BIGGER THAN HAYSTACK AND RETURN -1
#
#
#     # RETURN: index of first occurence
#     return -1
#
# haystack = "sadbutsad"
# needle = "sad"
# find_index_of_first_occurance(needle, haystack)
#
#
#
# def longest_common_prefix(strs: list[str]) -> str:
#     if not strs:
#         return ""
#
#     prefix = strs[0]
#     for string in strs[1:]:
#         # WHILE THE STRING DOESN'T START WITH PREFIX
#         while not string.startswith(prefix):
#             # MATCH PREFIX MINUS LAST LETTER
#             prefix = prefix[:-1]
#             if not prefix:   # IF THERE IS NOTHING LEFT RETURN EMPTY STRING
#                 return ""
#     return prefix
#
# # Test Cases
# # print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
# # print(longest_common_prefix(["dog", "racecar", "car"]))     # Output: ""
# print(longest_common_prefix(["interview", "internet", "internal"]))  # Output: "inte"
# #
#



# 6. Valid Palindrome – Problem #125


# def is_palindrome(s: str) -> bool:
#     # STEP1: convert to lower
#     # STEP2: remove non-alphanumeric
#     # STEP3: check if same forward and backward
#     s_lower = s.lower()
#     new_string = ""
#     for i, val in enumerate(s_lower):
#         if val.isalnum():
#             new_string = new_string + val
#     # or this
#     # new_string = ''.join(char for char in s_lower if char.isalnum())
#
#
#     str_length = len(new_string) // 2
#     if new_string == new_string[::-1]:
#         return True
#     else:
#         return False
#
# # Example Usage
# print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(is_palindrome("race a car"))                      # Output: False
# print(is_palindrome(" "))                               # Output: True
# print(is_palindrome("No lemon, no melon"))              # Output: True


# 415. Add Strings
# def add_strings(num1: str, num2: str) -> str:
# Problem:  Given two non-negative integers num1 and num2 represented as strings, return their sum as a string.

# # Test Cases
# print(add_strings("11", "123"))   # Output: "134"
# print(add_strings("456", "77"))   # Output: "533"
# print(add_strings("0", "0"))      # Output: "0"
# print(add_strings("999", "1"))    # Output: "1000"


# # chatgpts
# def add_strings(num1: str, num2: str) -> str:
#     i, j = len(num1) - 1, len(num2) - 1  # Start from the end of both strings
#     carry = 0
#     result = []
#
#     # Process both strings from the end to the start
#     while i >= 0 or j >= 0 or carry:
#         digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0  # Convert char to int
#         digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0  # Convert char to int
#         total = digit1 + digit2 + carry  # Sum the digits and the carry
#
#         result.append(str(total % 10))  # Add the last digit of the total to result
#         carry = total // 10  # Update the carry for the next iteration
#
#         i -= 1  # Move to the previous digit in num1
#         j -= 1  # Move to the previous digit in num2
#
#     # Join the digits in reverse order to form the final result
#     return ''.join(reversed(result))
#
# # Test Cases
# print(add_strings("11", "123"))   # Output: "134"
# print(add_strings("456", "77"))   # Output: "533"
# print(add_strings("0", "0"))      # Output: "0"
# print(add_strings("999", "1"))    # Output: "1000"
