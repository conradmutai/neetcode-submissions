class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque() 
        fresh_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1 

        if fresh_count == 0:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        mins = 0

        while q and fresh_count > 0:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_count -= 1
            mins += 1
        
        return mins if fresh_count == 0 else -1