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

        image_width = 600;
        actual_cup_width = 5;
        focal_length = 350;

        top_right = cup_coordinates[3][0]
        top_left = cup_coordinates[0][0]

        distance = actual_cup_width * focal_length / abs(top_right - top_left)

        center_to_obj_pix = image_width / 2 - (top_right - top_left)
        dist_to_obj_pix = (actual_cup_width * focal_length) / distance

        angle = math.asin(center_to_obj_pix / dist_to_obj_pix)

        distance_angle = [distance, angle]
        return distance_angle
