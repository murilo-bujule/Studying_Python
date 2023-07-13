def operador_valido():
    while True:
        operador = input("Digite uma operador: (+, -, *, /) ")
        if operador != "+" or operador != "-" or operador != "*" or operador != "/" :
            break
    return operador