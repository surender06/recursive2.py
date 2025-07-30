def recursive(n):
    if n==0:
        return 0
    else:
       return n + recursive(n-1)
n=6
r=recursive(n)
print(r)