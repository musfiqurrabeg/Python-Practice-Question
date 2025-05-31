def max_consecutive_difference(lst):
    if len(lst) < 2:
        return 0
    max_diff = 0
    for i in range(len(lst) - 1):
        current_diff = abs(lst[i] - lst[i + 1])
        if current_diff > max_diff:
            max_diff = current_diff
    return max_diff
