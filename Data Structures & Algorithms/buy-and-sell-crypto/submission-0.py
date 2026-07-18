class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minz = prices[0]
        maxz = 0
        for i in prices:
            if i < minz:
                minz = i
            if i - minz > maxz:
                maxz = i - minz          
        
        return maxz