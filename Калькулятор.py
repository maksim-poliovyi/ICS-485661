f_num = float(input("Введіть число>>"))
oper = input("Введіть операцію>>")
s_num = float(input("Введіть друге число>>"))
if oper == '+':
    print(f_num +s_num)
elif oper == '-':
    print(f_num -s_num)
elif oper == '*':
    print(f_num *s_num)
elif oper == '/':
    print(f_num /s_num)
else:
    print("Error")
print("Enter, щоб вийти")
input()


