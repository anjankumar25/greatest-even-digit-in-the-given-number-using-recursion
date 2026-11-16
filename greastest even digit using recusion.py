def aa(a,v=0):
    if a == 0:
        return v
    e=a%10
    if e % 2 == 0:
        if e > v:
            v=e
    return aa(a//10,v)
print(aa(12333338863))