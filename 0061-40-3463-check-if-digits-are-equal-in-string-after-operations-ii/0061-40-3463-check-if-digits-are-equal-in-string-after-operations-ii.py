class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def cal(a, mod):
            count = 0
            while a > 0 and a % mod == 0:
                count += 1
                a //= mod
            return a % mod, count

        def test(mod):
            n = len(s)
            res = 0
            r = 1
            c = 0
            for i in range(n - 1):
                if c == 0:
                    res += r * (int(s[i]) - int(s[i + 1]))

                rr, cc = cal(n - 2 - i, mod)
                r = r * rr % mod
                c += cc

                rr, cc = cal(i + 1, mod)
                r = r * pow(rr, mod - 2, mod) % mod
                c -= cc
            return res % mod == 0
        return test(2) and test(5)