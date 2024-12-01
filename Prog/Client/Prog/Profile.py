#Coding:utf-8
"""
	Interface de gestion des profiles utilisateurs
"""
from Import_lay import *

class Profile(Layout):
	def __init__(self,parent):
		size = parent.Surf_size
		pos = parent.Surf_pos
		col = parent.Surf_col

		Layout.__init__(self,size,col,pos,parent)
		self.Set_size_and_pos()

		self.Date = TODAY().date__
		self.CLT_BASE = Client()
		self.GENE_B = General()
		self.Modif = str()
		self.Modif_dic = dict()
		self.Error_mes = str()

		self.add_all()

	def Foreign_surf(self):
		self.Get_Base()
		self.add_Perso()
		self.add_resid()
		self.add_connexion()
		self.add_conta()
		if self.Modif:
			self.Modif_surf()
			
	def Set_size_and_pos(self):
		int_w = 3
		int_h = 5

		pw,ph = self.part_size = ((100-(int_w*3))/2,
			(100-(int_h*3))/2)

		self.perso_pos = int_w,int_h

		rx,ry = self.resid_pos = int_w*2+pw,int_h

		cx,cy = self.conta_pos = int_w,int_h*2+ph

		self.conne_pos = rx,cy

		self.part_col = AFF_COL

	def Get_Base(self):
		ident = self.MAIN_LAY.Get_ident_cookies()
		Base = self.CLT_BASE.Get_pers_info(ident)
		self.ident_dic = dict()
		self.con_dic = dict()
		self.cont_dic = dict()
		self.resi_dic = dict()
		for key,val in Base.items():
			if key in ("Nom","Prénom",
		"Date de naissance",'Genre'):
				self.ident_dic[key] = val
			elif key in ("Pays",
		"Ville","Province",'Rue N°'):
				self.resi_dic[key] = val
			elif key in ("Téléphone","Whatsapp"):
				self.cont_dic[key] = val
			elif key in ("Email",
		"Mot de pass","Répéter le mot de pass"):
				self.con_dic[key] = val

		self.INFO_DIC = {
			TEXT.INFO_Perso : self.ident_dic,
			TEXT.INFO_Resid : self.resi_dic,
			TEXT.INFO_CON : self.con_dic,
			TEXT.INFO_CONT : self.cont_dic,
		}

	def add_Perso(self):
		Perso = INF_P(self.perso_pos,self,
			self.ident_dic,TEXT.INFO_Perso)
		self.Set_cont_obj(Perso)

	def add_resid(self):
		resid = INF_P(self.resid_pos,self,
			self.resi_dic,TEXT.INFO_Resid)
		self.Set_cont_obj(resid)

	def add_connexion(self):
		connexion = INF_P(self.conne_pos,self,
			self.con_dic,TEXT.INFO_CON)
		self.Set_cont_obj(connexion)

	def add_conta(self):
		conta = INF_P(self.conta_pos,self,
			self.cont_dic,TEXT.INFO_CONT)
		self.Set_cont_obj(conta)

	def Modif_surf(self):
		PART = Modif_form(self,self.Modif,self.Modif_dic,
			self.Error_mes)
		self.Add_priority_lay(PART)

	def Ret_handler(self,ret):
		"""
			Reste à définir les parties de gestion 
			de chaque services
		"""
		ident = self.MAIN_LAY.Get_ident_cookies()
		if '--' in ret:
			part = ret.split("--")[1]
			part_dic = self.INFO_DIC[part]
			if not part_dic:
				part_dic = {
					'votre email':self.CLT_BASE.Get_email(ident),
					"Ancien mot de pass":str(),
					'Nouveau mot de pass':str(),
					'Répéter mot de pass':str()
				}
			self.Modif = part
			self.Modif_dic = part_dic
			self.add_all()

	def Valider_form(self):
		ident = self.MAIN_LAY.Get_ident_cookies()
		if 'votre email' in self.Form:
			email = self.Form.get("votre email")
			MP = self.Form.get('Ancien mot de pass')
			M = self.CLT_BASE.Get_password(ident)
			if M == MP:
				P1 = self.Form.get("Nouveau mot de pass")
				P2 = self.Form.get("Répéter mot de pass")
				if P1 == P2:
					self.GENE_B.Set_this_client_info(email,P2)
				else:
					self.Error_mes = "Password invalide!"
					ret = f'M--{TEXT.INFO_CON}'
					self.Ret_handler(ret)
			else:
				self.Error_mes = "Password invalide!"
				ret = f'M--{TEXT.INFO_CON}'
				self.Ret_handler(ret)
		else:
			self.CLT_BASE.Save_pers_info(ident,self.Form)


	def Execution(self,request):
		ret = request.get('request')
		if ret:
			self.Ret_handler(ret)
		else:
			self.Form = request.get('form')
			self.Form.pop("Modifier")
			self.Valider_form()
			self.add_all()

