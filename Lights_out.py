grid = [[1,1,1], 
        [1,1,1],
        [1,1,1]]

game_win = 0

while game_win == 0:

    toggled_light = int(input ("Which light should be toggled? "))



    if toggled_light == 0:

        toggled_light_row = 0

        toggled_light_column = 0


    elif toggled_light == 1:

        toggled_light_row = 0

        toggled_light_column = 1


    elif toggled_light == 2:

        toggled_light_row = 0

        toggled_light_column = 2


    elif toggled_light == 3:

        toggled_light_row = 1

        toggled_light_column = 0


    elif toggled_light == 4:

        toggled_light_row = 1

        toggled_light_column = 1


    elif toggled_light == 5:

        toggled_light_row = 1

        toggled_light_column = 2


    elif toggled_light == 6:

        toggled_light_row = 2

        toggled_light_column = 0


    elif toggled_light == 7:

        toggled_light_row = 2

        toggled_light_column = 1


    elif toggled_light == 8:

        toggled_light_row = 2

        toggled_light_column = 2



    if grid[toggled_light_row][toggled_light_column] == 1:
        

        grid[toggled_light_row][toggled_light_column] = 0

    else: 
        grid[toggled_light_row][toggled_light_column] = 1


     
    if toggled_light_row > 0:

            if grid[toggled_light_row -1][toggled_light_column] == 1:
        

                grid[toggled_light_row -1][toggled_light_column] = 0

            else: 
                grid[toggled_light_row -1][toggled_light_column] = 0

    
    if toggled_light_row < 2:

            if grid[toggled_light_row +1][toggled_light_column] == 1:
        

                grid[toggled_light_row +1][toggled_light_column] = 0

            else: 
                grid[toggled_light_row +1][toggled_light_column] = 0



    if toggled_light_column > 0:

            if grid[toggled_light_row][toggled_light_column -1] == 1:
        

                grid[toggled_light_row][toggled_light_column -1] = 0

            else: 
                grid[toggled_light_row][toggled_light_column -1 ] = 0

    
    if toggled_light_column < 2:

            if grid[toggled_light_row][toggled_light_column +1] == 1:
        

                grid[toggled_light_row][toggled_light_column +1] = 0

            else: 
                grid[toggled_light_row][toggled_light_column +1] = 0


    
    print (grid)



    switches_on = 0
         
    for toggled_light_row in range (2):
         
        for toggled_light_column in range (2):

            switches_on += grid [toggled_light_row][toggled_light_column]


    if switches_on == 0:
         
         game_win= 1


    else:
         game_win = 0
    
    

if game_win == 1:
     

     print ("Congratulations, you won")




    




