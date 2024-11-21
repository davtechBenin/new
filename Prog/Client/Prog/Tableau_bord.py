#Coding:utf-8
"""
	Interface de tableau de bord du client
"""
from Import_lay import *

class Dashbord(Layout):
	def __init__(self,parent):
		size = parent.Surf_size
		pos = parent.Surf_pos
		col = parent.Surf_col

		Layout.__init__(self,size,col,pos,parent)

		self.Set_size_and_pos()

		self.add_all()

	def Foreign_surf(self):
		self.add_panier()
		self.add_solde()
		self.add_messages()
		self.add_commande()
		self.add_historique()

	def Set_size_and_pos(self):
		int_w = 3
		int_h = 5
		pw,ph = self.panier_size = 68,34
		px,py = self.panier_pos = int_w,int_h
		self.panier_col = MAIN_COL

		sw,sh = self.solde_size = 100-pw-px-(int_w*2),24
		sx,sy = self.solde_pos = pw+px+int_w,py
		self.solde_col = MAIN_COL
		
		mw,mh = self.messages_size = sw,100-sh-(int_h*3)
		mx,my = self.messages_pos = sx,sh+int_h*2
		self.messages_col = MAIN_COL
		
		cw,ch = self.commande_size = (pw-int_w)/2,100-ph-int_h*3
		cx,cy = self.commande_pos = px,ph+int_h*2
		self.commande_col = MAIN_COL
		
		hw,hh = self.historique_size = cw,ch
		hx,hy = self.historique_pos = cx+cw+int_w,cy
		self.historique_col = MAIN_COL

	def add_panier(self):
		size = self.panier_size
		pos = self.panier_pos
		col = self.panier_col
		panier = Layout(size,col,pos,self)

		panier.add_Text("panier",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(panier)

	def add_solde(self):
		size = self.solde_size
		pos = self.solde_pos
		col = self.solde_col
		solde = Layout(size,col,pos,self)

		solde.add_Text("solde",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(solde)

	def add_messages(self):
		size = self.messages_size
		pos = self.messages_pos
		col = self.messages_col
		messages = Layout(size,col,pos,self)

		messages.add_Text("messages",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(messages)

	def add_commande(self):
		size = self.commande_size
		pos = self.commande_pos
		col = self.commande_col
		commande = Layout(size,col,pos,self)

		commande.add_Text("commande",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(commande)

	def add_historique(self):
		size = self.historique_size
		pos = self.historique_pos
		col = self.historique_col
		historique = Layout(size,col,pos,self)

		historique.add_Text("historique",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(historique)

		