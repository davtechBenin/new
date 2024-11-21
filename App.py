#Coding:utf-8
"""
	Votre application ici. Cet module doit définir
	un objet qui gère l'ensemble de l'application.
"""

from lib.Pyweb.hand.Request_handler import Req_hand
from lib.Pyweb.Screen import screen

from color import *

from Prog.main import main
# Main représente le layour principal de l'application


class App(screen):
	def __init__(self):
		size = 100,100
		bg_color = MAIN_COL
		pos = (0,0)
		titre = "Le Rupin"
		screen.__init__(self,titre)

		Main = main(self,bg_color)
		self.Add_layout(Main)

	def Get_cookies(self):
		return self.Layout.Get_cook()

	def Run_execution(self,request):
		request = Req_hand(request).request
		#print(request)
		return self.Execution(request)
