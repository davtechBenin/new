#Coding:utf-8
"""
	Interface des favoris du client
"""
from Import_lay import *
from .Tableau_bord import Commande

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

		pw,ph = self.Liste_G_size = 35,(100-(int_h*2))
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
		self.commande_size = self.Liste_G_size
		self.commande_pos = self.Liste_G_pos
		self.commande_col = self.Liste_G_col
		Liste_G = CMD(self)
		self.Set_cont_obj(Liste_G)

	def add_D_encours(self):
		D_encours = CMD_encours(self)
		self.Set_cont_obj(D_encours)

	def add_D_rejetter(self):
		D_rejetter = CMD_rejetter(self)
		self.Set_cont_obj(D_rejetter)

	def add_demande(self):
		size = self.demande_size
		pos = self.demande_pos
		col = self.demande_col
		demande = Layout(size,col,pos,self)

		Y = 0
		S = 50,80
		pos = 0,Y
		accepter = CMD_Accepter(S,col,pos,demande)
		
		pos = S[0],Y
		satisfait = CMD_satisfait(S,col,pos,demande)
		

		demande.Set_cont_obj(accepter)
		demande.Set_cont_obj(satisfait)

		self.Set_cont_obj(demande)

class CMD(Commande):
	def __init__(self,parent):
		Commande.__init__(self,parent)
		self.part_size = 96,10
		self.add_all()

	def Foreign_surf(self):
		X = self.part_x
		Y = 7
		self.add_Text(TEXT.COMMANDE,(1,Y),(0,0),
			text_align = "center",text_color = TEXT_COL3,
			font_size = self.Txt_size)
		for cmd in self.Cont_L:
			pos = X,Y
			self.add_cmd(cmd,pos)
			Y += self.part_size[1]+4
		self.Incase()

	def add_cmd(self,cmd_dic,prt_p):
		L = Layout((1,1),self.part_col,
			(0,0),self)
		X = 0
		Y = 30
		for titre in cmd_dic:
			L.add_Text(titre,(1,Y),(X,0),
				text_color = TEXT_COL3,
				font_size = self.Txt_size,
				text_align = 'center')
			dic = cmd_dic[titre]
			
			part_w = 100/6
			for key,val in dic.items():
				S = part_w,100-Y
				L.add_Text(key,S,(X,Y),
					text_color = TEXT_COL2, 
					font_size = self.Txt_size,
					text_align = "center")
				X += part_w
				if key == 'Montant':
					val = self.format_val(val)
				L.add_Text(val,S,(X,Y),
					text_color = TEXT_COL4, 
					font_size = self.Txt_size,
					)
				X += part_w
		self.add_button(L.Run_html(),
			self.part_size,prt_p,Info = titre)

class CMD_SP(Layout):
	def __init__(self,size,col,pos,parent):
		Layout.__init__(self,size,col,pos,parent)
		"""
			Le formatage des commandes doivent
			être faite de puis le gestionnaire
			de la base de données principale
		"""
#
		
		self.part_size = 96,20
		self.part_x = 2
		self.part_col = APP_COL
		self.Set_BASE()

		#self.add_all()

	def Set_BASE(self):
		self.ident = self.MAIN_LAY.Get_ident_cookies()

	def Set_part_info(self):
		"""
			c'est ici qu'est définie le part_text
			et le part base
		"""
		pass

	def Foreign_surf(self):
		X = self.part_x
		Y = 13
		self.add_Text(self.part_text,(1,Y),(0,0),
			text_align = "center",text_color = TEXT_COL3,
			font_size = self.Txt_size)
		for cmd in self.Cont_L:
			pos = X,Y
			self.add_cmd(cmd,pos)
			Y += self.part_size[1]+8
		self.Incase()

	def Incase(self):
		if not self.Cont_L:
			T = TEXT.GET_PART_INFO(self.part_text)
			self.add_Text(T,(80,30),(10,30),
				text_color = SUCCES_COL,font_size = 1.3,
				text_align = 'center')

	def add_cmd(self,cmd_dic,prt_p):
		L = Layout((1,1),self.part_col,
			(0,0),self)
		X = 0
		Y = 30
		for titre in cmd_dic:
			L.add_Text(titre,(1,Y),(X,0),
				text_color = TEXT_COL3,
				font_size = self.Txt_size,
				text_align = 'center')
			dic = cmd_dic[titre]
			
			part_w = 100/4
			for key,val in dic.items():
				S = part_w,100-Y
				L.add_Text(key,S,(X,Y),
					text_color = TEXT_COL2, 
					font_size = self.Txt_size,
					text_align = 'center'
					)
				X += part_w
				if key == 'Montant':
					val = self.format_val(val)
				L.add_Text(val,S,(X,Y),
					text_color = TEXT_COL4, 
					font_size = self.Txt_size)
				X += part_w
		self.add_button(L.Run_html(),
			self.part_size,prt_p,Info = titre)

class CMD_encours(CMD_SP):
	def __init__(self,parent):

		size = parent.D_encours_size
		pos = parent.D_encours_pos
		col = parent.D_encours_col

		CMD_SP.__init__(self,size,col,pos,parent)

		self.Set_part_info()
		self.add_all()

	def Set_part_info(self):
		self.part_text = TEXT.ENCOURS
		CMD = Command_BB(self.ident)
		self.Cont_L = CMD.Get_cmd_lis(part = "Encours")

class CMD_rejetter(CMD_SP):
	def __init__(self,parent):
		size = parent.D_rejetter_size
		pos = parent.D_rejetter_pos
		col = parent.D_rejetter_col

		CMD_SP.__init__(self,size,col,pos,parent)

		self.Set_part_info()
		self.add_all()

	def Set_part_info(self):
		self.part_text = TEXT.REJETTER
		CMD = Command_BB(self.ident)
		self.Cont_L = CMD.Get_cmd_lis(part = "Rejetter")


class CMD_Accepter(CMD_SP):
	def __init__(self,S,col,pos,parent):
		CMD_SP.__init__(self,S,col,pos,parent)

		self.Set_part_info()
		self.add_all()

	def Set_part_info(self):
		self.part_text = TEXT.ACCEPTER
		CMD = Command_BB(self.ident)
		self.Cont_L = CMD.Get_cmd_lis(part = "Accepter")


class CMD_satisfait(CMD_SP):
	def __init__(self,S,col,pos,parent):
		CMD_SP.__init__(self,S,col,pos,parent)

		self.Set_part_info()
		self.add_all()

	def Set_part_info(self):
		self.part_text = TEXT.SATISFAIT
		CMD = Command_BB(self.ident)
		self.Cont_L = CMD.Get_cmd_lis(part = "Satisfait")

