def zmiana(path):
	with open(path, 'rb') as f:
		tekst = str(f.read())
	print("przed\n")
	print(f"{tekst}\n")
	x=tekst.find(r"\n")
	while x!=(-1):
		if tekst[(x-2):x] == r"\r":
			tekst = tekst[:(x-2)]+tekst[x:]
			x = tekst.find(r"\n", x+1)
		else:
			tekst = tekst[:x]+r"\r"+tekst[(x+1):]
			x = tekst.find(r"\n", x+3)
		
	print("po\n")
	print(tekst)

		

zmiana(r"Desktop/Programowanie/Lista 3/Plik2.txt")