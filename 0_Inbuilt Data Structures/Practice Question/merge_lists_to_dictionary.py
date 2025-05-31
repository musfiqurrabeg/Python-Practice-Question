def merge_lists_to_dictionary(keys, values):
    if len(keys) != len(values):
        return False  # Return False if lengths differ
    merged_dict = {}
    for i in range(len(keys)):
        merged_dict[keys[i]] = values[i]
    return merged_dict