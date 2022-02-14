# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# it is found that the number of ways that a person can reach the given co-ordinates x,y = num_ways (x-1,y)+num_ways(x,y-1) & since the bot can only move along right and down , all the corner values are set as 1

# using pure recursion
def num_path(m,n):
  if (m-1==0)|(n-1==0):
    return 1
  else:
    return num_path(m-1,n)+num_path(m,n-1)

# using bottom up approach 
def num_path_memo(m,n):
  dp=[[0 for i in range(n)] for j in range(m)]
  for x in range(0,m):
    for y in range(0,n):
      
      if ((x)==0|(y)==0):
        dp[x][y]=1
      else :
        dp[x][y]=dp[x-1][y]+dp[x][y-1]
  print(x,y,dp)
  return dp[m-1][n-1],dp


        


if __name__=='__main__':
  print(num_path(3,3))
  print(num_path_memo(3,3))
