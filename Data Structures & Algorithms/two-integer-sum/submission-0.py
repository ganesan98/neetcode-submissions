class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            curr = nums[i]
            comp = target - curr

            if comp in d:
                return [d[comp],i]
            d[curr]=i