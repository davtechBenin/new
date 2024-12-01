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

		self.Clt_Base = Client()

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
		self.messages_col = APP_COL
		
		cw,ch = self.commande_size = (pw-int_w)/2,100-ph-int_h*3
		cx,cy = self.commande_pos = px,ph+int_h*2
		self.commande_col = MAIN_COL
		
		hw,hh = self.historique_size = cw,ch
		hx,hy = self.historique_pos = cx+cw+int_w,cy
		self.historique_col = MAIN_COL

	def add_panier(self):
		panier = Panier(self)
		self.Set_cont_obj(panier)

	def add_solde(self):
		size = self.solde_size
		pos = self.solde_pos
		col = self.solde_col
		solde = Layout(size,col,pos,self)

		ident = self.MAIN_LAY.Get_ident_cookies()
		S = self.Clt_Base.get_solde(ident)

		Cmd = self.Clt_Base.get_cmd(ident)

		info = [("Solde disponible",S),
		("Commande en cours",Cmd)]

		txt_col = TEXT_COL2
		val_col = TEXT_COL4
		part_size = 50,30
		X = 0
		Y = 0
		for tup in info:
			txt,val = tup
			pos = (X,Y)
			val = self.format_val(val)
			solde.add_Text(f"{txt}:",part_size,pos,
				font_size = self.Txt_size,
				text_color = txt_col,
				text_align = 'right')
			pos = part_size[0],Y
			solde.add_Text(val,part_size,pos,
				font_size = self.Txt_size,
				text_color = val_col,
				text_align = 'center')
			Y += part_size[1]

		part_S = (40,30)
		X = 6.6
		but_L = ("Recharger","Historique")
		for but in but_L:
			solde.add_button(but,part_S,(X,Y),
				font_size = self.Txt_size,
				text_color = TEXT_COL3,
				bg_color = BUT_COL1,
				text_align = 'center')
			X += part_S[0]+6.6
		self.Set_cont_obj(solde)

	def add_messages(self):
		messages = Messages(self)
		self.Set_cont_obj(messages)

	def add_commande(self):
		commande = Commande(self)
		self.Set_cont_obj(commande)

	def add_historique(self):
		historique = Historique(self)
		self.Set_cont_obj(historique)

	def Execution(self,request):
		ret = request.get('request')
		if ret:
			self.Ret_handler(ret)
		else:
			form = request.get('form')
			self.Form_handler(form)
		self.add_all()
			
	def Form_handler(self,form):
		ident = self.MAIN_LAY.Get_ident_cookies()
		if 'Send_mes' in form:
			mes = form.get("message")
			self.Clt_Base.send_sms(ident,mes)

