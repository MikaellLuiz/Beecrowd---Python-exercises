i = int(input())

print(f"{i // 365} ano(s)")
i %= 365
print(f"{i // 30} mes(es)")
i %= 30
print(f"{i} dia(s)")
