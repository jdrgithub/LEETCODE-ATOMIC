# ### Basic Array Traversal and Manipulation Problems
#
#
# # Find Maximum in Array
# # Problem: Traverse the array to find and return the maximum value.
#
# def find_max(nums):
#     max_val = nums[0]
#     for num in nums:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# def find_max(nums):
#
#

# # Find Maximum in Array
# # Problem: Traverse the array to find and return the maximum value.

# nums = [3,4,6,8]
# print(find_max(nums=nums))
#
#
#
#
# # Reverse Array
# # Problem: Reverse the elements of an array in place.

# PROBLEM HOW TO
# Initialize two pointers: one at the beginning (left) and one at the end (right) of the array
# Continue swapping until the pointers meet in the middle
# Swap the elements at the left and right pointers
# Move the left pointer one step to the right
# Move the right pointer one step to the left
# Return the reversed array


#
# def reverse_array(nums):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
#     return nums
#
# #  Reverse Array
# # Problem: Reverse the elements of an array in place.

# nums = [3,2,2,5,4]
# print(reverse(nums))
#
#

#
# #  Remove Duplicates from Sorted Array
# # Problem: Given a sorted array, remove duplicates in place and return the new length of the array (without extra space).
#

# def remove_duplicates(nums):
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[i] != nums[j]:
#             i += 1  # move pointer forward cuz not duplicates
#             nums[i] = nums[j]   # update new i with value of non-duplicate j
#         # if duplicate just let j increment
#     return i + 1

#
# #  Remove Duplicates from Sorted Array
# # Problem: Given a sorted array, remove duplicates in place and return the new length of the array (without extra space).

# nums = [1,2,3,3,4,4]
# print(remove_duplicates(nums))
#
# 6. Move Zeros to the End
# Problem: Move all zero elements to the end of the array while maintaining the relative order of the non-zero elements.
#
# def move_zeros(nums):
#     l = 0  # where the last zero was or will be
#     for r in range(len(nums)):
#         if nums[r] != 0:   # if you find a number that is not zero
#             nums[l], nums[r] = nums[r], nums[l]  # swap it with the last zero
#             l += 1
#     return nums
#
#
# Problem: Move all zero elements to the end of the array while maintaining the relative order of the non-zero elements.

# nums=[0, 1, 0, 3, 12]
# print(move_zeros(nums))
#
#
#
# 7. Check if Array is Sorted
#
#
# def is_sorted(nums):
#     for i in range(1, len(nums)):
#         if nums[i] < nums[i - 1]:
#             return False
#     return True
#
#
# Problem: Check if an array is sorted in ascending order.
#

# nums = [1,2,3,5]
# print(is_sorted(nums))

#
#
# # 8. Find First Unique Element
# # Problem: Find the first element in the array that appears only once.
#
# def first_unique(nums):
#     count = {}
#     for num in nums:
#         count[num] = count.get(num, 0) + 1
#     for num in nums:
#         if count[num] == 1:
#             return num
#     return False
#
#
#
# # Problem: Find the first element in the array that appears only once.
# # STRATEGY - hash table
#
#
# nums = [1,1,2,3,3,4]
# print(first_unique(nums))
#
#
# # 9. Rotate Array
# # Problem: Rotate an array to the right by k steps.
#
# def rotate_array(nums, k):
#     k %= len(nums)   # k = k % len(nums)  -> reduces k to a number with in the length of the array
#     nums[:] = nums[-k:] + nums[:-k]
#     return nums
#
#
#
# # 9. Rotate Array
# # Problem: Rotate an array to the right by k steps.
#

# def rotate_array(nums, k):
#
#

#
# k = 3
# nums = [1,2,3,4,5,6]
# print(rotate_array(nums,k))
#
#
#
#
# # 11. Find the Second Largest Element
# # Problem: Find the second largest element in an array.
#

# def second_largest(nums):
#     largest = second = float('-inf')
#
#     for num in nums:
#         if num > largest:
#             second = largest
#             largest = num
#         elif second > num and num != largest:
#             second = num
#
#     return second if second != float('-inf')
#
# # Example usage
# nums = [3, 1, 4, 4, 5, 6, 5]
# print(second_largest(nums))  # Output: 4

#
# # 12. Find Missing Number (0 to N)
# # Problem: Given an array containing numbers from 0 to n with one number missing, find the missing number.
#
# def missing_number(nums):
#     n = len(nums)
#     total_sum = n * (n + 1) // 2
#     return total_sum - sum(nums)
#

# # 12. Find Missing Number (0 to N)
# # Problem: Given an array containing numbers from 0 to n with one number missing, find the missing number.

# def find_missing_number(nums):
#
#     for num in range(1, len(nums) - 1):
#         if nums[num] != nums[num - 1] + 1:
#             return nums[num - 1] + 1
#
#
# nums = [1,2,4,5,6]
# print(find_missing_number(nums))

# # 13. Find Intersection of Two Arrays
# # Problem: Given two arrays, find their intersection.
#
# def array_intersection(nums1, nums2):
#     set1 = set(nums1)
#     set2 = set(nums2)
#     return list(set1 & set2)



#
#
# # 13. FIND INTERSECTION OF TWO ARRAYS
# # Task: Given two arrays, find their intersection.

# def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
#     seen = set(nums1)
#
#     result = []
#
#     for num in nums2:
#         if num in seen:
#             result.append(num)  # Add to result
#             seen.remove(num)    # Remove from hashset
#     return result
#
#
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# print(intersection(nums1, nums2))

