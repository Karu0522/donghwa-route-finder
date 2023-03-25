from tkinter import *
import tkinter.messagebox
from collections import deque

graph=[
    [],
    [2,3,5,6],
    [1,3,11],
    [1,2,4,5,10,11],
    [3,5,7,8,9,10],
    [1,3,4,6,7],
    [1,5,7,16],
    [4,5,6,8,15,16],
    [4,7,9,14,15],
    [4,8,10,13,14],
    [3,4,9,11,12,13],
    [2,3,10,12],
    [10,11,13],
    [9,10,12,14],
    [8,9,13,15],
    [7,8,14,16],
    [6,7,15,17],
    [16,18,19],
    [17,19,20],
    [17,18,20],
    [18,19]
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
    12:'Starfield',
    13:'Haru',
    14:'Pearland',
    15:'Truetown',
    16:'Mancho',
    17:'Bluetree',
    18:'Miso',
    19:'Sky',
    20:'Nitro'
}

cityReverse={v:k for k,v in city.items()} 

def search():
    try:
        start=cityReverse[entry1.get()]
        end=cityReverse[entry2.get()]
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
        result.config(text=f'{city[start]}에서 {city[end]}까지의 최단거리: {path[end]}')
    except KeyError:
        tkinter.messagebox.showerror("오류","올바르지 않은 값입니다.")

tk=Tk()
tk.title('Donghwa')
tk.geometry('400x100')
label=Label(tk,text='동화 도시 최단거리 계산기')
label.pack()
button=Button(tk,text='계산하기',command=search)
button.pack(side=RIGHT,padx=10,pady=10)
entry1 = Entry(tk,width=50,border=1,relief='solid')
entry1.pack()
entry2 = Entry(tk,width=50,border=1,relief='solid')
entry2.pack()
result=Label(tk,text='')
result.pack()
tk.mainloop()