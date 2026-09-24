class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # dfs
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        def dfs(row, col):
            visited.add((row, col))

            area = 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    (nr, nc) not in visited and
                    grid[nr][nc] == 1):
                    area += dfs(nr, nc)

            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area