from script import script
import pyautogui
from typing import List
import pyperclip
from keyboard import press
import time

time.sleep(5)


def parse(s: str, *, n: int = 1980) -> List[str]:
    for i in range(len(s) // n):
        yield str(s[(i * n) : (i * n) + n])


for i in parse(script):
    pyperclip.copy("```\n" + i + "\n```")
    pyautogui.hotkey("ctrl", "v")
    press("enter")
    time.sleep(1)
