# Selection sort 

#Selection sort involves finding the minimum element in one pass through the array
#and then swapping it with the first position of the unsorted part of the array.
#Time complexity of selection sort is O(n^2) in all cases


test =[1000,1234,356,12,34,56,7,64567,36,453623,6,3467,2]



def selection_sort(nums):
  len_nums=len(nums)
  

  for x in range(len_nums):
    # For each loop set the samllest value to x
    smallest_val=nums[x]
    #index=x
    for y in range(x+1,len_nums):
      # if the nums[y] is smaller than the value in num[y], the reset the samllest val and index 
      if nums[y]<smallest_val:
        smallest_val=nums[y]
        nums[y]=nums[x]
        nums[x]=smallest_val

        
    print(nums, nums[x],nums[y],smallest_val)
    
    
        
        #print(temp,nums[y],nums)
        

      
  return nums



if __name__=='__main__':
  print (selection_sort(test))