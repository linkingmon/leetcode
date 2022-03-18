class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor){
        vector<vector<bool>> colored;
        for(int i = 0 ; i < image.size() ; ++i)
            colored.push_back(vector<bool>(image[0].size(),false));
        color(sr, sc, image, colored, image[sr][sc], newColor);
        return image;
    }
    void color(int sr, int sc, vector<vector<int>>& image, vector<vector<bool>>& colored, int val, int newColor){
        if(!colored[sr][sc] && image[sr][sc]==val) {image[sr][sc] = newColor; colored[sr][sc] = true;}
        else return;
        if(sr-1>=0) color(sr-1, sc, image, colored, val, newColor);
        if(sr+1<image.size()) color(sr+1, sc, image, colored, val, newColor);
        if(sc-1>=0) color(sr, sc-1, image, colored, val, newColor);
        if(sc+1<image[0].size()) color(sr, sc+1, image, colored, val, newColor);
    }
};