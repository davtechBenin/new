#Coding:utf-8
"""
	La base de donner des Favoris. il est utiliser pour
	la sauvegarde des favoris du client. 

	Nous avons les services favoris et les boutiques favoris
"""
from . import Connection as CN
from time import time
from random import choice

from .Basic_fonc import GET_KEY_LIST

class Favoris:
	def __init__(self,ident):
		self.ident = ident
		self.dossier = "Le_Rupin"
		self.fichier = f'Commande/{self.ident}'

# Général
	def Add_data(self,key,data):
		dos = self.dossier
		fic = self.fichier
		return CN.Save_data(dos,fic,key,data)

	def Get_data(self,key):
		dos = self.dossier
		fic = self.fichier
		return CN.Get_data(dos,fic,key)

	def Sup_data(self,key):
		dos = self.dossier
		fic = self.fichier
		return CN.Sup_data(dos,fic,key)

	def Save_service_favoris(self,service):
		"""
			service doit être:
				name
				catégories
				note
		"""
		key = 'Service_favoris'
		name = service['name']
		cate = service['cetégorie']
		note = service['note']

		all_serv = self.Get_service_favoris()
		cat_dic = all_serv.get(cate,dict())
		if name in cat_dic:
			del cat_dic[name]
		else:
			cat_dic[name] = {"Note":note}
		all_serv[cate] = cat_dic

		self.Add_data(key,all_serv)


	def Get_service_favoris(self):
		key = 'Service_favoris'
		dic = self.Get_data(key)
		if not dic:
			dic = dict()
		return dic

	def Save_boutique_favoris(self,boutique):
		"""
			boutique doit être:
				name
				catégories
				note
		"""
		key = 'Boutique_favoris'
		name = boutique['name']
		cate = boutique['cetégorie']
		note = boutique['note']

		all_serv = self.Get_service_favoris()
		cat_dic = all_serv.get(cate,dict())
		if name in cat_dic:
			del cat_dic[name]
		else:
			cat_dic[name] = {"Note":note}
		all_serv[cate] = cat_dic

		self.Add_data(key,all_serv)


	def Get_boutique_favoris(self):
		key = 'Boutique_favoris'
		dic = self.Get_data(key)
		if not dic:
			dic = dict()
		return dic





















# Base global
	def Save_gene(self,part,name):
		"""
			Ici, on lui donne la partie et le nom

			part représente les différentes types de 
			commandes
		"""
		key = f"General/{part}"
		lis = self.Get_gene(part)
		if name not in lis:
			lis.append(name)
		self.Add_data(key,lis)

	def Get_gene(self,part):
		key = f"General/{part}"
		Liste = self.Get_data(key)
		if not Liste:
			Liste = list()
		return Liste

	def Sup_gene(self,part,name):
		key = f"General/{part}"
		Liste = self.Get_gene(part)
		ind = Liste.index(name)
		del Liste[ind]
		self.Add_data(key,Liste)



