x=[1,2,3,4]
y=[1,2,4,4]
z=[6,4,3,2,1,7]

target =9

# Brute force approach 
def sum_1(arr,target):

  for val_1 in range(len(arr)):
    for val_2 in range(val_1+1,len(arr)):

      if arr[val_1]+arr[val_2]==target:
        print(arr[val_1],arr[val_2])
        return True 
  return False 

#print(sum_1(y,target))

# the time complexity is high O(n^2)

def sum_2(arr,target):

  complement=[]

  for val in arr:
    if target-val in complement:
      print(val,target-val)
      return True
    complement.append(val)
  return False

print(sum_2(z,target))

