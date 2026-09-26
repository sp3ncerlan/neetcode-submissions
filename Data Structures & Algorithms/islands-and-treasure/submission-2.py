class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # (shortest) distance to nearby chest
        queue = deque() # (row, col, dist)
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        while queue:
            row, col, dist = queue.popleft()
            grid[row][col] = dist

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    (nr, nc) not in visited and
                    grid[nr][nc] == 2147483647):
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))