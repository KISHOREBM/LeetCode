class Solution {
public:
    void make(vector<vector<char>>& grid, int i, int j, vector<vector<char>>& val) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == '0' || val[i][j] == '1') {
            return;
        }

        val[i][j] = '1'; // Mark as visited
        make(grid, i, j + 1, val); // Right
        make(grid, i, j - 1, val); // Left
        make(grid, i - 1, j, val); // Up
        make(grid, i + 1, j, val); // Down
    }

    // Function to count the number of islands
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        if (rows == 0) return 0;
        int cols = grid[0].size();

        vector<vector<char>> val(rows, vector<char>(cols, '0')); // Initialize val matrix

        int count = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1' && val[i][j] == '0') {
                    make(grid, i, j, val);
                    cout << "Island found at: (" << i << ", " << j << ")\n";
                    count++;
                }
            }
        }
        return count;  
    }
};