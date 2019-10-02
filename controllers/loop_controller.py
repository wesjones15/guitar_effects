import pyo
import pygame
import os


path = os.path.join(os.path.expanduser("~"), "Desktop/coding-practice/pythonstuffprezip")
loopfile = os.path.join(path, "loop.wav")

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

# Initialize Loopfile Variables



size = 0.5      # range 0-1
damp = 0.5  # range 0-1
bal = 0.5   # range 0-1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("X Button")
                print("size =", size)
                x_button = True
            if event.button == 1:
                print("A Button")
                print("damp =", damp)
                a_button = True
            if event.button == 2:
                print("B Button")
                print("damp =", damp)
                b_button = True
            if event.button == 3:
                print("Y Button")
                print("size =", size)
                y_button = True
            if event.button == 4:
                print("L Button")
                print("bal =", bal)
                L_button = True
            if event.button == 5:
                print("R Button")
                print("bal =", bal)
                R_button = True
            if event.button == 9: # start button
                done = True
        
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0: # X
                x_button = False
                # print('X sustained for', x_count, "ticks")
                print("size =", size)
                x_count = 0
            if event.button == 1: # A
                a_button = False
                # print('A sustained for', a_count, "ticks")
                print("damp =", damp)
                a_count = 0
            if event.button == 2: # B
                b_button = False
                # print('B sustained for', b_count, "ticks")
                print("damp =", damp)
                b_count = 0
            if event.button == 3: # Y
                y_button = False
                # print('Y sustained for', y_count, "ticks")
                print("size =", size)
                y_count = 0
            if event.button == 4: # L
                L_button = False
                # print('L sustained for', L_count, "ticks")
                print("bal =", bal)
                L_count = 0
            if event.button == 5: # R
                R_button = False
                # print('R sustained for', R_count, "ticks")
                print("bal =", bal)
                R_count = 0
    
    # Logic Section
    if x_button:
        if x_count % 30 == 0 and size < 1.0:
            size += 0.05
        x_count += 1
    elif y_button:
        if y_count % 30 == 0 and size > 0.0:
            size -= 0.05
        y_count += 1 

    if a_button:
        if a_count % 30 == 0 and damp < 1.0:
            damp += 0.05
        a_count += 1
    elif b_button:
        if b_count % 30 == 0 and damp > 0.0:
            damp -= 0.05
        b_count += 1
    
    if L_button:
        if L_count % 30 == 0 and bal > 0.0:
            bal -= 0.05
        L_count += 1
    elif R_button:
        if R_count % 30 == 0 and bal < 1.0:
            bal += 0.05
        R_count += 1
    
    # Execution Section
    audioIn.out()
    record = pyo.Record(audioIn, filename=loopfile, chnls=1, fileformat=0)

    clock.tick(60)
pygame.quit()