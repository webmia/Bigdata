# coding: cp949
A = True
B = False

if A==False and B==False:
    print("A==False and B==False 조건이어야 수행되는 조건문")

if A and B == False:
    print("A==False and B==False 조건이어야 수행하는 의도라면 현재  A는 True 인데도 print가 되기때문에 조건식이 잘못 작성되었음")
