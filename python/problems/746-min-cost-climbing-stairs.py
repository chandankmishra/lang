"""
746. Min Cost Climbing Stairs
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top 
of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

"""
class Solution {
	    public int minCostClimbingStairs(int[] cost) {
	        int n = cost.length;
	        int[] dp = new int[n];
	        dp[0] = cost[0];
	        dp[1] = cost[1];
	        for(int i = 2;i < n;i++){
	        	dp[i] = Math.min(dp[i-2], dp[i-1]) + cost[i];
	        }
	        return Math.min(dp[n-2], dp[n-1]);
	    }
	}	
  
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int *dp = new int[n + 1];
        dp[0] = dp[1] = 0;
        for (int i = 2; i <= n; i++) {
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1]);
        }
        int ans = dp[n];
        delete []dp;
        return ans;
    }
};

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        cost.push_back(0);
        vector<int> dp(cost.size());
        dp[0] = cost[0];
        dp[1] = cost[1];
        for (int i = 2; i < dp.size(); ++i)
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];
        return dp.back();
    }
};

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        
        return min(dp[-1], dp[-2])
        
        
  class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        cost.push_back(0);
        int n = cost.size();        
        
        vector<int> f(n, 0);
        f[0] = cost[0];
        f[1] = cost[1];
        for (int i = 2; i < n; ++i) {
            f[i] = min(f[i-1], f[i-2])+cost[i];
        };
        return f[n-1];
        
    }
};
