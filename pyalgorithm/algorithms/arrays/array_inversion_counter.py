from array import array


def _count_inversion_and_sort_in_array(a: array, start_index: int, end_index: int) -> int:
    print(f"[loop begin] start {start_index} end {end_index} array: {a}")
    if start_index == end_index:
        return 0

    if start_index + 1 == end_index:
        if a[start_index] > a[end_index]:
            temp = a[start_index]
            a[start_index] = a[end_index]
            a[end_index] = temp
            return 1
        else:
            return 0

    middle_index = (start_index + end_index) // 2
    print(f"  middle {middle_index} of start {start_index} and end {end_index}")
    left_end_index = middle_index
    right_start_index = middle_index + 1
    left_inversion_count = _count_inversion_and_sort_in_array(a, start_index, left_end_index)
    right_inversion_count = _count_inversion_and_sort_in_array(a, right_start_index, end_index)

    additional_inversion_count = 0
    left_index = start_index
    right_index = right_start_index
    new_array = array('i', [0] * ((end_index - start_index) + 1))
    while left_index <= left_end_index and right_index <= end_index:
        new_array_index = (left_index - start_index) + (right_index - right_start_index)
        if a[left_index] <= a[right_index]:
            new_array[new_array_index] = a[left_index]
            left_index = left_index + 1
        else:
            additional_inversion_count = additional_inversion_count + (left_end_index - left_index) + 1
            new_array[new_array_index] = a[right_index]
            right_index = right_index + 1

    if left_index <= left_end_index:
        for i in range(left_index, left_end_index + 1):
            new_array[(i - start_index) + (end_index - left_end_index)] = a[i]
    elif right_index <= end_index:
        for i in range(right_index, end_index + 1):
            new_array[(i - right_start_index) + (right_start_index - start_index)] = a[i]

    print(f"start {start_index} end {end_index} new array: {new_array}")

    for i in range (0, (end_index - start_index) + 1):
        a[i + start_index] = new_array[i]

    count = left_inversion_count + right_inversion_count + additional_inversion_count
    print(f"[loop end] count {count} start {start_index} end {end_index} array: {a}")
    return count


def count_inverses_in_array(a: array) -> int:
    length = len(a)
    return _count_inversion_and_sort_in_array(a, 0, length - 1)