import speech_recognition as sr

def speech_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for test input...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:

            audio = recognizer.listen(source, timeout=0.5, phrase_time_limit=2)
            test_input = recognizer.recognize_google(audio)
            return test_input
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the test input.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

if __name__ == "__main__":
    test_result = speech_input()
    if test_result:
        print(f"Recognized test input: {test_result}")
