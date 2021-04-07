import pyautogui
import sys
import time
import random
from pyclick import HumanClicker
from pynput import keyboard

exec_stop = False
mode = "autoclicker"

def run():
    hc = HumanClicker()
    while exec_stop is False:
        if mode == "autoclicker":
            try:
                hc.move((951, 946), 1)
                hc.click()
                hc.move((967, 656), 1)
                hc.click()
                time.sleep(random.uniform(0.5, 1))
                hc.move((533, 863), 1)
                hc.click()
            except:
                print("An error occurred: ", sys.exc_info()[0])
        else:
            try:
                print(pyautogui.position())
                time.sleep(1)
            except:
                print("An error occurred: ", sys.exc_info()[0])
    sys.exit(0)


def on_press(key):
    if key == keyboard.Key.f11:
        global mode
        mode = "pos_logger" if mode == "autoclicker" else "autoclicker"
        print("Toggling mode...")
        return
    elif key == keyboard.Key.f12:
        print("Shutting down...")
        global exec_stop
        exec_stop = True
        return


def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    run()


if __name__ == '__main__':
    main()
