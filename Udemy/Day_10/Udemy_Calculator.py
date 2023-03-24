from Calculator_art import logo
import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def cal(oper, f_num, n_num):
    """사칙연산 계산기"""
    if (oper == "+"):
        print(f"{f_num} + {n_num} = {f_num + n_num}")
        return f_num + n_num
    if (oper == "-"):
        print(f"{f_num} - {n_num} = {f_num - n_num}")
        return f_num - n_num
    if (oper == "*"):
        print(f"{f_num} * {n_num} = {f_num * n_num}")
        return f_num * n_num
    if (oper == "/"):
        print(f"{f_num} / {n_num} = {f_num / n_num}")
        return f_num / n_num


print(logo)
# opers = {
#     "+" : add,
#     "-" : sub,
#     "*" : mul,
#     "/" : div
# }
# 함수를 따로 4개 짜면 이렇게 딕셔너리로 함수를 지정하는 짓도 가능함
# func = opers["+"] 하면 func이 add 함수가 되는 식.

# while 도 있지만 이렇게 재귀하는것도 가능


def calculator():

    repeat = "y"
    f_num = float(input("What is the first number?: "))

    while (repeat == "y"):
        print("+\n-\n*\n/")
        oper = input("Pick an operation: ")
        n_num = float(input("What's the next number?: "))
        f_num = cal(oper, f_num, n_num)

        repeat = input(
            f"Type 'y' to continue calculating with {f_num}, or type 'n' to start a new calculation: ")

    clearConsole()
    calculator()


calculator()
