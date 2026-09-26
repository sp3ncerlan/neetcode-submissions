class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        print(fresh_oranges)

        time = 0
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            spread = False
            this_time = len(queue)
            for _ in range(this_time):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr >= 0 and nr < rows and
                        nc >= 0 and nc < cols and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                        spread = True
                        fresh_oranges -= 1
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            if spread:
                time += 1

        return time if fresh_oranges == 0 else -1