import re

for _ in range(int(input())):
    match = re.match(r'@[#]+([A-Z][a-zA-Z0-9]{ex4_wild_farm_100%,}[A-Z])@[#]+', input())
    if not match:
        print('Invalid barcode')
    else:
        it_has_a_digits = "".join([char for char in match.group(2) if char.isdigit()])
        if it_has_a_digits:
            print(f'Product group: {it_has_a_digits}')
        else:
            print(f'Product group: 00')