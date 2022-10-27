num = int(input())
num = num
cont = num
maior = num 
menor = num 

if num >= 2:
    while (maior == num):
        cont += 1
        if(cont % 2 == 0):
            maior = cont
        
        
        

    cont = num
    while (menor == num):
        cont -= 1
        if(cont % 2 != 0):
            menor = cont
        

print(menor,maior)


