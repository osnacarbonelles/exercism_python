def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        i = 0
        j = 0
        while i < len(strand_a):
            if strand_a[i] != strand_b[i]:
                i += 1
                j += 1
            else:
                i += 1
        return j
    raise ValueError('Longitud invalida')
