import time
import pyautogui
from pynput import mouse
import os

'''This script will require an input from the user in seconds
and repeat a left button click every n seconds.
After entering the time interval the next left button click 
of the mouse will set the position at which the clicks will be repeated.
To exit the script press the right button of the mouse'''

click_position = None
continue_clicking = False
click_interval = None

def keep_clicking(click_position, continue_clicking, click_interval):
    if continue_clicking == False:
        exit()
    while continue_clicking:
        time.sleep(click_interval)
        pyautogui.click(click_position)

def on_click(x, y, button, pressed):
    global click_position, continue_clicking, click_interval
    if button == mouse.Button.left and pressed:
        continue_clicking = True
        if click_position == None: 
            click_position = (x, y)
            print(f"Now clicking every {click_interval} seconds at {click_position[0]}, {click_position[1]}")
    elif button == mouse.Button.right and pressed:
        print("Right button clicked. Stopping.")
        os._exit(0)

def get_time_interval():
    try:
        user_input = float(input('Enter the time interval for the click in seconds and the press Enter: '))
        if user_input == float(0):
            os._exit(0)
        return user_input
    except ValueError:
        print('Enter a valid float or write 0 to stop the program')
        get_time_interval()       

click_interval = get_time_interval()   
print(f'''\nNow the next click with the left button of the mouse 
will be the position at which the click will be repeated every {click_interval} seconds.\n''')
with mouse.Listener(on_click=on_click) as listener:
    while not continue_clicking:
        time.sleep(1)
    while continue_clicking == True and click_position != None:
        keep_clicking(click_position, continue_clicking, click_interval)