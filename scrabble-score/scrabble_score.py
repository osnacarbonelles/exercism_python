scores = {
    letra: puntos
    for letras, puntos in [
        ("AEIOULNRST", 1),
        ("DG", 2),
        ("BCMP", 3),
        ("FHVWY", 4),
        ("K", 5),
        ("JX", 8),
        ("QZ", 10),
    ]
    for letra in letras
}


def score(palabra):
    return sum([
        scores[letra]
        for letra in palabra.upper()
    ])
