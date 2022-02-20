# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


nums=[1,2,3]

def subset(nums):
  print(nums)

  if len(nums)==0:
    return []
  elif len(nums)==1:
    return nums

  else:
    print(nums[0])
    val=[nums[0]].append(subset(nums[1:]))

  return val

if __name__=='__main__':

  print(subset(nums))