a = input("Podaj działanie (np 273+51): ")
def	dzialanie(a):
	if "+" in a:
		x = a.find("+")
		r=str(int(a[:x])+int(a[x:]))
	elif "-" in a:
		x = a.find("-")
		r=str(int(a[:x])+int(a[x:]))
	elif "*" in a:
		x = a.find("*")
		r=str(int(a[:x])*int(a[(x+1):]))

	m=max(len(r),len(a[:x]),len(a[x:])-1)
	
	print((a[:x]).rjust(m))
	print((a[x:]).rjust(m))
	print(m*"-")
	print(r.rjust(m))