class Panier(Layout):
	def __init__(self,parent):
		size = parent.panier_size
		pos = parent.panier_pos
		col = parent.panier_col
		Layout.__init__(self,size,col,pos,parent)

		self.Panier_base = Panier_BB

		self.Set_size_and_pos()

		self.Corp = Layout(self.corp_size,self.corp_col,
			self.corp_pos,self)
		self.Corp.Set_overflow()
		self.add_all()

	def Foreign_surf(self):
		ident = self.MAIN_LAY.Get_ident_cookies()
		self.Panier_base = self.Panier_base(ident)
		dic = self.Panier_base.Get_All_data()
		self.CAT_DIC = dic

		self.montant = self.Panier_base.Get_prix()
		self.all_cat = len(dic)
		self.all_art = int()
		for cat in dic:
			self.all_art += len(dic[cat])
		self.Set_entete()
		self.Add_Corp()

	def Set_entete(self):
		"""
			Les valeurs sont à prendre depuis la base
			de données
		"""
		pan_txt = TEXT.PANIER_TEXT
		val1 = self.montant

		cat_txt = TEXT.CATEGORIE_TEXT
		val2 = self.all_cat

		art_txt = TEXT.ARTICLE_TEXT
		val3 = self.all_art

		txt_list = pan_txt,cat_txt,art_txt
		val_list = val1,val2,val3
		txt_col = TEXT_COL2
		val_col = TEXT_COL3
		dec = 3

		Panier = Layout(self.ent_size,self.ent_col,
			self.ent_pos,self)
		part_size = int(100/6),1
		part_y = 0
		txt_x_dec = part_size[0]*2
		X = 0+dec
		for txt in txt_list:
			pos = X,part_y
			Panier.add_Text(txt,part_size,pos,
				text_color = txt_col,
				bg_color = self.Get_bg_color())
			X += txt_x_dec
		X = part_size[0]+dec
		for val in val_list:
			pos = X,part_y
			val = self.format_val(val)
			Panier.add_Text(val,part_size,pos,
				text_color = val_col,
				bg_color = self.Get_bg_color())
			X += txt_x_dec

		self.Set_cont_obj(Panier)

	def Set_Categorie(self,Cat_dic,cart_pos):
		Categorie = Layout(self.cart_size,self.cart_col,
			cart_pos,self.Corp)
		Categorie.Set_overflow()
		Categorie.Set_box_shadow(10,TEXT_COL1)
		Categorie.Set_border_top_right_radius(1)
		Categorie.Set_border_bottom_left_radius(1)
		#Categorie.Set_bottom_border(2,TEXT_COL3)
		for cat,val in Cat_dic.items():
			Categorie.add_Text(cat,(1,20),(0,0),
				font_size = self.Txt_size,
				text_color = TEXT_COL3,text_align = 'center')
			part_x = self.cat_part_x
			part_y = 21
			for s_cat in val:
				thi_pos = part_x,part_y
				dic = val[s_cat]
				S_L = Layout((1,1),
					APP_COL,(0,0),Categorie)
				S_L.add_Text(s_cat,(1,50),(0,0),
					text_color = TEXT_COL2)
				X = 0
				Y = 50
				W = 100/6
				H = 20
				S = W,H
				for key,V in dic.items():
					key = str(key)
					V = self.format_val(V)
					pos = X,Y
					S_L.add_Text(key,S,pos,
						text_color = TEXT_COL4,
						font_size = self.Txt_size-.1)
					X += W
					pos = X,Y
					S_L.add_Text(V,S,pos,
						text_color = TEXT_COL3,
						font_size = self.Txt_size-.1)
					X += W
				Categorie.add_button(S_L.Run_html(),
					self.cat_part_size,thi_pos,Info = s_cat)
				part_y += self.cat_part_size[1]+5
		self.Corp.Set_cont_obj(Categorie)

	def Add_Corp(self):
		Categories = self.CAT_DIC

		X = self.cart_x_dep
		Y = self.cart_y
		for cat_dic in Categories:
			self.Set_Categorie(cat_dic,(X,Y))
			X += self.cart_size[0]+5
		if not Categories:
			self.Corp.add_Text("Pas d'articles",
				(80,30),(10,30),text_align = 'center',
				font_size = self.Txt_size+.4,
				text_color = SUCCES_COL)
		self.Set_cont_obj(self.Corp)

	def Set_size_and_pos(self):
		col = self.Get_bg_color()
		self.ent_size = 1,20
		self.ent_pos = 0,0
		self.ent_col = col

		self.corp_size = 1,100-self.ent_size[1]-2
		self.corp_pos = 0,self.ent_size[1]+1
		self.corp_col = col

		self.cart_size = 40,96
		self.cart_x_dep = 1.2
		self.cart_y = 2
		self.cart_col = FRONT_COL

		self.cat_part_size = .9,40
		self.cat_part_x = .05

