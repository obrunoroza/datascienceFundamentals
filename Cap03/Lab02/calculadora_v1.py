# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

from time import sleep


def valida_operacao() -> int:
    while True:
        try:
            operacao: int = int(input("Escolha a operação:  "))
            if operacao >= 1 and operacao <= 5:
                return operacao
            else:
                print("Operação invalida!")
                sleep(1)                
        except ValueError:
            print("Operação invalida!")
            sleep(1)
        continue


def valida_number() -> float:
    while True:
        try:
            number: float = float(input(f"Digite um numero: "))
            return number
        except ValueError:
            print("Numero invalido!")
            sleep(1)
        continue


def realiza_operacao(n1: float, n2: float, op: int) -> str:
    if op == 1:
        print(f"Resultado: {n1:.2f} + {n2:.2f} = {n1 + n2:.2f}")
    elif op == 2:
        print(f"Resultado: {n1:.2f} - {n2:.2f} = {n1 - n2:.2f}")
    elif op == 3:
        print(f"Resultado: {n1:.2f} x {n2:.2f} = {n1 * n2:.2f}")
    elif op == 4:
        if n2 <= 0:
            print("Não pode haver divisão por zero!")        
        else:
            print(f"Resultado: {n1:.2f} / {n2:.2f} = {n1 / n2:.2f}")
    else:
        print("Saindo....")
        sleep(2)
        exit(0)


def main() -> None:
    print("\n******************* Python Calculator *******************")
    print("Selecione a operação desejada: \n")
    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    print("[5] - Sair\n")

    operacao: int = valida_operacao()
    number1: float = valida_number()
    number2: float = valida_number()
    realiza_operacao(number1, number2, operacao)
    

if __name__ == '__main__':
    main()

