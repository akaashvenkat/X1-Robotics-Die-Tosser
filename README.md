# X1-Robotics-Die-Tosser
UCLA ASME X1 Robotics 2017-18: High Accuracy Die Tosser Project


testCV.py:
- - - - - 
-


detectCup.py:
- - - - - - - 
Either takes an input image (when running on Ubuntu VM) or captures an image using a camera (when using Raspberry Pi). Isolates the red regions of an image, and then searches for rectangles, ultimately detecting the red solo cup. Saves image of detected cup in the same directory as the program. Prints the pixel coordinates of the corners of the cup, to terminal.

*If using program on RPi: Set "CAMERA_ENABLED" to 1 at the top of the program, and run program with command "python detectCup.py".
*If using program on Ubuntu VM: Set "CAMERA_ENABLED" to 0 at the top of the program, and run program with command "python detectCup.py -i <path_to_input_image>".


setupInstructions
- - - - - - - - -
Contains instructions to set up Ubuntu Virtual Machine and Raspberry Pi environments.
