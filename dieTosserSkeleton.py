
distance = 0.0
yawAngle = 0.0

#rpi.gpio
def main():
    initSetup()
    parseLocation()
    launchSequence(distance, yawAngle)

#Initial setup for motor controls and camera
def initSetup():
    print "Initial setup"

#Retrieve information encrypted inside the
#location.txt file and parse the variables
def parseLocation():
    global distance, yawAngle
    file = open('location.txt', 'r')
    data = file.readline().split(",")
    location = [float (i) for i in data]
    distance = location[0]
    yawAngle =  location[1]

#
def launchSequence(distance, yawAngle):

    print "\n%sm away" % distance
    print "%s degrees\n" % yawAngle

    adjustYawAngle(yawAngle)
    adjustPitchAngle(distance)

    #Basic kinematics to calculate the force at which the
    #launching mechanism needs to propell the object at
    power = 0 #value of calculation go here

    shoot(power)

def adjustYawAngle(angle):
    print "Adjusting Yaw Angle"

def adjustPitchAngle(distance):
    print "Adjusting Pitch Angle"

def shoot(power):
    print "Shoot Sequence"

if __name__ == '__main__':
  main()
