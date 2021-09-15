from typing import Collection
import pyautogui
import time

def main():
    #cookie_point = [<your_x_value_here>, <your_y_value_here>]

    while True:
        #pyautogui.click(cookie_point[0], cookie_point[1])
        print(pyautogui.position())
        time.sleep(0.25)

if __name__ == '__main__':
    main()
