def find_anagrams(word, candidates):
    return [ test for test in candidates 
        if word.lower() != test.lower()
        if sorted((word.lower())) == sorted(test.lower())
        ]