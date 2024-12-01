#Coding:utf-8
"""
	Module de définition de la surface de gestion des
	services
"""
from Import_lay import *
from .TTT import *

class Services_lay(Layout):
	def __init__(self,parent):
		size = parent.Services_size
		pos = parent.Services_pos
		col = parent.Services_col

		Layout.__init__(self,size,col,pos,parent)

		self.ident = self.MAIN_LAY.Get_ident_cookies()
		self.Info_service_size = 17.99,96
		self.Info_service_pos = 12.01,2
		self.Info_service_col = MAIN_COL

		self.Prof_bar_size = 5,96
		self.Prof_bar_pos = 3,2
		self.Prof_bar_col = AFF_COL

		self.details_size = 68.99,1
		self.details_pos = 31.01,0
		self.details_col = self.Get_bg_color()
		self.add_all()

	def Info_set(self):
		self.Info_txt = "Information général sur le service"
		"""
			C'est ici que les informations 
			seront traiter en fonction du 
			service choisi
		"""

	def Foreign_surf(self):
		self.Info_set()
		self.Add_info_service()
		self.Set_Prof_bar()
		self.Add_details()

	def Set_Prof_bar(self):
		size = self.Prof_bar_size
		pos = self.Prof_bar_pos
		col = self.Prof_bar_col
		L = Layout(size,col,pos,self)
		L.Set_border_radius(3)

		Part_size = 1,15
		Part_Y = 5

		for tup in PROF_PART(self.ident):
			img,txt = tup
			pos = (0,Part_Y)
			a = self.Set_img(img,Part_size,pos,txt)
			L.Set_cont_obj(a)
			Part_Y += 17

		self.Set_cont_obj(L)
	
	def Set_img(self,img,size,pos,txt):
		w,h = size
		h = 60
		R = txt.split(' ')
		R = ''.join(R)
		Ret = urllib.parse.urlencode({'request':R})
		Ret = "?"+Ret
		
		P = bl.p("")

		img = bl.image(img,txt)
		img.Set_size(*(.8,h))
		img.Set_position((.1,0))
		img.Set_border_radius(5)

		T = bl.p(txt)
		T.Set_font_size(self.Txt_size)
		T.Set_size(*(1,30))
		T.Set_text_align('center')
		T.Set_position((0,h+5))
		T.Set_bottom_border(2,TEXT_COL3)

		P.Set_cont_obj(img)
		P.Set_cont_obj(T)

		a = bl.anchor(Ret,P.Run_html())
		a.Set_size(*size)
		a.Set_position(pos)
		a.Set_text_color(TEXT_COL2)
		a.Set_bg_color(AFF_COL)

		

		return a

	def Add_info_service(self):
		size = self.Info_service_size
		col = self.Info_service_col
		pos = self.Info_service_pos
		L = Layout(size,col,pos,self)
		L.add_Text(self.Info_txt,
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

