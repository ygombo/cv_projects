import cv2
import pytesseract
# read image
im = cv2.imread('./handwritten.jpg')
# configurations
config = ('-l eng --oem 1 --psm 3')
# pytesseract
text = pytesseract.image_to_string(im, config=config)
# print text
text = text.split('n')
print(text)
