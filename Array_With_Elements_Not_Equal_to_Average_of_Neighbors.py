class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=1
        while i < len(nums)-1:
            if (nums[i-1] + nums[i+1]) / 2 == nums[i]:        #compare nums[i] to the average of it's previous and it's next elements
                tmp=nums[i]                                         #swap nums[i] with the element next to it 
                nums[i]=nums[i+1]
                nums[i+1]=tmp
            if (nums[i-2] + nums[i]) / 2 == nums[i-1]:        #check for error caused by current swapping on previous elements
                i-=1
            else:
                i+=1
        return nums
                
