N = int(input())
N -= 1
i = 0
x = 0
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

if (0 <= N <= 25):
    while i <= N:
        x = 0
        while x <= i:
            print(alfabeto[i],end="")
            x += 1
        print(end="\n")
        i += 1
