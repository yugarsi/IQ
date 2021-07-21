class Solution:
    '''
    Algorithm = in a single loop find the minprice and maxprofit AFTER min price hasbeen found
    '''
    #min
    def maxProfit(self, prices) -> int:
        #[10, 3, 10, 1, 2]
        maxprofit = 0
        minp = float("inf")
        for price in prices:
            if price < minp:
                minp = price  # first find minp
            elif price - minp > maxprofit:
                maxprofit = price - minp  # within same loop if you do something after,
                # it always happens after, e.g. minp is determined first then profit is calculated. i.e.
                # profit after minp is determined.

        return maxprofit