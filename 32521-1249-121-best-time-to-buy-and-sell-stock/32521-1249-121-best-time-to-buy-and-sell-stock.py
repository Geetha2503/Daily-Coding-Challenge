class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices: 10 9 8 7 6 5 ---> return 0
        days:    0 1 2 3 4 5
                        (17, 5)
        cur_prof = max(cur_prof, pre_prof)
        prices: 10 12 3 5 8 20 5
        days:    0  1 2 3 4  5 6 

        '''
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
