# UCLA ASME X1 Robotics '17-'18: High Accuracy Die Tosser

- - - - - - - 
## testCV.py


- - - - - - - 
## detectCup.py

Either takes an input image (when running on Ubuntu VM) or captures an image using a camera (when running on Raspberry Pi). Isolates the red regions of the image, and then searches for rectangles, ultimately detecting the red solo cup. Saves image of detected cup in the same directory as the program. Returns the pixel coordinates of the corners of the cup.

If running program on Ubuntu VM: **Set "CAMERA_ENABLED" to 0** at the top of file, and run:
> python detectCup.py -i <path_to_input_image> 

If running program on Raspberry Pi: **Set "CAMERA_ENABLED" to 1** at the top of file, and run:
> python detectCup.py 

- - - - - - - - -
## setupInstructions
Contains instructions to set up Ubuntu Virtual Machine and Raspberry Pi environments.
