import fcntl
import os
import pyautogui
import random
import time
l_perintah = ["pinggoogle.com || chmod +x timingkuda.sh","ls","curl","./timingkuda.sh","wget"]
#dikek i jeda 5 menit supaya ketika proses nambah workspace baru gak tabrak an ambe focus_satu_satu (function ndek web e )
time.sleep(10)
with open("counter.txt", 'r') as file:
    try:
        fcntl.flock(file.fileno(), fcntl.LOCK_EX)
        counter = 0
        while True :
            print(counter)
            # buat ngereload setiap 4 jam 
            if(counter == 80):
                #tab1
                pyautogui.moveTo(307,47)
                pyautogui.click(button='left')
                time.sleep(20)
                pyautogui.moveTo(94,88)
                pyautogui.click(button='left')
                time.sleep(60)
                #tab2
                pyautogui.moveTo(491,51)
                pyautogui.click(button='left')
                time.sleep(20)
                pyautogui.moveTo(94,88)
                pyautogui.click(button='left')
                time.sleep(60)
                #tab3
                pyautogui.moveTo(667,47)
                pyautogui.click(button='left')
                time.sleep(20)
                pyautogui.moveTo(94,88)
                pyautogui.click(button='left')
                time.sleep(60)
                #tab4
                pyautogui.moveTo(841,49)
                pyautogui.click(button='left')
                time.sleep(20)
                pyautogui.moveTo(94,88)
                pyautogui.click(button='left')
                time.sleep(60)
                counter = 0
            # tab 1
            perintah = l_perintah[random.randint(0,len(l_perintah)-1)]
            pyautogui.moveTo(307,47)
            pyautogui.click(button='left')
            time.sleep(20)
            pyautogui.moveTo(610,520)
            pyautogui.click(button='left')
            time.sleep(10)
            pyautogui.write(perintah)
            pyautogui.press("enter")
            time.sleep(10)
            # tab 2
            perintah = l_perintah[random.randint(0,len(l_perintah)-1)]
            pyautogui.moveTo(491,51)
            pyautogui.click(button='left')
            time.sleep(20)
            pyautogui.moveTo(610,520)
            pyautogui.click(button='left')
            time.sleep(10)
            pyautogui.write(perintah)
            pyautogui.press("enter")
            time.sleep(10)
            # tab 3
            perintah = l_perintah[random.randint(0,len(l_perintah)-1)]
            pyautogui.moveTo(667,47)
            pyautogui.click(button='left')
            time.sleep(20)
            pyautogui.moveTo(610,520)
            pyautogui.click(button='left')
            time.sleep(10)
            pyautogui.write(perintah)
            pyautogui.press("enter")
            time.sleep(10)
            # tab 4
            perintah = l_perintah[random.randint(0,len(l_perintah)-1)]
            pyautogui.moveTo(841,49)
            pyautogui.click(button='left')
            time.sleep(20)
            pyautogui.moveTo(610,520)
            pyautogui.click(button='left')
            time.sleep(10)
            pyautogui.write(perintah)
            pyautogui.press("enter")
            # tab 5
            pyautogui.moveTo(1027,49)
            pyautogui.click(button='left')
            time.sleep(20)
            counter = counter+1
    except Exception as e_lock:
        print(f"Error saat mengunci file: {e_lock}")
