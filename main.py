import pyautogui
import time
# from pynput import keyboard

# Global variables
cursor_position_log = []
delay_duration = 0.5

user_input = ""
calculation_instructions = []

# Test variables
key_file_names = {
    "0": "zero.png",
    "1": "one.png", 
    "2": "two.png",
    "3": "three.png",
    "4": "four.png",
    "5": "five.png",
    "6": "six.png",
    "7": "seven.png",
    "8": "eight.png",
    "9": "nine.png",
    "!": "negate.png",
    "+": "plus.png",
    "-": "minus.png",
    "*": "times.png",
    "/": "divide.png",
    "=": "equal.png"
}


# Main functions
def ask_mathematical_expression():
    global user_input

    user_input = pyautogui.prompt(text = "Compute: ", 
                            title = "Enter Mathematical Expression", 
                            default = "2+7")

def parse_user_input(user_input):
    global calculation_instructions

    for character in user_input:
        if character != " ":
            calculation_instructions.append(character)
    
    calculation_instructions.append("=")


def do_unorthodox_computation(calculation_instructions):
    for character in calculation_instructions:
        key_location = get_key_location("images/" + key_file_names[character])
        centered_key_location = get_centered_key_location(key_location)

        hover(centered_key_location, delay_duration)
        pyautogui.click()


# Utility functions
def log_cursor_location():
    cursor_position_log.append(pyautogui.position())

def press_key(key_name):
    pyautogui.keyDown(key_name)
    pyautogui.keyUp(key_name)

def delay(seconds):
    time.sleep(delay_duration)

def hover(key_location, duration):
    x_coordinate, y_coordinate = key_location

    pyautogui.moveTo(x_coordinate, y_coordinate, duration)

# Accessor functions
def get_key_location(image_source):
    return pyautogui.locateOnScreen(image_source)

def get_centered_key_location(key_location):
    return pyautogui.center(key_location)

# Test functions
def test_all_keys(key_file_names):
    for key in key_file_names:
        key_location = get_key_location("images/" + key)
        centered_key_location = get_centered_key_location(key_location)

        cursor_position_log.append(centered_key_location)

        hover(centered_key_location, delay_duration)


# Main code
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

# test_all_keys(key_file_names)

ask_mathematical_expression()
parse_user_input(user_input)
do_unorthodox_computation(calculation_instructions)

print(calculation_instructions)

pyautogui.alert(text = cursor_position_log, 
                title = "Cursor Position Log", 
                button = "Okay")
