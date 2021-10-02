# given a set of array it should return the first recurring character 

nums=[2,2,4,5]

# Brute force approach with an exit clause O(n^2)


def rec(nums):
  hash_table={}

  for index,val in enumerate(nums):

    if val in hash_table:
      return val 
    hash_table[val]=index
  return "No val Found"

print(rec(nums))

