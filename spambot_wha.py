'''
    Description: Send messages from python to whatsapp.
    Author: aulerjbailey
    Video: https://youtu.be/4DGBVlMmzYs
'''
import pyautogui, webbrowser
from time import sleep

# include your country code and no spaces
phone = 'PHONE_NUMBER_HERE'

# open whatsapp web
webbrowser.open(f'https://web.whatsapp.com/send?phone={phone}')
sleep(10)

# open a simple file
with open('song.txt','r') as file:
    # iterate
    for line in file:
        # write the lines on page opened
        pyautogui.typewrite(line)

        # press enter (send message)
        pyautogui.press("enter")