def quick_sort(list):
    if len(list) <= 1:
        return list

    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


def partition(list, start, end):
    pivot = list[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] > pivot:
            right -= 1
        print(left,right)
        if left > right:
            done = True
        else:

            list[left], list[right] = list[right], list[left]

        print(list)

    list[start], list[right] = list[right], list[start]

    return right


def quick_sort_cpp_style(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort_cpp_style(list, start, pivot - 1)
        quick_sort_cpp_style(list, pivot + 1, end)
    return list


if __name__ == '__main__':
    num = [5, 1, 4, 7, 2, 6, 8, 3]


    result = quick_sort_cpp_style(num, 0, len(num) - 1)
    print(result)
