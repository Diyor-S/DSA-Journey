"""
Not one , but a group of Anagrams. 
"""

class Solution:
    """
    Input: list[str]
    Output: list[list[str]]

    We need to group the strings that can form the same word.
    
    One thing I noticed is that, the length of our ouput list is    gonna be equal to the number of distinct words.

    That judging by the result, whichever word we come across first that is gonna be the anchor towards which we are gonna look for word formation.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a hash table
        hash_table = {}

        # iterating over the string
        for string in strs:
            # Initializing the list of 26 English letters filling with zeros
            count_chars = [0] * 26 

            # Iterating over the chars of the string
            for ch in string:
                # ord() - function in Python returns ASCII value of the 
                # unicode character!
                # We are subtrating whatever character we are iterating over
                # from the starting position which is represented by the 
                # 'a' - 0.
                # We are increasing that number's value by one.
                # This is actually NEW technique I learned, we are not having 
                # keys like with hash table, but we are implicitly using 
                # the values of the list, to represent the count - number of appearances of the characters.
                count_chars[ord(ch) - ord('a')] += 1
            print(f"For string: {string}, char_count: {count_chars}")

            # And then we are converting the list of count numbers into the 
            # string to use that string as the dictionary key.
            # so basically each key would be unique for unique word,
            # meaning act tac would go to the same key, because their count
            # number list would be identical, even tho the order is different.
            key = ",".join([str(c) for c in count_chars])

            print(f"Key for {string}: {key}")

            # Check whether this key is present, if not,
            # then initialize it with value storing the list
            if key not in hash_table:
                hash_table[key] = []

            # We just add the string under the key
            hash_table[key].append(string)

        # Convert the dictvalues instance back to the list
        return list(hash_table.values())


"""
Conclusion about the approach with "ord".

Memory Complexity:

1. Used hash_table O(n)
2. Used list with 0-26 letters (count numbers) O(n_max=26) -> O(1).
3. Used list to store each distinct word, O(n * k), n - number of strings,
k - max length

Overall: O(n) + O(1) + O(n * k) => O(n * k) memory complexity.

Time Complexity: 

1. Iterating over the strings O(n)
2. Iterating over the characters O(k)

Overall: O(n * k)
"""


"""
Conclusion:

Memory Complexity:

O(n) because we are initializing list, hash_table, O(n + n) => O(2n) => O(n)

Time Complexity:

1. We are iterating over the strings list O(n).
2. Within each iteration of the string, we are iterating over the final_list
This means that, if there are no anagram and but there are all distinct values
Then we have to move O(n) for strings and O(n) for iteration over all values within final list which results in O(n^2).


Solution:

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Base case
        if len(strs) == 1:
            return [strs]
        
        # Prepare the final list
        final_list: list[list[str]] = []
        
        # Iterate over the give input
        for string in strs:
            placed = False

            # If there are any lists added, we must compare our current string
            # with the first string of each of those lists.
            for group in final_list:
                # If they are anagrams
                if self.is_anagram(string, group[0]):
                    # then put into one list
                    group.append(string) 
                    placed = True
                    break

            # If there are no groups or no anagram match at all
            # then we append our string wrapping it into a list
            if not placed:
                final_list.append([string])

        # At the end, just return the ready list    
        return final_list

    # Algorithm that I learned from solving "Valid Anagram" problem
    def is_anagram(self, s, t):
        # Base case
        if len(s) != len(t):
            return False

        # The idea is to use hashtables
        # to count the character appearances
        char_counts = {}

        # First fill up the hash_table with characters and their count from the
        # first string
        for ch in s:
            if ch not in char_counts:
                char_counts[ch] = 1
            else:
                char_counts[ch] += 1
            
        # And each time we see the chacter same  as character in the first string
        # We subtract the count, and also at the same time 
        # we should check whether our count now is under zero or not
        # that means that there are actually more same characters in the 
        # second string and they are already not anagrams.
        for ch in t:
            if ch not in char_counts:
                return False
            else:
                char_counts[ch] -= 1

                if char_counts[ch] < 0:
                    return False
        
        return True

Result:
TimeLimit Exceeded...
"""