#Coding:utf-8
"""
	Cet module définie les gestionnaires d'ajout
	et de modification de l'affichage ainsi que la
	gestion des retours de fonction.

	Les méthodes à prendre en compte ici sont:
		Execution -> qui prend la requette
		Ret_handler -> qui prend en compte le retour d'une méthode
		Foreign_surf -> pour la définition des affichage
		add_all -> pour la mise à jour de la surface
		Set_cookies -> pour la définition des cookies
		Get_cookies -> pour la récupération au niveau du screen
"""
try:
	from .wid import wid
except:
	from wid import wid

class Layout(wid):
	def __init__(self,size,bg_color,pos,parent,
		style_obj = None):
		wid.__init__(self,size,bg_color,pos,parent,
			style_obj)
		self.MAIN_LAY = parent.MAIN_LAY

	def Set_BASE(self):
		pass

	def add_all(self):
		self.init_list()
		self.Set_BASE()
		self.Foreign_surf()

	def Foreign_surf(self):
		pass

	def Execution(self,request):
		ret = request.get('request')
		part = request.get('part_request')
		form = request.get("form")
		if part:
			self.Part_handler(part)
		elif ret:
			self.Ret_handler(ret)
		elif form:
			self.Form_handler(form)
		self.add_all()

	def Form_handler(self,form):
		pass

	def Ret_handler(self,ret):
		pass

	def Part_handler(self,part):
		pass

	def Set_cookies(self,cookie,*param):
		pass

	def get_cookies(self):
		return self.MAIN_LAY.Get_cookies()

	def get_ident(self):
		return self.MAIN_LAY.Get_ident_cookies()



