from pyo import *
import os

server = Server(audio="portaudio", nchnls=1).boot()
path = os.path.join(os.path.expanduser("~"), \
     "Desktop/coding-practice/pythonstuffprezip/sounds")
loop_file = os.path.join(path, "loop3.wav")

duration = 20

audio_in = Input(chnl=0)
# chorus = Chorus(audio_in, depth=.5, feedback=.25, bal=.5)
loop = Record(audio_in, filename=loop_file, \
     chnls=1, fileformat=0,quality=1)

clean = Clean_objects(duration, loop)

clean.start()
server.start()

server.gui(locals())