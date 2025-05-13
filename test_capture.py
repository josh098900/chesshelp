import pyautogui
import cv2
import numpy as np

# Take a screenshot of your full screen
screenshot = pyautogui.screenshot()
frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Show the screenshot
cv2.imshow("Screen Capture", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
