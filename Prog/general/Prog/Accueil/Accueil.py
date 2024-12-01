#Coding:utf-8

from lib.Pyweb.Layout import Layout
from lib.Pyweb.core import balises as bl
from lib.Pyweb.core import form
Css = bl.style
from .. import TEXT
from color import *

import urllib

class Main(Layout):
	def __init__(self,parent):
		size = 1,1
		bg_color = APP_COL
		pos = (0,0)
		Layout.__init__(self,size,bg_color,pos,parent)

		self.present_size = .7,.6
		self.present_pos = .025,.05
		self.present_col = OPTION_COL

		self.Connexion_size = .225,.55
		self.Connexion_pos = .75,.075
		self.Connexion_col = AFF_COL

		self.Services_size = .7,.25
		self.Services_pos = self.present_pos[0],.7
		self.Services_col = AFF_COL

		self.Services_T_size = (self.Connexion_size[0],
			self.Services_size[1])
		self.Services_T_pos = (self.Connexion_pos[0],
			self.Services_pos[1])
		self.Services_T_col = self.Get_bg_color()

#
		self.Present = Present(self)
		self.Connexion = Connexion(self)
		self.Services = Services(self)
		self.Services_T = Services_T(self)

		self.add_all()

	def Foreign_surf(self):
		
		self.Set_cont_obj(self.Present)
		self.Set_cont_obj(self.Connexion)
		self.Set_cont_obj(self.Services)
		self.Set_cont_obj(self.Services_T)

	def Set_error(self,mes):
		self.Connexion.Error_txt = mes
		self.Connexion.add_all()
		self.add_all()

class Present(Layout):
	def __init__(self,parent):
		size = parent.present_size
		pos = parent.present_pos
		col = parent.present_col
		Layout.__init__(self,size,col,pos,parent.parent)

		self.CSS()
		self.Render()

	def CSS(self):
		self.log_css = Css()
		self.log_css.Set_size("200px","200px")
		self.log_css.Set_position((2.5,5))

	def Render(self):
		logo = bl.image(TEXT.LOGO,
			"logo Rupin")
		logo.Set_style(self.log_css)
		logo.Set_border_radius(30)
		logo.Set_box_shadow(2,AFF_COL)

		Descip = Layout((.6,.3),None,
			("250px",10),self)
		Descip.add_title('Le Rupin',(.8,.2),(.1,0),
			bg_color = None,text_color = TEXT_COL2)
		Descip.add_Text("Bref description",(.8,.8),(.1,.22),bg_color = None
			,font_size = .9,text_color = TEXT_COL2,)

		Object = Layout((.96,.5),None,
			(2.5,"210px"),self)
		Object.add_title('Notre objectif',(.8,.1),(.1,0),
			bg_color = None,text_color = TEXT_COL2,)
		Object.add_Text("L'objectif de votre organisation",(.8,.8),(.1,.15)
			,bg_color = None,font_size = .9
			,text_color = TEXT_COL2)

		self.Set_cont_obj(logo)
		self.Set_cont_obj(Descip)
		self.Set_cont_obj(Object)

