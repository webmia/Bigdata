# coding: cp949
card = input("ī�带 �����ϰ� �ֽ��ϱ�? (y/n) : ")
partnership = input("��Ű��ó �ý� �����Դϱ�? (y/n) : ")

if card == 'y':     card = True
else:               card = False

if partnership == 'y':     partnership = True
else:               partnership = False

#if card == True:
#    if partnership == True: <-11�� ������ �����ϰ� ó���ǹǷ� ��ø�� if�� ����� �ʿ䰡 ����
#        print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")
if card == True and partnership == True:
#if card and partnership ==True: <- ���� ���� ���� ������ �����ؾ���
else:
    print("�ɾ�ž� �մϴ�.")
