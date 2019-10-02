import keyboard
done = False
pluser = 0
def w_callback(key):
    # if keyboard.is_pressed(key):
    if pluser == 0:
        print('pressed', key)
    pluser += 1

def reset_pluser(pluser):
    pluser = 0

while not done:
    keyboard.on_press_key('w', w_callback)
    keyboard.on_release_key('w', reset_pluser(pluser))
    if keyboard.is_pressed('q'):
        done = True
