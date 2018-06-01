import math
#Implementation of findDistance and findFocalLength

#Calculates the distance(float) to an object
# - topLeft(int array) and topRight(int array) indicate the position of the cup in an image
# - focalLen(float) gives a relationship between actual width and pixel width of an object
# - actWidth(float) is the actual width in inches of the object
def findDistance(topLeft, topRight, focalLen, actWidth):
  distance = actWidth * focalLen / (topRight[0] - topLeft[0])
  return distance

#Calculates the focal length(float) of the camera
# - knownDistance(float) is the actual distance in inches from the camera to the object
# - actWidth(float) is the actual width in inches of the object
# - imageWidth(int) is the number of pixels the object appears to be wide in an image
def findFocalLength(knownDistance, actWidth, imageWidth):
  focalLength = knownDistance * imageWidth / actWidth
  return focalLength

#Testing out the two functions:
#An object that is 10cm is placed at 100cm, seems to be 30 pixels long
#focal = findFocalLength(100, 10, 30)

#An object topLeft pixel is at 360, the topRight is at 380, giving a pixel length of 20
#Same camera used so the focal length is the same, and the actual object detecting is 40cm long
#distance = findDistance(360, 380, focal, 40)

#Under the given conditions, the distance should be around 600cm
#print(distance)

def findAngle(topLeft, topRight, imageWidth, focalLen, actWidth, distToObj):
    #topLeft is the top left pixel of the image
    #topRight is the top right pixel of the image
    #imageWidth is the pixels in the width of the image
    #focalLen is the focal length of the camera
    #actWidth is the actual width of the image
    #distToObj is distance returned by findDistance

    #pixel = 0 at the very left of the field of view
    #angle returned is the angle between the center of the image and the object

    centerToObjPix = (topRight[0] - topLeft[0]) - imageWidth/2
    distToObjPixel = (actWidth*focalLen) / distToObj
    angle = math.asin(centerToObjPix/distToObjPixel)
    return angle

def findDistanceAndAngle1(cupCoordinates):
    #cupCoordinates is a list of coordinates of the image

    imageWidth = 600;
    ACTUAL_CUP_WIDTH = 5;
    FOCAL_LENGTH = 350;

    topRight = cupCoordinates[3][0]
    topLeft = cupCoordinates[0][0]

    distance = ACTUAL_CUP_WIDTH * FOCAL_LENGTH / abs(topRight - topLeft)

    centerToObjPix = imageWidth/2 - ((topRight - topLeft))
    distToObjPixel = (ACTUAL_CUP_WIDTH*FOCAL_LENGTH) / distance


    angle = math.asin(centerToObjPix/distToObjPixel)

    distanceAngle = [distance, angle]
    return distanceAngle

# cupCoordinates = [[264, 56], [270, 236], [355, 236], [376, 62]]
# print(findDistanceAndAngle1(cupCoordinates))

