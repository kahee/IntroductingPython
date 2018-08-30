# 그래프 인접리스트
ajd_list = [
    [2, 1], [3, 0], [3, 0], [9, 8, 2, 1],
    [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]
]

N = len(ajd_list)

# 저점 방문 여부 확인 용
visited = [False] * N


def dfs(v):
    visited[v] = True
    print(v, ' ', end='')
    for w in ajd_list[v]:
        if not visited[w]:
            # 정점) w에 인접한 정점으로 dfs()재귀호출
            dfs(w)


if __name__ == '__main__':
    print('DFS 방문순서')
    for i in range(N):
        if not visited[i]:
            dfs(i)

