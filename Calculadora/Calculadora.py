def soma(a, b):
    if b == 0:
        return a
    return soma(a + 1, b - 1)

def subtracao(a, b):
    if b == 0:
        return a
    return subtracao(a - 1, b - 1)



# Testes
print("Soma: ", soma(5, 3))  # 8
print("Subtração: ", subtracao(10, 4))  # 6
