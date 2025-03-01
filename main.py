import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load Known faces
harish_image = face_recognition.load_image_file("faces/passport img.jpg")

# encoding --> helps in comparing in form of numbers
harish_face_encoding = face_recognition.face_encodings(harish_image)[0]

nick_image = face_recognition.load_image_file("faces/nick1.jpg")
nick_face_encoding = face_recognition.face_encodings(nick_image)[0]

# names store
Known_face_encodings = [harish_face_encoding,nick_face_encoding]
Known_face_names = ["Harish", "Nick"]

# list of expected students
expected_students = Known_face_names.copy()

face_locations = []
face_encodings = []

# get current date and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", 'w+', newline="")
writer = csv.writer(f)

while True:
    # Grab a single frame of video
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # recognize face
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(Known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(Known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)
        
        if matches[best_match_index]:
            name = Known_face_names[best_match_index]

            # Add text if person present
        if name in Known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,100)
            fontScale = 1.5
            fontColor = (255,0, 0)
            lineType = 2
            thickness = 3
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font,fontScale,fontColor,thickness,lineType)

            if name in expected_students:
              expected_students.remove(name)
              current_time = now.strftime("%H:%M:%S")
              writer.writerow([name, current_time])


    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()    
cv2.destroyAllWindows()
f.close()