class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        x = [0]*len(nums)
        for i in range(len(nums)):
            x[i]=int(nums[i])
        x.sort()
        return str(x[len(x)-k])
