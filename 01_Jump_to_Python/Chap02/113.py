# coding cp949
#money = 1
#money = 7
money = 0

if money:
    print("택시를 타고가라")
#   print("도착했습니다.") <- indentation이 맞지 않아 에러
#   print("도착했습니다.")
else:
    print("걸어가라")
#   print("도착했습니다.") <- indentation이 맞지 않아 에러
#   print("도착했습니다.")<- 동일한 코드가 중복됨 / 프로그램 수정시 동일코드 로직변경이 누락 될 가능성이 있음
print("목적지에 도착햇습니다.") # <-중복코드제거
print("프로그램 종료합니다.")
