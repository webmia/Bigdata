def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result=result+i
    elif choice =="sub":
        result = args[0]
        for i in args[1:]:
            result=result-i
    elif choice == "mul":
        result =1
        for i in args:
            result = result*i
    elif choice == "div":
        result = args[0]
        for i in args[1:]:
            result = result/i
    return result

result4 = sum_mul('sum',1,2,3)
result1 = sum_mul('sub',1,2,3)
result2 = sum_mul('mul',1,2,3)
result3 = sum_mul('div',1,2,3)

print(result4)
print(result1)
print(result2)
print(result3)

