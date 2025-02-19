

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        string = 'interview' (n,t,r,v,w) -- n--> 1 
        
        output: 1
        
        s: 'gggggeeeetttthhhhaaa' output:-1
        
        {'i':2, 'n':1 ..}
        '''
        char_count = [0] * 26  # Array to store frequency (fixed size, O(1) space)
        
    # Step 1: Count occurrences
        for char in s:
            char_count[ord(char) - ord('a')] += 1  # Convert character to index

        # Step 2: Find first non-repeating character
        for index, char in enumerate(s):
            if char_count[ord(char) - ord('a')] == 1:
                return index

        return -1
                