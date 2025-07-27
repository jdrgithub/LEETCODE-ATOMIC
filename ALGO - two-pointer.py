#  TWO SUM

# VALID PALINDROME -
#
# NON-TWO POINTER APPROACH

# def isPalindrome(str):
#     new_str = ""
#
#     for char in str:
#         if char.isalnum():
#             new_str += char.lower()
#     return new_str == new_str[::-1]

def isPalindrome(str):
    new_str = ""
    for char in str:
        if char.isalnum():
            new_str += char.lower()
        return new_str == new_str[::-1]

'''
TWO POINTER APPROACH - LC125

A palindrome is a phrase that reads the same forward and backward after:

Converting uppercase letters to lowercase.
Removing non-alphanumeric characters (keeping only letters and numbers).
Given a string s, return:

True if it is a palindrome after processing.
False otherwise.

Initialize two pointers, left starting at the beginning of the string and right starting at the end of the string
Loop until the two pointers meet in the middle
Loop over moving the left pointer forward if the current characters are not alphanumeric
Loop over moving the right pointer backward if the current characters is not alphanumeric
Compare the characters at the left and right pointers (case insensitive)
If the characters don't match, it's not a palindrome
Move both pointers closer to the center
If all characters matched, the string is a palindrome
'''


# def isPalindrome(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         while left < right and not s[left].isalnum():
#             left += 1
#         while right > left and not s[right].isalnum():
#             right -= 1
#
#         if s[left].lower() != s[right].lower():
#             return False
#         # If previous checks pass, increment
#         left += 1
#         right -= 1
#
#     return True


# Example 1:  true
# s = "A man, a plan, a canal: Panama"
# # Example 2:  false
# s = "race a car"
# # Example 3:  true
# s = " "
# print(isPalindrome(s))


# LEETCODE 26 - REMOVE DUPLICATES FROM SORTED ARRAY
'''
Given two sorted integer array nums1 and nums2, merge nums2 into num1 as one sorted array.

The number of elements initiliazed in num1 and num2 are m and n.
nums1 is actually sized m + n to hold additional elements from nums2
 
RETURN -> NUMBERS OF UNIQUE ELEMENTS -> k

#  ANSWER
Start from the second position (index 1)
Check if the current number is A DUPLICATE
Place the unique element at the k-th index
Increment k to prepare for the next unique number
Return k

BASICALLY EVERYTIME THERE ISN'T A DUPLICATE PLUS ONE
'''

# def removeDuplicates(nums):
#     k = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[k] = nums[i]
#             k += 1
#
#     return k

# Example 1:
# nums = [1,1,2]
# Example 2:
# nums = [0,0,1,1,1,2,2,3,3,4]
#
# print(removeDuplicates(nums))

'''
88. Merge Sorted Array

Merge two sorted integer arrays, nums1 and nums2, into nums1 as a single sorted array.

- nums1 has size m + n, with the first m elements valid and the rest as placeholders (0s).
- nums2 has n elements to be merged into nums1.

Modify nums1 in-place to contain the merged, sorted array.
 
RETURN NUMS1
-----------------------------------
STEPS
Last index of nums1 where merging happens
Decriment pointers
Merge in reverse order
If there are remaining elements in nums2, copy them
---------------------------------------------------

'''

def merge(nums1, m, nums2, n):
    k = m + n - 1
    m += 1
    n += 1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[k] = nums1[m]
            m -= 1
        else:
            nums1[k] = nums2[n]
            n -= 1
        k -= 1

        while n >= 0:
            nums1[k] = nums2[n]
            n -= 1
            k -= 1

    return nums1


#Example 1:
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# Output: [1,2,2,3,5,6]
#
# Example 2:
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# # Output: [1]
#
# Example 3:
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# # Output: [1]
# print(merge(nums1, m, nums2, n))



'''
349. INTERSECTION OF TWO ARRAYS
Given two integer arrays nums1 and nums2,
return an array of their intersection
Each element in the result must be unique 
and you may return the result in any order.

STEPS:
Sort lists.
Make list to store results in.
Initialize two pointers to 0
While pointers are less than array lengths,
    Check if elements in first array are less than second
        if so increment pointer
    Check if elements in second array are less than first
        if so increment 2nd pointer
    If neither of these are true, then they are equal
        check if results is empty or if the element is last 
            (because everything is sorted)
Return result

'''

# def intersection(nums1, nums2):
    # nums1.sort()
    # nums2.sort()
    #
    # result = []
    # i, j = 0, 0
    #
    # while i < len(nums1) and j < len(nums2):
    #     if nums1[i] < nums2[j]:
    #         i += 1  # move the smaller one to find a bigger match
    #     elif nums1[i] > nums2[j]:
    #         j += 1  # move the smaller one to find a bigger match
    #     else:  # check for empty array or for duplication
    #         if not result or nums1[i] != result[-1]:  # O(k), where k = len(result)
    #             result.append(nums1[i])
    #         i += 1
    #         j += 1
    #
    # return result



# Example 1:
#
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# Output: [2]
# Example 2:
#
# nums1 = [4,9,5]
# nums2 = [9,4,9,8]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# print(intersection(nums1, nums2))


