#Coding:utf-8
from .htmlcore import balise
from pycss.csssheet import generalCss
class table(balise):
	def __init__(self):
		balise.__init__(self,'table')

		self.All_el = list()
		self.Def_default_style()

	def Def_default_style(self):
		Default = generalCss(bal = 'table')
		Default.Begin_css()
		Default.Add_css('border-collapse','collapse')
		Default.Set_margin('auto')
		Default.End_css()

		data_css = Default.Add_childs_css('th','td')
		conf_dic = {
		'width':'1px',
		'color':'black',
		'style':'solid'
		}
		data_css.Set_border(conf_dic)
		Default.Update_child_css(data_css)

		default_style = Default.Run_css()
		self.Set_style(default_style)

	def Begin_row(self,style = None,attrs_dic = dict()):
		self.row = balise('tr')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def Begin_header(self,style = None,attrs_dic = dict()):
		self.head = balise('thead')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def End_header(self):
		self.Set_cont_obj(self.head)
		self.row = balise('thead')

	def Begin_footer(self,style = None,attrs_dic = dict()):
		self.foot = balise('tfoot')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def End_footer(self):
		self.Set_cont_obj(self.foot)
		self.row = balise('tfoot')

	def Begin_body(self,style = None,attrs_dic = dict()):
		self.body = balise('tbody')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def End_body(self):
		self.Set_cont_obj(self.body)
		self.row = balise('tbody')

	def Set_data(self,cont,style = None,attrs_dic = dict(),bal='td'):
		data = balise(bal)
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		data.Set_attrs(attrs_dic)
		data.Set_cont_obj(cont)
		self.All_el.append()
		self.row.Set_cont_obj(data)

	def Set_header(self,cont,style = None,attrs_dic = dict()):
		self.Set_data(cont,style,attrs_dic,bal='th')

	def End_row(self):
		self.Set_cont_obj(self.row)
		self.row = balise('tr')

	def Set_title(self,cont,style_dic = None,caption_side = 'top'):
		self.title = balise('caption')
		self.title.Add_css('caption-side',caption_side)
		if style_dic:
			self.title.Add_mult_css(style_dic)
		self.Set_cont_obj(self.title)