#
#
# def array_intersection(nums1, nums2):
#     set1 = set(nums1)
#     set2 = set(nums2)
#     return list(set1 & set2)
#
#
#
#
#
# ### Additional Array Problems for Practice
#
# # 14. Remove Element
# # Problem: Remove all occurrences of a given element from an array, and return the new length.
#
# def remove_element(nums, val):
#     i = 0
#     for j in range(len(nums)):
#         if nums[j] != val:
#             nums[i] = nums[j]
#             i += 1
#     return i
#
#
# # 15. Find the Maximum Product of Two Elements
# # Problem: Find the maximum product of any two elements in the array.
#
# def max_product(nums):
#     nums.sort()
#     return (nums[-1] - 1) * (nums[-2] - 1)
#
#
# # 16. Replace Elements with Greatest Element on Right Side
# # Problem: Replace every element with the greatest element on its right side, and replace the last element with -1.
#
# def replace_elements(nums):
#     max_val = -1
#     for i in range(len(nums) - 1, -1, -1):
#         nums[i], max_val = max_val, max(nums[i], max_val)
#     return nums
#
#
# # 17. Merge Two Sorted Arrays
# # Problem: Given two sorted arrays, merge them into one sorted array.
#
# def merge_sorted_arrays(nums1, nums2):
#     return sorted(nums1 + nums2)
#
#
# # 18. Find Disappeared Numbers
# # Problem: Given an array of integers where 1 ≤ a[i] ≤ n, find all the numbers that are missing.
#
# def find_disappeared_numbers(nums):
#     return list(set(range(1, len(nums) + 1)) - set(nums))
#
#
# # 19. Check for Duplicates
# # Problem: Determine if there are any duplicates in the array.
#
# def contains_duplicate(nums):
#     return len(nums) != len(set(nums))
#
#
# # 20. Find Pivot Index
# # Problem: Find the pivot index of the array where the sum of the elements to the left is equal to the sum of the elements to the right.
#
# def pivot_index(nums):
#     total_sum = sum(nums)
#     left_sum = 0
#     for i, num in enumerate(nums):
#         if left_sum == total_sum - left_sum - num:
#             return i
#         left_sum += num
#     return -1
#
#
# # 21. Replace Zeros with Ones
# # Problem: Replace every zero in the array with one.
#
# def replace_zeros_with_ones(nums):
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums[i] = 1
#     return nums
#
#
# # 22. Max Consecutive Ones
# # Problem: Find the maximum number of consecutive 1s in an array.
#
# def find_max_consecutive_ones(nums):
#     max_count, count = 0, 0
#     for num in nums:
#         if num == 1:
#             count += 1
#             max_count = max(max_count, count)
#         else:
#             count = 0
#     return max_count
#
#
# # 23. Find Majority Element
# # Problem: Find the element that appears more than half the time in an array.
#
# def majority_element(nums):
#     count, candidate = 0, None
#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += (1 if num == candidate else -1)
#     return candidate
#
#
# # 24. Find Kth Largest Element
# # Problem: Find the kth largest element in an unsorted array.
#
# def find_kth_largest(nums, k):
#     nums.sort()
#     return nums[-k]
#
#
# # 25. Maximum Subarray (Kadane’s Algorithm)
# # Problem: Find the contiguous subarray with the maximum sum.
#
# def max_subarray(nums):
#     max_sum = cur_sum = nums[0]
#     for num in nums[1:]:
#         cur_sum = max(num, cur_sum + num)
#         max_sum = max(max_sum, cur_sum)
#     return max_sum
#
#
# # 26. Find Single Non-Duplicate Element
# # Problem: Find the element that appears exactly once in an array where every other element appears twice.
#
# def single_non_duplicate(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result
#
#
# # 27. Find the Intersection of Two Arrays (No Duplicates)
# # Problem: Given two arrays, find their intersection and remove any duplicates.
#
# def intersection(nums1, nums2):
#     return list(set(nums1) & set(nums2))
#
#
# # 28. Product of Array Except Self
# # Problem: Return an array where each element is the product of all elements except itself.
#
# def product_except_self(nums):
#     result = [1] * len(nums)
#     left_prod = 1
#     for i in range(len(nums)):
#         result[i] = left_prod
#         left_prod *= nums[i]
#     right_prod = 1
#     for i in range(len(nums) - 1, -1, -1):
#         result[i] *= right_prod
#         right_prod *= nums[i]
#     return result
#
#
#
# 29) Flatten this:
#
# def flatten_list(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flat_list.extend(flatten_list(item))
#         else:
#             flat_list.append(item)
#     return flat_list
#
# def flatten_list(nested_list):
#     flatlist = []
#     for i in nested_list:
#         if isinstance(i, list):
#             flatlist.extend(flatten_list(i))
#         else:
#             flatlist.append(i)
#     return flatlist
#
#
# nested_list = [1, 3, 5, [3, 4, [2, 5]]]
# flattened = flatten_list(nested_list)
# print(flattened)
#
#
#
# #  WITH ITERTOOLS
# from itertools import chain
#
# nested_list = [1, 3, 5, [3, 4, [2, 5]]]
# flattened = list(chain.from_iterable(
#     item if isinstance(item, list) else [item] for item in nested_list
# ))
# print(flattened)
