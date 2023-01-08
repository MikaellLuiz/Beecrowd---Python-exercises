n = int(input())

print(f"{n // 3600}:", end="")
n %= 3600
print(f"{n // 60}:", end="")
n %= 60
print(f"{n}")