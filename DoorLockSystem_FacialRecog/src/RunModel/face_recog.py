import cv2 as cv
import face_recognition as fr
import time
import os

faceAuth = False
training_img = []
image_encodings = []

class face_recog:
    def train_img_arr():
        return training_img
    
    
    def train_img_encode():
        return image_encodings

    
    
    def image_collection():
        print("Enter image collection mode for training...")
        cam = cv.VideoCapture(0)     
        cv.namedWindow("Press Space to take a Photo", cv.WINDOW_NORMAL)

        img_counter = 0
        while True:
            path_to_image = os.getcwd()
            _, frame = cam.read()
            if not _:
                print("Failed to grab a frame")
                break
            cv.imshow("Press space to take a photo", frame)

            key = cv.waitKey(1)
            if key == ord('q'):
                print("Escaping Image Collection Mode")
                break
            elif key == ord(' '):
                image_name = f"training-{img_counter}-img.jpg"
                path_to_image += f"/DoorLockSystem_FacialRecog/src/user_img/" + image_name
                cv.imwrite(path_to_image, frame)
                print(f"Image #{img_counter + 1} is written !")
                img_counter += 1
        
        print("Exiting Image Collection mode...")
        cam.release()
        cv.destroyAllWindows()


    def training_mode():
        print("Now starting Training Mode")
        path = os.getcwd() + "/DoorLockSystem_FacialRecog/src/user_img/"

        print("Loading images for training...")

        for img in os.listdir(path):
            if (img.endswith(".jpg")):
                name = img.split(".img")[0]
                training_img.append(name)

                image = fr.load_image_file(path + img)    
                encoding = fr.face_encodings(image)
                image_encodings.append(encoding)
        
        print("Training Done !")



    
    def takePhoto():
        print("Opening Camera to take Photo...")
        cam = cv.VideoCapture(0)
        counter = 0
        while counter != 1:
            _, frame = cam.read()
            if not _:
                print("Failed to grab Frame")
                break
            cv.imshow("Please look into the Camera", frame)
            
            key = cv.waitKey(1)

            if key == ord('q'):
                print("Escape hit, closing...")
                break
            elif key == ord(' '):
                img_name = "TempPhoto.jpg"
                path = os.getcwd() + "/DoorLockSystem_FacialRecog/src/unknown_img/" + img_name
                cv.imwrite(path, frame)
                counter += 1

        cam.release()
        cv.destroyAllWindows()
        print("Exiting Photo Mode")
        time.sleep(1)
        print("Processing Image...")
        face_recog.compareFaces(frame)


    def compareFaces(image):
        global faceAuth

        print("Trying to recognize faces...\n")
        face_encoding_unknown = fr.face_encodings(image)[0]

        if image_encodings == []:
            face_recog.build_arrays()

        matches = []

        # Add loop to include all encodings into a single tuple
        for enc in image_encodings:
            matches.append(fr.compare_faces(face_encoding_unknown, enc, 0.9))

        for match in matches:
            for m in match:
                if m == True:
                    faceAuth = True
                    break

        if faceAuth == True:
            print("Access Granted !")
        else:
            print("Not recognized.")



    def build_arrays():
        global training_img
        global image_encodings

        path = os.getcwd() + "/DoorLockSystem_FacialRecog/src/user_img/"

        for img in os.listdir(path):
            if (img.endswith(".jpg")):
                name = img.split(".img")[0]
                training_img.append(name)

                image = fr.load_image_file(path + img)    
                encoding = fr.face_encodings(image)
                image_encodings.append(encoding)
