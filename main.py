
import json
from speechInput import speech_input
from Keyword import extract_keywords
from speechWithImg import display_images_in_order
from FaceDetector import detect_faces

def main():
    print("Checking for face...")
    if detect_faces():
        print("Face detected. Proceeding with the application.")
        choice = input("Would you like to use voice recognition? (y/n): ")
        if choice.lower() == 'y':
            user_input = speech_input()
            if user_input:
                keywords = extract_keywords(user_input)
                if keywords:
                    for keyword in keywords:
                        display_images_in_order(keyword)
                else:
                    print("No keywords found in the input.")
        elif choice.lower() == 'n':
            user_input = input("Enter your destination: ")
            keywords = extract_keywords(user_input)
            if keywords:
                for keyword in keywords:
                    display_images_in_order(keyword)
            else:
                print("No keywords found in the input.")
        else:
            print("Invalid option. Please enter 'y' for yes or 'n' for no.")
    else:
        print("No face detected. Exiting the application.")

if __name__ == "__main__":
    main()
