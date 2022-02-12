# N be the number of steps and x=[1,2,..n] be the number of steps a person could take ,
# What is the possible number of combinations 

##### First lets try to solve the problem recursively where x=[1,2]

### looks like fib 
def num_ways(n,x):

  if (n==0)|(n==1):
    return 1
  else :
    total_ways=0
    for val in x:
      if n-val>0:
        total_ways+=num_ways(n-val,x)
    return total_ways
    

##### Try to solve it using memoization ######

def num_ways_memo(n,x,memo):
  if memo[n] is not None:
    return memo[n]
  
  if (n==0)|(n==1):
    memo[n]=1
    return 1
  
  
  else :
    total_ways=0
    for val in x:
      if n-val>0:
        total_ways+=num_ways_memo(n-val,x,memo)
      
    memo[n]=total_ways
  return total_ways

#################### Bottom up approach #################


def num_ways_btm(n,x):
  if (n==0):
    return 1
  memo=[None]*(n+1)
  memo[0]=1
  for num in range(1,n):
    total_ways=0
    
    for val in x:
      
      if num-val>=0:
        #print(num-val)
        total_ways+=memo[num-val]


    memo[num]=total_ways
  return memo[n-1]




if __name__=='__main__':

  num=4
  test=[1,2]
  memo=[None]*(num+1)
  print(num_ways(num,test))
  print(num_ways_memo(num,test,memo))
  print(num_ways_btm(num,test))

