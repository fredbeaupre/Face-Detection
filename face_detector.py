import cv2
from random import randrange


### CODE FOR PICTURES STARTS HERE ###


# Load pre-trained data
# trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
#img = cv2.imread('solvay.png')



# Convert to grayscale
#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
# coordinate of the top left corner is returned
# along with the width and height of the square
#face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#print (face_coordinates)

# Draw rectangles around the faces
# first tuple is coordinates of top left corner
# second tuple is bottom right corner calculated from coordinates and height and width
#for (x, y, w, h) in face_coordinates:
    # cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

#cv2.imshow('Face-detection algorithm', img)
#cv2.waitKey()
### CODE FOR PICTURES ENDS HERE ###



### CODE FOR VIDEOS STARTS HERE ###

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

# Iterate over all frame in the video
while True:
    
    # Read current frame
    successful_frame_read, frame = webcam.read()
    # Convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    # Draw the rectangle on each frame
    for (x, y, w, h) in face_coordinates:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
    # Show
    cv2.imshow('Face-detection', frame)
    key = cv2.waitKey(1)

    # stop functionality on pressing 'q' or 'Q'
    if key==81 or key==113:
        break

webcam.release()
    