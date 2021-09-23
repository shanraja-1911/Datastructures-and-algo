# Maximum sub array problem

nums=[8,-19,5,-4,20]

# Largest sum = 6

# Brute force technique (O(n^2))

current_sum=0
best_sum=max(nums)
for i in range (0,len(nums)):
  for j in range(i,len(nums)):

    current_sum= sum(nums[i:j+1])
    best_sum=max(best_sum,current_sum)
  
print(best_sum)

# using while loop 
# current_sum=0
# first_pass=0
# flag=0
# lp=0
# rp=len(nums)
# if len(nums)==1:
#   print(nums[0])
# while lp<rp:
#   current_sum=sum(nums[lp:rp])
#   print(current_sum)
#   if first_pass==0:
#     best_sum=max(nums)
#     first_pass=1
#   best_sum=max(current_sum,best_sum)
#   print(lp,rp,nums[lp:rp])
#   if flag==0:
#     lp+=1
#     flag=1
#   else:
#     rp-=1
#     flag=0


# print(best_sum)

# Efficient algorithm 
current_sum=0
best_sum=max(nums)

for n in nums:
  if current_sum<0:
    current_sum=0
  current_sum+=n
  best_sum=max(current_sum,best_sum)

print(best_sum)