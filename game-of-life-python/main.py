import random
def create_grid(n, m):
    grid = [[1 if j < i + 1 else 0 for j in range(m)] for i in range(n)]
    # for row in grid:
    #     for element in row:
    #         element = random.randint(0,1)
    print(grid)
    return grid

create_grid(5,5)