#Implementation of findDistance and findFocalLength

#Returns the distance to an object when given the image width, the focal length, and the actual width of the object
def findDistance(topLeft, topRight, focalLen, actWidth):
  distance = actWidth * focalLen / abs(topRight - topLeft)
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