class INF_P(Layout):
	def __init__(self,pos,parent,dic,info):
		size = parent.part_size
		col = parent.part_col
		Layout.__init__(self,size,col,pos,parent)
		self.Set_box_shadow(10,BUT_COL1,
			rayon_detalement = 5)
		self.Set_border_radius(1)

		self.Base = dic

		self.info = info

		self.add_all()


	def Foreign_surf(self):
		H = 90/(len(self.Base)+2)
		Y = 10
		dec = H/(len(self.Base)+2)
		self.add_Text(self.info,(1,Y),(0,0),
			text_align = 'center',text_color = TEXT_COL3,
			underline = True,font_size = self.Txt_size,
			)
		Y += dec
		for key,val in self.Base.items():
			S = 30,H
			x = 20
			self.add_Text(key,S,(x,Y),text_align = 'left',
				text_color = TEXT_COL2,font_size = self.Txt_size)
			x += S[0]
			self.add_Text(val,S,(x,Y),text_align = 'left',
				text_color = TEXT_COL4,
				font_size = self.Txt_size+.1)
			Y += H+dec

		but_H = 16
		self.add_button('Modifier',(70,but_H),(15,Y),
			Info = 'M--'+self.info,text_align = 'center',
			text_color = TEXT_COL3,font_size = self.Txt_size+.2,
			radius = 3,shadow = 10,shadow_color = BUT_COL1)

class Modif_form(Layout):
	def __init__(self,parent,modif_part,info_dic,Error_mes):
		self.H = 100/(len(info_dic)+5)
		self.Dec = 5
		size = 40,10*(len(info_dic)+2)
		pos = 30,(100-size[1])/2
		col = AFF_COL
		Layout.__init__(self,size,col,pos,parent)
		self.Set_border_radius(2)
		self.Set_box_shadow(10,BUT_COL1)
		self.Error_mes = Error_mes

		url = urllib.parse.urlencode({'request':f'M**{modif_part}'})
		url = "?"+url
		self.F = form.form('Modifier',action = "/")
		self.F.Set_bg_color(AFF_COL)
		self.F.Set_border_radius(2)
		self.F.Set_box_shadow(10,BUT_COL1)
		self.info_dic = info_dic
		self.add_all()

	def Foreign_surf(self):
		W = 50
		lab_css = Css()
		lab_css.Set_size(W,self.H)
		lab_css.Set_text_color(TEXT_COL2)
		lab_css.Set_margin_left(2)
		#lab_css.Set_text_align("")

		Inp_css = Css()
		Inp_css.Set_size(W,self.H)
		Inp_css.Set_border_radius(0)
		Inp_css.Set_border(0)
		Inp_css.Set_box_shadow(5,BUT_COL1)
		Inp_css.Set_bg_color(AFF_COL)
		Inp_css.Set_text_color(TEXT_COL3)

		But_css = Css()
		But_css.Set_size(70,self.H)
		But_css.Set_text_color(TEXT_COL4)
		But_css.Set_border_radius(2)
		But_css.Set_border(0)
		But_css.Set_box_shadow(10,BUT_COL1)
		But_css.Set_bg_color(AFF_COL)
		
		Y = self.H
		for key,val in self.info_dic.items():
			lab_css.Set_position((0,Y+3))
			Inp_css.Set_position((W-5,Y))
			if 'mot de pass' in key:
				self.F.Set_password_input(key,
					value = val,
					inp_style = Inp_css,
					lab_style = lab_css)
			else:
				self.F.Set_text_input(key,value = val,
					inp_style = Inp_css,
					lab_style = lab_css)
			Y += self.H + self.Dec

		But_css.Set_position((15,Y+self.Dec))
		self.F.End_form(submit_name = 'Valider',
			Submit_style = But_css)

		self.Set_cont_obj(self.F)

		self.add_Text(self.Error_mes,(.8,3),
			(10,90),font_size = self.Txt_size,
			text_color = ERROR_COL,text_align = 'center')

