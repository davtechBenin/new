#Coding:utf-8
"""
	Module de définition du layout principale

	Chaque partie sera représenter par un part_request.
"""
from lib.Pyweb.Main_Layout import Main_Layout
from lib.Pyweb.Main_Layout import Main_Layout

from Prog.general.Prog import Main as Ac_Main

from color import *

class main(Main_Layout):
	def __init__(self,parent,bg_color):
		Main_Layout.__init__(self,parent,bg_color)


	def Set_lays(self):
		self.Part_dic = {
			"Accueil":Ac_Main.main(self).Run(),
		}#Pour stocker les surfaces des parties
