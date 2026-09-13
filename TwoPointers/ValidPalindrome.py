"""
Valid Palindrome - String?
"""

class Solution:
    """
    Task gives us the input string. We must find our whether that string is valid Palindrome or not. 
    In other words, the string should be read exactly the same in both directions.
    """

    def isPalindrome(self, s: str) -> bool:
        """
        We have seen TC: O(n), MC: O(n) approach.
        But the best one: TC: O(n), MC: O(1) approach.

        How can we achieve that?
        Well "Two pointers" approach is the one that allows us
        to avoid allocating extra memory for the string, 
        and allows us to inspect the string "IN-PLACE".

        There is also the concept of being "Alpha-Numeric",
        meaning contains only Letters and numbers.
        """
        # First pointer is at the beginning of the input string
        left = 0
        # Second pointer starts at the end of the input string
        right = len(s) - 1
        # And they keep moving closer to each other!

        # While those two pointers do not cross each other
        while left < right:
            # And if character from beginning range not alphanum
            while left < right and not s[left].isalnum():
                # Move pointer by one to the right
                left += 1
            # And if character from end range not alphanum
            while left < right and not s[right].isalnum():
                # Move the pointer to the left by one
                right -= 1

            # Turn the characters to the lowercase, 
            # and then compare them for equality
            if s[left].lower() != s[right].lower():
                # If at any point, the characters are not same
                # we return False - not a palindrome.
                return False

            # If our characters were the same, we move pointers
            left += 1
            right -= 1
            
        # If we reach here, then the string is a palindrome
        return True 

"""
Conclusion:

Approach 2:

Two pointer approach.

Memory Complexity:
1. O(1), no allocation of the entire string.
2. Only allocating two integer pointers O(1).

Time Complexity:
1. O(n) - iteration over the entire string once.

Approach 1:

Memory Complexity:
1. Creating a cleaned copy O(n)
2. Creating reversed copy O(n)

Overall: O(n) + O(n) => O(2n) => O(n), we drop the constants

Time Complexity:
1. Creating a reversed copy also requires iteration over the 
each character of the string, so O(n)

Solution:
    def isPalindrome(self, s: str) -> bool:
        # Creating a new string of the length possibly O(n)
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        
        # Creating a reversed version and comparing
        return cleaned == cleaned[::-1]


Note: Two pointers approach should be learned to be able to 
react O(1) Memory Complexity, meaning current solution is not the
most optimal.

"""