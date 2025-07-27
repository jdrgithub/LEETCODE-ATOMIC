# TWO POINTER TWO

# Given a string s, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# EXAMPLE
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Input: s = "race a car"
# Output: false


def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left <= right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].ower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True


""" 
Given a sorted array of integers nums and an integer target, 
return True if there exist two numbers such that nums[i] + nums[j] == target.

Return False if no such pair exists.

Examples:
"""
nums = [1, 2, 4, 6, 10]
target = 8
# True  # 2 + 6
"""
nums = [1, 2, 3, 9], target = 8  
False  # no such pair

"""

"""
Given a sorted array nums, remove the duplicates in-place
such that each unique element appears only once. 
Return the number of unique elements.

You must use O(1) extra space and modify the array in-place.

Examples:
"""
nums = [1, 1, 2]
"""
Output: 2  
nums is now [1, 2, _]  # (the underscore can be anything)

Input: nums = [0,0,1,1,1,2,2,3,3,4]  
Output: 5  
nums is now [0, 1, 2, 3, 4, _, _, _, _, _]     

"""


def remove_duplicates(nums):
    write = 1

    for read in range(len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write


"""
Given a sorted array of integers nums (which may include negatives),
return a new array of the squares of each number, also sorted in non-decreasing order.

Examples:
"""
nums = [-4, -1, 0, 3, 10]
"""
Output: [0, 1, 9, 16, 100]

Input: nums = [-7, -3, 2, 3, 11]  
Output: [4, 9, 9, 49, 121]
"""


def square_and_sort(nums):
    n = len(nums)
    left, right = 0, n - 1
    result = [0] * n
    pos = n - 1

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1

        pos -= 1

    return result


""" 
Problem 4: Move Zeros

Given an array nums, move all the zeros to the end 
while maintaining the relative order of the non-zero elements. 
You must do this in-place (no new array), and use the two-pointer technique.

🔸 Example:
"""
nums = [0, 1, 0, 3, 12]
""" 
Output: [1, 3, 12, 0, 0]

Constraints:
Modify the array in-place.
Try to do it in one pass if possible (or at least O(n) time)
Don't use a sort.
"""


def move_zeros(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums


print(move_zeros(nums))


"""

## 🧩 Problem 5: Reverse a String In-Place
Write a function that reverses an array of characters 
**in-place** using the two-pointer technique. Do not return a new array.

### Constraints:

* Modify the input list directly
* You must use the two-pointer approach — not `[::-1]`, not `reverse()`

### 🔸 Example:
"""
s = ["h", "e", "l", "l", "o"]
"""
Output: ["o", "l", "l", "e", "h"]

Input:  ["H", "a", "n", "n", "a", "h"]  
Output: ["h", "a", "n", "n", "a", "H"]
"""


def reverse_string_array(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


print(reverse_string_array(s))


"""
Problem 6: Find a Pair with Target Difference

Given a sorted array nums and an integer k, 
return True if there exists a pair of numbers 
such that the difference between them is exactly k
"""

nums = [1, 3, 5, 7, 9]
k = 4
"""
Output: True  # 5 - 1 = 4 or 7 - 3 = 4

Input: nums = [1, 2, 3, 4, 5], k = 10  
Output: False
"""


"""
Problem 6: Find a Pair with Target Difference

Given a sorted array nums and an integer k, 
return True if there exists a pair of numbers 
such that the difference between them is exactly k.
"""
nums = [1, 3, 4, 9]
k = 6

"""
Output: True  # 5 - 1 = 4 or 7 - 3 = 4

Input: nums = [1, 2, 3, 4, 5], k = 10  
Output: False
"""


def diff(nums, k):
    left, right = 0, 1

    while right < len(nums):
        diff = nums[right] - nums[left]

        if right == left:
            right += 1
        elif diff == k:
            return True
        elif diff < k:
            right += 1
        else:
            left += 1

    return False


print(diff(nums, k))