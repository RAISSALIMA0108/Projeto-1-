import random
numero_secreto = random.randint(1,10)
while True:
    palpite=int(input("Qual seu palpite ? :"))
    if palpite==numero_secreto :
        print("Voce acertou !")
        break
    elif palpite<numero_secreto:
        print("Não deu certo tente de novo!")
    else:
        print("Muito grande esse numero errou feio!")

        #JOGO DE ADIVINHAÇÃO COM O COMPUTADOR ADIVINHE SE FOR CAPAZ DE ACERTAR 