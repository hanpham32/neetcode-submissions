class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        # append all elements in the given direction
        # `row` and `col` track how many boundaries/edges remained
        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return
            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])
            # sub-problem
            # swap (row, col) -> (col, row-1) bc we shrunk one side
            dfs(col, row-1, r, c, dc, -dr) # swap (dr, dc) -> (dc, -dr) to turn 90%
        # start by going to the right
        dfs(m, n, 0, -1, 0, 1)
        return res