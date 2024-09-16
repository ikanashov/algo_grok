def merge_sorted_list(list1: list[int], list2: list[int]) -> list[int]:
    merged_list = []

    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return nums[left], nums[right]
        elif current_sum < target:
            left += 1  # увеличиваем левый указатель
        else:
            right -= 1  # уменьшаем правый указатель
    return None  # если такой пары нет
