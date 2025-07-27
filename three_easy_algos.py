# COMMENTS TO HELP CLARIFY THE SOLUTIONS.
# 1. Two-Pointer Technique
# Pointer Example 1: Reverse String
def reverse_string(s):
    # Convert the string to a list to allow modification (strings are immutable in Python)
    s = list(s)
    left, right = 0, len(s) - 1

    # Use two pointers, one starting from the beginning and one from the end
    while left < right:
        # Swap characters at the pointers
        s[left], s[right] = s[right], s[left]
        # Move the pointers towards the center
        left += 1
        right -= 1

    return ''.join(s)  # Convert list back to string

# Explanation: By using two pointers, we swap characters in place until the pointers meet in the middle.
print(reverse_string("hello"))  # Output: "olleh"

# Pointer Example 2: Valid Palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Move `left` to the next alphanumeric character or stop if `left` meets `right`
        if not s[left].isalnum():
            left += 1
            continue

        # Move `right` to the previous alphanumeric character or stop if `right` meets `left`
        if not s[right].isalnum():
            right -= 1
            continue

        # Compare characters, ignoring case
        if s[left].lower() != s[right].lower():
            return False

        # Move pointers towards the center
        left += 1
        right -= 1

    return True



# Explanation: We use two pointers to skip over non-alphanumeric characters and check for palindrome properties.
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True


# 2. Hash Maps / Frequency Counting
# Example 1: First Unique Character in a String
def first_uniq_char(s):
    # Use a dictionary to count the frequency of each character
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with a frequency of 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1  # Return -1 if no unique character exists

# Explanation: By counting frequencies first, we can quickly identify the first unique character in linear time.
print(first_uniq_char("leetcode"))  # Output: 0 (index of 'l')



# Example 2: Valid Anagram
def is_anagram(s, t):
    # Anagrams must have the same length
    if len(s) != len(t):
        return False

    # Use a dictionary to count characters in the first string
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract counts based on the second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


# Explanation: We count characters for both strings and ensure they match, which makes it easy to verify an anagram.
print(is_anagram("listen", "silent"))  # Output: True

# 3. Efficient String Manipulation & Parsing
# Example 1: String to Integer (atoi)
def my_atoi(s):
    s = s.strip()  # Remove leading/trailing spaces
    if not s:
        return 0

    # Initialize variables
    index, sign, total = 0, 1, 0

    # Check if the first character is a sign
    if s[0] in "+-":
        sign = -1 if s[0] == '-' else 1
        index += 1

    # Convert characters to integer until a non-digit is found
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        total = total * 10 + digit
        index += 1

    return total * sign

# Explanation: We handle leading spaces, signs, and non-digit characters, mimicking the behavior of `atoi`.
print(my_atoi("  -42"))  # Output: -42

# Example 2: Implement strStr() (Finding Substring)
def str_str(haystack, needle):
    # Return 0 if needle is an empty string
    if not needle:
        return 0

    # Iterate over possible starting points in haystack
    for i in range(len(haystack) - len(needle) + 1):
        # Compare substring with needle
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1  # Return -1 if the substring is not found

# Explanation: We use slicing to compare each possible substring in the haystack with the needle.
print(str_str("hello", "ll"))  # Output: 2

