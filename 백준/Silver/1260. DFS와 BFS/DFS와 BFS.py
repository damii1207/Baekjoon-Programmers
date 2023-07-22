from collections import deque
n, m, v = map(int,input().split())

# 인접리스트
graph =  [[] for _ in range(n+1)] # 1번부터 n번까지의 정점 사용

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)  #  양방향이라서 서로 값 입력해줌

for i in range(1, n+1):
    graph[i].sort() # 순서 보장을 위해 오름차순 정렬 필요
# print(graph)

def bfs(start):
    queue = deque()
    visited = [0 for _ in range(n+1)]  # 0번부터 n번 정점까지
    queue.append(start) # 시작 정점 push
    visited[start]=1

    while len(queue) > 0: # if queue is not empty do while
        curr = queue[0]
        print(curr, end=' ')
        for nxt in graph[curr]: # [2,3,4]  정점간의 팔로우 관계 확인
            if visited[nxt] == 0 : # 방문 여부 확인
                visited[nxt] = 1
                queue.append(nxt)
        queue.popleft() # 다음 절정에 대한 처리를 다 했으니  pop()

dfs_sol = 0
bfs_sol = 0

visit = [0 for _ in range(n+1)]
visit[v] = 1

def dfs(curr):
    print(curr, end=' ')
    for nxt in graph[curr]:
        if visit[nxt] ==0:
            visit[nxt] = 1
            dfs(nxt)

dfs(v)
print()
bfs(v)