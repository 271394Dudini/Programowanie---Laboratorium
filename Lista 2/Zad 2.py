from PIL import Image

def miniatura(nazwa1, rozmiar, nazwa2):    # 'Desktop/śmieszne obrazki hihi/michał.jpg'
	obraz = Image.open(nazwa1)
	obraz.convert('RGB').save('Desktop/smieszne obrazki hihi/1.jpg', "JPEG")
	obraz1 = Image.open('Desktop/smieszne obrazki hihi/1.jpg')
	obraz2 = obraz1.resize(rozmiar)
	obraz2.save(nazwa2)

miniatura('Desktop/smieszne obrazki hihi/1.png', (100,100), 'Desktop/smieszne obrazki hihi/1.jpg')