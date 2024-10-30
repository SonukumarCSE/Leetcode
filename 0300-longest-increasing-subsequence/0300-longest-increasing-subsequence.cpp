#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> dp;
    
    Solution() {
        dp = vector<vector<int>>(2501, vector<int>(2501, -1));
    }

    int solve(int idx, int prev, vector<int>& nums) {
        if (idx >= nums.size()) {
            return 0;
        }
        if (dp[idx][prev + 1] != -1) { // Using prev + 1 to handle -1 index as 0
            return dp[idx][prev + 1];
        }
        
        int take = 0;
        if (prev == -1 || nums[idx] > nums[prev]) {
            take = 1 + solve(idx + 1, idx, nums);
        }
        int not_take = solve(idx + 1, prev, nums);
        
        dp[idx][prev + 1] = max(take, not_take);
        return dp[idx][prev + 1];
    }

    int lengthOfLIS(vector<int>& nums) {
        return solve(0, -1, nums);
    }
};
