def is_isogram(string):
    letras = []

    for letra in string:
        letra = letra.lower()
        if letra.isalpha() and letra in letras:
            return False
        else:
            letras.append(letra)
    return True
