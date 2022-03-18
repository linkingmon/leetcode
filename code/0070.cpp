class Solution {
public:
    vector <int> ans;
    vector <bool> calculate;
    int climbStairs(int n) {
        ans = vector<int>(n+1,0);
        calculate = vector<bool>(n+1,false);
        return climbStairs_sub(n);
    }
    int climbStairs_sub(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        int step_1, step_2, val;
        if(calculate[n-1]) 
            step_1 = ans[n-1];
        else{
            step_1 = climbStairs_sub(n-1);
            ans[n-1] = step_1;
            calculate[n-1] = true;
        }
        if(calculate[n-2]) 
            step_2 = ans[n-2];
        else{
            step_2 = climbStairs_sub(n-2);
            ans[n-2] = step_2;
            calculate[n-2] = true;
        }
        return step_1 + step_2;
    }
};