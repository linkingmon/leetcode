class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row;
        for(row = 0 ; row < matrix.size() ; ++row)
            if(matrix[row][0] > target) break;
        if(row == 0) return false;
        for(int col = 0 ; col < matrix[0].size() ; ++col)
            if(matrix[row-1][col] == target) return true;
        return false;
    }
};