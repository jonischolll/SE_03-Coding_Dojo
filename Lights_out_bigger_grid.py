

"""
grid = [[1,1,1], 
        [1,1,1],
        [1,1,1]]

"""

grid_size = 5

grid = [[1 for grid_row in range(grid_size)] for grid_column in range (grid_size)]

game_win = 0


print (grid)



while game_win == 0:

    
    
    toggled_light = int(input ("Which light should be toggled? "))

    row = toggled_light // grid_size
    column = toggled_light % grid_size



    if grid[row][column] == 1:
        

        grid[row][column] = 0

    else: 
        grid[row][column] = 1


    last_row = row - 1
    next_row = row + 1

    last_column = column - 1
    next_column = column + 1
     
    if row > 0:

            if grid[last_row][column] == 1:
        

                grid[last_row][column] = 0

            else: 
                grid[last_row][column] = 0


    
    if row < (grid_size - 1):

            if grid[next_row][column] == 1:
        

                grid[next_row][column] = 0

            else: 
                grid[next_row][column] = 0



    if column > 0:

            if grid[row][last_column] == 1:
        

                grid[row][last_column] = 0

            else: 
                grid[row][last_column] = 0

    
    if column < (grid_size - 1):

            if grid[row][next_column] == 1:
        

                grid[row][next_column] = 0

            else: 
                grid[row][next_column] = 0


    
    print (grid)



    switches_on = sum(sum(x) for x in grid)

    print (F"Remaining switches: {switches_on}")
         

    if switches_on == 0:
         
         game_win= 1

         print ("Congratulations, you won")


