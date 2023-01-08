n = int(input())
i = 0
u = 0
x = 0
while(n > 0):
    x = int(input())
    if(x >= 10 and x <= 20):
        i += 1
    else:
        u += 1
    n -= 1
print(f"{i} in\n{u} out")