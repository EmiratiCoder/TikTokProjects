import pyautogui
from time import sleep

def spamTexts():
    numberOfMessages = int(input('How many messages do you want to send?'))

    if numberOfMessages > 100:
        print('You can not send more than 100 messages')
    else:
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        for i in range(numberOfMessages):
            pyautogui.typewrite('Follow EmiratiCoder!!')
            pyautogui.press('enter')

spamTexts()