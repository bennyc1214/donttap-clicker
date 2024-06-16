import keyboard
from PIL import Image, ImageGrab
import pyautogui
import os

#careful about screen resolution and positioning

def save_pics(number=0):
    filename = f'image_{number:04d}.png'
    game.save(filename, 'PNG')

def start():
    recorded_events = keyboard.record(until='enter')
    text = ''.join(e.name for e in recorded_events if e.event_type == 'down')
    if ('start' in text.lower()):
        return True
    else:
        return False

def game_start():
    game = ImageGrab.grab(bbox =(925, 400, 1920, 1295))
    rgb_im = game.convert("RGB")
    r,g,b = rgb_im.getpixel((12, 12))
    if (r==255 and g==255 and b==255): #white, game is started or over
        print('game started or over')
        return True
    else:
        print('game not started')
        return False
    print(r,g,b)
    
def check_colour(x=0, y=0):
    
    r,g,b = rgb_im.getpixel((x, y))
    if (g!=255):
       pyautogui.click(x+925, y+400) 

start()
while (not game_start()):
    print('no')
while (not (keyboard.is_pressed('esc'))):
    game = ImageGrab.grab(bbox =(925, 400, 1920, 1280))

    rgb_im = game.convert("RGB")
    check_colour(120, 50)
    check_colour(365, 50)
    check_colour(630, 50)
    check_colour(860, 50)

    check_colour(120, 310)
    check_colour(365, 310)
    check_colour(630, 310)
    check_colour(860, 310)

    check_colour(120, 560)
    check_colour(365, 560)
    check_colour(630, 560)
    check_colour(860, 560)

    check_colour(120, 810)
    check_colour(365, 810)
    check_colour(630, 810)
    check_colour(860, 810)


