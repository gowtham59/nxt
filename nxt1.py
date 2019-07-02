o1=input()
b2=input()
c3="abcdefghijklmnopqrstuvwxyz"
d4=[]
e5=[]
s6=""
for i in range(0,len(o1)):
    for j in range(0,len(c3)):
        if o1[i]==c3[j]:
            d4.append(j+1)
        if b2[i]==c3[j]:
            e5.append(j+1)
for k in range(0,len(d4)):
    tot=d4[k]+e5[k]
    if(tot<=26):
        s6=s6+c3[tot-1]
    else:
        m=tot-26
        s6=s6+c3[m-1]
print(s6)
