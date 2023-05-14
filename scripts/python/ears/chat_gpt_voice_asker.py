import openai
import speech_recognition as sr
import os

from scripts.python.mouth.display_notification import display_notification

def asker():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is not None:
        print("API key found.")
    else:
        print("OPENAI_API_KEY environment variable is not set.")
        exit()
    # Set up OpenAI API key
    openai.api_key = api_key
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    try:
        # Convert speech to text
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        # Generate response from OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=60
        )

        if 'choices' in response and len(response['choices']) > 0:
            generated_text = response['choices'][0]['text'].strip()
            # Display the recognized text as a notification
            display_notification(generated_text)
            print("Generated response:", generated_text)
        else:
            print("No response received from the API.")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


