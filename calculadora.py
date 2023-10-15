# Definindo as funções para as operações matemáticas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

# Função principal da calculadora
def calculadora():
    operacoes = {
        '+': soma,
        '-': subtracao,
        '*': multiplicacao,
        '/': divisao
    }

    while True:
        print("Selecione a operação:")
        print("+ para adição")
        print("- para subtração")
        print("* para multiplicação")
        print("/ para divisão")
        print("Pressione qualquer outra tecla para sair")

        operacao = input("Digite a operação desejada: ")

        if operacao not in operacoes:
            print("Saindo...")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            resultado = operacoes[operacao](num1, num2)
            print(f"O resultado é: {resultado}")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")

# Chamando a função principal
calculadora()
