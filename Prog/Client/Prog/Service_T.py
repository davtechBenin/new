#Coding:utf-8
"""
	Interface des favoris du client
"""
from Import_lay import *

class Service_T(Layout):
	def __init__(self,parent):
		size = parent.Surf_size
		pos = parent.Surf_pos
		col = parent.Surf_col

		Layout.__init__(self,size,col,pos,parent)
		self.CV_SURF = False
		self.SMS_SURF = False

		self.Set_size_and_pos()

		self.add_all()

	def Foreign_surf(self):
		self.add_Guide()
		self.add_Mail()
		if self.CV_SURF:
			self.Add_priority_lay(CV(self))
		elif self.SMS_SURF:
			self.Add_priority_lay(SMS(self))

	def Set_size_and_pos(self):
		int_w = 3
		int_h = 5

		pw,ph = self.Guide_size = 55,100-(int_h*2)
		px,py = self.Guide_pos = int_w,int_h
		self.Guide_col = AFF_COL

		WWW = 100-(int_w*3)-pw

		sw,sh = self.Mail_size = WWW,ph
		sx,sy = self.Mail_pos = px+pw+int_w,py
		self.Mail_col = AFF_COL


	def add_Guide(self):
		Guide = Info_recrut(self)
		self.Set_cont_obj(Guide)

	def add_Mail(self):
		Mail = form_recrut(self)
		self.Set_cont_obj(Mail)

	def Ret_handler(self,ret):
		if ret == TEXT.CV_but:
			self.CV_SURF = True
		elif ret == TEXT.mes_but:
			self.SMS_SURF = True

class Info_recrut(Layout):
	def __init__(self,parent):
		size = parent.Guide_size
		pos = parent.Guide_pos
		col = parent.Guide_col
		Layout.__init__(self,size,col,pos,parent)
		self.size_and_pos()
		self.add_all()
	
	def size_and_pos(self):
		x_dep = 3
		y_dep = 2
		lw,lh = self.logo_size = 35,40
		lx,ly = self.logo_pos = x_dep,y_dep

		ow,oh = self.org_size = 100-(x_dep*3)-lw,lh
		ox,oy = self.org_pos = lx+x_dep+lw,ly
		self.org_col = self.Get_bg_color()

		pw,ph = self.pres_size = 100-(x_dep*2),100-(y_dep*3)-lh
		px,py = self.pres_pos = x_dep,ly+lh+y_dep
		self.pers_col = APP_COL

	def Foreign_surf(self):
		self.add_logo()
		self.add_org()
		self.add_present()

	def add_logo(self):
		log = TEXT.LOGO
		self.add_image(log,'logo',self.logo_size,self.logo_pos,
			'Le Rupin',radius = 30)

	def add_org(self):
		L = Layout(self.org_size,self.org_col,self.org_pos,self)
		L.add_Text(TEXT.ORG_REC,
			(80,30),(10,20),font_size = 1.6,
			text_color = TEXT_COL2,
			text_align = 'center')
		self.Set_cont_obj(L)

	def add_present(self):
		L = Layout(self.pres_size,self.pers_col,self.pres_pos,
			self)
		L.Set_box_shadow(1,BUT_COL1)
		L.add_Text(TEXT.PRESENT_REC,
			(80,30),(10,20),font_size = 1.6,
			text_color = SUCCES_COL,
			text_align = 'center')
		self.Set_cont_obj(L)

