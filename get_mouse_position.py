import pyautogui
import time

print("You have 5 seconds to move your mouse to the **top-left** corner of the board...")
time.sleep(5)
top_left = pyautogui.position()
print(f"Top-left corner: {top_left}")

print("Now move your mouse to the **bottom-right** corner of the board. You have 5 seconds...")
time.sleep(5)
bottom_right = pyautogui.position()
print(f"Bottom-right corner: {bottom_right}")

region = (top_left.x, top_left.y, bottom_right.x - top_left.x, bottom_right.y - top_left.y)
print(f"Region for cropping: {region}")
