#Coding:utf-8
"""
	Interface de gestion des services générale
	proposer par le système coté client
"""
from Import_lay import *

from Prog.general.Prog import TEXT as TEXT2

from Prog.Services.Service_surf import Services_lay

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
		self.Surface_col = APP_COL

	def add_service_F(self):
		size = self.service_F_size
		pos = self.service_F_pos
		col = self.service_F_col
		service_F = Layout(size,col,pos,self)
		service_F.Set_overflow()
		service_F.Set_box_shadow(10,AFF_COL)
		X_dep = 3
		X = 0
		Y = self.S_text_Y
		for i in self.Service_L:
			service_F.add_button(i,self.S_text_size,
				(X,Y),Info = i,font_size = .9,
				text_align = 'center',
				text_color = TEXT_COL2,
				bg_color = self.S_text_bg_color)
			X += self.S_text_size[0]+X_dep
		
		self.Set_cont_obj(service_F)

	def add_Surface(self):
		self.Services_size = self.Surface_size
		self.Services_pos = self.Surface_pos
		self.Services_col = self.Surface_col

		Surface = Ser_S(self)
		#Surface.Info_set(self.Serv)
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


class Ser_S(Services_lay):
	def __init__(self,parent):
		Services_lay.__init__(self,parent)


	def Info_set(self):
		self.Info_txt = f'Infos Générale de {self.parent.Serv}'

