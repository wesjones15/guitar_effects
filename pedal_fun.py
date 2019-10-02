from pyo import Server, Input, Chorus, Delay, Sine

# Initialize Audio Server
server = Server(audio="portaudio",nchnls=1).boot()
server.start()

# Initialize Audio Feed
audio_in = Input(chnl=0)

# Initialize Effect Variables
depth = 0.5
feedback = 0.5
bal = 0.5

# Pedal Effect Initialization
input = audio_in
chorus = Chorus(audio_in, depth=depth, feedback=feedback, bal=bal)
lfo = Sine(freq=4,phase=.5,mul=.5,add=.3)
delay = Delay(audio_in, delay=0.25, feedback=lfo, maxdelay=3)

# Output
input.out()
chorus.out()
delay.out()

# GUI Effect Controllers
audio_in.ctrl()
chorus.ctrl(title="Chorus")
lfo.ctrl(title="Sine")
delay.ctrl(title="Delay")

server.gui(locals())