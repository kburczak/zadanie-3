eur = 100
usd = 100
eur_to_usd = [1.0903, 1.0920, 1.0914, 1.0869, 1.0916, 1.0997, 1.1051, 1.0985, 1.0925]
trend = 0

for i in range(1, len(eur_to_usd)):
    if eur_to_usd[i] > eur_to_usd[i-1]:
        if trend < 0:
            trend = 0
        trend = trend + 1
    elif eur_to_usd[i] < eur_to_usd[i-1]:
        if trend > 0:
            trend = 0
        trend = trend - 1

    if trend > 0:
        eur = eur + usd / eur_to_usd[i]
        usd = 0
    elif trend < 0:
        usd = usd + eur * eur_to_usd[i]
        eur = 0

print("całość na początku w dolarach", 100 + 100 * eur_to_usd[0])
print("całość na początku w euro", 100 + 100 / eur_to_usd[0])

print(f'euro: {eur}')
print(f'dolary: {usd}')
