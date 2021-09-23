

nums=[3,2,4]
target=6

def two_sum(nums,target):

  hash_map={}
  for key,val in enumerate(nums):
    print(key,val)
    if (target-val) in hash_map:
      return [hash_map[target-val],key]

    hash_map[val]=key


print(two_sum(nums,target))