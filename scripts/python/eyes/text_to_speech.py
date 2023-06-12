import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Convert text to speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()


# Convert speech to text
if __name__ == '__main__':
    speak_text("Hello, my name is Cartuli. I am your personal assistant. How can I help you?")
