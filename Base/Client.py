#Coding:utf-8
"""
	La base des clients. Un client est créé par defaut
	avec son identifiant
"""
from . import Connection as CN
from random import choice
from lib.DAV_BASE.MyData import TODAY

class Client:
	def __init__(self):
		self.dossier = 'Le_Rupin'
		self.fichier = 'Client'

		self.Finance_key = 'Finance'

# Fichier temporaire
	def Save_temp(self,key,dic):
		"""
			Cette méthode est utiliser pour stocker
			les informations temporaire dont la validation
			nécessite la vérification du mot de pass de 
			l'utilisateur

			key doit être l'identifiant du client
		"""
		dos = self.dossier
		fic = 'Client/temp'
		return CN.Save_data(dos,fic,key,dic)

	def Get_temp(self,key):
		"""
			Cette méthode est utiliser pour recupérer
			les informations temporaire
		"""
		dos = self.dossier
		fic = 'Client/temp'
		return CN.Get_data(dos,fic,key)

	def Sup_temp(self,key):
		"""
			Cette méthode est utiliser pour Supprimer le
			fichier temporaire
		"""
		dos = self.dossier
		fic = 'Client/temp'
		return CN.Sup_data(dos,fic,key)

# Général
	def Add_data(self,ident,key,data):
		dos = self.dossier
		fic = f"{self.fichier}/{ident}"
		return CN.Save_data(dos,fic,key,data)

	def Get_data(self,ident,key):
		dos = self.dossier
		fic = f"{self.fichier}/{ident}"
		return CN.Get_data(dos,fic,key)

	def Sup_data(self,ident,key):
		dos = self.dossier
		fic = f"{self.fichier}/{ident}"
		return CN.Sup_data(dos,fic,key)

# Creation du client
	def Add_clt(self,ident,dic):
		"""
			ident est l'identifiant
			dic représente les informations de connection
		"""
		key = 'INFO_CON'
		return self.Add_data(ident,key,dic)

	def Get_info_connection(self,ident):
		key = 'INFO_CON'
		return self.Get_data(ident,key)

# gestion des emails
	def Get_email(self,ident):
		info_con = self.Get_info_connection(ident)
		return info_con["email"]

	def change_email(self,ident,email):
		info_con = self.Get_info_connection(ident)
		info_con['email'] = email
		self.Add_clt(ident,info_con)

# Gestion des mots de pass
	def Get_password(self,ident):
		info_con = self.Get_info_connection(ident)
		return info_con["mot de pass"]

	def change_password(self,ident,password):
		info_con = self.Get_info_connection(ident)
		info_con['mot de pass'] = password
		self.Add_clt(ident,info_con)

# Gestion de code de confirmation
	def Get_conf_code(self,ident):
		key = "CONF_CODE"
		a = ['A','B',"C","D",1,2,3,4,5,6,7,8,9,0]
		L = list()
		while len(L) < 6:
			i = choice(a)
			L.append(i)
		self.Add_data(ident,key,L)
		return L

	def Conf_code(self,ident,code):
		key = "CONF_CODE"
		Cod = self.Get_data(ident,key)
		if Cod == code:
			self.Sup_data()
			return True
		else:
			return False

	def Sup_conf_code(self,ident):
		key = "CONF_CODE"
		self.Sup_data(ident,key)

# Gestion d'information personnelle
	"""
		Ceci regroupe de façon générale toutes les 
		information concernat le client.
	"""
	def Save_pers_info(self,ident,dic):
		key = 'PERSONAL_INFO'
		Pers = self.Get_pers_info(ident)
		Pers.update(dic)
		return self.Add_data(ident,key,Pers)

	def Get_pers_info(self,ident):
		key = 'PERSONAL_INFO'
		Pers = self.Get_data(ident,key)
		#print(Pers)
		if not Pers:
			Pers = dict()
		return Pers

# Gestion des finances
	def add_solde(self,ident,montant):
		key = self.Finance_key+"/solde"
		solde = self.get_solde()
		solde += float(montant)
		self.Add_data(ident,key,solde)
		hist = {
			"motif":"solde",
			"montant":montant
		}
		self.add_historique(ident,hist)

	def get_solde(self,ident):
		key = self.Finance_key+"/solde"
		solde = self.Get_data(ident,key)
		if not solde:
			solde = float()
		return float(solde)

	def add_cmd(self,ident,montant):
		key = self.Finance_key+"/cmd"
		cmd = self.get_cmd()
		cmd += float(montant)
		self.Add_data(ident,key,cmd)
		hist = {
			"motif":"cmd",
			"montant":montant
		}
		self.add_historique(ident,hist)

	def get_cmd(self,ident):
		key = self.Finance_key+"/cmd"
		cmd = self.Get_data(ident,key)
		if not cmd:
			cmd = float()
		return float(cmd)

	def init_cmd(self,ident):
		m = float()
		key = self.Finance_key+"/cmd"
		self.Add_data(ident,key,m)

	def add_historique(self,ident,hist):
		"""
			hist doit être:
				motif (solde ou cmd)
				montant
		"""
		moti = hist['motif']
		mont = hist['montant']
		key = self.Finance_key+"/historique"

		dic = self.get_historique(ident)
		date = TODAY().date__
		heur = TODAY().hour
		D = {
			"Montant":mont,
			"Heur":heur
		}
		date_dict = dic.get(date,dict())
		motif_liste = date_dict.get(moti)
		motif_liste.append(D)
		date_dict[moti] = motif_liste
		dic[date] = date_dict
		self.Add_data(ident,key,dic)

	def get_historique(self,ident):
		key = self.Finance_key+"/historique"
		his_dic = self.Get_data(ident,key)
		if not his_dic:
			his_dic = dict()
		return his_dic

# la gestion des Messages
	def send_sms(self,ident,mes):
		key = "message"
		typ = 'Send'
		dic = self.get_mes_dic(typ,mes)
		lis = self.get_sms(ident)
		lis.append(dic)
		self.Add_data(ident,key,lis)

	def receive_sms(self,ident,mes):
		key = "message"
		typ = 'Receive'
		dic = self.get_mes_dic(typ,mes)
		lis = self.get_sms(ident)
		lis.append(dic)
		self.Add_data(ident,key,lis)

	def get_sms(self,ident):
		key = "message"
		lis = self.Get_data(ident,key)
		if not lis:
			lis = list()
		return lis

	def get_mes_dic(self,typ,mes):
		date = TODAY().date__
		dic = {
			typ:{
				"Message":mes,
				"Date":date,
				'Heure':TODAY().hour
			}
		}
		return dic








