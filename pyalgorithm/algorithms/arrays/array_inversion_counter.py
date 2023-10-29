from array import array


def _count_inversion_and_sort_in_array(
    a: array, start_index: int, end_index: int
) -> int:
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
    left_end_index = middle_index
    right_start_index = middle_index + 1
    left_inversion_count = _count_inversion_and_sort_in_array(
        a, start_index, left_end_index
    )
    right_inversion_count = _count_inversion_and_sort_in_array(
        a, right_start_index, end_index
    )

    additional_inversion_count = 0
    left_index = start_index
    right_index = right_start_index
    left_array_copy = a[start_index:right_start_index]
    while left_index <= left_end_index and right_index <= end_index:
        update_index = left_index + (right_index - right_start_index)
        if left_array_copy[left_index - start_index] <= a[right_index]:
            a[update_index] = left_array_copy[left_index - start_index]
            left_index = left_index + 1
        else:
            additional_inversion_count = (
                additional_inversion_count + (left_end_index - left_index) + 1
            )
            a[update_index] = a[right_index]
            right_index = right_index + 1

    if left_index <= left_end_index:
        for i in range(left_index, left_end_index + 1):
            a[i + (end_index - left_end_index)] = left_array_copy[i - start_index]

    count = left_inversion_count + right_inversion_count + additional_inversion_count
    return count


def count_inverses_in_array(a: array) -> int:
    length = len(a)
    return _count_inversion_and_sort_in_array(a, 0, length - 1)
