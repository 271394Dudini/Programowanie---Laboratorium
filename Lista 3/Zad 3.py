from PyPDF2 import PdfWriter, PdfReader

def sklejpdf(pdfs,nazwa):
	nowy=PdfWriter()
	for i in range(len(pdfs)):
		plik = PdfReader(pdfs[i])
		for j in range(len(plik.pages)):
			nowy.add_page(plik.pages[j])
	nowy.write(nazwa)

sklejpdf([r"Desktop\Programowanie\Lista 3\zad 3\Lista_MST_1.pdf",r"Desktop\Programowanie\Lista 3\zad 3\Lista_MST_2.pdf",r"Desktop\Programowanie\Lista 3\zad 3\wzory.pdf"],r"Desktop\Programowanie\Lista 3\zad 3\nowy.pdf")