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
    xDiff = 0.0
    maxXDiff = 0.0
    maxXSum = 0.0
    for i in range(0,4):
        for j in range(i+1,4):
            xDiff = abs(coordinates[i][0] - coordinates[j][0])
            if xDiff > maxXDiff:
                maxXDiff = xDiff
                maxXSum = abs(coordinates[i][0] + coordinates[j][0])

    distance = CONST_OBJECTWIDTH * CONST_FOCALLENGTH / (maxXDiff)
    angle = (maxXSum / float(CONST_IMAGEWIDTH) - 1.0) * CONST_ANGLEOFVIEW / 2.0

    array = [distance, angle]
    return array
