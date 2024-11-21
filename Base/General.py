#Coding:utf-8
"""
	Base de donnée général de l'application
	Enrégistement d'un client:
		- Email
		- mot de pass
		- on retourn un identifiant unique de 8 chiffres
"""
from . import Connection as CN
from time import time
from random import choice

from .Client import Client

class General:
	def __init__(self):
		self.dossier = 'Le_Rupin'
		self.fichier = 'General'

		self.Clt_Base = Client()

# Général
	def Add_data(self,key,data):
		dos = self.dossier
		fic = self.fichier
		return CN.Save_data(dos,fic,key,data)

	def Get_data(self,key):
		dos = self.dossier
		fic = self.fichier
		return CN.Get_data(dos,fic,key)

# Gestion des clients
	def add_client(self,data):
		key = "CLT_RUPIN"
		email = data.get("Email")
		m_pas = data.get("Mot de pass")

		dic = self.get_client()
		if email in dic:
			return "Error","Un client existe déjà avec cet email !"
		
		ind =str(len(dic)+1)
		len_ind = len(ind)
		for i in range(0,8-len_ind):
			ind+="0"

		"""
			La base est composé de :
				email = [mot de pass, identifiant]
		"""
		dic[email] = [m_pas,ind]
		clt_dic = {"email":email,
		"mot de pass":m_pas}
		self.Clt_Base.Add_clt(ind,clt_dic)
		self.Add_data(key,dic)
		return ind

	def get_client(self):
		key = "CLT_RUPIN"
		dic = self.Get_data(key)
		if not dic:
			dic = dict()
		return dic

	def get_this_client(self,email,m_pas):
		dic = self.get_client()
		if email in dic:
			m_p,ind = dic[email]
			if m_p == m_pas:
				return ind
			else:
				return False
		else:
			return None

# Gestion des employers
	def add_employer(self,data):
		key = "EMP_RUPIN"
		email = data.get("Email")
		m_pas = data.get("Mot de pass")

		dic = self.get_employer()
		if email in dic:
			return "Un employé existe déjà avec cet email !"
		
		ind =str(len(dic)+1)
		len_ind = len(ind)
		for i in range(0,8-len_ind):
			ind+="0"

		"""
			La base est composé de :
				email = [mot de pass, identifiant]
		"""
		dic[email] = [m_pas,ind]
		self.Add_data(key,dic)
		return ind

	def get_employer(self):
		key = "EMP_RUPIN"
		dic = self.Get_data(key)
		if not dic:
			dic = dict()
		return dic

# Gestion des admins
	def add_admin(self,data):
		key = "ADM_RUPIN"
		email = data.get("Email")
		m_pas = data.get("Mot de pass")

		dic = self.get_admin()

		if email in dic:
			return "Un admin existe déjà avec cet email !"
		
		ind =str(len(dic)+1)
		len_ind = len(ind)
		for i in range(0,8-len_ind):
			ind+="0"

		"""
			La base est composé de :
				email = [mot de pass, identifiant]
		"""
		dic[email] = [m_pas,ind]
		self.Add_data(key,dic)
		return ind

	def get_admin(self):
		key = "ADM_RUPIN"
		dic = self.Get_data(key)
		if not dic:
			dic = dict()
		return dic
