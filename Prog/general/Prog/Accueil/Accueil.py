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
		size = 90,98
		bg_color = AFF_COL
		pos = (5,1.2)
		Layout.__init__(self,size,bg_color,pos,parent)
		self.Set_box_shadow(20,TEXT_COL2)
		self.Set_overflow()

		self.image_size = 96,60
		self.image_pos = 2,0
		self.Init_all()
		self.ACCUEIL = True

	def Init_all(self):
		self.ACCUEIL = False
		self.TELECHA = False
		self.INSTALA = False
		self.UTILISA = False

	def Foreign_surf(self):
		if self.ACCUEIL:
			self.Accueil()

		elif self.TELECHA:
			self.Telecha()

		elif self.INSTALA:
			self.Instala()

		elif self.UTILISA:
			self.Utilisa()

	def Telecha(self):
		self.Set_cont_obj(Telechargement(self))

	def Instala(self):
		self.Set_cont_obj(Installation(self))

	def Utilisa(self):
		self.Set_cont_obj(Utilisation(self))

	def Accueil(self):
		self.Set_cont_obj(Image_part(self))
		self.Menu_set()
		self.Content()

	def Menu_set(self):
		menu_size = self.image_size[0],6
		menu_pos = 2,self.image_size[1]
		lay = Layout(menu_size,self.Get_bg_color(),menu_pos,
			self)
		MENUS = TEXT.MENUS
		part_w = 100/(len(MENUS)+1)
		x_dep = X = part_w/(len(MENUS)+1)
		for M in MENUS:
			pos = X,0
			lay.add_button(M,(part_w,1),pos,
				Info = M,text_align = "center",
				bg_color = TEXT_COL4,font_size = .8,
				radius= 10,shadow = 5)
			X += part_w+x_dep
		self.Set_cont_obj(lay)

	def Content(self):
		pos = 2,self.image_size[1]+7
		Lay = Layout((96,32),self.Get_bg_color(),pos,self)
		Lay.Set_overflow()
		
		Info = bl.dic()
		val_css = Css(size = (86,1))
		val_css.Set_padding_top(2)
		val_css.Set_text_align('justify')


		for key,val in TEXT.ACCUEIL.items():
			Info.Set_terme(key)
			Info.Set_def(val,val_css)
		Lay.Set_cont_obj(Info)


		self.Set_cont_obj(Lay)

	def Execution(self,request):
		req = request.get("request")
		self.Ret_handler(req)

		self.add_all()

	def Ret_handler(self,ret):
		if ret:
			if ret == "Téléchargement":
				self.Init_all()
				self.TELECHA = True
			elif ret == 'Installation':
				self.Init_all()
				self.INSTALA = True
			elif ret == 'Utilisation':
				self.Init_all()
				self.UTILISA = True
			else:
				self.Init_all()
				self.ACCUEIL = True

class Image_part(Layout):
	def __init__(self,parent):
		size = parent.image_size
		pos = parent.image_pos
		col = parent.Get_bg_color()
		Layout.__init__(self,size,col,pos,parent)
		self.Set_overflow()


		self.img_s = 80,87
		self.img_x = 0
		self.img_y = 10

		for img,title in TEXT.Img_l:
			pos = self.img_x,self.img_y
			self.add_image(img,'',self.img_s,pos,title,
				radius = 0)
			self.add_Text(title,(self.img_s[0]-20,6),
				(pos[0]+10,0),text_align = 'center',
				radius = 2,shadow = 10)
			self.img_x += self.img_s[0] + 5

class Telechargement(Layout):
	def __init__(self,parent):
		size = 96,98
		pos = 2,1.1
		col = parent.Get_bg_color()
		Layout.__init__(self,size,col,pos,parent)
		self.add_all()

	def Foreign_surf(self):
		Y = 13
		
		L = Layout((1,1),self.Get_bg_color(),(0,0),self)
		L.Set_overflow()
		for key,val in TEXT.TELECHARGEMENT.items():
			mess,mont,but = val
			pos = 2,Y
			L = self.add_part(L,key,mess,mont,but,pos)
			Y += 43

		self.Set_cont_obj(L)

		self.add_Text('Téléchargement',size = (1,8),
			pos = (0,0),text_align = 'center',
			bg_color = TEXT_COL4,font_size = 1,
			padding_top = 1,shadow = 20,
			radius = 10)

	def add_part(self,L,titre,mess,mont,but,pos):
		dic = Layout((96,39),TEXT_COL1,pos,L)
		dic.Set_box_shadow(10,TEXT_COL2)
		dic.Set_border_top_left_radius(2)
		dic.Set_border_bottom_right_radius(2)

		dic.add_Text(titre,(80,10),(0,0),font_size = 1.2,
			text_color = TEXT_COL3,margin_left = 2)
		dic.add_Text(mess,(93,50),(5,14),
			text_align ='justify',font_size = 1)

		L.Set_cont_obj(dic)
		L.add_button(f"Obtenir le Pack {titre} \
			<br>à {mont}",(60,12),
			(0,pos[1]+26),Info = but,web_page = True,
			margin_left = 20,bg_color = DISABLE_BUT3,
			text_align = "center",font_size = 1.1,
			text_color = TEXT_COL1,shadow_inset = True,
			radius = 40,shadow = 40,
			shadow_color = TEXT_COL2)
		return L

