usr_inp = input()
di = {let: usr_inp.count(let) for let in usr_inp}
[print(f"{let}: {num} time/s") for let, num in sorted(di.items(), key=lambda x: x[0])]