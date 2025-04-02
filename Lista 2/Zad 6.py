# a = input("Podaj działanie (np 273+51)")
a="275121221+2002222223"
x = a.find("+")
print(len(a[:x]))
print(len(a[x:])-1)
b=" "
c="-"
r=len(a[:x])-len(a[x:])+1
m=max(len(a[:x]),len(a[x:]))
if r<0:
	d1=abs(r)
	d2=0
else:
	d1=0
	d2=r

print(f"""{(d1+1)*b}{a[:x]}
+{d2*b}{a[(x+1):]}
{m*c}
{int(a[:x])+int(a[(x+1):])}""")