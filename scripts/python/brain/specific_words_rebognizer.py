import spacy


def recognize_words(sentence, word1, word2):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    found_words = []
    for token in doc:
        if token.text.lower() == word1.lower() or token.text.lower() == word2.lower():
            found_words.append(token.text)

    return found_words


# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
word1 = "fox"
word2 = "dog"
found_words = recognize_words(sentence, word1, word2)
print(found_words)
