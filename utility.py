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

#def findAngle(topLeft, topRight, imageWidth, focalLen, actWidth, distToObj):
    #imageWidth is the pixels in the width of the image
    #distToObj is distance returned by findDistance
    #pixel = 0 at the very left of the field of view

#    centerToObjPix = (topRight[0] - topLeft[0]) - imageWidth/2
#    distToObjPixel = (actWidth*focalLen) / distToObj
#    angle = math.asin(centerToObjPix/distToObjPixel)
#    return angle

#Calculates the yaw angle(float) that the cup is away from the center of the image
#(Angle is zero at the center of the image)
#(A negative angle indicates the cup is on the left of the center line)
#(A positive angle indicates the cup is on the right of the center line)
# - topLeft(int array) and topRight(int array) indicate the position of the cup in an image
# - imageWidth(int) is the number of pixels of the image
# - angleOfView(float) tells the angle of view the camera is capable of taking images
def findAngle(topLeft, topRight, imageWidth, angleOfView):
    #Determine the center location of the cup within the image
    cupPixel = topRight - topLeft#topRight[0] - topLeft[0]
    cupLocation = topLeft + cupPixel/2#topLeft[0] + (cupPixel/2)

    #Use ratios of the location vs the image width to determine the yaw angle of the cup
    angle = ((cupLocation / imageWidth) - (0.5)) * angleOfView

    #Returns the calculated result
    return angle

print(findAngle(20, 70, 100, 60))
