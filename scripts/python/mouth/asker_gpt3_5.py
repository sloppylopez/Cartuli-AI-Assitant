import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the model and tokenizer
model_name = "gpt2"  # or any other GPT-2 model variant
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


# Define a function for interacting with the model
def chat_with_model(user_input):
    # Tokenize the user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt")

    # Generate the attention mask
    attention_mask = torch.ones_like(input_ids)

    # Generate a response from the model
    response = model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=100,
                              num_return_sequences=1)

    # Decode and return the response
    return tokenizer.decode(response[:, input_ids.shape[-1]:][0], skip_special_tokens=True)


# Start the conversation
print("GPT-4: Hello! How can I assist you today?")
user_input = input("User: ")

while user_input.lower() != "bye":
    # Get the model's response
    model_response = chat_with_model(user_input)

    print("GPT-4:", model_response)

    # Get the user's next input
    user_input = input("User: ")

print("GPT-4: Goodbye! Have a nice day!")
