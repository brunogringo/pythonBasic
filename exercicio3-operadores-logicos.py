# Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decida se ela está apta a ser do exercito.
# Para entrar no execito é preciso ter mais de 18 anos, pesar pelo menos 60 quilos
# e ter medir mais ou igual a 1,70 metros

# Make a program that asks for the age, weight and height from a one person,
# then decide if this person can join the army.
# To join the army must be 18 years old, weight at least 60 kilos and be 1,70 meters height

idade = int(input('Qual a idade?  '))
peso = float(input('Qual o peso?  '))
altura = float(input('Qual é a altura?  '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
   print('Esta pessoa está apta a entrar no exercicito')
elif idade < 18:
   print('A idade mínima é 18 anos')
elif peso < 60:
   print('O peso mínimo é 60 kilos')
else:
   print('A altura minima é 1.70 metros')

print('Same form, but in english')
age = int(input('How old are the person?  '))
weight = float(input('How much the person weight?  '))
height = float(input('How height is this person?  '))

if idade >= 18 or peso >= 60 or altura >= 1.70:
   print('This person can join the army')
elif idade < 18:
   print('The minimum age is 18 years')
elif peso < 60:
   print('The minimum weight is 60 kilos')
else:
   print('The minimum height is 1.70 meters')