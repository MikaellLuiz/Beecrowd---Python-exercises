vp = 0
vi = 0
vpo = 0
vne = 0
for i in range(5):
    n = float(input())
    if(n % 2 == 0):
        vp += 1
    else:
        vi += 1
    if(n < 0):
        vne += 1
    elif(n > 0):
        vpo += 1
print(f"{vp} valor(es) par(es)")
print(f"{vi} valor(es) impar(es)")
print(f"{vpo} valor(es) positivo(s)")
print(f"{vne} valor(es) negativo(s)")