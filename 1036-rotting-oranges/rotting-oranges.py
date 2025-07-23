from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q = deque()
        fresh = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        count = 0
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                if visited[r][c]:
                    continue
                visited[r][c] = True

                for i, j in direction:
                    nr, nc = r + i, c + j
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1 and not visited[nr][nc]:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            count += 1

        if fresh != 0:
            print(fresh)
            return -1

        return count
