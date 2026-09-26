class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque()
        for row in range(rows):
            queue.append((row, 0))
        for col in range(cols):
            queue.append((0, col))

        while queue:
            row, col = queue.popleft()
            pacific.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    (nr, nc) not in pacific and
                    heights[nr][nc] >= heights[row][col]):
                    queue.append((nr, nc))

        queue = deque()
        for row in range(rows):
            queue.append((row, cols - 1))
        for col in range(cols):
            queue.append((rows - 1, col))

        while queue:
            row, col = queue.popleft()
            atlantic.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    (nr, nc) not in atlantic and
                    heights[nr][nc] >= heights[row][col]):
                    queue.append((nr, nc))

        both = pacific & atlantic
        return [list(cell) for cell in both]