#coding: cp949
flag=0
while True:
    print("Ȧ���� �Է��ϼ���(0 <-����): ",end="")
    num=int(input())
    if num%2==0:
        if num != 0:
            print("¦���� �Է��ϼ̽��ϴ�. ���Է� ��Ź�帳�ϴ�.")
        elif num==0:
            print("���α׷��� �����մϴ�.")
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
       
    
        
