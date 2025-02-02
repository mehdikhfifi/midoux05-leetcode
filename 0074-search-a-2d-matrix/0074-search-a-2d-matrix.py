class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # run binary search twice, first on the first elements of the rows of each matrix, then on the row chosen

        m = len(matrix)
        first_elements = [matrix[i][0] for i in range(len(matrix))]

        # run binary search

        left, right = 0, len(first_elements)-1

        while left <= right:

            mid = left + (right - left)//2

            if first_elements[mid] == target:
                return True
            elif first_elements[mid] < target:
                left = mid + 1
            elif first_elements[mid] > target:
                right = mid -1
        print(mid)

        row_index = right
        if row_index < 0:  # If `right` went negative, target is smaller than matrix[0][0]
            return False
        if row_index >= m:  # If `right` exceeded bounds, return False
            return False

        row_elements = [matrix[row_index][i] for i in range(len(matrix[0]))]

        left, right = 0, len(row_elements)-1

        while left <= right:

            mid = left + (right - left)//2

            if row_elements[mid] == target:
                return True
            elif row_elements[mid] < target:
                left = mid + 1
            elif row_elements[mid] > target:
                right = mid -1
        return False