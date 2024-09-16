def get_max_unique(list1: list[int]) -> int:
    if not list1:
        return None
    cnt_map = {}

    max_item = float("-inf")

    for item in list1:
        if item not in cnt_map:
            cnt_map[item] = 1
        else:
            cnt_map[item] += 1

    for key, value in cnt_map.items():
        if key > max_item and value == 1:
            max_item = key

    return max_item if max_item != float("-inf") and cnt_map[max_item] < 2 else None


# not worked
def get_max_unique_2(list1: list[int]) -> int:
    if not list1:
        return None
    cnt_map = {}

    max_item = float("-inf")
    old_max_item = float("-inf")

    for item in list1:
        if item not in cnt_map:
            cnt_map[item] = 1
            if item > max_item:
                old_max_item = max_item
                max_item = item
        else:
            if item == max_item:
                max_item = old_max_item
            cnt_map[item] += 1

    return max_item if cnt_map[max_item] < 2 else None
