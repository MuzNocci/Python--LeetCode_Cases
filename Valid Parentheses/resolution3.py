def isValid(s):
    
    lista = []
    dicio = {'(':')','[':']','{':'}'}
    
    for i in s:
        if i in dicio:
            lista.append(i)
        else:
            if not lista or dicio[lista.pop()] != i:
                return False
    
    return not lista
    
print(isValid('([)]'))