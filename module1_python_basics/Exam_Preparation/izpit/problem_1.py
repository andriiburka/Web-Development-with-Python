# Задача 1. Великденска пекарна


# •	цената на килограм захар е с 25% по-ниска от тази на килограм брашно
# •	цената на една кора с яйца е с 10% по-висока от цената на килограм брашно
# •	цената на един пакет мая е с 80% по-ниска от цената на килограм захар

# Изход
# Да се отпечата на конзолата едно число:
# •	Сумата, която ще им е необходима, форматирана до втория знак след десетичната запетая

cena_brashno_za_kg = float(input())
kolichestvo_kg_brashno = float(input())
kolichestvo_kg_zahar = float(input())
broi_kori_qica = int(input())
paketi_maq = int(input())

cena_kg_zahar = 0
cena_kora_qica = 0
cena_paket_maq = 0

cena_kg_zahar = cena_brashno_za_kg - (cena_brashno_za_kg * 0.25)

cena_kora_qica = cena_brashno_za_kg + (cena_brashno_za_kg * 0.1)

cena_paket_maq = cena_kg_zahar - (cena_kg_zahar * 0.80)

suma_brashno = cena_brashno_za_kg * kolichestvo_kg_brashno
suma_zahar = cena_kg_zahar * kolichestvo_kg_zahar
suma_qica = cena_kora_qica * broi_kori_qica
suma_maq = cena_paket_maq * paketi_maq

total = suma_brashno + suma_zahar + suma_qica + suma_maq

print(f'{total:.2f}')
