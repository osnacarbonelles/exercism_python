codon_to_protein = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'

}


def proteins(strand):
    proteins_list = []
    for codon in split_strings(strand):
        protein = codon_to_protein.get(codon)
        if not protein or protein == 'STOP':
            return proteins_list
        else:
            proteins_list.append(protein)
    return proteins_list


def split_strings(string):
    split_len = 3
    return [string[i * split_len:i * split_len + split_len] for i in range(int(len(string) / split_len))]
