class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Creating a new string of the length possibly O(n)
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        
        # Creating a reversed version and comparing
        return cleaned == cleaned[::-1]

"""
Conclusion:

Memory Complexity:
1. Creating a cleaned copy O(n)
2. Creating reversed copy O(n)

Overall: O(n) + O(n) => O(2n) => O(n), we drop the constants

Time Complexity:
1. Creating a reversed copy also requires iteration over the 
each character of the string, so O(n)

Note: Two pointers approach should be learned to be able to 
react O(1) Memory Complexity, meaning current solution is not the
most optimal.

"""