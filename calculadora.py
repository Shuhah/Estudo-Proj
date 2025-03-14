def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divisão(x, y):
    if y == 0:
        return "Bugo tudo"
    return x / y

def calc():
    while True:
        print("operação: \n1. Soma\n2. Subtração\n3. multiplicação\n4. Divisão\n5. Sair")

        op = input("Qual o código da operação?")

        if op == '5':
            break
        
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo Número: "))

        if op == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif op == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif op == '3':
            print(f"{num1} - {num2} = {multi(num1, num2)}")
        elif op == '4':
            print(f"{num1} / {num2} = {divisão(num1, num2)}")
        elif op == '5':
            break
            
        else:
            print("inválido!")

calc()