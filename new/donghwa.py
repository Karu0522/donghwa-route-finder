from collections import deque

graph=[
    [],
    [2,3,5,6],
    [1,3,11],
    [1,2,4,5,10,11],
    [3,5,7,8,9,10],
    [1,3,4,6,7],
    [1,5,7,19,20],
    [4,5,6,8,19],
    [4,7,9,17,18,19],
    [4,8,10,15,16,17],
    [3,4,9,11,13,14,15],
    [2,3,10,12,13],
    [11,13],
    [10,11,12,14],
    [10,13,15],
    [9,10,14,16],
    [9,15,17],
    [8,9,16,18],
    [8,17,19],
    [6,7,8,18,20],
    [6,19]
]

city={
    1:'Central',
    2:'Seaside',
    3:'Newmoon',
    4:'Neo',
    5:'Day',
    6:'Nova',
    7:'Dream',
    8:'Lato',
    9:'Snow',
    10:'Wind',
    11:'Raon',
    12:'Nitro',
    13:'Starfield',
    14:'Sky',
    15:'Haru',
    16:'Bluetree',
    17:'Pearland',
    18:'Miso',
    19:'Truetown',
    20:'Mancho'
}

cityReverse={v:k for k,v in city.items()} 

def search(start,end):
    path=[0]*21
    visited=[False]*21
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                path[i]=path[v]+1
                queue.append(i)
                visited[i]=True
    print(f'{city[start]}에서 {city[end]}까지의 최단거리: {path[end]}')

while True:
    a=input("출발 도시를 입력하세요: ")
    if a not in cityReverse:
        print('없는 도시입니다.')
        continue
    b=input("도착 도시를 입력하세요: ")
    if b not in cityReverse:
        print('없는 도시입니다.')
        continue
    search(cityReverse[a],cityReverse[b])

