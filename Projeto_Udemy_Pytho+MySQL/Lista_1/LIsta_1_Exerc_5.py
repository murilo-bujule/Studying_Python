import _operador_valido as opv

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro número: "))

operador = opv.operador_valido()

if operador == "+" :
    print(f"{num1} + {num2} = {num1 + num2}")
elif operador == "-" :
    print(f"{num1} - {num2} = {num1 - num2}")
elif operador == "*" :
    print(f"{num1} * {num2} = {num1 * num2}")
elif operador == "/" :
    print(f"{num1} / {num2} = {num1 / num2}")

