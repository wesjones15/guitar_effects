import pyo
import pygame

s = pyo.Server(audio="portaudio",nchnls=1).boot()
s.start()
audioIn = pyo.Input(chnl=0)

done = False
pygame.init()
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

# Initialize Chorus Variables
delay = 0.5     # range 0-5
feedback = 0.5  # range 0-1
balance = 0.5   # range 0-1
ticker = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("X Button")
                # print("Depth =", depth)
                x_button = True
            if event.button == 1:
                print("A Button")
                # print("Feedback =", feedback)
                a_button = True
            if event.button == 2:
                print("B Button")
                # print("Feedback =", feedback)
                b_button = True
            if event.button == 3:
                print("Y Button")
                # print("Depth =", depth)
                y_button = True
            if event.button == 4:
                print("L Button")
                # print("Bal =", balance)
                L_button = True
            if event.button == 5:
                print("R Button")
                # print("Bal =", balance)
                R_button = True
            if event.button == 9: # start button
                done = True
        
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0: # X
                x_button = False
                print('X sustained for', x_count, "ticks")
                # print("Depth =", depth)
                x_count = 0
            if event.button == 1: # A
                a_button = False
                print('A sustained for', a_count, "ticks")
                # print("Feedback =", feedback)
                a_count = 0
            if event.button == 2: # B
                b_button = False
                print('B sustained for', b_count, "ticks")
                # print("Feedback =", feedback)
                b_count = 0
            if event.button == 3: # Y
                y_button = False
                print('Y sustained for', y_count, "ticks")
                # print("Depth =", depth)
                y_count = 0
            if event.button == 4: # L
                L_button = False
                print('L sustained for', L_count, "ticks")
                # print("Bal =", balance)
                L_count = 0
            if event.button == 5: # R
                R_button = False
                print('R sustained for', R_count, "ticks")
                # print("Bal =", balance)
                R_count = 0
    
    # Logic Section
    if x_button:
        if x_count % 30 == 0 and depth < 5:
            depth += 0.1
        x_count += 1
    elif y_button:
        if y_count % 30 == 0 and depth > 0:
            depth -= 0.1
        y_count += 1 

    if a_button:
        if a_count % 30 == 0 and feedback < 1:
            feedback += 0.05
        a_count += 1
    elif b_button:
        if b_count % 30 == 0 and feedback > 0:
            feedback -= 0.05
        b_count += 1
    
    if L_button:
        if L_count % 30 == 0 and balance > 0:
            balance -= 0.05
        L_count += 1
    elif R_button:
        if R_count % 30 == 0 and balance < 1:
            balance += 0.05
        R_count += 1


    # Execution Section
    lfo = pyo.Sine(freq=1000,phase=.5,mul=.5,add=.3)
    delay = pyo.Delay(audioIn, delay=delay, feedback=lfo, maxdelay=3).out()

    clock.tick(60)
pygame.quit()