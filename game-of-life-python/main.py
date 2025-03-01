def create_grid(n, m):
    grid = [[False] * m for _ in range(n)]
    grid[0][0] = True
    return grid