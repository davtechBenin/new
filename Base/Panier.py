#Coding:utf-8
"""
	La base de donner des panier est formater par défaut
	avec l'identifiant de l'utilisateur

	principe de base:
		Une commande enrégistrée est par défaud considérée
		comme une commande en cours. Les attributs suplémentaire
		lui seront attribuer au niveau administrateur.

	Nous avons donc 4 types de commande:
		-> Encours
		-> Satisfait
		-> Rejetter
		-> Accepter
"""
from . import Connection as CN
from time import time
from random import choice

from .Basic_fonc import GET_KEY_LIST

class Panier:
	def __init__(self,ident):
		self.ident = ident

		self.dossier = "Le_Rupin"
		self.fichier = f'Panier/{self.ident}'

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

# All catégories info
	def Add_all_cat(self,categorie):
		key = "catégorie"
		liste = self.Get_all_cat()
		liste.append(categorie)
		self.Add_data(key,liste)

	def Get_all_cat(self):
		key = 'categorie'
		L = self.Get_data(key)
		if not L:
			L = list()
		return L

	def Sup_all_cat(self):
		key = 'categorie'
		self.Sup_data(key)
#
	
	def add_article(self,art_dic):
		"""
			Un Art_dic doit être:
				catégorie: str
				name:
				PVU:
				Qté:
				Montant:
		"""
		key =art_dic.get("catégorie")
		if not key:
			return False
		else:
			self.Add_all_cat(key)

			All_dic = self.Get_Arts(key)
			dic = {
					'PVU' : art_dic["PVU"],
					'Qté' : art_dic["Qté"],
					'Montant' : art_dic["Montant"],
			}
			D = All_dic.get(art_dic['name'])
			if not D:
				D = dic
			else:
				D["Qté"] += dic["Qté"]
				D["Montant"] += dic['Montant']

			M = D['Montant']
			self.Add_prix(M)

			All_dic[art_dic["name"]] = D

			self.Add_data(key,All_dic)

	def Get_Arts(self,key):
		'''
			Cette méthode permet d'obtenir l'ensemble
			des articles selon une catégorie donnée
		'''
		dic = self.Get_data(key)
		if not dic:
			dic = dict()
		return dic

	def Get_All_data(self):
		lis = list()
		for key in self.Get_all_cat():
			lis.append(self.Get_Arts(key))
		return lis

# Les prix du panier
	def Add_prix(self,mont):
		key = 'Montant'
		mont_T = self.Get_prix()
		mont_T += float(mont)
		self.Add_data(key,mont_T)

	def Get_prix(self):
		key = "Montant"
		P = self.Get_data(key)
		if not P:
			P = int()
		return P

class Command:
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

# Commande en cours
	def add_cmd(self,part,cmd_dic):
		"""
			part représente le type de commande

			Un cmd_dic doit être:
				name:
				Montant:
				Date:
				Status:
		"""
		name = cmd_dic["name"]
		self.Save_gene(part,name)
		key = f"{part}/{name}"

		self.Add_data(key,cmd_dic)

	def Update_cmd(self,part,cmd_dic):
		name = cmd_dic["name"]
		self.Save_gene(part,name)
		key = f"{part}/{name}"

		dic = self.Get_cmd(part,name)
		M = dic.get('Montant',float())
		M += float(cmd_dic["Montant"])
		cmd_dic["Montant"] = M

		self.Add_data(key,cmd_dic)

	def Get_cmd(self,part,name):
		'''
			Cette méthode permet d'obtenir l'ensemble
			des articles selon une catégorie donnée
		'''
		key = f"{part}/{name}"

		dic = self.Get_data(key)
		if not dic:
			dic = dict()
		return dic

	def Sup_cmd(self,part,name):
		key = f"{part}/{name}"
		self.Sup_data(key)
		self.Sup_gene(part,name)

	def Get_cmd_lis(self,part = "All"):
		lis = list()
		if part == "All":
			part = ("Encours","Satisfait","Rejetter","Accepter")
		else:
			part = part,
		for P in part:
			name_list = self.Get_gene(P)
			for name in name_list:
				cmd = self.Get_cmd(P,name)
				CM = self._transf_cmd(cmd)
				lis.append(CM)
		return lis

	def _transf_cmd(self,cmd):
		name = cmd["name"]
		date = cmd["Date"]
		stat = cmd["Status"]
		mont = cmd["Montant"]
		dic = {
			name:{
				"Montant":mont,
				"Date":date,
				"Status":stat
			}
		}
		return dic

	def UP_cmd_status(self,last_part,new_part,cmd_dic):
		name = cmd_dic["name"]
		self.Sup_cmd(last_part,name)
		self.add_cmd(new_part,cmd_dic)


class Activite:
	"""
		Ici nous avons deux types de base.
		une pour les activités récente (10)
		et l'autre pour les activitées de chaque jours
	"""
	def __init__(self,ident):
		self.ident = ident
		self.dossier = "Le_Rupin"
		self.fichier = f'Activite/{self.ident}'

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

# Base global
	def Save_gene(self,date):
		"""
			Ici, on lui donne la partie et la date
		"""
		key = "General"
		lis = self.Get_gene()
		if date not in lis:
			lis.append(date)
		self.Add_data(key,lis)

	def Get_gene(self):
		key = "General"
		Liste = self.Get_data(key)
		if not Liste:
			Liste = list()
		return Liste

# 
	def Add_activite(self,act_dict):
		"""
			act_dict doit être:
				name
				Montant
				Date
		"""
		date = act_dict["Date"]
		act = {
			act_dict["name"]:{
				'Montant':act_dict["Montant"],
				"Date":act_dict["Date"]
			}
		}
		lis = self.All_dic(date)
		lis.append(act)
		self.Add_data(date,lis)

		self.Save_activite_recente(act)

	def All_act(self,date):
		Data = self.Get_data(date)
		if not Data:
			Data = list()
		return Data

	def Save_activite_recente(self,act):
		key = "Recente"
		lis = self.Get_activite_recente()
		if len(lis)==10:
			del lis[9]
		if lis:
			lis.insert(0,act)
		else:
			lis = [act]
		self.Add_data(key,lis)

	def Get_activite_recente(self):
		key = 'Recente'
		Data = self.Get_data(key)
		if not Data:
			Data = list()
		return Data
