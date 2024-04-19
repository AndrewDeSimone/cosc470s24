# Importing all necessary libraries 
import cv2 
import os 
  
# Read the video from specified path 
cam = cv2.VideoCapture("solutions\Lab 6\Eclipse 2024.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('solutions\Lab 6\data'): 
        os.makedirs('solutions\Lab 6\data')
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = r'C:\Users\andre\Documents\GitHub\cosc470s24\solutions\Lab 6\data\frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
