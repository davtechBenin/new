#Coding:utf-8
"""
	Interface de gestion des services générale
	proposer par le système coté client
"""
from Import_lay import *

from Prog.general.Prog import TEXT as TEXT2

class Service_G(Layout):
	def __init__(self,parent):
		size = parent.Surf_size
		pos = parent.Surf_pos
		col = parent.Surf_col

		Layout.__init__(self,size,col,pos,parent)

		self.Service_L = [i for i in TEXT2.Serv_dic]
		self.Serv = self.Service_L[0]

		self.Set_size_and_pos()

		self.add_all()

	def Foreign_surf(self):
		self.add_service_F()
		self.add_Surface()

	def Set_size_and_pos(self):
		int_w = 3
		int_h = 5

		pw,ph = self.service_F_size = 94,10
		px,py = self.service_F_pos = int_w,0
		self.service_F_col = self.Get_bg_color()

		self.S_text_size = 15,65
		self.S_text_Y = 15
		self.S_text_bg_color = AFF_COL

		sw,sh = self.Surface_size = pw,100 - ph-int_h
		sx,sy = self.Surface_pos = int_w,ph + int_h*.5
		self.Surface_col = MAIN_COL

	def add_service_F(self):
		size = self.service_F_size
		pos = self.service_F_pos
		col = self.service_F_col
		service_F = Layout(size,col,pos,self)
		service_F.Set_overflow()

		X_dep = 3
		X = 0
		Y = self.S_text_Y
		for i in self.Service_L:
			service_F.add_button(i,self.S_text_size,
				(X,Y),Info = i,font_size = .9,
				text_align = 'center',
				bg_color = self.S_text_bg_color)
			X += self.S_text_size[0]+X_dep
		
		self.Set_cont_obj(service_F)

	def add_Surface(self):
		size = self.Surface_size
		pos = self.Surface_pos
		col = self.Surface_col
		Surface = Layout(size,col,pos,self)

		Surface.add_Text(self.Serv,(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(Surface)

	def Ret_handler(self,ret):
		"""
			Reste à définir les parties de gestion 
			de chaque services
		"""
		self.Serv = ret
		self.add_all()

	def Execution(self,request):
		ret = request.get('request')
		self.Ret_handler(ret)
