# Simple Conway's Game of Life
# Start with a small 5x5 grid (0 = dead, 1 = alive)
print('Name:Likith raj,USN:1AY24AI061')
grid = [
[0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0],
]
def count_neighbors(grid, r, c): count = 0
for i in range(r-1, r+2):
 for j in range(c-1, c+2):
  if (i == r and j == c) or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
   conSnue
   count += grid[i][j]
   return count
   def next_generaSon(grid): new_grid = []
    for r in range(len(grid)): new_row = []
    for c in range(len(grid[0])):
     neighbors = count_neighbors(grid, r, c) if grid[r][c] == 1 and neighbors in [2, 3]:
     new_row.append(1)
  elif grid[r][c] == 0 and neighbors == 3:
   new_row.append(1) else:
   new_row.append(0) new_grid.append(new_row)
   return new_grid
   def print_grid(grid): for row in grid:
    print(''.join('■' if cell else ' ' for cell in row)) 
    print()
    # Run one generaSon and print
print("Current GeneraSon:") 
print_grid(grid)
grid = next_generaSon(grid) print("Next GeneraSon:") 
print_grid(grid)
