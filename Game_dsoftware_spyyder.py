# -*- coding: utf-8 -*-

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
