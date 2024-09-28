def fibonat(a):
    if a == 1:
      return 1
    if a == 2:
       return 1
    else:
       return fibonat(a-1) + fibonat(a-2)
    
def mostratudo(a):
   for i in range (1, a+1):
     print(fibonat(i))  

print("Digite um numero e veja seu Fibonati : ")
a = int(input())

mostratudo(a)


   
  

