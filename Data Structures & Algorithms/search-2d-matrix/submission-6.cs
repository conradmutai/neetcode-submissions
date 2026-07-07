public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.Length, COLS= matrix[0].Length;

        int left = 0, right = ROWS * COLS - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            int row = m / COLS, int col = m % COLS;

            if (target > matrix[row][col]) {
                left = middle + 1;
            } else if (target < matrix[row][col]) {
                right = middle - 1;
            } else {
                return true;
            }
        } 
        return false;
    }
}
