import tiktoken

from tools.logger import logger


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string. Same algorith used by chatGPT."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    logger(num_tokens)
    return num_tokens


if __name__ == "__main__":
    num_tokens_from_string("tiktoken is great!", "cl100k_base")
