class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        // Empty vector that will contain our answer
        vector<int> targetIndices;
        // Hashtable that stores the differences that each index need 
        unordered_map<int, int> hashTableWithTheDifferencesNeeded;
        for(int i = 0; i < nums.size(); i++){
            int second_integer = target - nums.at(i);
            if (hashTableWithTheDifferencesNeeded.find(second_integer) != 
               hashTableWithTheDifferencesNeeded.end()){
                targetIndices.push_back(i);
                targetIndices.push_back(hashTableWithTheDifferencesNeeded.
                                        find(second_integer)->second);
                break;
            } else hashTableWithTheDifferencesNeeded[nums.at(i)] = i;
        }
        return targetIndices;
    }
};