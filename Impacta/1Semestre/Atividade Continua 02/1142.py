N = int(input())
i = 1

if(0 <= N <= 10):
    while i <= 10:
        print("{} x {} = {}".format(N,i,N*i))
        i += 1
