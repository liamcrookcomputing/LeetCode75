class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        kidWithCandies = 0

        for x in range(len(candies)):
            kidWithCandies = candies[x] + extraCandies
            result.append(kidWithCandies >= max(candies))

        return result
    