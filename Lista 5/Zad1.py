import tkinter as tk
import customtkinter as ctk

import requests as req
import xml.etree.ElementTree as ET

waluty=["PLN"]
kursy=[1]
wifi=""
try:
	with req.get(r"https://static.nbp.pl/dane/kursy/xml/a095z250519.xml") as rq:
		with open(r'Desktop\Programowanie\Lista 5\kurs.xml', 'wb') as file:
			file.write(rq.content)
except:
	wifi="Brak dostępu do internetu, skorzystano z ostatnio pobranych danych."
	
tree = ET.parse(r"C:\Users\User\Desktop\Programowanie\Lista 5\kurs.xml")
root = tree.getroot()
for pozycja in root.findall('pozycja'):
	nazwa_waluty = pozycja.find('nazwa_waluty')
	waluty.append(nazwa_waluty.text)
	kurs = pozycja.find('kurs_sredni')
	kurs = kurs.text.replace(",",".")
	kursy.append(kurs)
    


class MainWindow:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Przelicznik walut")
		self.window.geometry("600x500+700+100")
		self.window.resizable(False, False)
		self.window.configure(bg="antiquewhite2")
		self.widgets()
	

	def widgets(self):

		self.label0 = tk.Label(self.window, text="Przelicznik Walut", bg="antiquewhite2", font="Impact 45")
		self.label0.pack(pady=25)

		self.label = tk.Label(self.window, text="Z", bg="antiquewhite2", font="Luminari 20")
		self.label.place(x=125,y=160)

		self.label1 = tk.Label(self.window, text="NA", bg="antiquewhite2", font="Luminari 20")
		self.label1.place(x=350,y=160)

		self.label2 = tk.Label(self.window, text=wifi, bg="antiquewhite2", font="Luminari 10")
		self.label2.place(x=30,y=450)

		self.lista1 = ctk.CTkOptionMenu(self.window, values=waluty, fg_color="OrangeRed4", button_color="firebrick4", font=("Luminari",15), button_hover_color="gray10")
		self.lista1.place(x=125,y=200)

		self.lista2 = ctk.CTkOptionMenu(self.window, values=waluty,button_color="firebrick4", fg_color="OrangeRed4", font=("Luminari",15), button_hover_color="gray10")
		self.lista2.place(x=350,y=200)

		self.button = tk.Button(self.window, text="Przelicz",font="Boulder 20")
		self.button.place(x=225,y=350,height=50,width=150)
		self.button.config(command=self.kalk)

		self.entry = tk.Entry(self.window,font="Luminari 20")
		self.entry.place(x=125,y=250,height=50,width=130)

		self.wynik = tk.Label(self.window,font="Luminari 20")
		self.wynik.place(x=350,y=250,height=50,width=130)

		self.exit = tk.Button(self.window, text="Wyjście", font="Luminari 15")
		self.exit.place(x=450,y=420,height=40,width=80)
		self.exit.config(command=quit)
	

	def kalk(self):
		n = float(self.entry.get())
		indeks1 = waluty.index(self.lista1.get())
		w1=float(kursy[indeks1])
		indeks2 = waluty.index(self.lista2.get())
		w2=float(kursy[indeks2])
		wynik = format(n*w1/w2, '.2f')
		self.wynik.config(text=(wynik))

	def run(self):
		self.window.mainloop()
