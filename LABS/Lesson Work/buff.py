damage = float(input("Damage: "))
buff = float(input("Buff: "))
new_damage = round(damage + buff, ndigits=2)
print(f"{new_damage:.2f}")
