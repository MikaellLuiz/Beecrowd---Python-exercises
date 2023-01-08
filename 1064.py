Vp = 0
soma = 0
for i in range(6):
    n = float(input())
    if(n > 0):
        Vp += 1
        soma += n
print(f"{Vp} valores positivos")
print(f"{soma/Vp:0.1f}")