# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        len_num=len(nums)
        if (sum(nums[1:])==0):
            return 0

        for x in range(1,len_num):
            #print(nums[:x-1],nums[x:])
            sum_bef=sum(nums[:x-1])
            sum_aft=sum(nums[x:])
            if sum_bef==sum_aft:
                return x-1
        
        if (sum(nums[:len_num-1])==0):
            return len_num-1
        
        return -1
            
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sum_count=0
        
        for x in range(0, len(nums)):
            if sum_count == sum(nums[x+1:]):
                return x
            else :
                sum_count+=nums[x]
            
        return -1