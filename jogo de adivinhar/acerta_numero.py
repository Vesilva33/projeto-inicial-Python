import random
print("seja bem vindo ao jogo de adivinhações!")
n1_number = input("digite o numero teto do Desafio:")

if n1_number.isdigit():
     n1_number = int( n1_number)
else:
    print("ERRO o valor não e numero ! favor execute novamente e informe um numero!")     
    quit()
    
random_number = random.randint (0,n1_number)
n1_choices = 0

while True:
    coloca_number = input("Adivinha o Número: ")
    
    if coloca_number.isdigit(): 
      coloca_number = int (coloca_number)
        
    else:
       print("ERRO o valor não e numero ! favor execute novamente e informe um numero!") 
       continue
   
    n1_choices = n1_choices  + 1
      
    if coloca_number == random_number:
        print("Acertou")   
        break
    elif coloca_number > random_number:
        print("Chutou alto,o numero randonico é menor que isso ....")
    else:
        print("Chutou baixo,o numero randonico é maior que isso ....")   
        
print("n° de tentativas: "+str(n1_choices))         
        