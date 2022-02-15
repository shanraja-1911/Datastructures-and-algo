# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



def two_sum(lst,target):
  hash_lst={}

  for index,val in enumerate(lst):
    if target-val in hash_lst:
      return [index,hash_lst[target-val]]
    hash_lst[val]=index



if __name__=='__main__':
  print(two_sum([2,7,11,15],9))