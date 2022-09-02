class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // We start the longest prefix as if it were equal to the first string in the vector strs
        int maxPrefixSize = strs[0].size();      
        for (int i = 0; i<strs.size(); i++){
            for (int j = 0; j < maxPrefixSize; j++){
                // If this index of the string we are traversing doesn't match the initial string, we should update the size of our prefix
                if (strs[0][j] != strs[i][j] && j < maxPrefixSize){
                    maxPrefixSize = j;
                    break;
                }
            }
        }
        // Found a prefix and so we print the orignal string from the beginning until the index maxPrefixSize 
        if (maxPrefixSize)
            return strs[0].substr(0, maxPrefixSize);
        else 
            return "";
    }
};