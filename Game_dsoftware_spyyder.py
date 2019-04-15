# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:31:34 2019

@author: dorad
"""

'''
SCRIPT DA HISTORIA
    
Inicio: perguntar nome do jogador e da dupla
1. Cena1: Bixo entra no insper achando que vai ser fácil > Pós semanas de PI, tem 4 dias pra fazer
 o EP com a dupla
    Escolha: Biblioteca ou 4° Jogar Mario Kart
        Biblioteca: Encontra amigos da sala que querem ir jogar mario kart, vão para o 4°
        Mario Kart: Joga até tarde
2. Cena 2: Dia seguinte, aulas de NatDes e InstruMed
    Escolha: ir no Sujinhus pos aula ou ir fazer o EP
        Sujinhus: Veterano valentão aparece! 
            >> Combate! valor do dado
            import random p/ o valor dele
        Fazer o EP: Nao consegue entender muito bem o que e pra fazer
3.  

4. Cena 4: desespero bate, pergunta pra dupla se ele fez a parte dele e ele diz que não (fazer 
situaçãozinha da pergunta > conversa)
    Escolha: Ir atras do professor ou pedir ajuda pros amigos pra fazer o projeto
        Professor: encontrar ele, 3 tentativas: import random o local que ele vai estar do insper, se vc
        acertar, ele te da uma chance, se vc errar, vc perde
        Amigos: nenhum dos seus amigos sabem fazer
5. Cena 5: dia da entrega, vc nao conseguiu acabar o seu programa!
'''

hit_points = []
dinheiro = []
inventario = {}


titulo1 = "Cena1: Primeiro contato"
print (titulo1)
comprimento1 = len(titulo1)
print (comprimento1*"-")

print ()

historia1 = "A semana pós PI se iniciou com uma aula de Design de Software e o professor passando um trabalho denominado 'EP' pra ser feito em duplas, após o termino da aula seus amigos te chamam pra ir pro Sujinhus"
print(historia1)

escolha1= input("Você pode escolher: Ir ao Sujinhus ou ir fazer o Ep, o que você escolhe? ")
while escolha1 != "Sujinhus" or "Ep":
    denovo1 = input("Escolha inválida! Escolha entre 'Sujinhus' ou 'Ep'")
    break
#if denovo1 == "Sujinhus":