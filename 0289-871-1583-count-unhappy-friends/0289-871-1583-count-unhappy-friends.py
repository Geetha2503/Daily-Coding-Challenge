class Solution:
	def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

		sc = defaultdict()

		for u,v in pairs:
			
			sc[u],sc[v] = (preferences[u][:preferences[u].index(v)],
										 preferences[v][:preferences[v].index(u)])
			
		return sum(any(u in sc[v] for v in sc[u]) for u in range(n))