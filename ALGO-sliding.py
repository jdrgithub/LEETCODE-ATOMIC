

# 1)
# LeetCode 1876:
# Substrings of Size Three with Distinct Characters)
# Given a string s, return the number of good substrings of length three.
# A good substring is a substring of length three with all distinct characters.

# def countGoodSubstrings(s: str) -> int:
#     count = 0
#     for i in range(len(s) - 2):  # Sliding window of size 3
#         substring = s[i:i+3]
#         if len(set(substring)) == 3:  # Check if all characters are distinct
#             count += 1
#     return count

# print(countGoodSubstrings("xyzzaz"))  # Output: 1
# print(countGoodSubstrings("aababcabc"))  # Output: 4
# print(countGoodSubstrings("abc"))  # Output: 1 (Only "abc" itself)
# print(countGoodSubstrings("aaa"))  # Output: 0 (No substring has distinct characters)


# TEST CASES
# print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3, 3, 5, 5, 6, 7]
# print(maxSlidingWindow([9, 11], 2))  # [11]
# print(maxSlidingWindow([4, -2], 1))  # [4, -2]
# print(maxSlidingWindow([1,3,1,2,0,5], 3))  # [3, 3, 2, 5]
# print(maxSlidingWindow([], 3))  # [] (Edge case: empty input)
# print(maxSlidingWindow([1], 1))  # [1] (Edge case: single element)
# print(maxSlidingWindow([7,2,4], 2))  # [7, 4]

# 2)
# LEETCODE 209
# https://www.youtube.com/watch?v=aYqYMIqZx5s
# 09. Minimum Size Subarray Sum
# Given an array of positive integers NUMS and an integer target,
# RETURN the MINIMUM LENGTH of a CONTIGUOUS SUBARRAY
# whose SUM is at least TARGET.
# If no such subarray exists, return 0.

# FIND THE SMALLEST SUBARRAY WHO'SE SUM IS GREATER THAN THE TARGET

def min_subarray(k, nums):
    l = 0
    current_sum = 0  # Renamed 'sum' to 'current_sum' to avoid conflict
    min_length = float('inf')

    for r in range(len(nums)):
        current_sum += nums[r]
        while current_sum >= k:
            min_length = min(min_length, r - l + 1)
            current_sum -= nums[l]
            l += 1

    return 0 if min_length == float('inf') else min_length


# print(min_subarray(7, [2,3,1,2,4,3]))  # Expected output: 2
# print(min_subarray(4, [1,4,4]))        # Expected output: 1
# print(min_subarray(11, [1,1,1,1,1,1,1,1]))  # Expected output: 0
# print(min_subarray(15, [5,1,3,5,10,7,4,9,2,8]))  # Expected output: 2
# print(min_subarray(5, [2,3,1,1,1,1,1]))  # Expected output: 2


# 3)
# LEETCODE PROBLEM 3 Longest Substring Without Repeating Characters
# Problem Statement:
# Given a string s, find the length of the longest substring
# that does not contain repeating characters.

# def length_of_longest_substring(s):
#     charSet = set()
#     l = 0
#     max_length = 0
#
#     for r in range(len(s)):
#         while s[r] in charSet:
#             charSet.remove(s[l])
#             l += 1
#         charSet.add(s[r])
#         max_length = max(max_length, r - l + 1)
#
#     return max_length

# print(length_of_longest_substring("abcabcbb"))  # Expected: 3 ("abc")
# print(length_of_longest_substring("bbbbb"))    # Expected: 1 ("b")
# print(length_of_longest_substring("pwwkew"))   # Expected: 3 ("wke")
# print(length_of_longest_substring(""))         # Expected: 0
# print(length_of_longest_substring("dvdf"))     # Expected: 3 ("vdf")
#


# 4)
# LeetCode 485 - Max Consecutive Ones
# Given a binary array nums, find the maximum number of consecutive 1s in the array.

# def findMaxConsecutiveOnes(nums):
#     max_count = 0
#     current_count = 0
#
#     for num in nums:
#         if num == 1:
#             current_count += 1
#             max_count = max(max_count, current_count)
#         else:
#             current_count = 0  # Reset count when a zero is encountered
#
#     return max_count


# Example Usage
# print(find_max_consecutive_ones([1,1,0,1,1,1]))  # Output: 3

# 5)
# LeetCode 643: Maximum Average Subarray I
# Problem Summary:
# Given an integer array nums of length n and an integer k,
# find the contiguous subarray of length k
# that has the maximum average
# and return that maximum average value.

# def findMaxAverage(nums, k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum
#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)
#
#     return max_sum / k


# Test Cases
# print(findMaxAverage([1,12,-5,-6,50,3], 4))  # Expected Output: 12.75
# print(findMaxAverage([5], 1))  # Expected Output: 5.0
# print(findMaxAverage([0,1,1,3,3], 2))  # Expected Output: 3.0
# print(findMaxAverage([-1,-2,-3,-4], 2))  # Expected Output: -1.5
# print(findMaxAverage([7,4,5,8,8,3,6,7], 3))  # Expected Output: 7.0





# FOR LATER ----------------------------
# THIS IS MEDIUM LEETCODE 239 IS SIMILAR AND THEORETICALLY SIMPLER
# LeetCode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# Problem Statement:
# Given an integer array nums and an integer limit,
# return the size of the longest continuous subarray
# where the absolute difference between any two elements is less than or equal to limit.

# def longestSubarray(nums, limit):
#     pass
#
#
# # Test case
# nums = [8, 2, 4, 7]
# limit = 4
# print("Final Answer:", longestSubarray(nums, limit))



# LeetCode 239: Sliding Window Maximum
# https://www.youtube.com/watch?v=DfljaUwZsOk
# Problem Statement:

# LeetCode 239: Sliding Window Maximum - HARD
# Given an array nums and an integer k,
# RETURN the MAXIMUM ELEMENT in each sliding window of size k.

# Use a DEQUE to STORE INDICES of useful elements.
# Remove indices of elements that are out of the window.
# MAINTAIN A DECREASING ORDER of values in the deque.

# Use a deque to track indices of useful elements
# Remove elements from the right of deque if they are smaller than the current element
# Remove the leftmost element if it is out of the window
# Append the max value (nums[q[0]]) once the window is full

# KEY POINTS
# ----------
# Elements are added to the queue from the window
# When adding, only add elements if they are lower
# Because it's a queue (FIFO)
# Then the leftmost value is the max.
# Once the max from a window is found,
# The value is added to result
# And the rest of the elements can be removed from queue
#

from collections import deque

def maxSlidingWindow(nums, k):
    output = []
    q = deque()  # INDICES
    l = r = 0

    # pop smaller values from q
    while r < len(nums):
        # POP SMALLER VALUES FROM Q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # IF OUT OF BOUNDSremove left val from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output


# **Test Cases**
# print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
# print(maxSlidingWindow([9,11], 2))               # Output: [11]
# print(maxSlidingWindow([4,3,2,1], 2))            # Output: [4,3,2]
# print(maxSlidingWindow([1], 1))                  # Output: [1]
# print(maxSlidingWindow([1,3,1,2,0,5], 3))        # Output: [3,3,2,5]
#
# FOR LATER ----------------------------