#Coding:utf-8
"""
	Cet module définie les méthodes d'ajout d'élément
	dans une balise div pris comme la surface d'afficahage.
	Il ne définie pas les méthodes de gestion des 
	données a affiché.
"""
try:
	from .core.balises import *
except:
	from core.balises import *

import urllib

def transform(x,y):
	if type(x)!= str:
		if x <= 1:
			x*=100
	if type(y)!= str:
		if y <= 1:
			y*=100
	return (f"{x}%",f"{y}%")

def transform_to_int(x):
	if type(x) != str:
		if x <= 1:
			x *= 100
	return x

class wid(div):
	def __init__(self,size,bg_color,pos,parent,
		style_obj = None):

		div.__init__(self,size = size,pos = pos,
			bg_color = bg_color)
		if style_obj:
			self.Set_style(style_obj)

		self.parent = parent

		self.Y_Curent = 0 #Toujours en pourcentage

	def init_list(self):
		self.Y_Curent = 0
		self.Cont = str()
		self.el_list = list()

	def Set_cont_obj(self,cont_obj):
		#Ici, cont_obj doit forcement être un objet balise
		self.el_list.append(cont_obj)
		self.Cont+=cont_obj.Run_html()
		H = cont_obj.Get_size(1)
		Y = cont_obj.Get_position(1)
		self.Y_Curent = H+Y

	def add_surf(self,bal,size,bg_color,pos,cont = str(),
		style_obj = None):
		bal_obj = balise(bal,size = size,pos = pos,
			bg_color = bg_color)
		if cont:
			bal_obj.Set_cont_obj(cont)
		if style_obj:
			bal_obj.Set_style(style_obj)
		self.Set_cont_obj(bal_obj)

	def add_Text(self,text,size,pos,font_size = None,
		italic = False,bold = 100,underline = False,
		text_color = (0,0,0),bg_color = tuple(),
		text_align = 'left',font_name = list(),
		bal_name = "p",style_obj =None):
	#
		if not bg_color:
			bg_color = self.Get_bg_color()
		if not font_size:
			font_size = self.Txt_size
		S = style(size,bg_color,font_size,pos)
		if font_name:
			S.Set_font_family(*font_name)
		if italic:
			S.Set_font_style('italic')
		S.Set_font_weight(bold)
		S.Set_underline(underline)
		S.Set_text_align(text_align)
		S.Set_text_color(text_color)
		if style_obj:
			S.Set_style(style_obj)
		Text_obj = balise(bal_name)
		Text_obj.Set_cont_obj(text)
		Text_obj.Set_style(S)
		self.Set_cont_obj(Text_obj)

	def add_button(self,text,size,pos,Info = str(),
		font_name = str(),font_size = 1,italic = None,
		bold = None,underline = False,text_color = (0,0,0),
		text_align = 'left',New_page = False,
		bg_color = tuple(),style_obj = None,**wid_args):
	#
		if not bg_color:
			bg_color = self.Get_bg_color()
		if not font_size:
			font_size = self.Txt_size
		S = style(size,bg_color,font_size,pos)
		if font_name:
			S.Set_font_family(*font_name)
		if italic:
			S.Set_font_style('italic')
		S.Set_font_weight(bold)
		S.Set_underline(underline)
		S.Set_text_align(text_align)
		S.Set_text_color(text_color)
		S.Set_display('block')
		#S.Add_css("writing-mode","horizontal-tb")
		if style_obj:
			S.Set_style(style_obj)
		
		if not Info:
			Info = text
		dic = {"request":Info}
		href = urllib.parse.urlencode(dic)
		T = p(text)
		but_obj = anchor(f"/?{href}",T.Run_html())
		but_obj.Set_style(S)
		if New_page:
			but_obj.Set_target()
		self.Set_cont_obj(but_obj)

	def add_image(self,url,alt,size,pos,title):
		img_obj = image(url,alt)
		size = transform(*size)
		pos = transform(*pos)
		img_obj.Set_title(title)
		img_obj.Set_size(*size)
		img_obj.Set_position(pos)
		self.Set_cont_obj(img_obj)

	def add_table(self,table_obj):
		# Doit être définie directement avec l'objet CSS
		self.Set_cont_obj(table_obj)

	def add_form(self,form_obj):
		# Pareil pour le table
		self.Set_cont_obj(form_obj)

	def add_title(self,text,size,pos,bal_name = "h2",**text_args):
		self.add_Text(text,size,pos,bal_name = bal_name,
			**text_args)

	def add_link(self,text,url,size,pos,
		bg_color = (200,200,200),underline = False,
		text_color = (0,0,0),text_size = .85,
		new_wind =False):
		A = anchor(url,text)
		if new_wind:
			A.Set_target()
		A.Set_size(*size)
		P = transform(*pos)
		A.Set_position(P)
		if bg_color:
			A.Set_bg_color(bg_color)
		A.Set_underline(underline)
		A.Set_text_color(text_color)
		A.Set_font_size(text_size)

		self.Set_cont_obj(A)
