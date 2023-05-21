import hashlib


def generate_hash(file_content):
    """Generate a hash from the contents of a file."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(file_content.encode('utf-8'))
    return sha256_hash.hexdigest()


def get_hash_from_file(file_path):
    """Generate hash from file."""
    with open(file_path, 'r+') as file:
        file_content = file.read()
        hash_value = generate_hash(file_content)
        return hash_value


# Example usage
given_file_path = 'C:/Users/sergi/PycharmProjects/Cartuli-AI-Assitant/scripts/python/code_to_be_refactored/ginea_pig.py'
print(get_hash_from_file(given_file_path))
