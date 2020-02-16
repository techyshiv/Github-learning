#INPUT:[1,2,3,4,5]
#OUTPUT:[120,60,40,30,24]
l=[1,2,3,4,5]
result=[]
pos=0
mul=1
for i in range(len(l)):
    for i in l:
        if i==l[pos]:
            None
        else:
            mul*=i
    result.append(mul)
    mul=1
    print(pos)
    pos+=1
print(result)
