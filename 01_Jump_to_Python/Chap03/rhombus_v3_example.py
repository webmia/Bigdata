#coding: cp949
output_msg="Ȧ���� �Է��ϼ���(0 <- ����) : "
blank=" "
star="*"
hyphen="-"
vertical_bar="|"
print("������ ��� ���α׷� ver2.0\n")

while True:
    print(output_msg,end='')
    customer_input = int(input())

    if customer_input == 0:
        print("���α׷��� �����մϴ�.")
        break
    elif customer_input % 2 == 0:    
        print("¦���� �Է��ϼ̽��ϴ�. ���Է� ��Ź�帳�ϴ�.")
        continue

    star_count=1
    blank_count=(customer_input-star_count)//2
    
    print(blank,end='')
    print(hyphen*customer_input,end='')
    print(blank)

    while True:
        print(vertical_bar+(blank*blank_count)+(star*star_count)+(blank*blank_count)+vertical_bar)
        if star_count == customer_input:
            break
        blank_count -= 1
        star_count += 2
    while True: 
        if star_count == 1:
            break
        star_count -= 2
        blank_count += 1
        print(vertical_bar+(blank*blank_count)+(star*star_count)+(blank*blank_count)+vertical_bar)
    print(blank,end='')
    print(hyphen*customer_input,end='')
    print(blank)
