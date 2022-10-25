notatb = float(input())
notapr = float(input())


media = (notatb + notapr) / 2


if media >= 6:
    print("aprovado")

if media < 6:
    for x in range(6,11):
        notasub = (notatb + x) / 2 
        if (notasub >= 6):
            print("talvez com a sub")
            break
    else:
        print("reprovado")
    





