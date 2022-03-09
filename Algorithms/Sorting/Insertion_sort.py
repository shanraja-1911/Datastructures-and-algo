
# Similar to how the human brain thinks
#In Insertion sort, for the first iteration we fix the first element, assuming it is at its correct position
#Then we loop through the rest of the elements and insert them in their correct positions, with respect to the alreay sorted part of the array
#Time complexity is O(n^2) in worst case


test=[0,0,0,-1,2,-1233]

def insertion_sort(nums):

  # Start looping from 1 to the length of nums 
  for x in range(1,len(nums)):
    print(nums)
    # let the size of y be the lenght of the subset of nums , spliced by x
    y=len(nums[:x])

    #print(x,y,nums[:x])
    # While the subset if atleast of size 2 i.e nums[0] and nums [1] exists
    while y>0:
      # If the later is greater than the former , then swap 
      if nums[y-1]>nums[y]:
        #print(nums,nums[y-1],nums[y])
        temp=nums[y-1]
        nums[y-1]=nums[y]
        nums[y]=temp
        y-=1

      # If the number is already in the right place , then we exit
      elif nums[y]>nums[y-1]:
        #print('early exit')
        y=0

      else :
        # If the value is not big enough then it shoulf just stay at its place
        #print('not big')
        y=0

  return nums 


if __name__=='__main__':

  print(insertion_sort(test))
      