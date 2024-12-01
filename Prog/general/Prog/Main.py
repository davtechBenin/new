#Coding:utf-8
"""
	Module de création de la page d'accueil de la 
	surface générale
"""
from lib.Pyweb.Layout import Layout
from lib.Pyweb.core import balises as bl
from lib.Pyweb.core import form

Css = bl.style
from . import TEXT
from color import *
import urllib

from .Accueil.Accueil import Main
from .Accueil.Inscription import Inscription,General
from ...Client.Prog.ACC import ACC
from ...Services.Ser_Main import Ser_main

class main(Layout):
	def __init__(self,parent):
		size = 1,1
		col = AFF_COL
		pos = 0,0
		Layout.__init__(self,size,col,pos,parent)

		self.Ret = "Accueil"
		self.Ins_ind = int()

		self.Base = General()

		self.Accueil = Main(self.parent)
		self.Inscrip = Inscription(self.parent)

		self.part_dic = {
			"Accueil":self.Accueil,
			"INSC":self.Inscrip,
			"SERV":Ser_main(self),
		}
		self.Curent_surf = self.Accueil
		#self.Service = 

	def Acc_def(self):
		"""
			C'est ici que je vais définir le swicht
			des connexions
		"""
		if self.MAIN_LAY.Get_ident_cookies():
			Acc = ACC(self.parent)
			self.Curent_surf = Acc
		else:
			self.Curent_surf = self.Accueil

	def Part_set(self,part_request):
		part_request = part_request.split("-")
		ret_l = list()
		if len(part_request)>1:
			part = part_request[0]
			ret_l = part_request[1:]
		else:
			part = part_request[0]
		
		if part == 'Accueil':
			self.Acc_def()
			self.Ret_handler(ret_l)

		elif 'INSC' in part:
			part,ind = part.split('_')
			self.Curent_surf = self.part_dic["INSC"]
			self.Curent_surf.This_ind = int(ind)
			self.Curent_surf.Save_Clt(self.Form)
		
			self.Curent_surf.Ret_handler(ret_l)	
			self.Curent_surf.add_all()

		elif 'SERV' == part:
			self.Curent_surf = self.part_dic[part]
			self.Curent_surf.Execution(self.request)

	def Foreign_surf(self):
		self.Set_cont_obj(self.Curent_surf)

	def Run(self):
		self.add_all()
		return self

	def Connexion_handler(self):
		email = self.Form["Email"]
		password = self.Form["password"]
		ind = self.Base.get_this_client(email,password)
		if not ind:
			self.Accueil.Set_error(TEXT.CONN_ERROR)
		else:
			Acc = ACC(self.parent)
			self.MAIN_LAY.Set_cook('IDENT',ind)
			self.MAIN_LAY.Curent_layout = Acc
			self.MAIN_LAY.add_all()

	def Execution(self,request):
		self.request = request
		part_request = request.get("part_request")
		self.Form = request["form"]
		if part_request:
			self.Part_set(part_request)
		else:
			self.Acc_def()
			self.Curent_surf.Execution(request)

		self.add_all()

	def Ret_handler(self,ret):
		if ret:
			if type(ret) == list:
				if "Conn" == ret[0]:
					self.Connexion_handler()

