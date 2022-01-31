def turn_right():
    turn_left()
    turn_left()
    turn_left()



if front_is_clear():
    put("token")
    move()
else:
    turn_left()
    put("token")
    move()

while not object_here("token"):
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
        
    
