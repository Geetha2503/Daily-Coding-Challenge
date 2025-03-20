class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(self, start, end):
            # Reverse elements in the array between start and end inclusive
            while start < end:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(self, 0, len(s) - 1)
        
        # Step 2: Add a temporary space at the end for easier word detection
        s.append(" ")
        
        # Step 3: Reverse each word
        l = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverse(self, l, i - 1)
                l = i + 1  # Move to the next word start
        
        # Step 4: Remove the temporary space
        s.pop()