def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        print(i)
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def selection(list):
    length = len(list)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if list[min_index] > list[j]:
                min_index = j
            list[min_index], list[i] = list[i], list[min_index]

    return list


def insertion(list):
    length = len(list)

    for i in range(1, length):
        curr_value = list[i]
        index = i
        print(curr_value, index)

        while index > 0 and list[index - 1] > curr_value:
            list[index] = list[index - 1]
            index -= 1
        list[index] = curr_value
        print(list)

    return list


if __name__ == '__main__':
    num = [5, 1, 4, 7, 2, 6, 8, 3]
    # result = bubble_sort(num)
    # result = selection(num)
    result = insertion(num)
    print(result)
