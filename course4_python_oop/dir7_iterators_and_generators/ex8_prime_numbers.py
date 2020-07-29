def get_primes(sequence):
    for el in sequence:
        if el < 2:
            continue
        is_prime = True

        for num in range(2, el):
            if el % num == 0:
                is_prime = False
        if is_prime:
            yield el
