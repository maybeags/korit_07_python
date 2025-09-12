from turtle import Turtle, Screen
from random import Random
# turtle 모듈에서 Turtle, Screen 클래스를 import해왔습니다.

t = Turtle()        # 터틀 객체를 생성했고, 객체명 t
screen = Screen()   # 스크린 객체 생성
# 이상의 경우만 작성했을 때 모니터가 깜빡이는 것을 확인할 수 있는데, 이는 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼지는 것입니다.

t.shape('turtle')           # Turtle의 메서드를 호출했는데 argument가 str
t.color('white')
screen.bgcolor('black')

# 랜덤 객체 생성
random = Random()           # hangman할 때 썼었습니다.
colors = [
    'dark red',
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
    'light yellow'
]

# t.forward(100.3)
# t.penup()
# t.forward(100.3)
# t.forward(100.3)
# t.pendown()
# t.forward(30)

# 점선 그리는 반복문
# for _ in range(10):
#     t.forward(15)
#     t.penup()
#     t.forward(15)
#     t.pendown()

# .left(각도)
# t.left(90)

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)
#
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
#
# for _ in range(6):
#     t.forward(100)
#     t.left(60)

# 그럼 오각형 / 육각형도 그려보세요.


# 이상을 일반화 시키기 위해서 알 수 있는 것은
'''
삼각형일 때 120
사각형일 때 90
오각형일 때 72
육각형일 때 60

십각형일 때 36
'''
# n = int(input('몇각형을 만드시겠습니까? >>> '))
# 얘는 도형 하나를 그리기 위한 반복문
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)

# 여러 개의 도형을 그리고 싶다면 도형을 그리는 반복문을 반복 -> 중첩 for

for i in range(3, 11):
    for _ in range(i):
        t.forward(100)
        t.left(360/i)




screen.exitonclick()