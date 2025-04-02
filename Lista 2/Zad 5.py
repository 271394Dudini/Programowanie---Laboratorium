from PIL import Image

def znak_wodny(image, znak):

	obraz = Image.open(image)
	znak_w = Image.open(znak)

	znak_w = znak_w.resize(obraz.size)
	znak_w.putalpha(128)

	im3 = Image.alpha_composite(obraz, znak_w) 
	im3.show() 
