x=['a',None,'c']
y=['x','y',None]


# brute force approach 
def common_val(x,y):
  
  for val_x in x:
    #print(val_x)
    for val_y in y:
      if val_x==val_y:
        #print('value found')
        return True 
  return False 

# this is a brute force approach 
ans=common_val(x,y)
print(ans)

# Most of the mested loop cases can be solved by using a hash map 
# In this case the hash map is not required as well 
def common_val_2(x,y):


  for x_val in x:
    if x_val in y:
      return True 
  return False

ans_2=common_val_2(x,y)
print(ans_2)


# Now its time to think about all the possible ways the code might break 

