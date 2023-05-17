def isValid(s):
    
    while s != '':
        u = s
        s = s.replace('()','').replace('[]','').replace('{}','')
        if u == s:
            break
    
    if s:
        return False
    else:
        return True
        
    
print(isValid('(])'))