## the problem statement given here is to merge two sorted array 

x=[1,4,6,7,9]
y=[1,2,3,5,9,10,11,12,13]

new_arr=[]
# 1. Brute Force type of approach  O(n^2)
j=0

# loop through the first array 
for i in range(0,len(x)):

  print(i,j)

# Check if the value of the first array is greater than the value in the second 
# iF yes append it to the list 
  if x[i]<y[j]:
    new_arr.append(x[i])
    
# If both the array contain equal values then append both and increment both 
  elif x[i]==y[j]:
    new_arr.append(x[i])
    new_arr.append(y[j])
    if j<(len(y)-1):
      j+=1
  
# If second array has higher value keep appending the second array till the condition fails 
  elif x[i]>y[j]:

    while ((x[i]>y[j]) and (j<(len(y)-1))):

      new_arr.append(y[j])
      if (j<(len(y)-1)):
        j+=1  
    new_arr.append(x[i])
  

# IF the first array is smaller than the second then add the remaining content to the list
if j<len(y)-1:
  new_arr.extend(y[j:])

print(new_arr)

# 2. Mapping type approach 

x=[1,4,6,7,9]
y=[1,2,3,5,9]

x_p=0
y_p=0
n_p=0
flag_1=0

new_arr=[]

while((x_p<len(x)) and (y_p<len(y))):
  #print(x_p,y_p)

  if x[x_p]<y[y_p]:
    new_arr.append(x[x_p])
    x_p+=1

  elif x[x_p]==y[y_p] :
    new_arr.append(x[x_p])
    new_arr.append(y[y_p])
    x_p+=1
    y_p+=1
  
  elif x[x_p]>y[y_p]:
    new_arr.append(y[y_p])
    y_p+=1

  if x_p==len(x)-1:
    flag=1


if flag==1:
  new_arr.extend(y[y_p:])
else :
  new_arr.extend(x[x_p:])
  
print(new_arr)
  

  
  
  


print(new_arr)






  

