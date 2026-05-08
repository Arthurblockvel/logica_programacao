import time
import random

print("#### jogo da adivinhação ####")
print()
print("estou pensando em um numero. . . ")

time.sleep(2)

numero = random.randint(0,10)

print("pensei!")
print("voce podera tentar adivinhar ele")
print()

#for i in range(1,4):
#    print(f"essa e a sua {i} tentativa!")
#    tentativa = int(input("digite um valor entre 0 e 10"))
#
#    if tentativa == numero:
#    else:
#        print("voce errou")
acertou = False
num_tentativa = 0
while acertou == False:
    num_tentativa += 1 # mesma coisa que num_tentativa = num_tentativa + 1
    print(f"essa e a {num_tentativa} tentativa")
    tentativa = int(input("digite um valor entre 0 e 10"))

    if tentativa == numero:
        print ("paraben, voce acertou")
        acertou = True
    else:
        print("voce errou") 
        if num_tentativa == 10: 
         print("voce e burro")