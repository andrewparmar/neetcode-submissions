import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = max(piles)
        l, u = 1, sum(piles)

        lowest = float("inf")

        while l <= u:
            rate = (l + u) // 2
            print(l, u, rate)
            if self.hoursToEat(rate, piles) > h:
                # invalid rate, raise floor
                l = rate + 1
            else:
                # valid rate, optimize
                lowest = min(lowest, rate)
                u = rate - 1

        return lowest

    def hoursToEat(self, rate, piles):
        total = 0
        for pile in piles:
            total += math.ceil(pile/rate)
        return total
        

        