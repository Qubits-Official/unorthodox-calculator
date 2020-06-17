import pyautogui
import time
# from pynput import keyboard

# Global variables
cursor_position_log = []
duration = 0.5


# Utility functions
def log_cursor_location():
    cursor_position_log.append(pyautogui.position())

def press_key(key_name):
    pyautogui.keyDown(key_name)
    pyautogui.keyUp(key_name)

def delay(seconds):
    time.sleep(duration)


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

# pyautogui.screenshot("screenshot1.png")

button_7_location = pyautogui.locateOnScreen("images/seven.png")
print(button_7_location)

button_7_point = pyautogui.center(button_7_location)
print(button_7_point)

button_7_x, button_7_y = button_7_point
pyautogui.moveTo(button_7_x, button_7_y, duration)
pyautogui.click()

print(cursor_position_log)
