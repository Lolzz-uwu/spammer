import time
import os
done = 0
print(''' MADE BY PERO HECKORS PLS USE ONLY PHAR EDUACTION PURPUSE BARY POWWERFUL SCIPTPS DONT USE UN ETHICKAL PURPUSES PLS THE PLOICES BILL SOW UP TO MUY DORE PLESE
-lolzz''')
time.sleep(4)
s = input('[+] do u want to go through the installation? y/n:')
if s == 'y':
    try:
        import pyautogui
    except Exception as o:
        print('[+] you dont seem to have pyautogui installed i will try to install it for u')
        time.sleep(3)
        os.system('pip install pyautogui ')
    else:
        print('[+] u have pyautogui installed')
import pyautogui
print('''                                                                                                                                       
 $$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$  _____|$$  __$$\  \____$$\ $$  _$$  _$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ 
\$$$$$$\  $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  \__|
 \____$$\ $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$ | $$ | $$ |$$   ____|$$ |      
$$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$$\ $$ |      
\_______/ $$  ____/  \_______|\__| \__| \__|\__| \__| \__| \_______|\__|      
          $$ |                                                                
          $$ |                                                                
          \__|                                                 ''')

word = input('[+] type the word u want to spam:')
times = int(input('[+] how many times do u want to spam?'))
g = input('[+] do u want to wait for some seconds after typing y/n:')
if g == 'y':
    wait = int(input('[+]for how many secs?:'))
start = input('''****************************IMPORTANT***********************************************************************************************************************
u will have 10 to open the dms or anything which u want to spam and make sure the thing where u want to spam is selected and the script is running type y to countinue:''')
print('staritng in 10 secs')
time.sleep(10)
while times > done:
    if g == 'y':
        pyautogui.typewrite(word)
        time.sleep(wait)
        pyautogui.press('enter')
        done = done + 1 
    else:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        done = done + 1
