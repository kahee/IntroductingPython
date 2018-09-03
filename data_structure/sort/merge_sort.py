def merge_sort(list):
    length = len(list)

    if length > 1:
        mid = length // 2
        left_list = list[:mid]
        right_list = list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i, j, k = 0, 0, 0

        length_left = len(left_list)
        length_right = len(right_list)

        while i < length_left and j < length_right:

            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
                k += 1

            else:
                list[k] = right_list[j]
                j += 1
                k += 1

        while i < length_left:
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < length_right:
            list[k] = right_list[j]
            j += 1
            k += 1

        return list


if __name__ == '__main__':
    num = [5, 1, 4, 7, 2, 6, 8, 3]

    result = merge_sort(num)
    print(result)
