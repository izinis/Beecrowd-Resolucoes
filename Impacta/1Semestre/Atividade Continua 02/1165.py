vcoin = 0
compra = 0.00

while(compra != -1.0):
    vcoin += compra
    compra = float(input())

print("VC$ {:.2f}".format(vcoin))
print("R$ {:.2f}".format(vcoin*2.50))


