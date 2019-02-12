# Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
# Após isso o programa irá perguntar o nome de todas as pessoas e montar uma lista de convidados e mostrar essa lista.

# Build a program to receive a number of peoples to be invited to a party.
# After that the program will ask the name for each person invited, build a list and then show this list.

quantidade = int(input('Digite o número de convidados: '))
convidados = []
i = 0

for i in range(quantidade):
    nome = input('Qual o nome do ' + str(i+1) + 'º convidado?  ')
    convidados.append(nome)
    i += 1

for convidado in convidados:
    print(convidado)

print('Same form, but in english')
quantity = int(input('How many invites: '))
invites = []
i = 0

for i in range(quantity):
    name = input('What is the name of the ' + str(i+1) + 'º invited?  ')
    invites.append(name)
    i += 1

for invite in invites:
    print(invite)