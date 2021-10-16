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

print('Choose something from the menu below:')
print('1- Spam texts prank\n')

choice =int(input('Enter a selection number: '))

if choice == 1:
    spamTexts()
else:
    print('invalid choice')

