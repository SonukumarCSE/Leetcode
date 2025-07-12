class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>>ans;
        sort(nums.begin() , nums.end());
        int n = nums.size();
        for(int i = 0; i < n-3; i++)
        {
            for(int j = i+1; j < n-2; j++)
            {
                int low = j+1, high = n-1;
                while(low < high)
                {
                     long long sum = static_cast<long long>(nums[i]) + nums[j] + nums[low] + nums[high];
                    if(sum == target)
                    {
                        ans.push_back({nums[i],nums[j],nums[low],nums[high]});
                        low++;
                        high--;
                        while(low < high && nums[low] == nums[low-1])
                            low++;
                        while(low < high && nums[high] == nums[high+1])
                            high--;
                    }
                    else if(sum < target)   low++;
                    else if(sum > target)   high--;
                }
                while(j < n-2 && nums[j] == nums[j+1])
                    j++;
            }
            while(i < n-3 && nums[i] == nums[i+1])
                i++;
        }
        return ans;
    }
};