# import the necessary packages
import numpy as np
import cv2


def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    #cv2.imshow('orig image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)

    cv2.imshow('Detect edges', edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

	# find the contours in the ed  ged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
    ( _, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key = cv2.contourArea)

	# compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
    return(knownWidth * focalLength) / perWidth


img1 = np.zeros((512,512,3), np.uint8)
img1 = cv2.rectangle(img1,(100,100),(300,400),(0,255,0),-1)
cv2.imwrite('img1.jpg', img1)

img2 = np.zeros((512,512,3), np.uint8)
img2 = cv2.rectangle(img2,(100,150),(200,300),(0,255,0),-1)
cv2.imwrite('img2.jpg', img2)


IMAGE_PATHS = ['2.jpg','3.jpg', '4.jpg']

img1 = cv2.imread('2.jpg')
img1S = cv2.resize(img1, (756,1008))
print 'Calibrating Known Image'
marker = find_marker(img1S)
#print(marker)

#cv2.imwrite('1.jpg', img1)
KNOWN_DIST = 11
KNOWN_WIDTH = 5.0


focalLength = (marker[1][0] * KNOWN_DIST ) / KNOWN_WIDTH

print 'Focal Length calculated: %f' % focalLength
count = 1

print 'Processing Images'
for imagePath in IMAGE_PATHS:
    print 'Processing Image %d' %count
    imageX = cv2.imread(imagePath)
    image = cv2.resize(imageX, (756,1008))

    marker = find_marker(image)

    inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])


    midX = marker[0][0]
    midY = marker[0][1]
    width = marker[1][0]
    ht = marker[1][1]

    tlX = int(midX - width/2)
    tlY = int(midY - ht/2)



    brX = int(marker[0][0]+marker[1][0]/2)
    brY = int(marker[0][1]+marker[1][1]/2)

    image = cv2.rectangle(image, (tlX, tlY), (brX, brY), (255,0,0) ,2)
    print 'Displaying identified object'
    print 'Distance in Inches: %f' % inches
    cv2.namedWindow('boxed image', cv2.WINDOW_NORMAL)
    cv2.imshow('boxed image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    count = count + 1

# for imagePath in IMAGE_PATHS:
#     image = cv2.imread(imagePath)
#     # load the image, find the marker in the image, then compute the
#     # distance to the marker from the camera
#     #image = cv2.imread(imagePath)
#     marker = find_marker(image)
#     inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
#
# 	# draw a bounding box around the image and display it
# 	#box = np.int0(cv2.cv.BoxPoints(marker))
# 	#cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
#     image = cv2.polylines(img, marker, True, (0,255,255))
#     cv2.putText(image, "%.2fft" % (inches / 12),
# 		(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
# 		2.0, (0, 255, 0), 3)
#         cv2.imshow("image", image)
#         cv2.waitKey(0)
