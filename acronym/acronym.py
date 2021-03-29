import re


def abbreviate(words):

    return ''.join([i[0] for i in re.findall('[A-Z]+\'?[A-Z]+|[A-Z]',
                    words.upper())])
