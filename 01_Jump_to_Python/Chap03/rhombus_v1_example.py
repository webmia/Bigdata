#coding: cp949
output_msg="홀수를 입력하세요(0 <- 종료) : "
blank=" "
star="*"
print("마름모 출력 프로그램 ver1.0\n")

while True:
    print(output_msg,end='')
    customer_input = int(input())

    if customer_input == 0:
        print("프로그램을 종료합니다.")
        break
    elif customer_input % 2 == 0:    
        print("짝수를 입력하셨습니다. 재입력 부탁드립니다.")
        continue

    star_count=1
    blank_count=(customer_input-star_count)//2

    while True:
        print((blank*blank_count)+(star*star_count))
        if star_count == customer_input:
            break
        blank_count -= 1
        star_count += 2
