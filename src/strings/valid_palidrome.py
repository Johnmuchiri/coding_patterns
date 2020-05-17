
"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        fixed_string = ""
        for i in s:
            if i.isalnum():
                fixed_string += i.lower()
        print(fixed_string)
        start = 0
        end = len(fixed_string) - 1

        while start < end:
            print(start, end)
            if fixed_string[start] != fixed_string[end]:
                return False
            start += 1
            end -= 1

        return True


