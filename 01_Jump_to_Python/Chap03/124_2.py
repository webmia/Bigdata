#coding: cp949

prompt = """
1.Add
2.Del
3.List
4.Quit

Enter number:"""

number = 0
while number != 4:
    print(prompt,end='') #<-end=''마지막 줄바꿈 없애는 기능
    number = int(input())
