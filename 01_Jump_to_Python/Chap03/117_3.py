# coding cp949
money = 2000
money = int(input("얼마를 가지고 있습니까?"))
#card = 1 <- 카드 소지 여부만 판단하므로 정수형은 메모리 공간을 낭비함
card = True
card = input("카드를 소지하고 있습니까? (y/n) : ")

if card == 'y':     card = True
else:               card = False

if money >= 3000:
    print("택시를 타고가라")
else:
    if card == True:
        print("택시를 타고가라") # 동일한 코드일 경우 중복
        print("카드 지원 택시]택시를 타고가라") # 중복 코드 아닌 경우 허용
    print("걸어가라")
