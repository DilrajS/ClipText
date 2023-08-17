import pyautogui
import cv2
import pytesseract
import pyperclip
import keyboard

print("Press the 'Print Screen' key to capture text.")

# Wait for the Print Screen key to be pressed
keyboard.wait('print_screen')

# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Preprocess the image
image = cv2.imread("screenshot.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# OCR with Pytesseract
text = pytesseract.image_to_string(thresh)

# Copy to clipboard
pyperclip.copy(text)

print("Text copied to clipboard!")
