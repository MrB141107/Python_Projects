from typing import Optional


def binary_search(array: list[int], target: int) -> Optional[int]:
    '''Simple implementation of binary search algorithm. It takes a sorted list
    and a target and returns the index of the target in the list. If the list
    doesn't contain the target that the algorithm returns None '''

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid

    return None


if __name__ == '__main__':
    '''testing that the algorithm works properly'''

    arr = [1, 4, 6, 8, 10, 15, 19, 25, 45, 48]
    num = 19

    result = binary_search(arr, num)

    if result is not None:
        print(f"The index of {num} is {result}")
    else:
        print(f"The list does not contain number {num}")
