class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def dfs(row, col):
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    (nr, nc) not in visited and
                    grid[nr][nc] == "1"):
                    dfs(nr, nc)

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands