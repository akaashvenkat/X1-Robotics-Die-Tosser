#Implementation of findDistAndAngle

#The actual physical width(float) of the object in inches
CONST_OBJECTWIDTH = 5.0

#The focal length(float) of this camera found using the focalLength() function
CONST_FOCALLENGTH = 500.0

#The angle of view(float) of this camera
CONST_ANGLEOFVIEW = 60.0

#The width of the image by the number of pixels in the horizontal direction
CONST_IMAGEWIDTH = 600

#Returns an array containing values of distance to object and yaw angle of object from center of images
# - Index 0 contains the distance(float) in inches
# - Index 1 contains the angle(float) in degrees, where 0 indicates the center of the image
def findDistAndAngle(coordinates):
    topLeft = (float)(coordinates[0][0])
    topRight = (float)(coordinates[3][0])

    distance = CONST_OBJECTWIDTH * CONST_FOCALLENGTH / (topRight - topLeft)
    angle = ((topLeft + topRight) / CONST_IMAGEWIDTH - 1.0) * CONST_ANGLEOFVIEW / 2.0

    array = [distance, angle]
    return array
