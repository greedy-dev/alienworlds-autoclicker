import pyautogui
import sys
import time
import python_imagesearch.imagesearch as imgsearch
from pyclick import HumanClicker
from pynput import keyboard

exec_stop = False
mode = "autoclicker"
# mode = "pos_logger"

def run():
    hc = HumanClicker()
    # While there's no 'execution stop' command passed
    while exec_stop is False:
        # If the script is in autoclicker mode
        if mode == "autoclicker":
            try:
                # Configure positions  of buttons based on your screen
                # Mine button
                if imgsearch.imagesearch("img/mine.png")[0] != -1:
                    hc.move((940, 1050), 1)
                    hc.click()

                time.sleep(1)
                # Claim TLM button
                if imgsearch.imagesearch("img/claim.png")[0] != -1:
                    hc.move((930, 715), 1)
                    hc.click()

                # Close error message button
                if imgsearch.imagesearch("img/timed_out.png")[0] != -1:
                    hc.move((1450, 350), 1)
                    hc.click()

                # Authorize transaction button
                if imgsearch.imagesearch("img/captcha_solved.png")[0] != -1:
                    hc.move((265, 700), 1)
                    hc.click()

                time.sleep(1)
                # Back to mining hub button
                if imgsearch.imagesearch("img/go_to_hub.png")[0] != -1:
                    hc.move((518, 964), 1)
                    hc.click()

                time.sleep(1)
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[1])
                sys.exit(0)
        # If the script is in position logger mode
        else:
            try:
                # Print position to console every second
                print(pyautogui.position())
                time.sleep(1)
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[2])


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
