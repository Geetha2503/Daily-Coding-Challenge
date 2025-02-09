class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        r = list(range(len(s)))

        def get_repr(n):
            if r[n] == n:
                return n
            
            r[n] = get_repr(r[n])
            return r[n]
        
        def unite(a, b):
            r_a = get_repr(a)
            r_b = get_repr(b)

            r[r_b] = r_a
        
        # build DSU
        for a, b in pairs:
            unite(a, b)
        d = defaultdict(lambda : [])

        # for each parent get sorted alphabet
        for pos, v in enumerate(r):
            # compact
            r[pos] = get_repr(r[pos])            
            d[r[pos]].append(s[pos])

        for k in d:
            d[k].sort(reverse = True)
        
        #print(d.items())
        #print(r)
        ret = []
        for pos, v in enumerate(s):
            # get parent
            #parent = get_repr(r[pos])
            #d[parent].sort()
            ret.append( d[r[pos]].pop())
            
        return "".join(ret)

        