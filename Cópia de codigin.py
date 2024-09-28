import queue
numiros = [52,3,4,87,55,63,71,9,4,1] # Lista com 10
numiros2 = [5,4,3,6,1] # Pilha com 5
fbanco = queue.Queue() # Cria a fila 
fbanco.put("Marcos")
fbanco.put("Uilian")   # Adicionando as "pessoas"
fbanco.put("Genival")
fbanco.put("Maria")
fbanco.put("Bernadete")

def menu():

    print("=" * 39,"\n Lista nº 1 = 10 elementos \n Lista nº2 = 5 numeros \n Fila Banco = 5 pessoas \n \n")
    print(" | Menu |  \n Escolha a função \n [1] Printe a lista nº 1 : \n [2] Printar os 3 primeiros e o 3 ultimos da lista nº 1 :")
    print(" [3] Printe o primeiro número da pilha: \n [4] Printe o ultimo número da pilha")
    print(" [6] Verificar se as listas estão vazias \n [7] Puxar todas pessoas da fila um a um \n [9] Fechar algoritimo :")
    escolha = int(input())

    if escolha == 1: # Printa a lista de 10 elementos
      print("=" * 39,"\n", numiros, "\n Aperte enter pra voltar ao menu : \n")
      volt = input("")
      return menu()
    
    elif escolha == 2: # Printa os 3 primeiros e 3 ultimos da lista de 10 elementos
       print("=" * 39)
       for x in range (0,3):
          print(numiros[x])
       for x in range (7,10):
          print(numiros[x])
       print("\n Aperte enter pra voltar ao menu : \n")
       volt = input("")
       return menu()
    
    elif escolha == 3: # Printa a pilha de 5 elementos
        print("=" * 39,"\n Não é possivel printar o primeiro elemento da pilha \n Aperte enter pra voltar ao menu : \n")
        volt = input("")
        return menu()

    elif escolha == 4:
       print("=" * 39,"\n", numiros2[4], "\n Aperte enter pra voltar ao menu : \n")
       volt = input("")
       return menu()
    
    elif escolha == 6:       # Verefica se as listas estão vazias e informa 
       print("=" * 39,"\n")

       if len(numiros) and len(numiros2) != 0:
          print("As listas não estão vazias")
       if len(numiros) and len(numiros2) == 0:
          print("As listas estão vazias")

    elif escolha == 7:       # Puxa a fila do banco um a um 
       print("=" * 39,"\n")

       for x in range(5):
          pessoa = fbanco.get()
          print(pessoa)

       print("\n Aperte enter pra voltar ao menu : \n")
       volt = input("")
       return menu()

    elif escolha == 9:
         exit

menu()