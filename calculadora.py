# Função para adição
def add(x, y):
   return x + y

# Função para subtração
def subtract(x, y):
   return x - y

# Função para multiplicação
def multiply(x, y):
   return x * y

# Função para divisão
def divide(x, y):
   return x / y

print("Selecione o tipo de operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite a opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
   print(num1, "+", num2, "=", add(num1, num2))

elif escolha == '2':
   print(num1, "-", num2, "=", subtract(num1, num2))

elif escolha == '3':
   print(num1, "*", num2, "=", multiply(num1, num2))

elif escolha == '4':
   if num2 == 0:
       print("Não é possível dividir por zero.")
   else:
       print(num1, "/", num2, "=", divide(num1, num2))
else:
   print("Opção inválida")
