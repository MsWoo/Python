#turtle, random을 사용하기 위해 import합니다.
#turtle은 t라는 이름으로 사용합니다.
import turtle as t
import random

#현재 r,g,b 값으로 pencolor를 설정하고
#입력받은 좌표로 선을 그으며 이동합니다.
def LeftClick(x, y) :
    global  r, g, b
    t.pencolor((r, g, b))
    t.pendown()
    t.goto(x, y)

#penup()을 사용해서 입력받은 좌표로 선을 긋지 않고 이동합니다.
def RightClick(x, y) :
     t.penup()
     t.goto(x, y)

#전역변수인 r,g,b에 random으로 발생시킨 난수를 저장합니다
def MidClick(x, y) :
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    
#turtle의 Size를 키우는 함수
#최대값은 9입니다.
def SizeUp():
    global tSize;
    if tSize < 10:
        tSize+=1
    t.shapesize(tSize)
    
#turtle의 Size를 줄이는 함수
#최소값은 1입니다.
def SizeDown():
    global tSize;
    if tSize > 1:
        tSize-=1
    t.shapesize(tSize)
    
#turtle의 Shape를 변경합니다(시계방향)
#shape 목록은 총 6개입니다. 
#끝에 도달했을 시에 처음으로 돌아갑니다.
def changeUp():
    global index, shapes
    if index == 5 :
        index = 0
    else :
        index += 1   
    t.shape(shapes[index])

#turtle의 Shape를 변경합니다(반시계방향)
#shape 목록은 총 6개입니다. 
#끝에 도달했을 시에 처음으로 돌아갑니다.    
def changeDown():
    global index, shapes
    if index == 0 :
        index = 5
    else :
        index -= 1   
    t.shape(shapes[index])
    
#turtle이 실행한 최근작업을 이전으로 되돌립니다.
def undo():
    t.undo()
    
#turtle 프로그램을 종료합니다.
def close():
    screen.bye()


#turtle의 초기값은 1, penSize는 10으로 고정입니다.
tSize = 1
pSize = 10

#turtle의 shape를 변경하기 위해 사용할 인덱스변수와
#turtle이 제공하는 shape, index {key:value}쌍으로 이루어진 dictionary
index = 0
shapes = { 0:"arrow", 1:"turtle", 2:"circle",
          3:"square", 4:"triangle", 5:"classic" }

#선의 색을 변경할 때 사용할 r,g,b변수에 대한 초기화
r, g, b = 0.0, 0.0, 0.0


#turtle 실행창의 이름을 지정합니다.
t.title('Turtle GrimPan')

#TurtleScreen의 메소드를 사용하기 위해
#screen이라는 변수에 TurtleScreen객체를 저장합니다.
screen = t.getscreen()

#turtle shape의 초기값은 arrow입니다.
t.shape('arrow')

#turtle의 pensize를 pSize에 들어있는 값으로 설정합니다.
t.pensize(pSize)

#turtle screen의 마우스 좌클릭, 우클릭, 휠클릭시 실행 될 함수들과 클릭 된 버튼의 정보입니다.
# 1 : 마우스 좌클릭, 2 : 마우스 휠 클릭,  3 : 마우스 우클릭
t.onscreenclick(LeftClick, 1)
t.onscreenclick(RightClick, 3)
t.onscreenclick(MidClick, 2)

#turtle screen에 입력되는 키값에 대해 실행 될 함수들입니다.
screen.onkeypress(SizeUp, "Up")
screen.onkeypress(SizeDown, "Down")
screen.onkeypress(changeUp, "Right")
screen.onkeypress(changeDown, "Left")
screen.onkeypress(undo, "z")
screen.onkeypress(close, "q")
screen.listen()


t.done()