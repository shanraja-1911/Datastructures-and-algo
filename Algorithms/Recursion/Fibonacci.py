# Get the Fibonacci recursively
# This approach takes O(2^N) and complex , istead we can store the values
def Fibonacci_rec(number):
  #print(number)
  if number ==0:
    return 0 
    
  elif number ==1:
    return 1
    
  elif number ==2:
    return 1
    
  elif number > 2:
    return Fibonacci_rec(number-2)+Fibonacci_rec(number-1)


# things to remember 
#- Store all the return value to memo
#- Make an array of NULL of size number + 1
#- 

def Fibonacci_mem(number,memo):

  if memo[number] is not None:
    return memo[number]
  
  if (number==0):
    fib_num= 0 
  
  if (number==1)| (number==2):
    fib_num =1
# If the call has already been executed then return the stored value 
  

# Else calculate the fibonacci and store it in the memo
  else :
    fib_num = Fibonacci_mem(number-1,memo)+Fibonacci_mem(number-2,memo)
  
  memo[number]=fib_num
  return fib_num

#################################### Bottom up approach ##################################

def Fibonacci_btm_up(number):
  memo=[None]*(number+1)
  if number==0:
    return 0
  if (number==1)|(number==2):
    return 1
  memo[0]=0
  memo[1]=1
  memo[2]=1
  for x in range(3,number+1):
    memo[x]= memo[x-1]+memo[x-2]
  
  return memo[number]




if __name__=='__main__':

  test_num=10
  print(Fibonacci_rec(test_num))
  print(Fibonacci_mem(test_num,[None]*(test_num+1)))
  print(Fibonacci_btm_up(test_num))