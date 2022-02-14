#########################
#You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

#You can either start from the step with index 0, or the step with index 1.

#Return the minimum cost to reach the top of the floor

##############################################################################


# We can do it with recursion or memoization but another approach could be bottom up approach

cost_1=[10,15,20]
cost_2=[1,100,1,1,1,100,1,1,100,1]

def minCostClimbingStairs(cost):
  if len(cost)<=2:
    return min(cost)
  # Since we want to solve this problem from the back
  cost.append(0) 
  for i in range(len(cost)-3,-1,-1):
    cost[i]=min ((cost[i]+cost[i+1]),(cost[i]+cost[i+2]))
  final_val=min(cost[0],cost[1])
  return final_val


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sum_pay = {0: cost[0], 1: cost[1]}
        for i in range(2, len(cost)):
            sum_pay[i] = min(sum_pay[i - 1], sum_pay[i - 2]) + cost[i]
        return min(sum_pay[len(cost) - 1], sum_pay[len(cost) - 2])



if __name__=='__main__':
  print(minCostClimbingStairs(cost_1))
  print(minCostClimbingStairs(cost_2))