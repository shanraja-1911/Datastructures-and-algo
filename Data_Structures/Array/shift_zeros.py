nums=[1,0,2,3,0,12]


current_index=0
for i in range(len(nums)):

  if nums[i]!=0:
    nums[current_index]=nums[i]
    current_index+=1

for i in range(current_index,len(nums)):
  nums[i]=0

print(nums)