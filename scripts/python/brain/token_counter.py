import spacy


def count_tokens(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    token_count = len(doc)
    return token_count


if __name__ == "__main__":
    # Example usage
    given_text = "This is an example sentence."
    num_tokens = count_tokens(given_text)
    print("Number of tokens:", num_tokens)
