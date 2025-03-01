def create_grid(n, m):
    grid = [[0] * m for _ in range(n)]
    grid[0][0] = 1
    return grid