divida = int(input())
pagar = int(input())
i = 1

while divida != 0:   
    if pagar > divida:
        pagar = divida    
    print("pagamento:",i)
    print("antes =",divida)
    divida -= pagar
    print("depois =",divida)
    print("-----")
    i += 1

     