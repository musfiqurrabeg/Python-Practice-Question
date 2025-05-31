def merge_dicts_with_overlapping_keys(dicts):
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict
