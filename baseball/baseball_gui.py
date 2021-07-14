import random
from tkinter import *

answer = range(1,10)
gameAnswer = random.sample(answer, 4)

tries = []

count = 0

def check() :
    global count
    
    tries.clear()
    count += 1
    scount = 0
    bcount = 0
    flag = 0
    
    a = int(ent.get())
    answer = a
    
    a1 = a//1000
    a = a%1000
    a2 = a//100
    a = a%100
    a3 = a//10
    a = a%10
    a4 = a//1

    tries.append(a1)
    tries.append(a2)
    tries.append(a3)
    tries.append(a4)
    
    for i in range(4):
        if tries[i] in gameAnswer:
            bcount+=1
            flag+=1
        if gameAnswer[i] == tries[i]:
            scount+=1
            flag+=1
        if flag == 2:
            bcount-=1
        flag = 0
    
    if(scount == 4):
        messagebox.showinfo("정답입니다.", "정답입니다 : "+str(count)+"번")
        root.destroy()
    else:
        t = str(scount) + "S " + str(bcount) + "B"
        messagebox.showinfo("정답", t)
        
        txt.insert(END, str(answer)+" "+t+"\n")
        
        ent.delete(0, END)

def enter(event) :
    check()

def answer() :
    strans = list(map(str, gameAnswer))
    hint = "정답은 " + strans[0] +", "+ strans[1] +", "+ strans[2] +", "+ strans[3] +" 입니다."
    messagebox.showinfo("정답", hint)
    
root = Tk()
root.title("숫자 야구 [ver 0.2]")
root.geometry("300x300+750+300")
root.resizable(False, False)

root.bind('<Return>', enter)

label = Label(root, text="숫자를 입력하세요.")
label.pack()

ent = Entry(root, width=5)
ent.pack()

btn = Button(root, text="시도하기", command=check)
btn.pack()

btn2 = Button(root, text="정답보기", command=answer)
btn2.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

txt = Text(root, width=30, height=15, yscrollcommand=scrollbar.set)
txt.pack()

root.mainloop()