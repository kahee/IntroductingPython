def pick(n, picked, to_pick):
    """
    n개의 원소 중 m개를 고르는 모든 조합을 찾는 알고리즘
    :param n: 젠처 원소의 수
    :param picked: 지금까지 고른 원소들의 번호 - list()
    :param to_pick: 더 고를 원소의 수
    :return:
    """

    # 기저 사례 : 더 고를 원소가 없을 때 고른 원소들 출력
    if to_pick is 0:
        return print(picked)

    # 고를 수 잇는 가장 작은 번호를 계산
    if len(picked) is 0:
        smallest = 0
    else:
        smallest = picked[-1] + 1

    # 이 단계에서 원소 하나를 고름
    for next in range(smallest, n):
        picked.append(next)
        pick(n, picked, to_pick - 1)
        picked.pop()


if __name__ == '__main__':
    result = list()
    pick(7, result, 4)
