#Coding:utf-8

"""
	Cet module permet la définition de liaison avec
	la base de données sur le serveur. 

	Par défaut, je vais simplement utiliser un gestionnaires
	de fichier interne

	Les fonctions définie ici seront remplacer par 
	les fonctions de gestion à réseau une fois que 
	la configuration terminer
"""
from lib.DAV_BASE.data_handler import myData

from pathlib import Path
import sys,os


Data_base = myData()

def Create_doss(dossier,fichier):
	default_P = Path.cwd()
	dos = f"BASE_DIR/{dossier}/{fichier}"
	for path in dos.split("/"):
		default_P = default_P.joinpath(path)
		if not default_P.exists():
			os.mkdir(default_P)
	return default_P

def Save_data(dossier,fichier,keys,data):
	"""
		Ici, dossier et fichier vont être considérer
		comme le dossier. la clé sera dont le fichier
	"""
	if ".dav" not in keys:
		keys = keys+'.dav'
	fichier = Create_doss(dossier,fichier)
	fichier = fichier.joinpath(keys)
	lenf = Data_base.dump(fichier,data)
	return lenf

def Get_data(dossier,fichier,keys):
	fichier = Create_doss(dossier,fichier)
	if ".dav" not in keys:
		keys = keys+'.dav'
	fichier = fichier.joinpath(keys)
	try:
		data = Data_base.load(fichier)
	except FileNotFoundError:
		data = False
	return data

def Sup_data(self,dossier,fichier,keys):
	fichier = Create_doss(dossier,fichier)
	if ".dav" not in keys:
		keys = keys+'.dav'
	fichier = Create_doss(dossier,fichier)
	fichier = fichier.joinpath(keys)
	if fichier.exists():
		os.remove(fichier)
		

