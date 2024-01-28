import cv2 
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
   
# Create an object to read  
# from camera 
video = cv2.VideoCapture('data/video/swing_short.mp4')

# so, convert them from float to integer. 
frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 
   
size = (frame_width, frame_height) 
   
# Below VideoWriter object will create a frame of above defined The output is stored in 'filename.avi' file. 
result = cv2.VideoWriter('filename.mp4', cv2.VideoWriter_fourcc(*'vp09'), 10, size) # works and displays!!!
# result = cv2.VideoWriter('filename.mp4', cv2.VideoWriter_fourcc(*'H264'), 10, size) # works
# result = cv2.VideoWriter('filename.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, size) # works
# result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size) # works
    
while(True): 
    ret, frame = video.read() 
  
    if ret == True:  
  
        # Write the frame into the 
        # file 'filename.avi' 
        result.write(frame) 
  
        # Display the frame 
        # saved in the file 
        #cv2.imshow('Frame', frame) 
  
        # Press S on keyboard  
        # to stop the process 
        #if cv2.waitKey(1) & 0xFF == ord('s'): 
        #    break
  
    # Break the loop 
    else: 
        break
  
# When everything done, release  
# the video capture and video  
# write objects 
video.release() 
result.release() 
    
# Closes all the frames 
#cv2.destroyAllWindows() 
   
print("The video was successfully saved") 