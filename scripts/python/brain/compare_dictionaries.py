def compare_dictionaries(dict1, dict2):
    matching_values = []
    for key in dict1:
        if key in dict2:
            matching_values.append(key)
    return matching_values


def return_non_matching_values(dict1, dict2):
    non_matching_values = {}

    for key in dict2:
        if key not in dict1:
            non_matching_values[key] = dict2[key]

    return non_matching_values


if __name__ == "__main__":
    # Example usage:
    dict1 = {'key1': ('value1', 123), 'key2': ('value2', 456), 'key3': ('value3', 789)}
    dict2 = {'key2': ('another_value2', 789), 'key4': ('value4', 987), 'key5': ('value5', 654)}

    result = compare_dictionaries(dict1, dict2)
    print(result)
