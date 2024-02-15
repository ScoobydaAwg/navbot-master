import json
import cv2 as cv
import pyttsx3
import time

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def show_image(image_path, timeout=2):
    img = cv.imread(image_path)
    cv.namedWindow("Navigation Image", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("Navigation Image", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow("Navigation Image", img)
    cv.waitKey(int(timeout * 1000))  # Convert timeout to milliseconds

def display_image_with_text(image_path, text):
    show_image(image_path)
    speak_text(text)
    time.sleep(1)

def display_images_in_order(keyword):
    # Load the JSON data
    with open("image.json", "r") as f:
        data = json.load(f)

    # Check if the keyword exists in the data
    if keyword in data["A_block"]["Floor_1"]:
        # Retrieve image information for the keyword
        images_info = data["A_block"]["Floor_1"][keyword]

        # Sort images based on their order
        sorted_images_info = sorted(images_info, key=lambda x: x.get("order", 0))

        # Loop through each image information
        for image_info in sorted_images_info:
            image_path = image_info["path"]
            description = image_info["description"]

            # Display image with description
            display_image_with_text(image_path, description)

    else:
        print(f"No images found for '{keyword}'.")
