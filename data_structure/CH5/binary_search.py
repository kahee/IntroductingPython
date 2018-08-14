import random


def binary_search(left, right, t):
    if left > right:
        # 탐색실패 ( 즉 , t가 리스트에 없음)
        return None

    # 리스트에서 탐색할 부분의 중간 항목의 인덱스 계산
    mid = (left + right) // 2

    if a[mid] == t:
        # 탐색 성공
        return mid

    if a[mid] > t:
        # 앞부분 탐색
        binary_search(left, mid - 1, t)
    else:
        # 뒷부분 탐색
        binary_search(mid + 1, right, t)


if __name__ == '__main__':
    a = [random.randint(1, 100) for _ in range(20)]
    print(binary_search(0, 19, 66))
