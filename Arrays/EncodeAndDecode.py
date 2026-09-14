from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i # start with digit: j = 0

            while j < len(s) and s[j].isdigit():
                # Get to the '#' 
                j += 1
            
            # Get the length without '#', s[0,1] => s[0]
            length = int(s[i:j])

            start = j + 1
            end = start + length

            res.append(s[start:end])

            i = end
        
        return res
