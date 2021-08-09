import cv2
import numpy
from numpy.lib.type_check import imag
# from matplotlib import pyplot as plt

# Automatic brightness and contrast optimization with optional histogram clipping
def automatic_brightness_and_contrast(image):
    di = image.shape
    brightness = numpy.sum(image) / (255 * di[0] * di[1])
    minimum_brightness = 1
    ratio = brightness / minimum_brightness
    print(di[0])
    print(di[1])
    print(brightness)
    if ratio >= 1:
        adjusted = cv2.convertScaleAbs(image, alpha = 1, beta = 255 * (minimum_brightness - brightness))  
        print("Image already bright enough")
        return adjusted
    else:
        image=cv2.convertScaleAbs(image, alpha = 1 / ratio, beta = 0)
        return image


# Otherwise, adjust brightness to get the target brightness
image = cv2.imread('new.jpg')
image2 = cv2.imread('bottle09_12-7-2021-21-27-35.jpg')
auto_result = automatic_brightness_and_contrast(image)
auto_result2 = automatic_brightness_and_contrast(image2)
cv2.imshow('auto_result', auto_result)
cv2.imshow('auto_result.png', auto_result2)
cv2.imshow('image', image)
cv2.imshow('image2', image2)
cv2.waitKey()