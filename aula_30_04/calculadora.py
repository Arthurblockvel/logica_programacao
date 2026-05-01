print("--------------------------")
print("     calculadora     ")
print("--------------------------")
print()
print("essa calculadora faz todas as perações")
print(" a partir de dois números que você informar")
print()

print(" digite o valor correspondente ao cálculo")
print("que vocé quer fazer")
print()
print("1 - as 4 operações")
print("2 - media de 3 valores")
print("3 - fómula de bháskara")
print()
opcao = int(input("digite a opção:"))

match opcao:
    case 1:
        first_num = float(input("digite o primeiro numero :"))
        scond_num = float(input("digite o segundo número:"))

        adicao = first_num + scond_num
        print("a adição resulta em:",adicao)

        subtracao = first_num - scond_num
        print("a subtração resulta em:",subtracao)

        multi = first_num * scond_num
        print("a multiplicação resulta em:",multi)

        if scond_num != 0:
            divisao = first_num / scond_num
            print("a divisão resulta em:",divisao)
        else:
            print()

    case 2:
        print("media de 3 valores")
        first_num = float(input("digite o primeiro numero:"))
        second_num = float(input("digite o segundo numero:"))
        third_num = float(input("digite o terceiro numero"))
        media = first_num + second_num + third_num / 3
        print("a média resulta em:", media)
        
    case 3:
        print("fórmula de bháskara")
