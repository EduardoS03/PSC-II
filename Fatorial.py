def fatorial(a):
    if a == 0:
      return 1
    else:
       return a * fatorial(a-1)

print("Digite um numero e veja seu fatorial : ")
a = int(input())

fatorial(a)

print("O resultado do número fatorado é igual a : ", fatorial(a))