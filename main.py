def find_min_max(arr):
    def divide_and_conquer(low, high):
        if low == high:
            return arr[low], arr[low]
        elif high == low + 1:
            return (min(arr[low], arr[high]), max(arr[low], arr[high]))

        mid = (low + high) // 2
        left_min, left_max = divide_and_conquer(low, mid)
        right_min, right_max = divide_and_conquer(mid + 1, high)

        return min(left_min, right_min), max(left_max, right_max)

    if not arr:
        raise ValueError("Масив не може бути порожнім")

    return divide_and_conquer(0, len(arr) - 1)


arr = [3, 1, 8, 2, 5, 10, -2, 7]
print(find_min_max(arr))