import pyautogui
import cv2
import numpy as np

# Define your region (left, top, width, height)
region = (835, 234, 606, 606)

# Capture that region of the screen
screenshot = pyautogui.screenshot(region=region)
frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Show just the board
cv2.imshow("Chessboard Only", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
