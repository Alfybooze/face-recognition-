import cv2 

#loades the HAAR pretrained model from cv2
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#face_classifier = cv2.cascadeclassifier(cv2.data.haarcascades +"haarcascade_frontalface_default")

#allows the cv2 video capture class to interface with the default systaem  camera
video_capture = cv2.VideoCapture(0)

#returns a tuple with the next video frames a checks weatherb it was read correctly
ret,frames = video_capture.read()

#this creates a funtion that turns the image from RGB to a gray image so it can be reead properly
def detect_bounding_box(vid):
    #turns the image into gray image
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    
# sets limts on the minimum width of pixielc can be read scales down the image
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
#loops through  a list of detected faces using a loop
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:
    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # use the function we created earlier to the video frame

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    # Check if 'q' or 'Escape' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:  # 27 is the ASCII code for the Escape key
        break

video_capture.release()
cv2.destroyAllWindows()
