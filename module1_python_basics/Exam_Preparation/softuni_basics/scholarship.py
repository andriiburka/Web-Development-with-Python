
# You cannot get a scholarship!
# 480.00
# 4.60
# 450.00
#
# You get a Social scholarship 147 BGN
# 300.00
# 5.65
# 420.00


# imports
import math

# inputs
dohod_v_leva = float(input())
sreden_uspeh = float(input())
min_rabotna_zaplata = float(input())
socialna_stipendiq = 0
socialna_stipendiq_bool = False
otlichen_rezultat_stipendiq = 0
otlichen_rezultat_stipendiq_bool = False


if dohod_v_leva < min_rabotna_zaplata and sreden_uspeh >= 4.5:
    socialna_stipendiq_bool = True
    socialna_stipendiq = min_rabotna_zaplata * 0.35

if sreden_uspeh > 5.50:
    otlichen_rezultat_stipendiq_bool = True
    otlichen_rezultat_stipendiq = sreden_uspeh * 25

if socialna_stipendiq_bool and otlichen_rezultat_stipendiq_bool:
    if socialna_stipendiq > otlichen_rezultat_stipendiq:
        print(f'You get a Social scholarship {math.floor(socialna_stipendiq)} BGN')
    else:
        print(f'You get a scholarship for excellent results {math.floor(otlichen_rezultat_stipendiq)} BGN')
elif socialna_stipendiq_bool:
    print(f'You get a Social scholarship {math.floor(socialna_stipendiq)} BGN')
elif otlichen_rezultat_stipendiq_bool:
    print(f'You get a scholarship for excellent results {math.floor(otlichen_rezultat_stipendiq)} BGN')
else:
    print('You cannot get a scholarship!')
