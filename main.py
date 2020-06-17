import pyautogui
import time
# from pynput import keyboard

# Global variables
cursor_position_log = []
duration = 0.5

# Test variables
key_names = ["zero.png", "one.png", "two.png", "three.png", "four.png", 
            "five.png", "six.png", "seven.png", "eight.png", "nine.png",
            "plus.png", "minus.png", "times.png", "divide.png", "equal.png", 
            "negate.png"]


# Utility functions
def log_cursor_location():
    cursor_position_log.append(pyautogui.position())

def press_key(key_name):
    pyautogui.keyDown(key_name)
    pyautogui.keyUp(key_name)

def delay(seconds):
    time.sleep(duration)

def hover(key_location, duration):
    x_coordinate, y_coordinate = key_location

    pyautogui.moveTo(x_coordinate, y_coordinate, duration)

# Accessor functions
def get_key_location(image_source):
    return pyautogui.locateOnScreen(image_source)

def get_centered_key_location(key_location):
    return pyautogui.center(key_location)

# Test functions
def test_all_keys(key_names):
    for key in key_names:
        key_location = get_key_location("images/" + key)
        centered_key_location = get_centered_key_location(key_location)

        hover(centered_key_location, duration)


log_cursor_location()
press_key("ctrl")

"""
pyautogui.alert(text = "Programmed by: Marc Peejay V. Viernes\nDate Created: July 16, 2020", 
                title = "Alert", 
                button = "I understand")

input = pyautogui.prompt(text = "Enter an arithmetic expression: ", 
                        title = "Prompt",
                        default = "9 + 3")

print(input)
"""

# pyautogui.screenshot("images/screenshot1.png")

test_all_keys(key_names)

print(cursor_position_log)
