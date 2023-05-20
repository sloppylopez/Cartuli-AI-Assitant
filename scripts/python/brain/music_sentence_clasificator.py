import spacy

def extract_info(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    app_name = ""
    song_name = ""
    author = ""

    for token in doc:
        if token.lower_ == "youtube":
            app_name = token.text
        elif token.lower_ == "song" and doc[token.i + 1].text == "'":
            song_name = doc[token.i + 2].text
            author = doc[token.i + 4].text

    return app_name, song_name, author

if __name__ == "__main__":
    # Example usage
    sentence = "YouTube song 'Shape of You' by Ed Sheeran"
    app, song, author = extract_info(sentence)
    print(f"App Name: {app}")
    print(f"Song Name: {song}")
    print(f"Author: {author}")
