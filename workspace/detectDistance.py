import argparse
import cv2
import math
import numpy as np
import os
import sys
import time


class distanceDetection:
        

    def findDistance(self, top_left, top_right, focal_len, act_width):
    
        distance = act_width * focal_len / abs(top_right[0] - top_left[0])
        return distance


    def findFocalLength(self, known_distance, known_width, image_width):
    
        focal_length = known_distance * image_width / known_width
        return focal_length


    def findAngle(self, top_left, top_right, image_width, focal_len, act_width, dist_to_obj):

        center_to_obj_pix = (top_right[0] - top_left[0]) - image_width / 2
        dist_to_obj_pix = (act_width * focal_len) / dist_to_obj
        angle = math.asin(center_to_obj_pix / dist_to_obj_pix)
        return angle


    def findDistanceAndAngle(self, cup_coordinates):
        
        image_width = 600
        actual_cup_width = 3.75
        focal_length = 453
        angle_of_view = 60.0
        
        x_diff = 0.0
        max_x_diff = 0.0
        max_x_sum = 0.0
        
        for i in range(0,4):
            for j in range(i, 4):
                x_diff = abs(cup_coordinates[i][0] - cup_coordinates[j][0])
                if x_diff > max_x_diff:
                    max_x_diff = x_diff
                    max_x_sum = abs(cup_coordinates[i][0] + cup_coordinates[j][0])
        
        distance = actual_cup_width * focal_length / max_x_diff
        angle = (max_x_sum / float(image_width) - 1.0) * angle_of_view / 2.0
        
        array = [distance, angle]
        return array
