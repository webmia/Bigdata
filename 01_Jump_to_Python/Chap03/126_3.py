#coding: cp949

coffee_number = 10
while True:
    money = int(input("���� �־��ּ��� : "))
    if money == 300:
        print("Ŀ�Ǹ� �ݴϴ�.")
        coffee_number = coffee_number - 1
    elif money > 300:
        print("�Ž����� %d�� �ְ� Ŀ�Ǹ� �ݴϴ�." %(money-300))
        coffee_number = coffee_number - 1
    else:
        print("���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�.")
    
    print("���� Ŀ���� ���� %d �� �Դϴ�. \n" %coffee_number)
    
    if not coffee_number:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break