class Connexion(Layout):
	def __init__(self,parent):
		size = parent.Connexion_size
		pos = parent.Connexion_pos
		col = parent.Connexion_col
		Layout.__init__(self,size,col,pos,parent.parent)
		self.Error_txt = str()

		self.add_all()

	def Foreign_surf(self):
		self.add_Text(TEXT.Con,(1,.3),(0,0),
			text_color = TEXT_COL2,text_align = 'center',
			font_size = .86)

		F_css = Css()
		F_css.Set_size(1,.4)
		F_css.Set_position((0,30))
		F_css.Set_bg_color(AFF_COL)

		inp_css = Css()
		inp_css.Set_size(.55,.2)
		inp_css.Set_position((32,0))
		inp_css.Set_bg_color(APP_COL)
		inp_css.Set_border(1,AFF_COL)
		inp_css.Set_text_color(TEXT_COL2)

		lab_css = Css()
		lab_css.Set_size(.3,.15)
		lab_css.Set_position((0,5))
		lab_css.Set_text_color(TEXT_COL2)
		lab_css.Set_display("block")
		lab_css.Set_text_align('right')
		lab_css.Set_font_size(.8)

		self.F = form.form("Connexion","Connexion",action="/Accueil/Conn")
		self.F.Set_style(F_css)
		self.F.Set_email_input(TEXT.EMAIL,inp_style = inp_css,
			lab_style = lab_css)
		#lab_css = Css()
		lab_css.Set_size(.3,.15)
		lab_css.Set_display("block")
		lab_css.Set_text_align('right')
		lab_css.Set_font_size(.8)
		lab_css.Set_position((0,35))

		#inp_css = Css()
		inp_css.Set_size(.55,.2)
		inp_css.Set_position((32,30))
		self.F.Set_password_input(TEXT.PASS,inp_style = inp_css,
			lab_style = lab_css)

		#inp_css = Css()
		inp_css.Set_size(.7,.23)

		inp_css.Set_position((15,65))
		inp_css.Set_text_color(TEXT_COL3)
		inp_css.Set_bg_color(BUT_COL1)
		inp_css.Set_border_radius(2)
		
		self.F.End_form(submit_name = TEXT.VALIDER,
			Submit_style = inp_css)

		self.Set_cont_obj(self.F)

		Conn_Css = Css()
		Conn_Css.Set_size(.7,.06)
		Conn_Css.Set_text_color(TEXT_COL3)
		Conn_Css.Set_font_size(.8)
		Conn_Css.Set_underline(False)
		Conn_Css.Set_text_align("center")
		Conn_Css.Set_position((15,73))

		#L = urllib.parse.urlencode({"request":"SAVE_NEW"})
		L = "/INSC_0"
		A = bl.anchor(L,"Pas encode de compte?")
		A.Set_style(Conn_Css)

		Erro_css = Css()
		Erro_css.Set_size(1,.2)
		Erro_css.Set_position((0,7))
		Erro_css.Set_text_align('center')
		Erro_css.Set_text_color(ERROR_COL)
		Erro_css.Set_font_size(.8)

		P = bl.p(self.Error_txt)
		P.Set_style(Erro_css)

		self.Set_cont_obj(A)
		self.Set_cont_obj(P)

class Services(Layout):
	def __init__(self,parent):
		size = parent.Services_size
		pos = parent.Services_pos
		col = parent.Services_col
		Layout.__init__(self,size,col,pos,parent.parent)
		self.add_Text(TEXT.SERVICE,(.7,.1),(.15,0),
			text_color = TEXT_COL4,font_size = .9,
			)
		self.Set_overflow()
		dic = TEXT.Serv_dic
		X = 2.5
		for name,img in dic.items():
			self.add_service(X,name,img)
			X+= 22.5

	def add_service(self,X,titre,image):
		Cont_css = Css()
		Cont_css.Set_size(.2,.7)
		Cont_css.Set_position((X,22.5))
		Cont_css.Set_bg_color(OPTION_COL)
		Cont_css.Set_display("block")

		bg_img_css = Css()
		bg_img_css.Set_size(.4,.7)
		bg_img_css.Set_position((.3,7))
		bg_img_css.Set_border_radius(20)

		bg_img = bl.image(image,'img')
		bg_img.Set_style(bg_img_css)

		log_css = Css()
		log_css.Set_size(.15,.3)
		log_css.Set_position((2.5,5))

		log = bl.image(TEXT.LOGO,"")
		log.Set_style(log_css)
		
		T_css = Css()
		T_css.Set_size(1,.48)
		T_css.Set_position((0,60))
		T_css.Set_text_color(TEXT_COL2)
		T_css.Set_text_align("center")
		
		T = bl.p(titre)
		T.Set_style(T_css)

		g = titre.split(' ')
		g = "".join(g)
		L = "/SERV/"+g

		Cont = bl.anchor(L,"")
		Cont.Set_style(Cont_css)
		Cont.Set_cont_obj(bg_img)
		Cont.Set_cont_obj(T)

		self.Set_cont_obj(Cont)

class Services_T(Layout):
	def __init__(self,parent):
		size = parent.Services_T_size
		pos = parent.Services_T_pos
		col = parent.Services_T_col
		Layout.__init__(self,size,col,pos,parent.parent)
		
		self.add_Text(TEXT.Cont_text,(1,.2),(0,0),
			text_color = TEXT_COL3,font_size = .8,
			underline = True,text_align = 'center',
			bg_color = None)

		Y = 15
		X1 = 0
		X2 = 30
		for key,num in TEXT.Contact_dict.items():
			self.add_Text(key,(X2,.2),(X1,Y),
				text_color = TEXT_COL4,font_size = .8,
				bg_color = None)
			self.add_Text(num,(70,.2),(X2,Y),
				text_color = TEXT_COL2,font_size = .9,
				bg_color = None)
			Y += 20

