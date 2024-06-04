import math

def calcular_area_quadrado():
    lado = float(input("Digite o valor do lado do quadrado: "))
    area = lado ** 2
    print(f"A área do quadrado é: {area}")

def calcular_area_retangulo():
    base = float(input("Digite o valor da base do retângulo: "))
    altura = float(input("Digite o valor da altura do retângulo: "))
    area = base * altura
    print(f"A área do retângulo é: {area}")

def calcular_area_losango():
    diagonal_maior = float(input("Digite o valor da diagonal maior do losango: "))
    diagonal_menor = float(input("Digite o valor da diagonal menor do losango: "))
    area = (diagonal_maior * diagonal_menor) / 2
    print(f"A área do losango é: {area}")

def calcular_area_trapezio():
    base_maior = float(input("Digite o valor da base maior do trapézio: "))
    base_menor = float(input("Digite o valor da base menor do trapézio: "))
    altura = float(input("Digite o valor da altura do trapézio: "))
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area}")

def calcular_area_triangulo():
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")

def calcular_area_circulo():
    raio = float(input("Digite o valor do raio do círculo: "))
    area = math.pi * raio ** 2
    print(f"A área do círculo é: {area:.2f}")

def menu():
    print("\nEscolha a figura geométrica para calcular a área:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Losango")
    print("4 - Trapézio")
    print("5 - Triângulo")
    print("6 - Círculo")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        calcular_area_quadrado()
    elif opcao == '2':
        calcular_area_retangulo()
    elif opcao == '3':
        calcular_area_losango()
    elif opcao == '4':
        calcular_area_trapezio()
    elif opcao == '5':
        calcular_area_triangulo()
    elif opcao == '6':
        calcular_area_circulo()
    elif opcao == '0':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
