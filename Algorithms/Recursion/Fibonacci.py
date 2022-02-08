# Get the Fibonacci recursively

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



if __name__=='__main__':

  print(Fibonacci_rec(10))