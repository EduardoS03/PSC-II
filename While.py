def fibonat(a):
    if a == 1:
      return 1
    if a == 2:
       return 1
    else:
       return fibonat(a-1) + fibonat(a-2)
    
def mostratudo(a):
   i = int(1) 
   while (i <= a):
     print(fibonat(i)) 
     i += 1

print("Digite um numero e veja seu Fibonati : ")
a = int(input())

mostratudo(a)
