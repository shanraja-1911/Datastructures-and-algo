# Problem : Reverse a given string 

val=" Hi My name is Shan"

# 1. Brute force approach ( treat the problem as a an array)




 # Solution is O(n)

def reverse(val):
  arr=list(val)
  for index in range(int(len(arr)/2)):
    temp=arr[index]
    arr[index]=arr[len(arr)-1-index]
    arr[len(arr)-1-index]=temp
  return "".join(arr)


print(reverse(val))