class Commande(Layout):
	def __init__(self,parent):
		size = parent.commande_size
		pos = parent.commande_pos
		col = parent.commande_col
		Layout.__init__(self,size,col,pos,parent)
		self.Set_box_shadow(10,TEXT_COL2)
		self.Set_border_radius(1)

		self.part_size = 96,20
		self.part_x = 2
		self.part_col = APP_COL

		self.add_all()

	def Set_BASE(self):
		ident = self.MAIN_LAY.Get_ident_cookies()
		self.CMD_B = Command_BB(ident)

		self.Cont_L = self.CMD_B.Get_cmd_lis()

	def Foreign_surf(self):
		X = self.part_x
		Y = 10
		self.add_Text(TEXT.COMMANDE,(1,Y),(0,0),
			text_align = "center",text_color = TEXT_COL3,
			font_size = self.Txt_size)
		for cmd in self.Cont_L:
			pos = X,Y
			self.add_cmd(cmd,pos)
			Y += self.part_size[1]+8
		self.Incase()

	def Incase(self):
		if not self.Cont_L:
			self.add_Text(TEXT.NO_C_MES,(80,30),(10,30),
				text_color = SUCCES_COL,font_size = 2,
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
			
			part_w = 100/6
			for key,val in dic.items():
				S = part_w,100-Y
				L.add_Text(key,S,(X,Y),
					text_color = TEXT_COL2, 
					font_size = self.Txt_size,
					)
				X += part_w
				if key == 'Montant':
					val = self.format_val(val)
				L.add_Text(val,S,(X,Y),
					text_color = TEXT_COL4, 
					font_size = self.Txt_size,
					text_align = 'center')
				X += part_w
		self.add_button(L.Run_html(),
			self.part_size,prt_p,Info = titre)

class Historique(Layout):
	def __init__(self,parent):
		"""
			Il s'agit de l'historique des activités
			donc activité récentes. C'est le même
			objet qui sera utiliser dans le cas des
			activités recente aussi
		"""
		size = parent.historique_size
		pos = parent.historique_pos
		col = parent.historique_col
		Layout.__init__(self,size,col,pos,parent)
		self.Set_box_shadow(20,TEXT_COL1)
		self.Set_border_top_right_radius(1)
		self.Set_border_bottom_left_radius(1)

		self.part_size = 96,20
		self.part_x = 2
		self.part_col = APP_COL

		self.add_all()

	def Set_BASE(self):
		ident = self.MAIN_LAY.Get_ident_cookies()
		B = Activite_BB(ident)
		self.Cont_L = B.Get_activite_recente()

	def Incase(self):
		if not self.Cont_L:
			self.add_Text(TEXT.NO_H_MES,(80,30),(10,30),
				text_color = SUCCES_COL,font_size = 2,
				text_align = 'center')

	def Foreign_surf(self):
		X = self.part_x
		Y = 10
		self.add_Text(TEXT.HISTORIQUE,(1,Y),(0,0),
			text_align = "center",text_color = TEXT_COL3,
			font_size = self.Txt_size)
		for his in self.Cont_L:
			pos = X,Y
			self.add_cmd(his,pos)
			Y += self.part_size[1]+8
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
			
			part_w = 100/4
			for key,val in dic.items():
				S = part_w,100-Y
				L.add_Text(key,S,(X,Y),
					text_color = TEXT_COL2, 
					font_size = self.Txt_size,
					text_align = 'right')
				X += part_w
				if key == 'Montant':
					val = self.format_val(val)
				L.add_Text(val,S,(X,Y),
					text_color = TEXT_COL4, 
					font_size = self.Txt_size,
					text_align = 'center')
				X += part_w
		self.add_button(L.Run_html(),
			self.part_size,prt_p,Info = titre)

class Messages(Layout):
	def __init__(self,parent):
		"""
			Il s'agit de l'historique des activités
			donc activité récentes. C'est le même
			objet qui sera utiliser dans le cas des
			activités recente aussi
		"""
		size = parent.messages_size
		pos = parent.messages_pos
		col = parent.messages_col
		Layout.__init__(self,size,col,pos,parent)
		self.Set_box_shadow(20,BUT_COL1)
		self.Set_border_radius(5,'px')

		self.Aff_Lay = Layout((1,75),col,(0,10),self)
		self.Aff_Lay.Set_overflow()

		self.part_size = 96,20
		self.part_x = 2
		self.part_col = APP_COL

		self.add_all()

	def Set_BASE(self):
		ident = self.MAIN_LAY.Get_ident_cookies()
		base = self.parent.Clt_Base
		self.Cont_L = base.get_sms(ident)

	def Foreign_surf(self):
		X = self.part_x
		Y = 0
		self.add_Text(TEXT.MESSAGE,(1,Y),(0,0),
			text_align = "center",text_color = TEXT_COL3,
			font_size = self.Txt_size)
		for his in self.Cont_L:
			pos = X,Y
			self.add_cmd(his,pos)
			Y += self.part_size[1]+8

		self.Set_cont_obj(self.Aff_Lay)
		self.add_mes_inp()

	def add_cmd(self,cmd_dic,prt_p):
		L = Layout((1,1),self.part_col,
			(0,0),self)
		X = 0
		Y = 30
		for typ in cmd_dic:
			mes = cmd_dic[typ]["Message"]
			P = bl.p(mes,size = None,pos = None)

			P.Set_width(.75)
			P.Set_bg_color(AFF_COL)
			P.Set_box_shadow(20,BUT_COL1)
			P.Set_font_size(self.Txt_size)
			if typ == "Receive":
				P.Set_border_top_right_radius(1)
				P.Set_border_bottom_right_radius(1)
				P.Set_border_bottom_left_radius(1)
				P.Set_text_color(TEXT_COL2)
				P.Set_margin_left(5,'%')
				P.Set_text_align('left')
				P.Set_padding_left(5,'%')
			elif typ == "Send":
				P.Set_border_top_left_radius(1)
				P.Set_border_bottom_right_radius(1)
				P.Set_border_bottom_left_radius(1)
				P.Set_text_color(TEXT_COL4)
				P.Set_margin_left(20,'%')
				P.Set_text_align('right')
				P.Set_padding_right(5,'%')
			
			
			P.height = 100
			P.pos = (0,0)


			self.Aff_Lay.Set_cont_obj(P)

	def add_mes_inp(self):
		size = 100,15
		pos = 0,85
		col = self.Get_bg_color()
		L = Layout(size,col,pos,self)
		L.Set_box_shadow(5,APP_COL)

		url = urllib.parse.urlencode({'request':'Send message'})
		url = "/?"+url
		F = form.form("Send_mes",action = url,
			bg_color = APP_COL)


		inp_style = Css()
		inp_style.Set_size(.7,.8)
		inp_style.Set_position((3,.1))
		inp_style.Set_bg_color(APP_COL)
		inp_style.Set_border_radius(1)
		inp_style.Set_border(0)
		inp_style.Set_box_shadow(10,BUT_COL1)
		inp_style.Set_text_color(TEXT_COL2)
		F.Set_input('text',"message",
			inp_style = inp_style,lab = False)
		but_style = Css()
		but_style.Set_size(.22,.8)
		but_style.Set_position((.75,.1))
		but_style.Set_text_color(TEXT_COL3)
		but_style.Set_border(0)
		but_style.Set_border_radius(5)
		but_style.Set_bg_color(BUT_COL1)
		but_style.Set_box_shadow(1,TEXT_COL3)
		F.End_form(submit_name = "Send",
			Submit_style = but_style)

		L.Set_cont_obj(F)

		self.Set_cont_obj(L)

	def Execution(self,request):
		print(request)

