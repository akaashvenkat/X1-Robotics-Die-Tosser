from detectDistance import *

import argparse
import cv2
import math
import numpy as np
import os
import sys
import time


OUTPUT_FILE = 'location.txt'
CAMERA_ENABLED = 1
if (CAMERA_ENABLED == 1):
    import picamera


class cupDetection:
    
    def __init__(self, img):
        
        self.img = img
        self.image = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
    
    
    def isolateRed(self):

        low_red_bounds  = np.array([155, 150, 10], dtype=np.uint8) #155,65,65
        high_red_bounds = np.array([205,255,255], dtype=np.uint8) #205. 255, 255
        mask = cv2.inRange(self.image, low_red_bounds, high_red_bounds)
        
        self.isolated_red_output = self.img.copy()
        self.isolated_red_output[np.where(mask==0)] = 0

        
    # Rectangle Identification algorithm from Mehmet Hanoglu
    # Details found on: https://mehmethanoglu.com.tr/blog/6-opencv-ile-dikdortgen-algilama-python.html
    def isolateRectangle(self):
        
        pixel_width  = 3000.0
        pixel_height = 2000.0
        pixel_margin = 10.0

        corners = np.array([[[pixel_margin, pixel_margin]],[[pixel_margin, pixel_height + pixel_margin]],[[pixel_width + pixel_margin, pixel_height + pixel_margin]],[[pixel_width + pixel_margin, pixel_margin]],])

        point_dest = np.array(corners, np.float32)
        self.isolated_rect_output = cv2.imread("isolatedRed.jpg")

        gray = cv2.cvtColor(self.isolated_rect_output, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 1, 10, 120)
        
        edges  = cv2.Canny(gray, 10, 250)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
        closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
        _, contours, h = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv2.contourArea(contour) > 2800 :
                arc_len = cv2.arcLength(contour, True)
                self.approx = cv2.approxPolyDP(contour, 0.1 * arc_len, True)
                if (len(self.approx) == 4):
                    point_src = np.array(self.approx, np.float32)
                    h, status = cv2.findHomography(point_src, point_dest)
                    out = cv2.warpPerspective(self.isolated_rect_output, h, (int(pixel_width + pixel_margin * 2), int(pixel_height + pixel_margin * 2)))
                    cv2.drawContours(self.isolated_rect_output, [self.approx], -1, (0, 200, 0), 2)
                    break
                else : pass


    def isolateCup(self):
        self.isolateRed()
        cv2.imwrite("isolatedRed.jpg", self.isolated_red_output)
        self.isolateRectangle()
        cv2.imwrite("isolatedCup.jpg", self.isolated_rect_output)
        os.remove("isolatedRed.jpg")
        time.sleep(.10)
        cv2.destroyAllWindows()


    def getPixelCoords(self):
        
        self.isolateCup()
        pixel_coords = [[self.approx[0][0][0], self.approx[0][0][1]], [self.approx[1][0][0], self.approx[1][0][1]], [self.approx[2][0][0], self.approx[2][0][1]], [self.approx[3][0][0], self.approx[3][0][1]]]
        print(pixel_coords)
        return pixel_coords
        return 1



def cameraInput():
    
    camera = picamera.PiCamera()
    camera.resolution = (3000, 2000)
    camera.hflip = True
    camera.vflip = True
    camera.capture('original.jpg')
    img = cv2.imread("original.jpg")
    return img


def parseInput():
    
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", help = "Path to Image")
    args = vars(arg_parse.parse_args())
    img = cv2.imread(args["image"])
    return img


def main():
    
    img = 0
    if (CAMERA_ENABLED == 1):
        img = cameraInput()
    else:
        img = parseInput()

    cupDetect = cupDetection(img)
    distanceDetect = distanceDetection()

    pixel_array = cupDetect.getPixelCoords()
    distance_and_angle = distanceDetect.findDistanceAndAngle(pixel_array)
    distance = distance_and_angle[0]
    angle = distance_and_angle[1]
    output_values = str(distance) + "," + str(angle)

    print("Distance: " + str(distance))
    print("Angle: " + str(angle))
    with open(OUTPUT_FILE, 'w') as file:
        file.write(output_values)
    
    os.remove("detectDistance.pyc")
    


if __name__ == '__main__':
    main()
