#Coding:utf-8
"""
	Interface des favoris du client
"""
from Import_lay import *

class Demandes(Layout):
	def __init__(self,parent):
		size = parent.Surf_size
		pos = parent.Surf_pos
		col = parent.Surf_col

		Layout.__init__(self,size,col,pos,parent)

		self.Set_size_and_pos()

		self.add_all()

	def Foreign_surf(self):
		self.add_Liste_G()
		self.add_D_encours()
		self.add_D_rejetter()
		self.add_demande()

	def Set_size_and_pos(self):
		int_w = 3
		int_h = 5

		pw,ph = self.Liste_G_size = 30,(100-(int_h*2))
		px,py = self.Liste_G_pos = int_w,int_h
		self.Liste_G_col = MAIN_COL

		WWW = ((100-int_w*4)-pw)/2

		sw,sh = self.D_encours_size = WWW,(100-(int_h*3))/2
		sx,sy = self.D_encours_pos = pw + int_w*2,int_h
		self.D_encours_col = MAIN_COL

		mw,mh = self.D_rejetter_size = sw,sh
		mx,my = self.D_rejetter_pos = sx+sw+int_w,int_h
		self.D_rejetter_col = MAIN_COL
		
		cw,ch = self.demande_size = sw*2+int_w,sh
		cx,cy = self.demande_pos = sx ,sh+int_h*2
		self.demande_col = MAIN_COL
		

	def add_Liste_G(self):
		size = self.Liste_G_size
		pos = self.Liste_G_pos
		col = self.Liste_G_col
		Liste_G = Layout(size,col,pos,self)

		Liste_G.add_Text("Liste_G",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(Liste_G)

	def add_D_encours(self):
		size = self.D_encours_size
		pos = self.D_encours_pos
		col = self.D_encours_col
		D_encours = Layout(size,col,pos,self)

		D_encours.add_Text("D_encours",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(D_encours)

	def add_D_rejetter(self):
		size = self.D_rejetter_size
		pos = self.D_rejetter_pos
		col = self.D_rejetter_col
		D_rejetter = Layout(size,col,pos,self)

		D_rejetter.add_Text("D_rejetter",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(D_rejetter)

	def add_demande(self):
		size = self.demande_size
		pos = self.demande_pos
		col = self.demande_col
		demande = Layout(size,col,pos,self)

		S = 50,80
		pos = 0,15
		accepter = Layout(S,col,pos,demande)
		accepter.add_Text("accepter",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")

		pos = S[0],15
		satisfait = Layout(S,col,pos,demande)
		satisfait.add_Text("satisfait",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")

		demande.add_Text("demandes",(1,10),(0,0),
			text_color = TEXT_COL1,font_size = 1,
			text_align = "center")
		demande.Set_cont_obj(accepter)
		demande.Set_cont_obj(satisfait)

		self.Set_cont_obj(demande)

