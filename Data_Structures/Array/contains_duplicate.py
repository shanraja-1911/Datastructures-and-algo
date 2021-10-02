# given an array return true if the same element appears twice

nums=[3,3]
nums_1=[1,2,3,4]


# 1) Brute force approach O(n^2)
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    if nums[i]==nums[j]:
      print( " 1)True" )

print("1) False") 


# 2) hash_map approach o(n)

hash_map={}
hash_map[nums[0]]=0
print(hash_map,3 in hash_map)

for index,x in enumerate(nums[1:]):
  print(index,x)

  if x in hash_map.values():
    print(True) 
  hash_map[x]=index
print(False)