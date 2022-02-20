### Bubble Sort#


test=[1,4,2,3,9,1]


# This is the simplest algorithm 

def bubble_sort(num):
  # get the length of the number of variables in the list 
  len_num=len(num)
  # no of times you wanted to run the inner check mechanism 
  for x in range(len_num):
    # Run it for the number of times you wanted to check the values 
    for y in range(len_num-1):
      # If the next number is greater than the present number 
      if num[y]>num[y+1]:
        # Swap the values
        num[y]=num[y]+num[y+1]
        num[y+1]=num[y]-num[y+1]
        num[y]=num[y]-num[y+1]
  
  return num 



if __name__=='__main__':

  print(bubble_sort(test))