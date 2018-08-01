from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key
import time
import threading


class Clicker(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.clicking = False  # if program is currently clicking or not
        self.running = True  # if program is running

    def start_alching(self):
        self.clicking = True

    def stop_alching(self):
        self.clicking = False

    def exit(self):
        self.stop_alching()
        self.running = False

    def run(self):
        while self.running:
            while self.clicking:
                mouse.click(self.button)
                time.sleep(self.delay)


delay = 1.6
button = Button.left
start = Key.f9
shut_down = Key.f10
mouse = Controller()
click_thread = Clicker(delay, button)
click_thread.start()


def on_press(key):
    if key == start:
        if click_thread.clicking:
            click_thread.stop_alching()
        else:
            click_thread.start_alching()
    elif key == shut_down:
        click_thread.exit()


with Listener(on_press=on_press) as listener:
    listener.join()
