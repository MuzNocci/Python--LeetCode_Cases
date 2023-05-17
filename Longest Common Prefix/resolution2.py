strs = ["flower","flow","flight"]

p = strs[0]
        
for i in strs:
    while not i.startswith(p):
        p = p[:-1]
        
print(p)
  

