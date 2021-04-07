import pyautogui
import sys
from pynput import keyboard

exec_stop = False


def run():
    while exec_stop is False:
        try:
            pyautogui.moveTo(951, 946, 0.5)
            pyautogui.click(951, 946)
            pyautogui.moveTo(967, 656, 0.5)
            pyautogui.click(967, 656)
            pyautogui.moveTo(533, 863, 0.5)
            pyautogui.click(533, 863)
        except:
            print("An error occurred: ", sys.exc_info()[0])
    sys.exit(0)


def on_press(key):
    if key == keyboard.Key.f12:
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