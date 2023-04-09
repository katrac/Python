# Importing 'random' module to pick a random number of mines and be able to insert the mines into random spots into the grid. 
# Importing 'copy' module to create hard copy of grids. 
import random
import copy

# User defining the size of grid. 
user_grid_rows = int(input("Please provide the number of rows of the grid: "))
user_grid_columns = int(input("Please provide the number of column of the grid: "))


# Creating a random number of mines. 
# It is specified that it cannot be more than the number of places in the grid less one spot.
# That's to make sure that there won't be a situation, where it is all mines.
number_of_mines = random.choice(range((user_grid_columns*user_grid_rows) - 1))

# Creating a grid based on earlier user inputs regarding the size of the grid.
# Pre-populate the grid with mine-free spots only. 
user_grid =[["-"] * user_grid_columns for row in range (user_grid_rows)]

# Get all the indices of the grid.
# It is going to be useful in random inserting of mines into the grid. 
grid_indices = [(row,col) for row in range(user_grid_rows) for col in range(user_grid_columns)]

# Randomly assign a number of indices, specified by the 'number_of_mines', from 'grid_indices'.
mine_spots = random.sample(grid_indices, number_of_mines)

# For the randomly assigned indices for mines 'mine_spots' insert '#'.
for row, col in mine_spots:
    user_grid[row][col] = "#"  

# Print the created grid with each row on a separate line.
print("\nThe Input Grid:\n")
for row in user_grid:
    print(row)

# Check for mines "#" and count them.
# Loop through each row and column of "user_grid".
# Check if the current element of 2D list is "-" and if so, initialize "grid_count" variable to zero.
for r in range(user_grid_rows):
    for c in range(user_grid_columns):
        if user_grid[r][c] == '-':
            grid_count = 0

# Loop through each row and column offset using the two nested for loops.
# Check if the indices are within the bound of the "user_grid", and if the element at that position is equal to "#".
# If conditions are true, add to the count of "grid_count".
            for r_2 in (-1, 0, 1):
                for c_2 in (-1, 0, 1):
                    if (0 <= r + r_2 < user_grid_rows) and (0 <= c + c_2 < user_grid_columns) and (user_grid[r + r_2][c + c_2] == "#"):
                        grid_count += 1

# After looping through all the offsets, set the current value of the element in "user_grid" to the "grid_count".
            user_grid[r][c] = str(grid_count)

# Creating the final output grid "final_grid" containing the count of adjacent mines.
# Iterate over each "cell" and "row_index" of the "user_grid", if it contains "#", then the "final_grid" should also contain "#".
# Otherwise, count the number of adjacent "#" in the "user_grid".
# The "if" statement checks if the indices are within bounds of the "user_grid" and if the corresponding cell is "#".
# If all the conditions are met, the True expression sums up to 1, otherwise it's False and sums up to 0. 
final_grid = [
    [
        "#" if cell == "#" else str(sum(
            (0 <= r + r_2 < user_grid_rows) and (0 <= c + c_2 < user_grid_columns) and (user_grid[r + r_2][c + c_2] == "#")
            for r_2 in (-1, 0, 1) for c_2 in (-1, 0, 1)
        )) 
        for c, cell in enumerate(user_grid[r])
    ] for r, row_index in enumerate(user_grid)
]

# Printing the "final_grid".
print("\nThe Output Grid:\n")
for element in final_grid:
    print(element)

