"""Solution to the pangram exercise."""
import string


def is_pangram(phrase):
    """Check if the phrase is a pangram.\n
       A pangram is a sentence using every letter of the alphabet
       at least once.

       Parameter
       ----------------------
       phrase : string | The phrase to test

       Returns
       ----------------------
       True if the phrase is a pangram, otherwhise False.
    """
    pangram = {c for c in phrase.lower() if c.isalpha()}
    return len(pangram) == len(string.ascii_lowercase)
