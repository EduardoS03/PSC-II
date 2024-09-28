def fibonat(a):
    if a == 1:
      return 1
    if a == 2:
       return 1
    else:
       return fibonat(a-1) + fibonat(a-2)

print("Digite um numero e veja seu Fibonati : ")
a = int(input())

fibonat(a)

print("O resultado do número fatorado é igual a : ", fibonat(a))