#Coding:utf-8
"""
	Module de définition du layout principale

	Chaque partie sera représenter par un part_request.
"""
from lib.Pyweb.Layout import Layout

from Prog.general.Prog import Main as Ac_Main

from .Client.Prog.ACC import ACC

from Prog.Services.Service_surf import Services_lay

from color import *

class main(Layout):
	def __init__(self,parent,bg_color):
		size = 100,100
		pos = (0,0)
		Layout.__init__(self,size,bg_color,pos,parent)
		self.MAIN_LAY = self
		self.Part_dic = {
			"Accueil":Ac_Main.main(self).Run()
		}#Pour stocker les surfaces des parties
		self.Curent_layout = Layout((100,100),bg_color,
			pos,self)
		self.request = dict()
		self.cookies = list()

		self.Services_size = 1,1
		self.Services_pos = (0,0)
		self.Services_col = APP_COL

		self.Service_lay = Services_lay(self)

	def Get_cookies(self):
		return self.request['cookies']

	def Get_cook(self):
		return self.cookies

	def Set_cook(self,name,val):
		self.cookies.append((name,val))

	def Get_ident_cookies(self):
		cookies = self.Get_cookies()
		for key in cookies:
			if 'IDENT' in key:
				return cookies[key]
		return str()

	def Set_Ident_cookies(self,val):
		self.Set_cook('IDENT',val)

	def Set_Curent_surf(self,ret):
		key = 'CURENT_SURF'
		self.Set_cook(key,ret)

	def Get_Curent_surf(self):
		cookies = self.Get_cookies()
		for key in cookies:
			if 'CURENT_SURF' in key:
				return cookies[key]
		return str()

	def Ret_handler(self,ret):
		ret_L = ret.split("-")
		cont = False
		if ret == "Accueil" and self.Get_ident_cookies():
			self.Curent_layout = ACC(self)
		else:
			if len(ret_L) > 1:
				ret = ret_L[0]
				cont = ret_L[1:]
			if ret in self.Part_dic:
				self.Curent_layout = self.Part_dic[ret]
				if cont:
					self.Curent_layout.Execution(self.request)
			if ret_L[0] == 'SERV':
				self.Curent_layout = self.Service_lay

	def Execution(self,request):
		self.request = request
		part_request = self.request.get('part_request',str())
		if not part_request:
			part_request = "Accueil"
		if part_request:
			self.Ret_handler(part_request)
			
		self.Curent_layout.Execution(self.request)
		return self.Curent_layout.Run_html()

