price = int(input()) # 금액 입력
credits = price//500 # 작동할 횟수 지정
count = 0 # 현재 작동한 횟수 카운팅 
sum = 0 # 주사위 값 저장 (합산)

while count <= credits: # 작동한 횟수가 전체 작동횟수이 될 때 까지
    dice = input()
    if dice == "RED" :
        break # 반복문 탈출 후 종료.

    elif dice == "BLUE" : 
        count += 1

    elif dice == "PURPLE" :
        num = int(input())
        sum += num # 주사위 값 저장 (합산)
        credits += 1 # 작동할 횟수 1 증가.
        count += 1 # 작동한 횟수 1 증가.

    elif dice == "ORANGE" or dice == "GREEN" or dice == "PINK" :
        num = int(input())
        sum += num 
        credits += 1 
        count += 1 

    else : # 예외 처리 (색상이 올바르게 입력되지 않은 경우)
        print("입력 값이 올바르지 않습니다 [RED, BLUE, PURPLE, ORANGE, GREEN, PINK")

print(int(sum/count)) # 정수 값(소숫점 X)으로 평균 값 출력 → 주사위 값 합산 ÷ 작동한 횟수

# 참고. 주사위 값 예외 처리가 되지 않음 (1~6 외의 값이 입력된 경우 오류 발생해야 함)