class form_recrut(Layout):
	def __init__(self,parent):
		size = parent.Mail_size
		pos = parent.Mail_pos
		col = parent.Mail_col
		Layout.__init__(self,size,col,pos,parent)
		self.size_and_pos()
		self.add_all()

	def size_and_pos(self):
		x_dep = 3
		y_dep = 2
		lw,lh = self.pres_size = 100-(x_dep*2),19
		lx,ly = self.pres_pos = x_dep,y_dep

		ow,oh = self.part_size = lw,lh
		self.part_x = x_dep
		self.part_y = y_dep

	def Foreign_surf(self):
		self.add_present()
		self.add_parts()

	def add_present(self):
		Txt = TEXT.PRESENT_FORM
		txt = bl.p(Txt)
		txt.Set_size(*self.pres_size)
		txt.Set_position(self.pres_pos)
		txt.Set_top_border(1,color = TEXT_COL2)
		txt.Set_right_border(1,color = TEXT_COL2)
		txt.Set_bottom_border(1,color = TEXT_COL3)
		txt.Set_left_border(1,color = TEXT_COL3)

		txt.Set_text_color(TEXT_COL2)
		txt.Set_text_align("center")
		txt.Set_padding_top(1)
		txt.Set_padding_left(2)
		txt.Set_padding_right(2)

		txt.Set_box_shadow(10,BUT_COL1)
		self.Set_cont_obj(txt)

	def add_parts(self):
		col = self.Get_bg_color()
		Y = (self.part_y*4) + self.pres_size[1]
		for but,text in TEXT.REC_PART.items():
			pos = self.part_x,Y
			L = Layout(self.part_size,col,pos,self)
			L.Set_box_shadow(10,BUT_COL1)
			L.Set_border_radius(2)
			L.add_Text(text,(80,50),(10,5),
				font_size = self.Txt_size+.3,
				text_color = TEXT_COL3,text_align ='center')
			L.add_button(but,(40,35),(30,55),Info = but,
				font_size = self.Txt_size+.2,text_color = TEXT_COL4,
				shadow = 10,radius = 1,
				text_align = 'center')

			self.Set_cont_obj(L)


			Y += self.part_size[1]+self.part_y
		self.add_button("Envoyer",(70,8),(15,Y),
			text_color = SUCCES_COL,font_size = self.Txt_size+.3,
			text_align = 'center',radius = 2,shadow = 10)

class form_status(Layout):
	def __init__(self,parent):
		size = parent.Mail_size
		pos = parent.Mail_pos
		col = parent.Mail_col
		Layout.__init__(self,size,col,pos,parent)
		self.size_and_pos()
		self.add_all()

	def size_and_pos(self):
		x_dep = 3
		y_dep = 2
		lw,lh = self.pres_size = 90,60
		lx,ly = self.pres_pos = 5,20

	def Foreign_surf(self):
		self.add_present()

	def add_present(self):
		Txt = TEXT.PRESENT_STATUS
		txt = Layout(self.pres_size,self.Get_bg_color(),
			self.pres_pos,self)
		txt.Set_top_border(1,color = TEXT_COL2)
		txt.Set_right_border(1,color = TEXT_COL2)
		txt.Set_bottom_border(1,color = TEXT_COL3)
		txt.Set_left_border(1,color = TEXT_COL3)

		txt.Set_border_radius(2)

		txt.Set_text_color(TEXT_COL2)
		txt.Set_text_align("center")
		txt.Set_padding_top(1)
		txt.Set_padding_left(2)
		txt.Set_padding_right(2)

		txt.Set_box_shadow(10,BUT_COL1)

		txt.add_Text(Txt,(80,30),(10,15),text_align ='center',
			text_color = TEXT_COL2,font_size = self.Txt_size+.2)

		status = "Traitement en cours"# pris avec la base
		col = SUCCES_COL
		if status in ("Rejetter","Refuser"):
			col = ERROR_COL
		txt.add_Text(status,(60,30),(20,35),text_color = col,
			font_size = self.Txt_size+.3,text_align = 'center',)

		txt.add_button("Modifier les informations",(50,20),
			(25,60),bg_color = BUT_COL1,radius = 2,
			shadow = 10,shadow_color = FRONT_COL,
			text_color = TEXT_COL3,font_size = self.Txt_size+.3,
			text_align = 'center',Info = 'MODIF_FORM_REC')

		self.Set_cont_obj(txt)

