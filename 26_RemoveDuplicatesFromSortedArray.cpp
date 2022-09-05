class Solution {
public:
   int removeDuplicates(vector<int>& nums) {
        unordered_map<int, int> myHash;
        int curr = 0, i = 0;
        while (i!=nums.size()){
            if (!myHash.count(nums[i])){
                myHash.insert({nums[i], 0});
                nums[curr] = nums[i];
                curr++;
            }
            i++;
        }
        return curr;
    }
};