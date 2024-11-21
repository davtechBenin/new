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

	def Foreign_surf(self):
		if self.Ret == "Accueil":
			cont = self.Accueil
		elif self.Ret == "INSC":
			cont = self.Inscrip
			cont.Save_Clt(self.Form)
			cont.This_ind = int(self.Ins_ind)
			cont.add_all()
		self.Set_cont_obj(cont)

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
		part_request = request.get("part_request")
		self.Form = request["form"]
		ret_L = part_request.split("-")
		cont = ret_L[1:]
		if cont:
			self.Ret_handler(cont)

	def Ret_handler(self,ret):
		if type(ret) == list:
			if "INSC" in ret[0]:
				self.Ret,self.Ins_ind = ret[0].split("_")
			if "Conn" == ret[0]:
				self.Connexion_handler()
		self.add_all()

