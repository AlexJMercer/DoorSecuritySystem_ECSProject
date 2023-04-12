import cv2

name = "hashu"

cam = cv2.VideoCapture(0)

cv2.namedWindow("Press space to take a photo", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Press space to take a photo", 1280, 720)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Press space to take a photo", frame)
    
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = name + ".jpg"
        path = "D:\Study\VIT-AP Study Materials\Semester 4\ECS Project Jahnavi\DoorSecuritySystem_ECSProject\DoorLockSystem_FacialRecog\\trainingData/" + img_name
        cv2.imwrite(path, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
cam.release()        

cv2.destroyAllWindows()
