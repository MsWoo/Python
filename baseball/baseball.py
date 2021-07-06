import random

print("-------숫자 야구--------")

answer = range(1,10)
gameAnswer = random.sample(answer, 4)

tri = []

while True:
    
    print("숫자를 입력하세요 (4자리)")
    
    tri.clear()
    
    scount = 0
    bcount = 0
    flag = 0

    a = int(input())
    
    if(a == 999):
        print(gameAnswer)
    if(a == -999):
        break

    a1 = a//1000
    a = a%1000
    a2 = a//100
    a = a%100
    a3 = a//10
    a = a%10
    a4 = a//1

    tri.append(a1)
    tri.append(a2)
    tri.append(a3)
    tri.append(a4)

    for i in range(4):
        if tri[i] in gameAnswer:
            bcount+=1
            flag+=1
        if gameAnswer[i] == tri[i]:
            scount+=1
            flag+=1
        if flag == 2:
            bcount-=1
        flag = 0
    
    if(scount == 4):
        print("정답입니다.")
        break

    print("%d S %d B" %(scount, bcount))
    print("")
