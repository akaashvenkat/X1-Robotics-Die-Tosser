#Implementation of findDistance, findFocalLength, and findAngle

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

def findAngle(topLeft, topRight, imageWidth, focalLen, actWidth, distToObj):
    #imageWidth is the pixels in the width of the image
    #distToObj is distance returned by findDistance
    #pixel = 0 at the very left of the field of view

    centerToObjPix = (topRight[0] - topLeft[0]) - imageWidth/2
    distToObjPixel = (actWidth*focalLen) / distToObj
    angle = math.asin(centerToObjPix/distToObjPixel)
    return angle

#Calculates the yaw angle(float) that the cup is away from the center of the image
#(Angle is zero at the center of the image)
#(A negative angle indicates the cup is on the left of the center line)
#(A positive angle indicates the cup is on the right of the center line)
# - topLeft(int array) and topRight(int array) indicate the position of the cup in an image
# - imageWidth(int) is the number of pixels of the image
# - focalLen(float) gives a relationship between actual width and pixel width of an object
# - actWidth(float) is the actual width in inches of the object, in this case, the cup
# - angleOfView(float) tells the angle of view the camera is capable of taking images
def findAngle(topLeft, topRight, imageWidth, focalLen, actWidth, angleOfView):
    #Calculate the distance to the object
    distToObj = findDistance(topLeft, topRight, focalLen, actWidth)

    #Determine the center location of the cup within the image
    cupPixel = topRight[0] - topLeft[0]
    cupLocation = topLeft[0] + (cupPixel/2)

    #Calculate the arc length of the circle within our field of view with radius distToObj
    arcLength = 2 * math.pi * distToObj * (angleOfView / 360)

    #Use ratios of the location vs the arc length to determine the yaw angle of the cup
    angle = ((cupLocation / arcLength) - (0.5)) * angleOfView

    #Returns the calculated result
    return angle
