# Faça uma função que recebe um objeto de coleção e retorna o valor do maior número dentro dessa coleção.
# Faça outra função que retorna o menor número dessa coleção

# Make a function that receive a collection object and return the value of the biggest number inside this collection
# Make another function that return the value of the smallest one


def maior_valor(obj):
    num_anterior = obj[0]
    for i in obj:
        if i > num_anterior:
            num_anterior = i
    return num_anterior


def menor_valor(obj):
    num_anterior = obj[0]
    for i in obj:
        if i < num_anterior:
            num_anterior = i
    return num_anterior


print(maior_valor([5, 234, 6, 32, 12]))
print(menor_valor([5, 234, 6, 32, 12]))
