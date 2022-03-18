class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> block(3,vector<int>(3,0));
        vector<int> row(9,0);
        vector<int> col(9,0);
        for(int i = 0 ; i < 9 ; ++i){
            for(int j = 0 ; j < 9 ; ++j){
                int bitmap;
                if(board[i][j] != '.'){
                    bitmap = 1 << (board[i][j]-'0');
                    if((row[i] & bitmap) == bitmap) return false;
                    if((col[j] & bitmap) == bitmap) return false;
                    if((block[i/3][j/3] & bitmap) == bitmap) return false;
                    row[i] |= bitmap;
                    col[j] |= bitmap;
                    block[i/3][j/3] |= bitmap;
                }
            }
        }
        return true;
    }
};