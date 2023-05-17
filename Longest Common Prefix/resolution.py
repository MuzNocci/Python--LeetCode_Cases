strs = ["flower","flow","flight"]

res = ''
prefix = strs[0]
 
for word in strs[1:]:
    while word[:len(prefix)] != prefix and prefix:
        prefix = prefix[:len(prefix)-1]
    if not prefix:
        break

print(prefix)