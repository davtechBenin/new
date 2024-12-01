#Coding:utf-8
"""
	Module de définition du layout principale

	Chaque partie sera représenter par un part_request.

	Cet module sera le pincipale à prendre en compte
	pour la définition de chaque partie principale
"""
from .Layout import Layout

class Main_Layout(Layout):
	def __init__(self,parent,bg_color):
		size = 100,100
		pos = (0,0)
		Layout.__init__(self,size,bg_color,pos,parent)
		self.MAIN_LAY = self
		
		self.Curent_layout = Layout((100,100),bg_color,
			pos,self)
		self.request = dict()
		self.cookies = list()

		self.default_surf_name = "Accueil"

		self.Set_lays()

	def Foreign_surf(self):
		pass
		

	def Set_lays(self):
		self.Part_dic = {
		self.default_surf_name:Layout(self.Get_size(),
			self.Get_bg_color(),self.Get_pos(),self)}
		#Pour stocker les surfaces des parties

	def Get_cookies(self):
		#return dict()
		return self.request.get('cookies',dict())

	def Get_cook(self):
		return self.cookies

	def Set_cook(self,name,val):
		self.cookies.append((name,val))

	def Get_ident_cookies(self):
		cookies = self.Get_cookies()
		for key in cookies:
			if 'IDENT' in key:
				return cookies[key]
		return str()

	def Set_Ident_cookies(self,val):
		self.Set_cook('IDENT',val)

	def Set_Curent_surf(self,ret):
		key = 'CURENT_SURF'
		self.Set_cook(key,ret)

	def Get_Curent_surf(self):
		cookies = self.Get_cookies()
		for key in cookies:
			if 'CURENT_SURF' in key:
				return cookies[key]
		return str()

	def Ret_handler(self,ret):
		"""
			la définition d'un ret handler
			ici ne voudra rien dire. et ne
			doit pas être prise en compte
		"""
		pass

	def Execution(self,request):
		"""
			Le principe à respecter ici est que, 
			chaque curent_layout doit gérrer ses 
			propre "request"
		"""
		self.request = request
		part_request = self.request.get('part_request',str())
		if not part_request:
			part_request = self.default_surf_name

		self.Curent_layout = self.Part_dic.get(part_request,
			self.Part_dic[self.default_surf_name])
			
		self.Curent_layout.Execution(self.request)
		
		return self.Curent_layout.Run_html()

