from pyo import *
import os

server = Server().boot()

path = os.path.join(os.path.expanduser("~"), \
     "Desktop/coding-practice/pythonstuffprezip/sounds")
loop_file = os.path.join(path, "loop.wav")
loop_two = os.path.join(path, "loop2_slim.wav")

player = SfPlayer(loop_file, speed=1, loop=True, offset=1)
chorus = Chorus(player, depth=.5, feedback=.5, bal=.5, mul=.5)
delay = Delay(player, delay=0.25, feedback=0, mul=.2)

player_two = SfPlayer(loop_two, speed=1, loop=True, offset=0.01, mul=.5)
chorus_two = Chorus(player, depth=.5, feedback=.5, bal=.5, mul=.7)

server.start()

player.out()
# chorus.out()
delay.out()

# player_two.out()
chorus_two.out()

player.ctrl()
chorus.ctrl()
delay.ctrl()
player_two.ctrl()
server.gui(locals())