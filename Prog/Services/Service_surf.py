#Coding:utf-8
"""
	Module de définition de la surface de gestion des
	services
"""
from Import_lay import *

class Services_lay(Layout):
	def __init__(self,parent):
		size = parent.Services_size
		pos = parent.Services_pos
		col = parent.Services_col

		Layout.__init__(self,size,col,pos,parent)


		self.Info_service_size = 30,96
		self.Info_service_pos = 1.01,2
		self.Info_service_col = MAIN_COL

		self.details_size = 68.99,1
		self.details_pos = 31.01,0
		self.details_col = self.Get_bg_color()
		self.add_all()


	def Foreign_surf(self):
		self.Add_info_service()
		self.Add_details()

	def Add_info_service(self):
		size = self.Info_service_size
		col = self.Info_service_col
		pos = self.Info_service_pos
		L = Layout(size,col,pos,self)
		L.add_Text("Information général sur le service",
			(1,30),(0,30),font_size = 2,
			text_color = TEXT_COL3,
			text_align = 'center')
		self.Set_cont_obj(L)

	def Add_details(self):
		size = self.details_size
		col = self.details_col
		pos = self.details_pos
		L = Layout(size,col,pos,self)
		L.add_Text("Listes des sous catégories",
			(1,30),(0,30),font_size = 2,
			text_color = TEXT_COL3,
			text_align = 'center')
		self.Set_cont_obj(L)

