class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        for i in range(1,num+1):
            di = str(i)
            ds = 0
            for j in range(len(di)):
                ds += int(di[j])
            if ds%2 == 0:
                c += 1
        return c