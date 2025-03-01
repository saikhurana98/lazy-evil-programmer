def create_grid(n, m):
    grid = [[1 if j == i else 0 for j in range(m)] for i in range(n)]
    print(grid)
    return grid

create_grid(5,5)