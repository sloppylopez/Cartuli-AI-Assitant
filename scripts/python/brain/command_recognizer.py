def defragment_input(doc):
    ai = ""
    command_action = ""
    target = ""
    for token in doc:
        if token.i == 0:
            ai = token.text
        elif token.i == 1:
            command_action = token.text
        elif token.i == 2:
            target = token.text

    print("AI:", ai)
    print("Command Action:", command_action)
    print("Target:", target)
    return ai, command_action, target


if __name__ == "__main__":
    import spacy

    nlp = spacy.load("en_core_web_sm")
    # Example usage
    user_input = "Moneypenny location hands"
    doc = nlp(user_input)
    defragment_input(doc)
