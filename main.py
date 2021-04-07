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
    # While there's no 'execution stop' command passed
    while exec_stop is False:
        # If the script is in autoclicker mode
        if mode == "autoclicker":
            try:
                # Configure positions based on your screen
                hc.move((951, 946), 1)
                hc.click()
                hc.move((967, 656), 1)
                hc.click()
                time.sleep(random.uniform(0.5, 1))
                hc.move((533, 863), 1)
                hc.click()
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[0])
        # If the script is in position logger mode
        else:
            try:
                # Print position to console every second
                print(pyautogui.position())
                time.sleep(1)
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[0])
    sys.exit(0)


def on_press(key):
    # When F11 key is pressed, toggle modes between Autoclicker and Position Logger
    if key == keyboard.Key.f11:
        global mode
        mode = "pos_logger" if mode == "autoclicker" else "autoclicker"
        print("Toggling mode...")
        return
    # When F12 key is pressed, stop executing the script
    elif key == keyboard.Key.f12:
        print("Shutting down...")
        global exec_stop
        exec_stop = True
        return


def main():
    # Listen for pressed keys
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    run()


if __name__ == '__main__':
    main()
