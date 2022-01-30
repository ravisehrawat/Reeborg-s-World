# solution 1
move()
move()
turn_left()
move()

# solution 2
while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()
    
