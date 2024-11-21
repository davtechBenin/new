#Coding:utf-8
"""
	Interface des favoris du client
"""
from Import_lay import *

class Favoris(Layout):
	def __init__(self,parent):
		size = parent.Surf_size
		pos = parent.Surf_pos
		col = parent.Surf_col

		Layout.__init__(self,size,col,pos,parent)

		self.Set_size_and_pos()

		self.add_all()

	def Foreign_surf(self):
		self.add_service_F()
		self.add_Activite_R()
		self.add_boutique_F()
		self.add_commande()

	def Set_size_and_pos(self):
		int_w = 3
		int_h = 5

		pw,ph = self.service_F_size = 27,(100-(int_h*2))
		px,py = self.service_F_pos = int_w,int_h
		self.service_F_col = MAIN_COL

		sw,sh = self.Activite_R_size = 40,(100-(int_h*3))/2
		sx,sy = self.Activite_R_pos = pw + int_w*2,int_h
		self.Activite_R_col = MAIN_COL

		mw,mh = self.boutique_F_size = 100-pw-sw-(int_w*4),ph-(int_h*2)
		mx,my = self.boutique_F_pos = pw+sw+(int_w*3),py+int_h
		self.boutique_F_col = MAIN_COL
		
		cw,ch = self.commande_size = sw,sh
		cx,cy = self.commande_pos = sx,sh+int_h*2
		self.commande_col = MAIN_COL
		

	def add_service_F(self):
		size = self.service_F_size
		pos = self.service_F_pos
		col = self.service_F_col
		service_F = Layout(size,col,pos,self)

		service_F.add_Text("service_F",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(service_F)

	def add_Activite_R(self):
		size = self.Activite_R_size
		pos = self.Activite_R_pos
		col = self.Activite_R_col
		Activite_R = Layout(size,col,pos,self)

		Activite_R.add_Text("Activite_R",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(Activite_R)

	def add_boutique_F(self):
		size = self.boutique_F_size
		pos = self.boutique_F_pos
		col = self.boutique_F_col
		boutique_F = Layout(size,col,pos,self)

		boutique_F.add_Text("boutique_F",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(boutique_F)

	def add_commande(self):
		size = self.commande_size
		pos = self.commande_pos
		col = self.commande_col
		commande = Layout(size,col,pos,self)

		commande.add_Text("commande",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(commande)

