class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<bool>> record;
        for(int i = 0 ; i <= n ; ++i) record.push_back(vector<bool>(k+1,false));
        vector<vector<vector<vector<int>>>> record_val;
        for(int i = 0 ; i <= n ; ++i){
            vector<vector<vector<int>>> record_val_temp;
            for(int j = 0 ; j <= k ; ++j){
                vector<vector<int>> vec;
                record_val_temp.push_back(vec);
            }
            record_val.push_back(record_val_temp);
        }
        return find(n, k, record, record_val);
    }
    vector<vector<int>> find(int n, int k, vector<vector<bool>>& record, vector<vector<vector<vector<int>>>>& record_val){
        vector<vector<int>> vec_1, vec_2;
        if(k == 1){
            for(int i = 1 ; i <= n ; ++i) vec_1.push_back(vector<int>(1,i));
            record_val[n][k] = vec_1;
            record[n][k] = true;
            return vec_1;
        }
        if(n > k){
            if(record[n-1][k]) vec_1 = record_val[n-1][k];
            else vec_1 = find(n-1, k, record, record_val);
        }
        if(record[n-1][k-1]) vec_2 = record_val[n-1][k-1];
        else vec_2 = find(n-1, k-1, record, record_val);
        for(int i = 0 ; i < vec_2.size() ; ++i)
            vec_2[i].push_back(n);
        vec_1.insert(vec_1.end(), vec_2.begin(), vec_2.end());
        record_val[n][k] = vec_1;
        record[n][k] = true;
        return vec_1;
    }
};