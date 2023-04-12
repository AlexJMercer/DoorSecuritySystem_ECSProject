from face_recog import *
from keypad_main import *

training_img = face_recog.train_img_arr
image_encodings = face_recog.train_img_encode


if __name__ == '__main__':
    choice = -1
    while choice != 3:
        print("\n___Welcome to Door Lock Security System !!___\n")
        print("Do you want to :")
        print("1) Add new users")
        print("2) Authenticate ")
        print("3) Exit System")

        print("Your choice : ")
        choice = int(input())
        if choice == 1:
            # Enter password to confirm identity
            # keypad.getDeets()
            # if keypad.getAuthToken() == True:
            face_recog.image_collection()
            face_recog.training_mode()
            # else:
            #     print("Wrong Password.")
            #     break

        elif choice == 2:
            face_recog.takePhoto()

        elif choice == 3:
            print("Bye bye !")

        else:
            print("Invalid Choice. Please Try Again...")
        
            

