symbols = "-,.!?"
ext_txt = open("text.txt", "r")
for i, txt_row in enumerate(ext_txt):
    if i % 2 == 0:
        for x in symbols:
            txt_row = txt_row.replace(x, "@")
        words = txt_row.split()[::-1]
        print(" ".join(words))
ext_txt.close()

''' TARGET
fault@ his wasn't it but him@ judge to quick was @I
safer@ is It here@ hide @Quick@
'''