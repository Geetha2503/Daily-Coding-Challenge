class Solution:
    def countBits(self, n: int) -> List[int]:
        
        '''
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's             in the binary representation of i.
        '''

        # n = len(ans_arr)+1 whcih i need to return 
        # 0, 1, 2, 3, 4 where n=4
        # 0, 01, 10, 11, 100. --> nums of 1's i need to showup that mean sum(ans_arr[i])
        #.  ans_arr = [0, 1, 1, 2, 1]

        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
