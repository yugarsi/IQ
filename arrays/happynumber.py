# Happy number,
# Check if sum of squares of number = 1 in loop

class Solution:
    # This functionn is O(no of digits), since int can have max 13 digits => O(13) = O(1) constant time
    def splitAndSquare(self, number):
        s = 0
        for i in number:
            s += int(i) * int(i)
        return s

    # solution using a set = time complexity is O(log n) where n is the number
    # it is becase if n  2 digit, maxsum = 9^2 + 9^2 = 81, n is 3 digit
    # maxsum = 9^2 + 9^2 + 9^2 = 243, n 4digit = 324
    # is 13 digits maxsum = 1053.  (the loop will run log n times)

    # Space complexity = log(n) same logic
    def isHappyUsingSet(self, n: int) -> bool:
        hset = set()

        while n != 1:

            hset.add(n)
            n = self.splitAndSquare(str(n))
            if n in hset:
                return False

        return True

    # APPROACH 2 = two fast and slow pointer approach
    def getNext(self, number):
        s = 0
        for i in number:
            s += int(i) * int(i)
        return s

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getNext(str(n))
        while fast != 1 and slow != fast:
            slow = self.getNext(str(slow))  # increment slow once
            fast = self.getNext(str(self.getNext(str(fast))))  # increment fast twice

        return fast == 1  # if fast == 1 return True else False