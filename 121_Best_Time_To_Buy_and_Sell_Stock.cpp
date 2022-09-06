class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i, leastValue = prices[0], profitMax = 0;
        for (int i = 0; i < prices.size(); i++){
            if (prices[i] <= leastValue) leastValue = prices[i];
            if (profitMax < prices[i] - leastValue) profitMax = prices[i] - leastValue;
        }
        return profitMax;
    }
};