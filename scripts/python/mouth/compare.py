import openai
import speech_recognition as sr
import spacy

from mouth.asker import get_open_ai_key

# Set up your OpenAI API key
openai.api_key = get_open_ai_key()

# Initialize speech recognition and language model
recognizer = sr.Recognizer()
nlp = spacy.load('en_core_web_sm')


def convert_speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Speech:", text)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service:", e)

    return ""


def chat_with_openai(messages):
    # Generate a response from OpenAI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=messages,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        user="user",
        system="system"
    )

    # Extract the generated message from the response
    generated_message = response.choices[0].text.strip().split('\n')[-1]

    return generated_message


def run_chatbot():
    # Example usage
    conversation = "User: Hello\nChatGPT: Hi, how can I assist you today?"

    while True:
        user_input = convert_speech_to_text()
        if not user_input:
            user_input = input("Enter your message manually: ")
        if user_input:
            doc = nlp(user_input)
            user_input = " ".join(token.text for token in doc)
            conversation += f"\nUser: {user_input}"
            response = chat_with_openai(conversation)
            conversation += f"\nChatGPT: {response}"
            print("ChatGPT:", response)
            if user_input.lower() == 'bye':
                break