class Installation(Layout):
	def __init__(self,parent):
		size = 96,98
		pos = 2,1.1
		col = parent.Get_bg_color()
		Layout.__init__(self,size,col,pos,parent)
		self.add_all()

	def Foreign_surf(self):
		Y = 3
		L = Layout((1,58),self.Get_bg_color(),(0,42),self)
		L.Set_overflow()
		for key,val in TEXT.INSTALLATION.items():
			mess,mont = val
			pos = 2,Y
			L = self.add_part(L,key,mess,mont,pos)
			Y += 50

		self.Set_cont_obj(L)
		self.Info_part()


	def Info_part(self):
		size = 1,40
		L = Layout(size,self.Get_bg_color,(0,0),self)
		L.Set_box_shadow(5,TEXT_COL2)
		L.add_Text(TEXT.INFO_INSTALLATION,(90,80),(5,17),
			font_size = 1,text_align = 'justify')
		L.add_Text('Installation',size = (1,15),
			pos = (0,0),text_align = 'center',
			bg_color = TEXT_COL4,font_size = 1,
			padding_top = 1,shadow = 20,
			radius = 10)
		self.Set_cont_obj(L)

	def add_part(self,L,titre,mess,mont,pos):
		dic = Layout((96,45),TEXT_COL1,pos,L)
		dic.Set_box_shadow(10,TEXT_COL2)
		dic.Set_border_top_left_radius(2)
		dic.Set_border_bottom_right_radius(2)

		T = f"{titre}: <i>{mess}</i>"
		dic.add_Text(T,(80,10),(0,0),font_size = 1.2,
			text_color = TEXT_COL3,margin_left = 2)
		dic.add_Text(mont,(93,50),(5,14),
			text_align ='justify',font_size = 1)

		L.Set_cont_obj(dic)
		
		return L



class Utilisation(Layout):
	def __init__(self,parent):
		size = 96,98
		pos = 2,1.1
		col = parent.Get_bg_color()
		Layout.__init__(self,size,col,pos,parent)
		self.add_all()

	def Foreign_surf(self):
		Y = 3
		L = Layout((1,78),self.Get_bg_color(),(0,22),self)
		L.Set_overflow()
		for key,val in TEXT.UTILISATION.items():
			mess = val
			pos = 2,Y
			L = self.add_part(L,key,mess,pos)
			Y += 50

		self.Set_cont_obj(L)
		self.Info_part()


	def Info_part(self):
		size = 1,20
		L = Layout(size,self.Get_bg_color,(0,0),self)
		L.Set_box_shadow(5,TEXT_COL2)
		L.add_Text(TEXT.INFO_UTILISATION,(90,80),(5,37),
			font_size = 1,text_align = 'justify')
		L.add_Text('Utilisation',size = (1,35),
			pos = (0,0),text_align = 'center',
			bg_color = TEXT_COL4,font_size = 1,
			padding_top = 1,shadow = 20,
			radius = 10)
		self.Set_cont_obj(L)

	def add_part(self,L,titre,mess,pos):
		dic = Layout((96,45),TEXT_COL1,pos,L)
		dic.Set_box_shadow(10,TEXT_COL2)
		dic.Set_border_top_left_radius(2)
		dic.Set_border_bottom_right_radius(2)

		dic.add_Text(titre,(80,10),(0,0),font_size = 1.2,
			text_color = TEXT_COL3,margin_left = 2)
		dic.add_Text(mess,(93,50),(5,14),
			text_align ='justify',font_size = 1)

		L.Set_cont_obj(dic)
		
		return L

