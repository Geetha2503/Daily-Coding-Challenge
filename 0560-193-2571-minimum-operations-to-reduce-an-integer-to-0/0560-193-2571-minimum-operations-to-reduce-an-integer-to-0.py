class Solution:
    def minOperations(self, n: int) -> int:

        from math import log2

        # Powers of 2: TC = SC = O(log2(n))
        '''
        powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
        # Why required till 131072 only? Because n <= 10^5.
        '''
        # (Good Practice) Keep it dynamic so that even if n > 10^5, code will work:
        # powers = [2**i for i in range(int(log2(n))+2)]
        powers = [1 << i for i in range(int(log2(n))+2)]

        ops = 0

        # While `n` doesn't become 0:
        while n:  # TC = O(1) because it doesn't matter what `n` is, we're directly subtracting the closest power of 2 from
            # it, so, it will fall to 0 in a couple of ops only (take a big number and check yourself to get the hang of it)

            # Find the power of 2 which is closest to n: TC = O(log2(n))
            '''
            min_diff, closest = float('inf'), None
            for p in powers:
                if abs(n-p) < min_diff:
                    min_diff, closest = abs(n-p), p
            '''
            # One-liner of above (Thanks for pointing it out @SmittyWerbenjagermanjensen):
            closest = min(powers, key=lambda p: abs(n-p))

            # (Absolute) Subtract it (the closest power of 2):
            n = abs(n-closest)

            ops += 1

        return ops