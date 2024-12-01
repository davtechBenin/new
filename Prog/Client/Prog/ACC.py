#Coding:utf-8

"""
	Interface de gestion générale du client.
	Les autres sufaces de gestion doivent être 
	programmer et importer dans un autre module.

	Seul la surface de l'option est universel
"""

from lib.Pyweb.Layout import Layout
from lib.Pyweb.core import balises as bl
from lib.Pyweb.core import form
Css = bl.style
from .. import TEXT
from color import *
import urllib

from Base.Client import Client


# Importation des surface d'interaction
from .Tableau_bord import Dashbord
from .Favoris import Favoris
from .Service_G import Service_G
from .Demandes import Demandes
from .Service_T import Service_T
from .Profile import Profile
#------
class ACC(Layout):
	def __init__(self,parent):
		size = 100,100
		pos = 0,0
		col = APP_COL

		Layout.__init__(self,size,col,pos,parent)

		self.Opt_size = 15.99,96
		self.Opt_pos = 1.01,2
		self.Opt_col = MAIN_COL

		self.Surf_size = 84,100
		self.Surf_pos = 16,0
		self.Surf_col = self.Get_bg_color()

		self.Sep_size = '.1%',96
		self.Sep_pos = self.Surf_pos[0]+1.5,2
		self.Sep_col = TEXT_COL1

		self.In_action = str()

		self.Opt_surf = Option(self)

		self.Surf_lis = [
			Dashbord(self),
			Favoris(self),
			Service_G(self),
			Demandes(self),
			Service_T(self),
			Profile(self)
		]
		self.Main_Surf = self.Surf_lis[0]
		self.add_all()

	def get_surf(self,ret):
		lis = self.Surf_lis
		Not_set = Layout(self.Surf_size,
			self.Surf_col,self.Surf_pos,self)
		Not_set.add_Text("Not yet Set",(1,30),
			pos = (0,30),text_color = ERROR_COL,
			text_align = 'center',font_size = 3
			)
		
		ind = TEXT.OPT_LIST.index(ret)
		if ind > len(lis)-1:
			return Not_set
		else:
			return lis[ind]

	def Set_in_action(self,ret):
		ind = self.Opt_surf.Option_list.index(ret)
		self.MAIN_LAY.Set_Curent_surf(str(ind))
		self.In_action = ret
		self.Opt_surf.In_action = ret
		self.Opt_surf.add_all()
		self.Main_Surf = self.get_surf(ret)

	def Foreign_surf(self):
		sep = Layout(self.Sep_size,self.Sep_col,
			self.Sep_pos,self)
		self.Set_cont_obj(self.Opt_surf)
		
		self.Set_cont_obj(self.Main_Surf)
		self.Set_cont_obj(sep)

	def Ret_handler(self,ret):
		if ret in self.Opt_surf.Option_list:
			if ret == self.Opt_surf.Option_list[-1]:
				from Prog.general.Prog.Main import main as AC_main
				self.AC_M = AC_main(self.MAIN_LAY)
				self.AC_M.add_all()
				self.MAIN_LAY.Curent_layout = self.AC_M
				self.MAIN_LAY.Set_Ident_cookies(str())
				self.MAIN_LAY.add_all()
			else:
				self.Set_in_action(ret)
		else:
			ind = self.MAIN_LAY.Get_Curent_surf()
			if ind:
				this_ret = self.Opt_surf.Option_list[int(ind)]
			
				self.Set_in_action(this_ret)

				self.Main_Surf.Execution(self.request)

		self.add_all()

	def Execution(self,request):
		self.request = request
		R = request.get('request')
		self.Ret_handler(R)

class Option(Layout):
	def __init__(self,parent):
		size = parent.Opt_size
		pos = parent.Opt_pos
		col = parent.Opt_col

		Layout.__init__(self,size,col,pos,parent)
		self.Set_box_shadow(10,BUT_COL1,
			rayon_detalement = 2)


		self.Element_w = 98

		self.Log_part_h = 30

		self.But_size = 97,8

		self.Option_list = TEXT.OPT_LIST
		self.In_action = self.Option_list[0]

		self.add_all()

	def Foreign_surf(self):
		self.add_logo()
		self.Place_opts()

	def add_logo(self):

		size = self.Element_w,self.Log_part_h

		pos = 1.01,1.01
		title = "Logo Le Rupin"
		url = TEXT.LOGO
		col = MAIN_COL
		L = Layout(size,col,pos,self)

		L.add_image(url,title,(75,90),(8,2),title)

		t_size = 1,10
		T_pos = 0,90
		L.add_Text(TEXT.LOGO_TEXT,t_size,T_pos,
			font_size = .96,text_align = 'center',
			text_color = TEXT_COL4)
		self.Set_cont_obj(L)

	def Place_opts(self):
		size = self.But_size
		X = 3
		Y = 35
		Styl = Css()
		Styl.Set_border_radius(2)
		for opt in self.Option_list:
			bg_color = self.Get_bg_color()
			text_col = OPT_TEXT_COL
			if opt == self.In_action:
				bg_color = APP_COL
				text_col = OPT_ACTION_TEXT_COL
			self.add_button(f"{opt}",size,(X,Y),opt,
				font_size = .9,bg_color = bg_color,
				text_color = text_col,radius = 2,
				x_dec = 1,inner_x_dec = 2)
			Y += size[1]