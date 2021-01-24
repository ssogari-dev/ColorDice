import random # RANDOM 함수 사용위한 모듈 로드.

price = int(input()) # 금액 입력
credits = price//500 # 작동할 횟수 지정
count = 0 # 현재 작동한 횟수 카운팅 
sum = 0 # 주사위 값 저장 (합산)

while count <= credits: # 작동한 횟수가 전체 작동횟수이 될 때 까지
    dice = random.randint(1,6) # 주사위 색상 지정
    num = random.randint(1,6) # 주사위 값 지정

    if dice == 1 : # RED (빨간색)
        print("RED")
        count += 1 # 작동한 횟수 1 증가
        break # 반복문 탈출 후 종료.

    elif dice == 2 : # BLUE (파란색)
        print("BLUE")
        count += 1

    elif dice == 3 : # PURPLE (보라색)
        print("PURPLE")
        print(num) # 주사위 값 출력
        sum += num # 주사위 값 저장 (합산)
        credits += 1 # 작동할 횟수 1 증가.
        count += 1 # 작동한 횟수 1 증가.

    elif dice == 4 : # ORANGE (주황색)
        print("ORANGE")
        print(num)
        sum += num
        credits += 1
        count += 1

    elif dice == 5 : # GREEN (초록색)
        print("GREEN")
        print(num)
        sum += num
        credits += 1
        count += 1

    elif dice == 6 : # PINK (분홍색)
        print("PINK")
        print(num)
        sum += num
        credits += 1
        count += 1

print(int(sum/count)) # 정수 값(소숫점 X)으로 평균 값 출력 → 주사위 값 합산 ÷ 작동한 횟수



## 사용자가 금액 입력 (input)
##
## < 반복문 1회 작동마다 >
##   RANDOM 통해 주사위 색상(dice) 지정 [ 각 색상에 숫자 배정 ]
##   RANDOM 통해 주사위 값(num) 지정
##     < dice 값에 따라 >
##        1 RED : 작동한 횟수(count) 증가 후 break으로 반복문 탈출 (종료)
##        2 BLUE : count만 증가
##        3~6 : 작동할 횟수(credits) 증가, count 증가, 주사위 값(num)을 합산하여 저장(sum)
## 
## 반복문 종료 후, sum을 count로 나누어 평균값 출력 (단, int로 소숫점 빼고 정수값으로 출력)