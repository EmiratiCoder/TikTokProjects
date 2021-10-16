import pyautogui #pip install pyautogui
from time import sleep

def spamTexts():
    numberOfMessages = int(input('How many messages do you want to send?'))
    theMsg = input('Enter the message you want to send')
    if numberOfMessages > 100:
        print('You can not send more than 100 messages')
    else:
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        for i in range(numberOfMessages):
            pyautogui.typewrite(theMsg)
            pyautogui.press('enter')

def pressSpaceSpam():
    for i in range(3, 0, -1):
        print(i)
        sleep(1)
    for i in range(100):
        pyautogui.press('space')

print('Choose something from the menu below:')
print('1- Spam texts prank\n2-spacebar tiktok challenge')

choice =int(input('Enter a selection number: '))

if choice == 1:
    spamTexts()
elif choice==2:
    pressSpaceSpam()
else:
    print('invalid choice')

print('©ALL RIGHTS RESERVED TO @EmiratiCoder')