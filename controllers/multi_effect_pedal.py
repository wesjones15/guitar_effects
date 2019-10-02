import pyo
import pygame
import os

path = os.path.join(os.path.expanduser("~"), "Desktop/coding-practice/pythonstuffprezip")
loopfile = os.path.join(path, "loop.wav")

pygame.init()
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

s = pyo.Server(audio="portaudio",nchnls=1).boot()
s.start()

audioIn = pyo.Input(chnl=0)

# Effect Booleans
standardOut = False
chorusEffect = False
delayEffect = False
delayLength = 0.5
delaySpd = 0

makeLoop = False
loopStarted = False
playLoop = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("X Button")
                standardOut = not standardOut
                # while pressed, record loop
                # the action for this event should go down below
                # this if statement should just toggle a boolean
            if event.button == 1:
                print("A Button")
                chorusEffect = not chorusEffect
                # when pressed, turn chorus effect on or off
            if event.button == 2:
                print("B Button")
                delayEffect = not delayEffect
                # when pressed, turn delay effect on or off
            if event.button == 3:
                print("Y Button")
                if loopStarted == False and makeLoop == False:
                    print("1")
                    makeLoop = True
                elif loopStarted == True and makeLoop == True:
                    makeLoop = False
                    playLoop = True
                    # record.stop()


            if event.button == 4:
                print("L Button")
                if delayLength > 0:
                    delayLength += -.1
            if event.button == 5:
                print("R Button")
                if delayLength < 1:
                    delayLength += 0.1
            if event.button == 9: # start button
                done = True
        
        if event.type == pygame.JOYBUTTONUP:
            # When button is released, stop action
            # if event.button == 0: # X
            #     standardOut = False
            # if event.button == 1: # A
                
            # if event.button == 2: # B

            # if event.button == 3: # Y
            if event.button == 4: # L
                delaySpd = 0
                print("Delay:", delayLength)
            if event.button == 5: # R
                delaySpd = 0
                print("Delay:", delayLength)
    
    # Logic Section
    if standardOut == True:
        audioIn.out()
    if chorusEffect == True:
        chorus = pyo.Chorus(audioIn, depth=0.5, feedback=0.5, bal=0.5).out()
    if delayEffect == True:
        delay = pyo.Delay(audioIn, delay=delayLength, feedback=0.5).out()
    
    if makeLoop == True:
        print("2")
        loopStarted = True
        record = pyo.Record(audioIn, filename=loopfile, chnls=1, fileformat=0)
        # on button press, start recording, 
        # on next button press, stop recording
        # and immediately begin playing back loop
    
    # if playLoop == True:
    #     table = pyo.SndTable(loopfile)
    #     looper = pyo.Looper(table=table).out()

    clock.tick(60)
pygame.quit()
