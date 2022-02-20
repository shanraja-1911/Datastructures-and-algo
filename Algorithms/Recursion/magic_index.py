# Find the index in an array where the index == value in the array of sorted distinct numbers

# Lets start with the basic approach where we go over the array and return the value that meets the index ; 
# Time complexity O(n)

def magic_index(arr):
  for i in range(len(arr)):
    if i==arr[i]:
      return i
    
  return -1 

# recursion - Binary search tree

def magic_index_rec(arr):

  mid=int(len(arr)/2)
  print(mid,arr)

  if len(arr)>0:
    if (arr[mid]==mid):
      return arr[mid]
      
    elif mid>arr[mid]:
      return magic_index_rec(arr[mid+1:])
      
    elif mid<arr[mid]:
      return magic_index_rec(arr[:mid])
  
  return -1 

  



if __name__=='__main__':
 #print(magic_index([-1,0,1,2,4,10]))
  print(magic_index_rec([-1,0,1,2,4,10]))
  