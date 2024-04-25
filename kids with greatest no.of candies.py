class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	          return (m := max(candies), [*map(lambda x: x + extraCandies >= m, candies)])[1]
