def calculadora():
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite o número da operação desejada (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é {resultado}.")
    elif operacao == '2':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é {resultado}.")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é {resultado}.")
    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é {resultado}.")
        else:
            print("Erro: divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")

calculadora()
