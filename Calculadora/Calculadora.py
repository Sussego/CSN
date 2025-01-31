def soma(a, b):
    if b == 0:
        return a
    return soma(a + 1, b - 1)

def subtracao(a, b):
    if b == 0:
        return a
    return subtracao(a - 1, b - 1)

def multiplicacao(a, b):
    if b == 0:
        return 0
    if b > 0:
        return soma(a, multiplicacao(a, b - 1))
    return -multiplicacao(a, -b)



# Testes
print("Soma: ", soma(5, 3)) 
print("Subtração: ", subtracao(10, 4)) 
print("Multiplicação: ", multiplicacao(2, 4))