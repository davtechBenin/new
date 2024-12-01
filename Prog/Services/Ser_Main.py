#Coding:utf-8
'''
	Module de définition générale des surfaces de gestion
	de la partie services
'''
from lib.Pyweb.Layout import Layout
from lib.Pyweb.core import balises as bl
from lib.Pyweb.core import form

Css = bl.style
from color import *

from .Service_surf import Services_lay
import urllib


class Ser_main(Layout):
	def __init__(self,parent):
		size = 1,1
		pos = 0,0
		col = APP_COL
		Layout.__init__(self,size,col,pos,parent)


		self.Servi_interface_dic = {

		}
		self.Services_size = 1,1
		self.Services_pos = 0,0
		self.Services_col = self.Get_bg_color()
		self.default_surf = Services_lay(self)

	def Part_set(self,part_request):
		part_request = part_request.split('-')[1]
		self.Curent_surf = self.Servi_interface_dic.get(
			part_request,self.default_surf)

	def Foreign_surf(self):
		self.Set_cont_obj(self.Curent_surf)

	def Run(self):
		self.add_all()
		return self

	def Execution(self,request):
		part_request = request.get('part_request')
		self.Part_set(part_request)
		"""
			Une fois la surface de gestion identifie, on lui
			donne la requette pour une gestion interne
		"""
		self.Curent_surf.Execution(request)

		self.add_all()





