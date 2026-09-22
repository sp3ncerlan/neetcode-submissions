class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] == 0):
                return 1

            visited.add((row, col))
            
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            total = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr, nc) not in visited:
                    total += dfs(nr, nc)

            return total

        result = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    return dfs(row, col)

        return result