#coding: cp949

coffee_number = 10

print("<Sw ��Ű��ó ���Ǳ� Ver 1.0>")

menu ="""
<menu>
1. Ŀ�� ����
2. Ŀ�� �ܷ� Ȯ��
3. ���α׷� ����
�޴��� �����ϼ��� : """
while True:
    print(menu,end='')
    choice = int(input())

    if choice == 1:
        while True:
            money = int(input("�ݾ��� �Է��ϼ��� : "))
            if money == 300:
                print("Ŀ�Ǹ� �ݴϴ�.\n")
                coffee_number = coffee_number - 1
            elif money > 300:
                print("Ŀ�Ǹ� �ݴϴ�. ���� �Ž����� %d�Դϴ�.\n" %(money-300))
                coffee_number = coffee_number - 1
            else:
                print("�ݾ��� %d ���ڶ��ϴ�.\n" %(300-money))
            if not coffee_number:
                print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.\n")
                break

    elif choice == 2:
        print("���� Ŀ���� ���� %d �� �Դϴ�. \n" %coffee_number)
    
    elif choice == 3:
        print("���α׷��� �����մϴ�.")
        break
   
