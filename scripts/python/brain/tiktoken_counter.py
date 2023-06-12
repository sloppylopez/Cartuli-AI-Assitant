import tiktoken

from tools.logger import logger, logger_err

cl_k_base = "cl100k_base"


def count_num_tokens_price(num_tokens, model_name):
    # Define the price per 1000 tokens for each model
    model_prices = {
        "text-davinci-003": 0.002,  # Price per 1000 tokens for gpt-3.5-turbo-8 model
        # Add other models and their corresponding prices here
    }

    # Get the price per 1000 tokens for the specified model
    price_per_1000_tokens = model_prices.get(model_name)

    if price_per_1000_tokens is None:
        return None  # Return None if the model is not found in the model_prices dictionary

    # Calculate the approximate cost by dividing the number of tokens by 1000, then multiplying by the price per 1000 tokens
    cost = (num_tokens / 1000) * price_per_1000_tokens

    return cost


def count_total_tokens(non_matching_values):
    total_tokens = 0
    try:
        for key, value in non_matching_values.items():
            tokens = num_tokens_from_string(value[0], cl_k_base)
            total_tokens += tokens
    except Exception as e:
        logger_err(e)
        pass

    return total_tokens


#                Model	Prompt	     Completion
# 8K context	$0.03 / 1K tokens	$0.06 / 1K tokens
# 32K context	$0.06 / 1K tokens	$0.12 / 1K tokens
# If we are refactoring we can assume the code will be an arbitrary percent smaller than the original to estimate price
# Ergo, we should be able to calculate some kind of ponder mean of the price of the refactored code.
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string. Same algorith used by chatGPT."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    logger(num_tokens)
    return num_tokens


if __name__ == "__main__":
    num_tokens_from_string("tiktoken is great!", "cl100k_base")
    count_num_tokens_price("tiktoken is great!")
