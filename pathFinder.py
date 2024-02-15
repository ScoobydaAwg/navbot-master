import speech_recognition as sr

def speech_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for room number...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=1)
            room_number = recognizer.recognize_sphinx(audio)
            return room_number
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

if __name__ == "__main__":
    user_input = speech_input()
    if user_input:
        print(f"Recognized room number: {user_input}")
