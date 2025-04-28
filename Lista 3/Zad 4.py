import qrcode
import cv2

def makeqr(dane,nazwa=r"Desktop\kopia.png"):
	img = qrcode.make(dane)
	img.save(nazwa)

makeqr("kokokoko eurospoko")

def readqr(image):
	img = cv2.imread(image)
	det = cv2.QRCodeDetector()
	data = det.detectAndDecode(img)
	print(data[0])

readqr(r"Desktop\kopia.png") 