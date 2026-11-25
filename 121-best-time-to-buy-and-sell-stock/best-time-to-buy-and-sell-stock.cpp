class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int max_profit = INT_MIN;
        int best_buy = INT_MAX;

        for(int i=0; i<prices.size(); i++){
            best_buy = min(prices[i] , best_buy);
            int curr_price = prices[i];
            max_profit = max(max_profit ,curr_price-best_buy);
        }

        return max_profit;
    }
};