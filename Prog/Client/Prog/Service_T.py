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

		self.Set_size_and_pos()

		self.add_all()

	def Foreign_surf(self):
		self.add_Guide()
		self.add_Mail()
		self.add_SMS()

	def Set_size_and_pos(self):
		int_w = 3
		int_h = 5

		pw,ph = self.Guide_size = 100-int_w*2,(100-(int_h*3))/2
		px,py = self.Guide_pos = int_w,int_h
		self.Guide_col = MAIN_COL

		WWW = (100-int_w*3)/2

		sw,sh = self.Mail_size = WWW,ph
		sx,sy = self.Mail_pos = px,py*2+ph
		self.Mail_col = MAIN_COL

		mw,mh = self.SMS_size = sw,sh
		mx,my = self.SMS_pos = sx+sw+int_w,sy
		self.SMS_col = MAIN_COL

	def add_Guide(self):
		size = self.Guide_size
		pos = self.Guide_pos
		col = self.Guide_col
		Guide = Layout(size,col,pos,self)

		Guide.add_Text("Guide",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(Guide)

	def add_Mail(self):
		size = self.Mail_size
		pos = self.Mail_pos
		col = self.Mail_col
		Mail = Layout(size,col,pos,self)

		Mail.add_Text("Mail",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(Mail)

	def add_SMS(self):
		size = self.SMS_size
		pos = self.SMS_pos
		col = self.SMS_col
		SMS = Layout(size,col,pos,self)

		SMS.add_Text("SMS",(1,30),(0,30),
			text_color = TEXT_COL3,font_size = 2,
			text_align = "center")
		self.Set_cont_obj(SMS)

	