import math
#Implementation of findDistance and findFocalLength

#Returns the distance to an object when given the image width, the focal length, and the actual width of the object
def findDistance(topLeft, topRight, focalLen, actWidth):
  distance = actWidth * focalLen / abs(topRight[0] - topLeft[0])
  return distance

#Returns the focal length of the camera when given the actual distance to the object, the actual width of the object, and the image width that appears on screen
def findFocalLength(knownDistance, knownWidth, imageWidth):
  focalLength = knownDistance * imageWidth / knownWidth
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
