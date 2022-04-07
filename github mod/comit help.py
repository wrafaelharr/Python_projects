import win32api
import win32con
import time

#functions
def to_bool(key_in):
    if (key_in < -10): key_in = True
    else: key_in = False
    return key_in

def one_click(key_in, timer):
    if (key_in and time.time() - timer > 0.2): timer = time.time()
    return time.time() - timer == 0, timer

def mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#stored values
click_pos = []

#timers
timer1 = time.time()
timer2 = time.time()

#states
recording = True
playing = True
fix_first = True

#delays
delay = 0.00000001

#loop
run = True
while run:
    #get buttons
    mouse_l = win32api.GetKeyState(0x1)
    mouse_l = to_bool(mouse_l)
    esc = win32api.GetKeyState(0x1B)
    esc = to_bool(esc)
    l_shift = win32api.GetKeyState(0xA0)
    l_shift = to_bool(l_shift)
    cap_l = win32api.GetKeyState(0x14)
    cap_l = to_bool(cap_l)

    #start recording
    state_r, timer1 = one_click(cap_l, timer1)
    if state_r: 
        if recording: recording = False
        else: 
            recording = True
            click_pos = []
    
    #record mouse clicks
    if (recording and playing == False):
        state_ml, timer1 = one_click(mouse_l, timer1)
        if (state_ml): click_pos.append(win32api.GetCursorPos())

    #fix first
    if (fix_first and len(click_pos) > 0): 
        del click_pos[0]
        fix_first = False

    # start playback
    state_shift, timer2 = one_click(l_shift, timer2)
    if state_shift:  
        if playing: playing = False
        else: playing = True

    # play back clicks
    if playing and recording == False:
        for pos in click_pos:
            # set position
            win32api.SetCursorPos(pos)

            # do click
            mouse_click()
    else: time.sleep(delay) #delay

    #readouts  
    if (recording): print('recording')
    elif (playing): print('playing')
    else: print('PRESS: caps or shift') 

    # end loop
    if (esc): run = False