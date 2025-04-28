def nawiasy(tekst):
	stos=[]
	l1=['[','{','(','<']
	l2=[']','}',')','>']
	for ch in tekst:
		for j in range(4):
			if ch==l1[j]:
				stos.append(l2[j])
		for j in range(4):
			if ch==l2[j]:
				if len(stos)==0:
					return print(False)
				if ch!=stos[-1]:
					return print(False)
				else:
					stos.pop()
	if len(stos) != 0:
		return print(False)
	return print(True)

nawiasy(r"<>{mmm()}<>")