class form_val(Layout):
	def __init__(self,parent):
		size = parent.Mail_size
		pos = parent.Mail_pos
		col = parent.Mail_col
		Layout.__init__(self,size,col,pos,parent)
		self.size_and_pos()
		self.add_all()

	def size_and_pos(self):
		x_dep = 3
		y_dep = 2
		lw,lh = self.pres_size = 90,60
		lx,ly = self.pres_pos = 5,20

	def Foreign_surf(self):
		self.add_present()

	def add_present(self):
		Txt = TEXT.PRESENT_VAL
		txt = Layout(self.pres_size,self.Get_bg_color(),
			self.pres_pos,self)
		txt.Set_top_border(1,color = TEXT_COL2)
		txt.Set_right_border(1,color = TEXT_COL2)
		txt.Set_bottom_border(1,color = TEXT_COL3)
		txt.Set_left_border(1,color = TEXT_COL3)

		txt.Set_border_radius(2)

		txt.Set_text_color(TEXT_COL2)
		txt.Set_text_align("center")
		txt.Set_padding_top(1)
		txt.Set_padding_left(2)
		txt.Set_padding_right(2)

		txt.Set_box_shadow(10,BUT_COL1)

		txt.add_Text(Txt,(80,30),(10,10),text_align ='center',
			text_color = TEXT_COL2,font_size = self.Txt_size+.2)

		status = TEXT.FELICITATION_PESENT
		col = SUCCES_COL
		
		txt.add_Text(status,(60,30),(20,35),text_color = col,
			font_size = self.Txt_size+.3,text_align = 'center')

		form = {
			"Email :":'RupinEmpl-xxxxx@rupin.com',
			"Password :":"xxxxx"
		}# provenant de la base
		Y = 55
		part_h = 14
		for key,val in form.items():
			T = Layout((90,part_h),self.Get_bg_color(),(5,Y),
				txt)
			T.Set_box_shadow(20,BUT_COL1)

			T.add_Text(key,(25,part_h),(0,0),
				text_color = TEXT_COL4,font_size = self.Txt_size+.2,
				text_align = 'right')
			T.add_Text(val,(60,part_h),(30,0),
				text_color = TEXT_COL3,font_size = self.Txt_size+.2,
				text_align = ' center')

			Y += part_h+5
			txt.Set_cont_obj(T)
		
		self.Set_cont_obj(txt)

class CV(Layout):
	def __init__(self,parent):
		size = 40,70
		pos = 30,15
		col = AFF_COL
		Layout.__init__(self,size,col,pos,parent)

		F = form.form("CV")
		F.Set_bg_color(col)

		F.Set_size(90,70)
		F.Set_position((5,15))

		inp_css = Css()
		inp_css.Set_size(80,10)
		inp_css.Set_position((10,50))
		inp_css.Set_border(0)
		inp_css.Set_border_radius(2)
		inp_css.Set_box_shadow(10,BUT_COL1)
		inp_css.Set_bg_color(col)
		inp_css.Set_text_color(TEXT_COL2)

		F.Set_input('file','le cv',lab = False,inp_style = inp_css)

		but_css = Css()
		but_css.Set_size(40,10)
		but_css.Set_position((50,70))
		but_css.Set_border(0)
		but_css.Set_border_radius(2)
		but_css.Set_box_shadow(10,BUT_COL1)
		but_css.Set_bg_color(col)
		but_css.Set_text_color(TEXT_COL3)

		F.End_form(submit_name = "Envoyer",Submit_style = but_css)

		self.Set_cont_obj(F)
		self.add_Text(TEXT.CV_INFO,(80,10),(10,20),
			text_color = TEXT_COL2,font_size = self.Txt_size+.2,
			text_align = 'center')

class SMS(Layout):
	def __init__(self,parent):
		size = 40,70
		pos = 30,15
		col = AFF_COL
		Layout.__init__(self,size,col,pos,parent)

		F = form.form("SMS")
		F.Set_bg_color(col)

		F.Set_size(90,70)
		F.Set_position((5,15))

		inp_css = Css()
		inp_css.Set_size(1,70)
		inp_css.Set_position((0,10))
		inp_css.Set_border(0)
		inp_css.Set_border_radius(1)
		inp_css.Set_padding_left(1)
		inp_css.Set_padding_right(1)
		inp_css.Set_padding_top(1)
		inp_css.Set_box_shadow(10,BUT_COL1)
		inp_css.Set_bg_color(col)
		inp_css.Set_text_color(TEXT_COL2)

		F.Set_textarea('Message',style = inp_css)

		but_css = Css()
		but_css.Set_size(50,10)
		but_css.Set_position((25,90))
		but_css.Set_border(0)
		but_css.Set_border_radius(2)
		but_css.Set_box_shadow(10,BUT_COL1)
		but_css.Set_bg_color(col)
		but_css.Set_text_color(TEXT_COL3)

		F.End_form(submit_name = "Envoyer",Submit_style = but_css)

		self.Set_cont_obj(F)
		self.add_Text(TEXT.SMS_INFO,(80,10),(10,5),
			text_color = TEXT_COL2,font_size = self.Txt_size+.2,
			text_align = 'center')





