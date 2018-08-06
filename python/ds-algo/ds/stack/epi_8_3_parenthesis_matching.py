def is_well_formed1(nstr):
    left_chars = []
    for ch in nstr:
        if ch == "(":
            left_chars.append(")")
        if ch == "{":
            left_chars.append("}")
        if ch == "[":
            left_chars.append("]")
        if ch == ")":
            if not left_chars or ch != left_chars.pop():
                return False
        if ch == "}":
            if not left_chars or ch != left_chars.pop():
                return False
        if ch == "]":
            if not left_chars or ch != left_chars.pop():
                return False
    return True


def is_well_formed2(nstr):
    left_chars = []
    LOOKUP = {'{': '}', '[': ']', '(': ')'}
    for ch in nstr:
        if ch in LOOKUP:
            left_chars.append(ch)
        elif not left_chars or (ch != LOOKUP[left_chars.pop()]):
            return False
    return True


nstr = "(){}(((({[[[]]]})){{[]}}[])"
print(is_well_formed2(nstr))
print(is_well_formed2("[[[]{}]([])]"))
