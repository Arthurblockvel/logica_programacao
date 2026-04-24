# Nesse Código analisaremos a idade do usuário e falaremos[]
# se é maior de idade ou não
nome = input("digite o seu nome")
idade =int (input("digite a sua idade"))
# A estrutura de decisão analisa uma comparação e excuta o código 
#com base na resposta. para utilizarmos a estrutura de decisão, precisamos
# de comparadores, que são :

# - > maior
# - < menor
# - == igual
# - != diferente
# - >= maior ou igual 
# - <= menor ou igual 
# - ! não
if idade >= 18 :
    print (" você é maior de idade!")
    if idade >=60:
        print ("você é idoso!")
        print (" Já pode pegar a carteirinha de estacionamento")
else:
    print (" você é menor de idade ")
    print ("não pode comprar cigarro no reino unido")
