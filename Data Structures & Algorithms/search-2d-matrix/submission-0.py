class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # run binary search on teh ranges f teh rows
        # run binary search on the selected row

        low = 0
        high = len(matrix) - 1
        target_row = -1

        while low <= high:
            middle = low + (high - low) // 2

            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                target_row = middle
                break
                
            elif target < matrix[middle][0]:
                high = middle - 1
            elif target > matrix[middle][-1]:
                low = middle + 1

        if target_row == -1:
            return False

        low = 0
        high = len(matrix[target_row]) - 1
        target_col = -1

        while low <= high:
            middle = low + (high - low) // 2

            if target == matrix[target_row][middle]:
                target_col = middle
                break
                
            elif target < matrix[target_row][middle]:
                high = middle - 1
            elif target > matrix[target_row][middle]:
                low = middle + 1
        
        if target_col == -1:
            return False

        return True

            