import sys
input=sys.stdin.readline

UP, RIGHT, DOWN, LEFT=(-1, 0), (0, 1), (1, 0), (0,-1)

CCTV={
    1: [[DOWN], [UP], [RIGHT], [LEFT]],
    2: [[DOWN, UP], [RIGHT, LEFT]],
    3: [[UP, RIGHT], [RIGHT, DOWN], [DOWN, LEFT], [LEFT, UP]],
    4: [[RIGHT, UP, LEFT], [DOWN, UP, LEFT], [DOWN, RIGHT, LEFT], [DOWN, RIGHT, UP]],
    5: [[DOWN, RIGHT, UP, LEFT]]
}

BLANK=0
WALL=6

def cctv_path(office, n, m, direction, visited):
    cctv_visited=set()

    for dn, dm in direction:
        new_n, new_m=n, m
        # print(f'방향: {dn, dm}')
        while True:
            new_n, new_m = new_n + dn, new_m + dm
            # print(f'new:{new_n, new_m}')
            #갈 수 있는 끝까지 감
            if not (0<=new_n<N and 0<=new_m<M): break            
            if office[new_n][new_m]==WALL: break
            
            if (new_n, new_m) in visited: continue # 이미 다른 CCTV가 방문한 장소    
            if office[new_n][new_m]>0: continue # CCTV를 만남

            # print('-> 추가됨')
            cctv_visited.add((new_n, new_m))

    return cctv_visited

def dfs(depth, visited):
    # 모든 CCTV의 방향 조합 완전탐색
    global min_blind, blank_cnt

    if depth == len(cctvs): #모든 CCTV 완료
        min_blind = min(min_blind, blank_cnt-len(visited))
        return

    (n, m), c_type = cctvs[depth]

    for dirs in CCTV[c_type]:
        new_visited = visited | cctv_path(office, n, m, dirs, visited)
        dfs(depth + 1, new_visited)

N, M=map(int, input().split())
office=[list(map(int, input().split()))for _ in range(N)]


# CCTV 목록 저장
cctvs = [((n, m), office[n][m]) 
         for n in range(N) for m in range(M)
         if 1 <= office[n][m] <= 5]
blank_cnt=sum(1 for n in range(N) for m in range(M) if office[n][m]==BLANK)

min_blind = 10**9
dfs(0, set())
print(min_blind)