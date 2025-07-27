# TWO POINTER TECHNIQUE

# ----------
# TWO SUM - TWO POINTER
# -----------

# Question:
# Write a Python function that takes a SORTED list of integers NUMS and an integer target as input.
# The function should return the indices of two numbers in nums such that their sum equals the target.
# Assume there is exactly one solution, and the input list is sorted in ascending order.
# Optimize the function to run in O(n) time complexity. If no such pair exists, return an empty list.

# PROBLEM STEPS
# Initialize two pointers at the start and end of the list.
# Keep moving the pointers until they meet.
# Calculate the sum of the two numbers at the pointers.
# If the sum matches the target:
# Return the indices of the two numbers.
# If the sum is less than the target:
# Move the left pointer to the right to increase the sum.
# If the sum is greater than the target:
# Move the right pointer to the left to decrease the sum.
# If no pair is found, return an empty list.


# def twoSumSorted(nums, target):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return [left, right]
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return []


#
# nums = [1, 2, 5, 7, 9, 11]
# target = 14
# result = twoSumSorted(nums, target)
# print(result)


# ---------------
# BINARY SEARCH
# -----------------

# Write a Python function that takes a SORTED LIST of integers nums and an INTEGER TARGET as input.
# The function should implement the BINARY SEARCH ALGORYTHM to FIND INDEX OF TARGET in nums.
# If the target is not found, return -1.
# The solution must have a time complexity of 𝑂(log𝑛).

# Initialize the pointers for the range of the search
# Continue until the range is valid (left does not surpass right)
# Calculate the midpoint to avoid overflow. adding offset to the left gives actual midpoint
# Check if the target is found at mid
# Return the index if found
# If the target is larger than nums[mid] move the left pointer to mid + 1 to search in the right half
# If the target is smaller than nums[mid] move the right pointer to mid - 1 to search in the left half
# If the loop exits, the target is not in the list
#

# def findFirstOccurrence(nums, target):
#     left, right = 0, len(nums) - 1  # Initialize the search range
#     result = -1                     # Default result, in case the target is not found
#     while left <= right:            # Continue as long as the search range is valid
#         mid = left + (right - left) // 2  # Calculate the middle index
#         if nums[mid] == target:     # If the middle element matches the target:
#             result = mid            # Save the current index (could be the first occurrence)
#             right = mid - 1         # Narrow the search to the left half to find earlier occurrences
#         elif nums[mid] < target:    # If the target is larger:
#             left = mid + 1          # Move the left pointer to the right half
#         else:                       # If the target is smaller:
#             right = mid - 1         # Move the right pointer to the left half
#
#     return result                   # Return the result (index of the first occurrence or -1)
#
#

# nums = [-10, -5, 0, 3, 8, 12, 20, 25, 30]
# target = 12
# result = findTarget(nums, target)
# print(result)

#
#


#
# ----------------------
# # HASHMAP TWO POINTER
# ---------------------

# PROBLEM
# Write a function two_sum(nums, target) that takes a list of integers nums and a target integer target.
# Return the INDICES s of the two numbers in nums that add up to target.

# Assume that there is exactly one solution, and you cannot use the same element twice.
# The solution should aim for optimal performance.
#

# ANSWER IN WORDS
# Initialize an empty dictionary to store numbers and their indices
# Loop through the list with both index and value
# Calculate the complement (the value needed to reach the target)
# Check if the complement is already in the hashmap
# If it exists, return the indices of the complement and the current number
# Otherwise, store the current number and its index in the hashmap

# SOLUTION
# def twoSumHash(num, target):
#     prevMap = {}
#
def hashTwoSum(nums, target):
    result = {}
    for i, num in enumerate(nums):
        complement = target - num  # number that would pair with this one
        if result[complement] == i:   # have we seen the pair before
            return [nums[complement], i]  # return the pair
        result[num] = i  # otherwise add the value and location for later

    return



# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Input: nums = [3,3], target = 6
# Output: [0,1]















# ---------------------
## SLIDING WINDOW
# ---------------------


# Problem Statement: Given an array of integers and a number k, find the maximum sum of a subarray of size k.


# Comments:
# Calculate the sum of the first k elements.
# Initialize max_sum with the first window sum.
# Iterate through the array, sliding the window by one position each time.
# Subtract the element leaving the window and add the element entering the window.
# Update max_sum if the current window_sum is greater.
# Return the maximum sum after iterating through all windows.

# https://www.youtube.com/watch?v=pT-lOE1on3M
#

# def max_sum_subarray(nums, k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum
#
#     for i in range(k, len(nums)):
#         window_sum = window_sum + nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)
#
#     return max_sum



# # Example usage:
# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# print(max_sum_subarray(nums, k))  # Output: 9
























