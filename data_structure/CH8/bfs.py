# 그래프 인접리스트
ajd_list = [
    [2, 1], [3, 0], [3, 0], [9, 8, 2, 1],
    [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]
]

N = len(ajd_list)
# 저점 방문 여부 확인 용
visited_dfs = [False] * N


def bfs(i):
    queue = []
    visited_dfs[i] = True
    queue.append(i)

    while len(queue) != 0:
        # 큐가 맨 앞에서 제거된 정점을 v가 참조하게함
        v = queue.pop(0)
        print(v, ' ', end='')
        for w in ajd_list[v]:
            if not visited_dfs[w]:
                visited_dfs[w] = True
                # v에 인접하면서 방문 안된 정점 큐에 삽입
                queue.append(w)


if __name__ == '__main__':
    print('BFS 방문순서')
    for i in range(N):
        if not visited_dfs[i]:
            bfs(i)
