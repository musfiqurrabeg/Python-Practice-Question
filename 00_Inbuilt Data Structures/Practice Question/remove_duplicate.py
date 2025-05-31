def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        # Check if item is already in unique_list manually
        is_duplicate = False
        for unique_item in unique_list:
            if unique_item == item:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_list.append(item)
    return unique_list