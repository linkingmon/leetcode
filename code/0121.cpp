class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> min_vec(prices.size());
        int min_val = prices[0];
        min_vec[0] = min_val;
        for(int i = 1 ; i < prices.size() ; ++i){
            min_val = min(min_val, prices[i]);
            min_vec[i] = min_val;
        }
        int max_val = 0;
        for(int i = 0 ; i < prices.size() ; ++i)
            max_val = max(prices[i] - min_vec[i], max_val);
        return max_val;
    }
};