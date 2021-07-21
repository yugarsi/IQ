class Solution:
    '''
    cut cake horizontal and vertical
    Let's use the first test case in the problem description as an example.
    If we were to only apply the horizontal cuts [1, 2, 4], we will end up with 4 pieces of cake,
    all with width = 4. Take the piece of cake with height = 2 between the cuts at 2 and 4,
    and make any vertical cut you want - notice that the height will always be 2.

    The same logic can be applied when considering the vertical cuts first -
    we will have many pieces of cake with height = h and varying widths.

    '''

    # O(MLOGM) + NlogN , O(1) space
    def maxArea(self, height: int, width: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Start by sorting the inputs
        horizontalCuts.sort()  # no need to sort if already sorted
        verticalCuts.sort()

        # Consider the edges first
        # initialize max height = first cut from top or bottom cut from below
        max_height = max(horizontalCuts[0], height - horizontalCuts[-1])

        print(max_height)
        for i in range(1, len(horizontalCuts)):
            # horizontalCuts[i] - horizontalCuts[i - 1] represents the distance between
            # two adjacent cuts = > possible cut piece
            # and thus a possible height
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])

        # Consider the edges first
        max_width = max(verticalCuts[0], width - verticalCuts[-1])

        for i in range(1, len(verticalCuts)):
            # verticalCuts[i] - verticalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible width
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        # Python doesn't need to worry about overflow - don't forget the modulo though!
        return (max_height * max_width) % (10 ** 9 + 7)