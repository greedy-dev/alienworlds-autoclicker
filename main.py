import pyautogui
import sys
import time
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
                hc.move((840, 710), 1)
                hc.click()
                time.sleep(5)
                hc.move((841, 583), 1)
                hc.click()
                time.sleep(5)
                hc.move((693, 667), 1)
                hc.click()
                time.sleep(5)
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[0])
                sys.exit(0)
        # If the script is in position logger mode
        else:
            try:
                # Print position to console every second
                print(pyautogui.position())
                time.sleep(1)
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[0])


def on_press(key):
    # When F11 key is pressed, toggle modes between Autoclicker and Position Logger
    if key == keyboard.Key.f11:
        global mode
        mode = "pos_logger" if mode == "autoclicker" else "autoclicker"
        print(f"Changing mode to {mode}")
    # When F12 key is pressed, stop executing the script
    elif key == keyboard.Key.f12:
        global exec_stop
        exec_stop = True
        print("Shutting down...")
        sys.exit(0)


def main():
    # Listen for pressed keys
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    run()


if __name__ == '__main__':
    main()
