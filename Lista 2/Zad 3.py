import os
import zipfile
import datetime

a = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
a = a.replace(" ","-")
a = a.replace(":","-")

def kopia_zip(dir):
	with zipfile.ZipFile(f"{dir[:8]}{a}_backup_{dir[8:]}.zip", 'w') as nowy:  # jak się pozbyć folderu Desktop i moje_dane
		for root,dirs,files in os.walk(dir):
			for i in range(len(files)):
				nowy.write(f"{root}/{files[i]}")
