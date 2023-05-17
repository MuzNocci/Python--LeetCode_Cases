def isValid(s):

    c = 0
    er = 0
    for i in s:
        n = c+1
        if i == '(':
            if s[n] != ')':
                er += 1
        if i == '[':
            if s[n] != ']':
                er += 1
        if i == '{':
            if s[n] != '}':
                er += 1
        c += 1
    if er > 0:
        result = False
    else:
        result = True
        
    return result

print(isValid('(]'))
