def check(pal):
    j = len(pal)
    for i in range(len(pal)):
        if pal[i] != pal[j - 1]:
            return False
        j -= 1
    return True
print(check("1212"))
