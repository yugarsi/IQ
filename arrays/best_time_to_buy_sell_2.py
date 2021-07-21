class Solution(object):
    # best time to buy sell 2
    # 7, 1, 5, 3, 6, 4
    # sum of all (valleys - peak) will always be greater than
    # one cumulative valley -peak transaction
    # O(N) and O(1) solution
    def maxProfit(self, prices):
        total = 0
        valley = prices[0]
        peak = prices[0]
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i + 1] <= prices[
                i]:  # while decreasing continue to increment i to find valley index
                i += 1
            valley = prices[i]

            while i < len(prices) - 1 and prices[i + 1] >= prices[
                i]:  # while increasing continue to increment i to find peak index
                i += 1
            peak = prices[i]
            total += peak - valley

        return total