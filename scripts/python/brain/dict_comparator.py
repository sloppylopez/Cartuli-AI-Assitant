from tools.logger import logger


def compare_dictionaries(dict1, dict2):
    matching_values = []
    for key in dict1:
        if key in dict2:
            matching_values.append(key)
    return matching_values


def return_non_matching_values(dict1, dict2):
    non_matching_values = {}
    try:
        logger("long_term_hash_memory: " + str(dict1))
        logger("target_file_contents: " + str(dict2))
        for value in dict2:  # Use 'value' instead of 'key' for iterating over list elements
            if value not in dict1:
                non_matching_values[value] = dict2[value]
    except Exception as e:
        logger(e)

    return non_matching_values


if __name__ == "__main__":
    # Example usage:
    dict1 = {'key1': ('value1', 123), 'key2': ('value2', 456), 'key3': ('value3', 789)}
    dict2 = {'key2': ('another_value2', 789), 'key4': ('value4', 987), 'key5': ('value5', 654)}
    print(dict1)
    print(dict2)
    result = compare_dictionaries(dict1, dict2)
    print(result)
    non_matching_values = return_non_matching_values(dict1, dict2)
    print(non_matching_values)
