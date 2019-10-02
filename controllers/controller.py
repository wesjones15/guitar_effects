import pygame
pygame.init()
done = False
clock = pygame.time.Clock()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()
x_button = False
x_count = 0
a_button = False
a_count = 0
b_button = False
b_count = 0
y_button = False
y_count = 0
L_button = False
L_count = 0
R_button = False
R_count = 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("X Button")
                x_button = True
                # while pressed, record loop
                # the action for this event should go down below
                # this if statement should just toggle a boolean
            if event.button == 1:
                print("A Button")
                a_button = True
                # when pressed, turn chorus effect on or off
            if event.button == 2:
                print("B Button")
                b_button = True
                # when pressed, turn delay effect on or off
            if event.button == 3:
                print("Y Button")
                y_button = True
            if event.button == 4:
                print("L Button")
                L_button = True
            if event.button == 5:
                print("R Button")
                R_button = True
            if event.button == 9: # start button
                done = True
        
        if event.type == pygame.JOYBUTTONUP:
            # When button is released, stop action
            if event.button == 0: # X
                x_button = False
                print('X sustained for', x_count, "ticks")
                x_count = 0
            if event.button == 1: # A
                a_button = False
                print('A sustained for', a_count, "ticks")
                a_count = 0
            if event.button == 2: # B
                b_button = False
                print('B sustained for', b_count, "ticks")
                b_count = 0
            if event.button == 3: # Y
                y_button = False
                print('Y sustained for', y_count, "ticks")
                y_count = 0
            if event.button == 4: # L
                L_button = False
                print('L sustained for', L_count, "ticks")
                L_count = 0
            if event.button == 5: # R
                R_button = False
                print('R sustained for', R_count, "ticks")
                R_count = 0
    
    # Logic Section
    if x_button:
        x_count += 1
    if a_button:
        a_count += 1
    if b_button:
        b_count += 1
    if y_button:
        y_count += 1
    if L_button:
        L_count += 1
    if R_button:
        R_count += 1

    clock.tick(60)
pygame.quit()