#Coding:utf-8

from lib.Pyweb.Layout import Layout
from lib.Pyweb.core import balises as bl
from lib.Pyweb.core import form
Css = bl.style
from .. import TEXT
from color import *
import urllib

from Base.Client import Client
from Base.General import General

from ....Client.Prog.ACC import ACC

class Inscription(Layout):
	def __init__(self,parent):
		Layout.__init__(self,(100,100),APP_COL,
			(0,0),parent)
		size = (.6,.9)
		pos = (.2,.025)
		col = AFF_COL

		self.Surf = Layout(size,col,pos,self)

		self.Ins_parts = TEXT.inscription_info
		self.Clt_Base = Client()
		self.Gen_Base = General()

		self.Error_txt = str()
		self.Succes_txt = str()

		self.This_ind = 0
		self.ERROR = False

	def Save_Clt(self,form):
		if form:
			if "Email" in form:
				ret = self.Gen_Base.add_client(form)
				if type(ret)==tuple:
					self.Error_txt = ret[1]
					self.ERROR = True
				else:
					ident = ret
					self.Set_Ident_cookies(ident)
					self.Succes_txt = TEXT.CLIENT_NEW
			elif 'Nom' in form:
				ident = self.Get_ident_cookies()
				self.Clt_Base.Save_pers_info(ident,form)
				self.Succes_txt = TEXT.CLIENT_NEW
			elif 'Pays' in form:
				ident = self.Get_ident_cookies()
				self.Clt_Base.Save_pers_info(ident,form)
				self.Succes_txt = TEXT.CLIENT_NEW
			elif "Téléphone" in form:
				ident = self.Get_ident_cookies()
				self.Clt_Base.Save_pers_info(ident,form)
				self.Succes_txt = TEXT.CLIENT_NEW

	def Set_Ident_cookies(self,ident):
		name = "IDENT"
		val = ident
		self.MAIN_LAY.Set_cook(name,val)

	def Get_ident_cookies(self):
		cookies = self.MAIN_LAY.Get_cookies()
		for key in cookies:
			if 'IDENT' in key:
				return cookies[key]
		return str()

	def Foreign_surf(self):
		if self.This_ind == len(self.Ins_parts):
			Acc = ACC(self.parent)
			self.MAIN_LAY.Curent_layout = Acc
		else:
			if self.ERROR:
				self.This_ind -= 1
			part = self.Ins_parts[self.This_ind]
			self.add_form(part[1])
			self.add_case(*part[0])

			self.Set_cont_obj(self.Surf)

	def add_case(self,ind,text):
		X = 10
		Y = 10
		for i in range(0,len(self.Ins_parts)):
			C = bl.anchor('',str(i+1))
			C.Set_size(.18,.04)
			C.Set_position((X,Y))
			if i < ind:
				C.Set_bg_color(TEXT_COL3)
			else:
				C.Set_bg_color(APP_COL)
			C.Set_text_color(TEXT_COL2)
			C.Set_text_align("center")

			self.Surf.Set_cont_obj(C)
			X += 20
		Txt = bl.p(text)
		Txt.Set_text_color(TEXT_COL3)
		Txt.Set_text_align("center")
		Txt.Set_font_size(.9)
		Txt.Set_size(1,.08)
		Txt.Set_position((0,14))
		self.Surf.Set_cont_obj(Txt)
		if self.Error_txt:
			t = self.Error_txt
			col = ERROR_COL
		else:
			t = self.Succes_txt
			col = SUCCES_COL
		self.Surf.add_Text(t,(1,.05),(0,.2),
			text_color = col,text_align = 'center')

	def add_form(self,liste):
		F = form.form("insc",'INSC',action = f"INSC_{self.This_ind+1}")
		H = 7
		Y = 30
		F.Set_bg_color(self.Surf.Get_bg_color())
		for part in liste:
			lab_css = Css()
			lab_css.Set_display('block')
			lab_css.Set_size(.24,H)
			lab_css.Set_position((20,Y+2))
			lab_css.Set_text_align("left")
			lab_css.Set_font_size(.9)
			lab_css.Set_text_color(TEXT_COL2)

			inp_css = Css()
			inp_css.Set_size(.37,H)
			inp_css.Set_position((40,Y))
			inp_css.Set_bg_color(APP_COL)
			inp_css.Set_border(1,AFF_COL)
			inp_css.Set_text_color(TEXT_COL2)

			if 'de pass' in part:
				F.Set_password_input(part,inp_style = inp_css,
				lab_style = lab_css,required = True)
			else:
				F.Set_text_input(part,inp_style = inp_css,
					lab_style = lab_css,required = True)
			Y += 10

		But_css = Css()
		But_css.Set_size(.3,.06)
		But_css.Set_position((.48,Y+3))
		But_css.Set_bg_color(APP_COL)
		But_css.Set_border(1,AFF_COL)
		But_css.Set_text_color(TEXT_COL3)
		But_css.Set_border_radius(2)
		F.End_form(submit_name = "Suivant",
			Submit_style = But_css)
		self.Surf.Set_cont_obj(F)



		





