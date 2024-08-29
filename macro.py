from  pynput.mouse import Button
from  pynput.keyboard import Key
import pynput
import pyautogui
import pygetwindow as gw
import keyboard
import time

# Pauses entre chaque action pour éviter d'aller trop vite
pyautogui.PAUSE = 0.1

KEYBOARD_CONTROLLER = pynput.keyboard.Controller()
MOUSE_CONTROLLER = pynput.mouse.Controller()
WINDOW_NAME = "Minecraft* 1.18.2 - Multiplayer (3rd-party Server)"
WINDOW = gw.getWindowsWithTitle(WINDOW_NAME)[0]

SLOT_1 = (815, 719)
SLOT_2 = (852, 719)
SLOT_3 = (890, 719)
SLOT_GET_ITEM_FROM_SACK = (962, 506)
SLOT_REFILL_SACK = (888,683)
POS_DROP = (890, 800)


def get_mouse_pos():
    print('The current pointer position is {0}'.format(MOUSE_CONTROLLER.position))


def hello_world_Sequence():
    time.sleep(2)
    pyautogui.press('h')
    pyautogui.press('e')
    pyautogui.press('l')
    pyautogui.press('l')
    pyautogui.press('o')
    pyautogui.press(' ')
    pyautogui.press('w')
    pyautogui.press('o')
    pyautogui.press('r')
    pyautogui.press('l')
    pyautogui.press('d')
    time.sleep(2)


def exploit_Sequence():
    time.sleep(1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(0.5)
    MOUSE_CONTROLLER.position = SLOT_1
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(0.1)
    MOUSE_CONTROLLER.position = SLOT_2
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('e')
    KEYBOARD_CONTROLLER.release('e')
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(1) # temps d'attente plus grand car server lag
    MOUSE_CONTROLLER.position = SLOT_GET_ITEM_FROM_SACK
    time.sleep(0.1)
    with KEYBOARD_CONTROLLER.pressed(Key.alt_l):
        MOUSE_CONTROLLER.click(Button.left, 2)
    time.sleep(1)  # temps d'attente plus grand car server lag
    KEYBOARD_CONTROLLER.press('e')
    KEYBOARD_CONTROLLER.release('e')
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('x')
    KEYBOARD_CONTROLLER.release('x')
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(0.5)
    MOUSE_CONTROLLER.position = SLOT_3
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.left)
    time.sleep(0.1)
    MOUSE_CONTROLLER.position = POS_DROP
    time.sleep(0.1)
    with KEYBOARD_CONTROLLER.pressed(Key.shift_l):
        MOUSE_CONTROLLER.click(Button.left)
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('e')
    KEYBOARD_CONTROLLER.release('e')
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('a')
    KEYBOARD_CONTROLLER.release('a')
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(1) # temps d'attente plus grand car server lag
    MOUSE_CONTROLLER.position = SLOT_GET_ITEM_FROM_SACK
    time.sleep(0.1)
    with KEYBOARD_CONTROLLER.pressed(Key.alt_l):
        MOUSE_CONTROLLER.click(Button.left, 2)
    time.sleep(1)  # temps d'attente plus grand car server lag
    KEYBOARD_CONTROLLER.press('e')
    KEYBOARD_CONTROLLER.release('e')
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('x')
    KEYBOARD_CONTROLLER.release('x')
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(0.5)
    MOUSE_CONTROLLER.position = SLOT_2
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.left)
    time.sleep(0.1)
    MOUSE_CONTROLLER.position = SLOT_1
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('e')
    KEYBOARD_CONTROLLER.release('e')
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('a')
    KEYBOARD_CONTROLLER.release('a')
    time.sleep(0.1)
    MOUSE_CONTROLLER.click(Button.right)
    time.sleep(1) # temps d'attente plus grand car server lag
    MOUSE_CONTROLLER.position = SLOT_REFILL_SACK
    time.sleep(0.1)
    with KEYBOARD_CONTROLLER.pressed(Key.alt_l):
        MOUSE_CONTROLLER.click(Button.left, 2)
    time.sleep(1)  # temps d'attente plus grand car server lag
    KEYBOARD_CONTROLLER.press('e')
    KEYBOARD_CONTROLLER.release('e')
    time.sleep(0.1)
    KEYBOARD_CONTROLLER.press('é')
    KEYBOARD_CONTROLLER.release('é')
    time.sleep(0.1)







def start_macro():

    print("MACRO - start.")

    WINDOW.activate()
    time.sleep(0.5)
    print("WINDOW - activated.")

    print("MACRO - starting ...")
    # hello_world_Sequence()
    exploit_Sequence()
    # get_mouse_pos()

    print("MACRO - end.")



while True :
    if keyboard.is_pressed('ctrl+m'):
        start_macro()
    if keyboard.is_pressed('ctrl+e'):
        break
    time.sleep(0.1)

# keyboard.add_hotkey('ctrl+m', start_macro)
keyboard.wait('ctrl+e')
