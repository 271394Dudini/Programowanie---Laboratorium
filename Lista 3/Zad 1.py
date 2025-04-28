import os
import shutil
import time
import datetime

a = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")   #pobranie czasu lokalnego
a = a.replace(" ","-")
a = a.replace(":","-")

def kopia(path, f=[], r=[]):
	cpath=f"Desktop/backup/copy_{a}"
	os.makedirs(cpath)
	for root,dirs,files in os.walk(path):   # 4 przypadki
		if len(f)!=0:
			for i in range(len(f)):
				if root==f[i]:
					if len(r)==0:
						for i in range(len(files)):
							shutil.copy(f"{root}/{files[i]}", cpath)
							if os.path.exists(f"{cpath}/{files[i]}"):
								if float(float(time.time()-os.path.getmtime(f"{root}/{files[i]}")))>259200.0:
									os.remove(f"{cpath}/{files[i]}")
					else:
						for i in range(len(r)):
							for j in range(len(files)):
								if files[j][(-len(r[i])):]==r[i]:
									shutil.copy(f"{root}/{files[j]}", cpath)
									if os.path.exists(f"{cpath}/{files[j]}"):
										if float(float(time.time()-os.path.getmtime(f"{root}/{files[j]}")))>259200.0:
											os.remove(f"{cpath}/{files[j]}")
		else:
			if len(r)==0:
				for i in range(len(files)):
					shutil.copy(f"{root}/{files[i]}", cpath)
					if os.path.exists(f"{cpath}/{files[i]}"):
						if float(float(time.time()-os.path.getmtime(f"{root}/{files[i]}")))>259200.0:
							os.remove(f"{cpath}/{files[i]}")
			else:
				for i in range(len(r)):
					for j in range(len(files)):
						if files[j][(-len(r[i])):]==r[i]:
							shutil.copy(f"{root}/{files[j]}", cpath)
							if os.path.exists(f"{cpath}/{files[j]}"):
								if float(float(time.time()-os.path.getmtime(f"{root}/{files[j]}")))>259200.0:
									os.remove(f"{cpath}/{files[j]}")
