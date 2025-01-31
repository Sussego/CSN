def soma(a, b):
    return a + b

def subtracao(a, b):
        return a - b 

def multiplicacao(a, b):
    if b == 0 or a == 0:
        return 0
    if b > 0 and a > 0:
        return soma(a, multiplicacao(a, b - 1))
    if b < 0:
        return -multiplicacao(a, -b)
    if a < 0:
        return -multiplicacao(-a, b)

def divisao(a, b):
    if a < b:
        return 0
    return soma(1, divisao(subtracao(a, b), b))

def resto_divisao(a, b):
    if a < b:
        return a
    return resto_divisao(subtracao(a, b), b)

def exponencial(base, exp):
    if exp == 0:
        return 1
    return multiplicacao(base, exponencial(base, exp - 1))

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return multiplicacao(n, fatorial(n - 1))


# Testes
print("Soma: ", soma(5, 3)) 
print("Subtração: ", subtracao(10, 4)) 
print("Multiplicação: ", multiplicacao(-4, -3))
print("Divisão: ", divisao(7, 2))
print("Resto da divisão: ", resto_divisao(7, 2))
print("Exponencial: ", exponencial(4, 3))
print("Fatorial: ", fatorial(5))