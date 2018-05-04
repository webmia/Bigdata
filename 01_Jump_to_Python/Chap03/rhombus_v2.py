#coding: cp949
flag=0
while True:
    print("홀수를 입력하세요(0 <-종료): ",end="")
    num=int(input())
    if num%2==0:
        if num != 0:
            print("짝수를 입력하셨습니다. 재입력 부탁드립니다.")
        elif num==0:
            print("프로그램을 종료합니다.")
            flag=1
            break
        continue
    elif flag==1:
        break
    i=0
    j=int(num/2)
    while True:
        if i%2==1:
            print(" "*j,end="")
            print("*"*i)
            j -= 1
        i += 1
        while True:
            i=num
            if i%2==1:
                j=0
                print(j)
                print("*"*i)
                j +=1
            elif i == 0 :
                break
             i -= 1
       
    
        
