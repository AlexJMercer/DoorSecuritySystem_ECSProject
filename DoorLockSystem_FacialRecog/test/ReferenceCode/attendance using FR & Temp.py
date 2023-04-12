# For face recognition
import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

# For temperature sensor
# from smbus2 import SMBus
# from mlx90614 import MLX90614
import time
# import board
# import digitalio
# import adafruit_character_lcd.character_lcd as characterlcd


lcd_columns = 16
lcd_rows = 2

# lcd_rs = digitalio.DigitalInOut(board.D26)
# lcd_en = digitalio.DigitalInOut(board.D19)
# lcd_d4 = digitalio.DigitalInOut(board.D13)
# lcd_d5 = digitalio.DigitalInOut(board.D6)
# lcd_d6 = digitalio.DigitalInOut(board.D5)
# lcd_d7 = digitalio.DigitalInOut(board.D11)


# lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
#                                       lcd_d7, lcd_columns, lcd_rows)
# bus = SMBus(1)
# sensor = MLX90614(bus, address=0x5A)

# lcd.clear()

# lcd.message = "Welcome"
# time.sleep(1)
# lcd.clear()



# Face Recognition Initialization
video_capture = cv2.VideoCapture(0)

known_faces_names = []
known_face_encoding = []

data_dir = "D:\Study\VIT-AP Study Materials\Semester 4\ECS Project Jahnavi\DoorSecuritySystem_ECSProject\DoorLockSystem_FacialRecog\src\RunModel\images/"
extensions = [".png", ".jpg"]
for image in os.listdir(data_dir):
    for extension in extensions:
        if(image.endswith(extension)):
            name = image.split(extension)[0]
            known_faces_names.append(name)
            
            student_image = face_recognition.load_image_file(data_dir + image)
            student_image_encoding = face_recognition.face_encodings(student_image)[0]
            known_face_encoding.append(student_image_encoding)
            #print(name) # prints the basename of the file without extension
#print(known_face_names)
            
students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + ".csv", 'w+', newline= '')
lnwriter = csv.writer(f)

while students:
    # lcd.clear()
    # lcd.message = "Taking\nAttendance..."
    
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if True:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
                
            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    
                    students.remove(name)
                    print(name + " - Attendance Marked")
                    # lcd.clear()
                    # lcd.message = name + "\nPresent"
                    time.sleep(3)
                    print("Check Temperature")
                    # lcd.clear()
                    # lcd.message = "Check\nTemperature"
                    time.sleep(3)
                    # lcd.clear()
                    # lcd.message = "Press Enter\nFor Temperature"
                    
                    check_temp = input("Hit enter to capture temperature")
                    # if check_temp == "":
                        # lcd.clear()
                        # temp = sensor.get_object_1()
                        # if (temp <= 37):
                        #     lcd.message = "Temp: " + str(temp) + " \n" + "Safe" 
                        # else:
                        #     lcd.message = "Temp: " + str(temp) + " \n" + "Not Safe"
                        #     time.sleep(1)
                        #     lcd.clear()
                        #     lcd.message = "Please Wear Mask"
                    
                    print("Students who are yet to mark their attendance - " + str(students))
                    
                    current_time = now.strftime("%H:%M")
                    lnwriter.writerow([name, current_time])
                    time.sleep(2)
                    # lcd.clear()
                # else:
                    # lcd.clear()
                    # lcd.message = "Attendance\nalready marked"
    cv2.imshow("attendance system", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# lcd.clear()
time.sleep(1)
# lcd.message = "All Students\nMarkedAttendance"
time.sleep(2)
# lcd.clear()
# lcd.message = "Turning Off..."
time.sleep(2)
# lcd.clear()
video_capture.release()
cv2.destroyAllWindows()
f.close()



