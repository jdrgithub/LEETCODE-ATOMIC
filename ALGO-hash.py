'''
1. TWO SUMS
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

RETURN INDICES

'''

# def twoSum(nums, target):
#     previous = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in previous:
#             return [previous[complement], i]
#         previous[num] = i
#
#     return []
# #
#

# return indices of the two numbers such that they add up to target.

nums = [2,7,11,15]
target = 9
# print(twoSums(nums, target))
# Output: [0,1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


'''
242. VALID ANAGRAM
Given two strings s and t, return true if t is an
anagram of s, and false otherwise.
'''

# def is_anagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#       return False
#     char_count = {}
#     for char in s:
#       char_count[char] = char_count.get(char, 0) + 1
#     for char in t:
#         if char not in char_count or char_count[char] == 0:
#           return False
#         char_count[char] -= 1
#     return True


'''
242. Valid Anagram
Given two strings s and t, return true if t is an
anagram of s, and false otherwise.
'''



# Example usage and test cases
# print(is_anagram("anagram", "nagaram"))  # Output: True
# print(is_anagram("rat", "car"))          # Output: False
# print(is_anagram("aabbcc", "bbaacc"))    # Output: True
# print(is_anagram("hello", "helloo"))     # Output: False
# print(is_anagram("", ""))                # Output: True (Empty strings are anagrams)



# 17. CONTAINS DUPLICATE
# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.



# def contains_duplicate(nums: list[int]) -> bool:
#     hashmap = {}
#     for num in nums:
#         if num in hashmap:
#             return True
#         hashmap[num] = 1
#     return False

# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.


# print(contains_duplicate([1, 2, 3, 1]))  # Output: True
# print(contains_duplicate([1, 2, 3, 4]))  # Output: False
# print(contains_duplicate([1, 1, 1, 1]))  # Output: True
# print(contains_duplicate([]))  # Output: False


#
# 49. INTERSECTION OF TWO ARRAYS
# Given two integer arrays nums1 and nums2,
# return an array of their intersection
# Each element in the result must be unique and you may return the result in any order.
# def intersection(nums1, nums2):
#     num_map = {}  # HashMap to store elements of nums1
#     result = []   # List to store unique intersection
#
#     # Store elements of nums1 in the hashmap
#     for num in nums1:
#         if num not in num_map:
#             num_map[num] = True  # Mark presence
#
#     # Iterate through nums2 and check if it exists in num_map
#     for num in nums2:
#         if num in num_map and num_map[num]:
#             result.append(num)
#             num_map[num] = False  # Ensure uniqueness by marking as used
#
#     return result

# Given two integer arrays nums1 and nums2,
# return an array of their intersection
# Each element in the result must be unique
# and you may return the result in any order.

# Example usage:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
#
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# Output: [2]
#
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# Output: [9,4]

# print(intersection(nums1, nums2))


# 7. FIRST UNIQUE CHARACTER IN A STRING
# Given a string s,
# find the first non-repeating character in it
# and return its index.
# If it does not exist, return -1.

# def first_unique(s):
#     hashmap = {}
#
#     for c in s:
#         hashmap[c] = hashmap.get(c, 0) + 1
#
#     for i, c in enumerate(s):
#         if hashmap[c] == 1:
#             return i
#
#     return -1

# Given a string s,
# find the first non-repeating character
# and RETURN ITS INDEX.
# If it does not exist already, RETURN -1.


# s = "lleetcode"  # 4 for t
# print(first_unique(s))

# ----------------------------------------------------------

# 49. GROUP ANAGRAMS
# https://www.google.com/search?q=49.+Group+Anagrams&oq=49.+Group+Anagrams&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIICAMQABgHGB4yBggEEAAYHjIGCAUQABgeMgYIBhAAGB4yBggHEAAYHjIGCAgQABgeMgYICRAAGB7SAQg3OTUxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:dbd0d080,vid:vzdNOK2oB2E,st:0
# Given an array of strings strs,
# group the anagrams
# together. You can return the answer in any order.



# from collections import defaultdict
#
# def groupAnagrams(strs):
#     # HashMap to store groups of anagrams
#     # Key: character count tuple, Value: list of anagrams
#     result = defaultdict(list)
#
#     for s in strs:
#         # Initialize a list of 26 zeros (for 'a' to 'z') to count character occurrences
#         count = [0] * 26  # create new count each time
#
#         # The lowercase alphabet starts at ord("a") = 97.
#         # To map 'a' to 0, 'b' to 1, etc., we subtract ord("a"):
#         for c in s:
#             count[ord(c) - ord("a")] += 1  # Increment the corresponding index based on the character
#
#         # Convert count list to tuple (hashable) and use as key
#         result[tuple(count)].append(s)

#     # Having grouped them
#     # Convert defaultdict values to a list of lists and return
#     return list(result.values())



# Given an array of strings strs,
# group the anagrams
# together. You can return the answer in any order.
from collections import defaultdict
def groupAnagrams(strs):
    result = defaultdict(list)
    for str in strs:
        count = [0] * 26
        for c in str:
            count[ord(c) - ord('a')] += 1
        result[tuple(count)].append(str)

    return list(result.values())





# Example Usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

#
# strs = [""]
# # Output: [[""]]
#
# strs = ["a"]
# # Output: [["a"]]
