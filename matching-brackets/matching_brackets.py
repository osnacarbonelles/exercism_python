brackets = {"(": ")", "[": "]", "{": "}"}


def is_paired(input_string):
    if not input_string:
        return True
    stack = []
    for c in input_string:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values():
            if not stack or c != stack.pop():
                return False
    return not stack
