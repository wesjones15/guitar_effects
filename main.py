import pyo

s = pyo.Server(audio="portaudio",nchnls=1).boot()

s.start()

a = pyo.Input(chnl=0)
# disto = pyo.Disto(a, drive=.75, slope=.5).out()

chorus = pyo.Chorus(a, depth=.9, feedback=.8, bal=.5).out()
delay = pyo.Delay(a, delay=0, feedback=.5)
chorustwo = pyo.Chorus(delay, depth=.5, feedback=.3, bal=.5).out()

lfo = pyo.Sine(freq=.5,phase=.5,mul=.5,add=.3)
delaytwo = pyo.Delay(a, delay=.05,feedback=lfo,maxdelay=3).out()
# output = pyo.Tone(a, freq=5000).out()
s.gui()

# combine this with the controller input detector with pygame
# use those button inputs to trigger guitar effects
# and they can start and stop loops
# functions and shit