import pyautogui
import sys
import time
import python_imagesearch as imgsearch
from pyclick import HumanClicker
from pynput import keyboard

exec_stop = False
# mode = "autoclicker"
mode = "pos_logger"

def run():
    hc = HumanClicker()
    # While there's no 'execution stop' command passed
    while exec_stop is False:
        # If the script is in autoclicker mode
        if mode == "autoclicker":
            try:
                # Configure positions based on your screen
                screen = imgsearch.region_grabber((0, 0, 1920, 1200))
                if imgsearch.imagesearcharea("./img/mine.png", 775, 975, 1105, 1100, screen)[0] != -1:
                    hc.move((940, 1050), 1)
                    hc.click()

                time.sleep(1)
                if imgsearch.imagesearcharea("./img/claimtlm.png", 825, 665, 1100, 775, screen)[0] != -1:
                    hc.move((930, 715), 1)
                    hc.click()

                time.sleep(1)
                if imgsearch.imagesearcharea("./img/uncomp_captcha.png", 135, 495, 475, 605, screen)[0] != -1:
                    hc.move((218, 552), 1)
                    hc.click()

                time.sleep(1)
                if imgsearch.imagesearcharea("./img/captcha_buttons.png", 95, 775, 270, 850, screen)[0] != -1:
                    hc.move((232, 811), 1)
                    hc.click()
                    time.sleep(30)

                time.sleep(1)

                if imgsearch.imagesearcharea("./img/comp_captcha.png", 155, 515, 315, 590, screen)[0] != -1:
                    hc.move((280, 650), 1)
                    hc.click()

                time.sleep(1)
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