'''
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must appear 
as many times as it shows in both arrays
and you may return the result in any order.


STEPS
Sort both arrays to enable two-pointer traversal
Initialize pointers for both arrays and an empty result list
Traverse both arrays until one pointer reaches the end
Compare elements at the current positions of the two pointers
Move the pointer of the smaller element forward
If elements at both pointers match, add to the result and move both pointers
Return the result after completing the traversal



def intersection(nums1, nums2):
    # Sort both arrays
    nums1.sort()
    nums2.sort()
    
    # Initialize pointers and result
    i, j = 0, 0
    result = []
    
    # Traverse both arrays using two pointers
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            # nums1[i] == nums2[j], add to result and move both pointers
            result.append(nums1[i])
            i += 1
            j += 1

    return result

'''
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums[1]:
            j += 1
        else:
            result.append(nums1[i])

    return result

def intersection1(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []
    i = j = 0

    # while if i < len(nums1) and j < len(nums2):





# Example 1:
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# Output: [2,2]

# Example 2:
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# Output: [4,9]

print(intersection(nums1, nums2))


'''
283. Move Zeroes
Given an integer array nums, 
move all 0's to the end of it 
while maintaining the relative order
of the non-zero elements.

NOTE: that you must do this in-place
without making a copy of the array.
'''

# def move_zeros(nums):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[k] = nums[k], nums[i]
#             k += 1
#
#     return nums

# Example 1:
# nums = [0,1,0,3,12]
# # Output: [1,3,12,0,0]

# Example 2:
# nums = [0]
# Output: [0]

# print(move_zeros(nums))

'''
167. Two Sum II - Input Array Is Sorted

You are given a 1-indexed sorted array. 
Find two numbers that add up to the target and return their indices as [index1, index2]. 
The indices start at 1, not 0. Use constant extra space.
'''

# def two_sum(nums, target):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return [left + 1, right + 1]
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#
#     return



# nums = [2,7,11,15]
# target = 9
# Output: [1,2]

# nums = [2,3,4]
# target = 6
# Output: [1,3]

# nums = [-1,0]
# target = -1
# Output: [1,2]

# print(two_sum(nums, target))

# ----------------------------------------------------------
'''
LEETCODE 15. 3Sum

Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

STEPS
Initialize the result list
Sort the array
Iterate through the array
Skip duplicate elements
Set two pointers for the remaining elements
Calculate the sum of the triplet
Do -> the first number + the total of the two-sum
Return the result list

NOTES:
Duplicate numbers can lead to repeated triplets in the result. 
    Without skipping duplicates, the triplet [-1, 0, 1] could be added multiple times


ANSWER
def three_sum(nums):
    result = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return result
    
'''





# Example 1:
# nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# nums = [0,1,1]
# Output: []
#
# Example 3:
# nums = [0,0,0]
# Output: [[0,0,0]]

# print(three_sum(nums))




'''
----------------------------------------------------------------
11. Container With Most Water

You are given an array height representing vertical lines:

Each line is at index i on the x-axis.
    The height of each line is height[i] on the y-axis.
    Find two lines that form a container with the x-axis. 

The container's:
    Width = distance between the two lines (right index - left index).
    Height = the shorter of the two lines.
    
Return the maximum area of water the container can hold.

BRUTE FORCE WILL FAIL DUE TO TIME COMPLEXITY

STRATEGY:  
We want the highest points and the greatest width.
To maximize the area, we always try to
find a taller boundary by moving the RIGHT OR LEFT pointer
    that points to the shorter line inward.
ERGO: THROW OUT WHICHEVER IS THE SMALLER ONE AND LOOK FOR A BIGGER ONE
KEEP MOVING POINTERS UNTIL LEFT AND RIGHT MEET
'''

# BRUTE FORCE
# def maxArea(height):
#     max_vol = 0
#     for l in range(len(height)):
#         for r in range(l + 1, len(height)):
#             width = r - l
#             least = min(height[l], height[r])
#             current = width * least
#             max_vol = max(max_vol, current)
#
#     return max_vol

# TWO POINTER
# def maxArea(height):
#     max_area = 0
#     left, right = 0, len(height) - 1
#     while left < right:
#         least = min(height[left], height[right])
#         current =  least * (right - left)
#         max_area = max(current, max_area)
#         if left > right:
#             right -= 1
#         else:
#             left += 1
#
#     return max_area


# height = [1,8,6,2,5,4,8,3,7]  # 49
# height = [1,1]  # 1
# print(maxArea(height))







'''
881. Boats to Save People

You are given:

An array people, 
    where people[i] is the weight of the i-th person.
An integer limit,
    representing the maximum weight a boat can carry.
Each boat can carry at most two people at the same time, 
    as long as their combined weight does not exceed limit.
The goal is to return the minimum number of boats needed to transport everyone.
'''
#
# def boats(people, limit):
#     people.sort()
#
#     res = 0
#     l, r = 0, len(people) - 1
#     while l <= r:
#         remain = limit - people[r]
#         r -= 1
#         res += 1  # one boat per cycle
#         if l <= r and remain >= people[l]:  # number left in limit is larger than people[l]:
#             l += 1   # this add the smallest to the boat
#
#     return res
#
#
#
# # people = [1,2]
# # limit = 3
# # Output: 1
# #
# people = [3,2,2,1]
# limit = 3
# # Output: 3
# #
# # people = [3,5,3,4]
# # limit = 5
# # Output: 4
# print(boats(people,limit))








































