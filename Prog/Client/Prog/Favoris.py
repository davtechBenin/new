#Coding:utf-8
"""
	Interface des favoris du client
"""
from Import_lay import *

from .Tableau_bord import Commande,Historique

class Favoris(Layout):
	def __init__(self,parent):
		size = parent.Surf_size
		pos = parent.Surf_pos
		col = parent.Surf_col

		Layout.__init__(self,size,col,pos,parent)
		self.Set_size_and_pos()

		self.Date = TODAY().date__

		self.add_all()

	def Set_BASE(self):
		ident = self.MAIN_LAY.Get_ident_cookies()
		self.Base = Favoris_BB(ident)

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
		service_F = Service_F(self)
		self.Set_cont_obj(service_F)

	def add_Activite_R(self):
		Activite_R = Act_R(self)
		self.Set_cont_obj(Activite_R)

	def add_boutique_F(self):
		boutique_F = Bout_F(self)
		self.Set_cont_obj(boutique_F)

	def add_commande(self):
		commande = Commande(self)

		
		self.Set_cont_obj(commande)

class Service_F(Layout):
	def __init__(self,parent):
		size = parent.service_F_size
		pos = parent.service_F_pos
		col = parent.service_F_col
		Layout.__init__(self,size,col,pos,parent)

		Base = self.parent.Base

		self.Service_base = Base.Get_service_favoris()
		self.add_all()

	def Foreign_surf(self):
		YYY = 5
		self.add_Text(TEXT.SF_TEXT,(1,YYY),(0,0),
			font_size = self.Txt_size,text_color = TEXT_COL3,
			text_align = "center",
			underline = True)
		S = Layout((94,100-YYY),AFF_COL,(5,YYY),self)
		Y = 0
		TW = 30
		NW = 30
		VW = 20
		H = 7
		YY = 5
		for Cat in self.Service_base:
			S.add_Text(Cat,(90,H),(0,Y),text_color = TEXT_COL2,
				font_size = self.Txt_size)
			Y += H+2
			Cat_Base = self.Service_base[Cat]
			col = S.Get_bg_color()
			
			for Ser,val in Cat_Base.items():
				But = Layout((98,100),col,(.01,0),S)
				But.Set_box_shadow(10,BUT_COL1)
				But.add_Text(Ser,(TW,H),(5,0),
					text_color = TEXT_COL3,
					font_size = self.Txt_size,
					text_align = 'center')
				X = 5 + TW
				for key,v in val.items():
					W = NW
					But.add_Text(key,(W,H),(X,0),
						text_color = TEXT_COL4,
						font_size = self.Txt_size,
						text_align = 'right')
					X += W
					But.add_Text(v,(VW,H),(X,0),
						text_color = TEXT_COL3,
						font_size = self.Txt_size,
						text_align = "center")
					X += VW
				S.add_button(But.Run_html(),(1,H),(0,Y),
					Info = Ser)
				Y += H + 2
		self.Set_cont_obj(S)
		self.Incase()

	def Incase(self):
		if not self.Service_base:
			self.add_Text(TEXT.NO_SF_MES,(80,30),(10,30),
				text_color = SUCCES_COL,font_size = 2,
				text_align = 'center')

class Act_R(Historique):
	def __init__(self,parent):
		parent.historique_size = parent.Activite_R_size
		parent.historique_pos = parent.Activite_R_pos
		parent.historique_col = parent.Activite_R_col
		Historique.__init__(self,parent)

class Bout_F(Layout):
	def __init__(self,parent):
		size = parent.boutique_F_size
		pos = parent.boutique_F_pos
		col = parent.boutique_F_col
		Layout.__init__(self,size,col,pos,parent)

		Base = self.parent.Base

		self.Service_base = Base.Get_boutique_favoris()
		
		self.add_all()

	def Foreign_surf(self):
		YYY = 5
		self.add_Text(TEXT.SF_TEXT,(1,YYY),(0,0),
			font_size = self.Txt_size,text_color = TEXT_COL3,
			text_align = "center",
			underline = True)
		S = Layout((94,100-YYY),AFF_COL,(5,YYY),self)
		Y = 0
		TW = 50
		NW = 30
		VW = 15
		H = 8
		YY = 5
		for Cat in self.Service_base:
			S.add_Text(Cat,(90,H),(0,Y),text_color = TEXT_COL2,
				font_size = self.Txt_size)
			Y += H+2
			Cat_Base = self.Service_base[Cat]
			col = S.Get_bg_color()
			
			for Ser,val in Cat_Base.items():
				But = Layout((98,100),col,(.01,0),S)
				But.Set_box_shadow(10,BUT_COL1)
				But.add_Text(Ser,(TW,H),(5,0),
					text_color = TEXT_COL3,
					font_size = self.Txt_size)
				X = 5 + TW
				for key,v in val.items():
					W = NW
					But.add_Text(key,(W,H),(X,0),
						text_color = TEXT_COL4,
						font_size = self.Txt_size)
					X += W
					But.add_Text(v,(VW,H),(X,0),
						text_color = TEXT_COL3,
						font_size = self.Txt_size)
					X += VW
				S.add_button(But.Run_html(),(1,H),(0,Y),
					Info = Ser)
				Y += H + 2
		self.Set_cont_obj(S)
		self.Incase()

	def Incase(self):
		if not self.Service_base:
			self.add_Text(TEXT.NO_BF_MES,(80,30),(10,30),
				text_color = SUCCES_COL,font_size = 2,
				text_align = 'center')


