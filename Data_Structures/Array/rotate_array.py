# given an array and a rotate num, try to rotate the array 


# Using a temperoary space 

temp_space=[]

arr=[1,2]
rot_num=5



def rotate(arr,rot_num):
  if len(arr)==1:
    return arr
  elif len(arr)-rot_num<=0:
    while rot_num>len(arr):
      rot_num=abs(len(arr)-rot_num)
    
  temp_space=arr[:len(arr)-rot_num]
  for x in range(rot_num):
    arr[x]=arr[-rot_num+x]
  arr[rot_num:]=temp_space
  return arr


print(rotate(arr,rot_num))

