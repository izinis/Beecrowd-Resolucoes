preco = float(input())
qtd = int(input())
compra=(preco*qtd)
compradesc = compra-(compra*0.10)
progressivo = (compra*qtd)*0.01
print("{:.2F}".format(compra))
print("{:.2f}".format(compradesc-progressivo))
