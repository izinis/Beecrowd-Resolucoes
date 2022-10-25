diasemana = input()
diasentrega = int(input())

lista = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado','domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado','domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado','domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

num = lista.index(diasemana)

entrega = num + diasentrega

if diasentrega == 0:
    print("chega hoje!")

else:
    print("sera entregue",lista[entrega])


