#Coding:utf-8
"""
	Cet module consiste à la définition d'un objet général
	pour la gestion effective d'une page html. Il met en relation
	tous les autre classe préalablement définie.
"""
try:
	from .core import balises
	from .core.style import style
except ModuleNotFoundError:
	import core.balises
	from core.style import style

import webbrowser

class screen:
	def __init__(self,titre = "PyWeb",
		css_file = str()):
		self.titre = titre
		self.css_file = css_file
		self.MAIN_LAY = self

		self.init()

	def init(self):
		titre = self.titre
		css_file = self.css_file
		self.HTML_page = "<!DOCTYPE html>\n<html>\n"
		head = balises.head(titre)
		self.temp = str()
		if css_file:
			head.Set_css_file(css_file)
		self.HTML_page += head.Run_html()

		self.Body = balises.body()
		self.parent = self.Body

		self.Layout_list = list()

	def Foreign_surf(self):
		pass

	def add_all(self):
		self.init()
		self.Foreign_surf()

	def Add_layout(self,layout):
		"""
			Un écran n'accept qu'un seul
			Layout
		"""
		self.Layout = layout
		#self.Body.Set_cont_obj(bal_obj)

	def End_page(self):
		body = self.Body.Run_html()
		self.HTML_page+=body
		self.HTML_page+='\n</html>'

	def Run(self):
		self.End_page()
		return self.HTML_page

	def create_page(self,name):
		from pathlib import Path as ph 
		work_dir = ph.cwd()
		dirs = name.split("/")
		if len(dirs)>1:
			for di in dirs[:-1]:
				work_dir = work_dir.joinpath(di)
				if not work_dir.exists():
					work_dir.mkdir()
		if ".html" not in name:
			name = name+'.html'
		with open(name,'w') as fic:
			fic.write(self.Run())
		
		return ph.cwd()/name

	def open_in_browser(self,name):
		path = self.create_page(name)

		webbrowser.open(str(path))

	def Execution(self,request):
		response = self.Layout.Execution(request)
		self.Body.init()
		self.Body.Set_cont_obj(response)
		return self.Run()

"""
	Le layout principale doit formater et retourné
	ce qui doit être afficher à l'écran comme 
	contenue de la balise body
"""
