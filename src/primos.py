# programa python com os numeros primos

VLimite = int(input("Digite o número limite: "))
VPrimos = []
VComposto = []
VLimite = VLimite + 1
for i in range(VLimite):
    if (i + 1) == 1:
        VComposto = VComposto + [i + 1]
    if (i + 1) not in VComposto:
        if (i + 1) != VLimite:
            VPrimos = VPrimos + [i + 1]
        if (i + 1) ** 2 > VLimite:
            i = VLimite
        else:
            for j in range(i + 1, VLimite, i + 1):
                VComposto = VComposto + [j]
print(VPrimos)

