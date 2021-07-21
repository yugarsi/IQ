#Best time to buy and sell with 2 transactions
class Solution:
    # DP solution O(Nk) time and O(Nk) space
    # k = 2 special case for best time to sell with 2 transaction
    def maxProfit(self, prices) -> int:

        # build a DP array of k+1 rows (i.e) profit with k transaction
        # and n days
        k = 2
        profits = []
        # DP array will have for each day with k transactions how much is the profit

        # The logic is
        for i in range(k + 1):
            profits.append([0] * len(prices))

        for t in range(1, k + 1):
            maxsofar = float("-inf")
            for d in range(1, len(prices)):
                # option are don't sell that day
                # then the profit will be profits[t][d-1]

                # If you sell on that day then you have to choose the cheapest day to
                # to buy and maximum profit with t-1 transactions before that day

                maxsofar = max(maxsofar,
                               profits[t - 1][d - 1] - prices[d - 1])

                profits[t][d] = max(profits[t][d - 1],
                                    maxsofar + prices[d])

        # the last element will be profit with k transactions
        return profits[-1][-1]

#O(N) time  and O(1) space solution for k=2 special case
#Algorithm is find max profit with one transaction and find if you will profit by reinvesting
#as two transactions are allowed

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit