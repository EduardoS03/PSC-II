numiros = [1,1]
tamanhu = len(numiros)    

print("Digite um numero e veja seu Fibonati : ")
a = int(input())

while (a > tamanhu):
    numiros.append(numiros[-1] + numiros[-2])
    tamanhu = len(numiros)
    print("O", tamanhu, "º numiro de fibonati é : ", numiros[-1])

print("E a lista completa ficou assim :", numiros)
