import requests
import webbrowser
from bs4 import BeautifulSoup

def wiki():
	czy="nie"
	link=r'https://pl.wikipedia.org/wiki/'
	while czy == "nie":
		url = 'https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona'
		strona = requests.get(url)
		n1 = (strona.text).find('<title>')
		n2 = (strona.text).find('</title>')
		print(strona.text[(n1+7):(n2-31)])
		czy=input("Czy podoba się tak strona (tak/nie)? ")
		if czy == "nie":
			print("Spróbujmy co innego")
		elif czy == "tak":
			tytuł = strona.text[(n1+7):(n2-31)]
			tytuł.replace(" ","_")
			webbrowser.open(f"{link}{tytuł}")
		else:
			return print("zła odpowiedź")
