insert = input().split(' ')
cod1 = int(insert[0])
quant1 = int(insert[1])
valorUn1 = float(insert[2])

insert = input().split(' ')
cod2 = int(insert[0])
quant2 = int(insert[1])
valorUn2 = float(insert[2])

total = valorUn1 * quant1 + valorUn2 * quant2

print(f"VALOR A PAGAR: R$ {total:.2f}")