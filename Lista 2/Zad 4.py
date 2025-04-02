from PyPDF2 import PdfWriter, PdfReader
import math

def split_pdf(file, x):
	plik = PdfReader(file)
	if x > len(plik.pages):
		return print("za mało stron w PDF")
	rem = len(plik.pages)%x
	q = math.floor(len(plik.pages)/x)
	i=0
	for i in range(x-1):
		nowy = PdfWriter()
		for j in range(q):
			nowy.add_page(plik.pages[i*q+j])
		nowy.write(f"{file[:-4]}_{i+1}.pdf")
		i+=1
	nowy1 = PdfWriter()
	for j in range(q+rem):
		nowy1.add_page(plik.pages[i*q+j])
	nowy1.write(f"{file[:-4]}_{i+1}.pdf")
			
split_pdf(r"Desktop\LOS ESTUDIOS\2 sem\Programowanie\Lista 2\Pdf zad 4\Pdf_inny3.pdf",3)
