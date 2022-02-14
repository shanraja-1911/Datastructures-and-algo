# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and space is marked as 1 and 0 respectively in the grid.



# using bottom up approach 
def num_path(obst):
  m=len(obst)
  n=len(obst[0])
  if (obst[0][0])|(obst[-1][-1])==1:
    return 0 
  
  dp=[[0 for _ in range(n) ] for _ in range(m)]
  dp[0][0]=1

  for x in range(m):
    for y in range(n):
      #print(x,y)

      if obst[x][y]==0:
        if x>0:
          dp[x][y]+=dp[x-1][y]
        if y>0:
          dp[x][y]+=dp[x][y-1]
      print(x,y,dp)
  print(dp)
  
  return dp[-1][-1]



        


if __name__=='__main__':
  obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
  #obstacleGrid=[[0],[1]]
  print(num_path(obstacleGrid))
  
