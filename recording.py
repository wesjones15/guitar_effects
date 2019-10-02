from pyo import *
# import os

# Audio inputs must be available.
s = Server(audio="portaudio", nchnls=2, duplex=1).boot()
s.start()
# Path of the recorded sound file.
# path = os.path.join(os.path.expanduser("~"), "Desktop/coding-practice/pythonstuffprezip/sounds", "loop.wav")


# Creates a two seconds stereo empty table. The "feedback" argument
# is the amount of old data to mix with a new recording (overdub).
t = NewTable(length=8, chnls=2, feedback=1)

# Retrieves the stereo input
# inp = Input([0,1])
inp = Input(chnl=0).out()

# Table recorder. Call rec.play() to start a recording, it stops
# when the table is full. Call it multiple times to overdub.
rec = TableRec(inp, table=t, fadetime=0.05)

# Reads the content of the table in loop.
osc = Osc(table=t, freq=t.getRate(), mul=.9).out()

s.gui(locals())