def isValid(s):
    
    c = 0
    ipar = False
    icol = False
    icha = False
    fpar = False
    fcol = False
    fcha = False
    
    for i in s:
        
        if i == '(':
            ipar = True
            for n in s[c:]:
                if n == ')':
                    fpar = True
            
        if i == '[':
            icol = True
            for n in s[c:]:
                if n == ']':
                    fcol = True
            
        if i == '{':
            icha = True
            for n in s[c:]:
                if n == '}':
                    fcha = True
            
        c += 1
    
    if fpar == ipar and fcol == icol and fcha == icha:
        result = True
    else:
        result = False

    return result
    
print(isValid('()[]{'))