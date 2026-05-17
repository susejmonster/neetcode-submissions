class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> stack;
        
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
     
            if (stack.find(diff) != stack.end()) {
                return {stack[diff], i};
            }
            
        
            stack[nums[i]] = i;
        }
        
        return {}; 
    }
};