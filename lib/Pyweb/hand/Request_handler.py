#Coding:utf-8

from werkzeug.wrappers import Request
"""
	C'est ici qu'est gérer l'ensemble des vues à envoyer
	comme reponse en fonction des données de request.
	La plus importante est que, nous avons un seul URL. 
	toutes les autres parties sont des parties de l'application
	asseccible via les coockies et les requettes
"""
class Req_hand:
	def __init__(self,request):
		
		self.request = self.Request_hand(request)
		"""
			Le dictionnaire request est doit être
			envoyer à la partie Execution du screen
		"""

	def Request_hand(self,REQ):
		red = Request(REQ)
		#"""
		method = REQ.get("REQUEST_METHOD")
		form,request = self.get_form(red.url)
		part_request = self.Url_path(REQ.get("REQUEST_URI"))
		cookies = self.get_cookies(REQ.get("HTTP_COOKIE"))
		lieu = self.get_lieu(REQ.get("HTTP_USER_AGENT"))


		req = {
			"method":method,
			"form":form,
			"request":request,
			"part_request":part_request,
			"cookies":cookies,
			"lieu":lieu
		}
		return req
		#"""
		#return dict()

	def get_lieu(self,text):
		#nav,ordi = text.split("(")
		#ordi,other = ordi.split(")")
		#ordi = ordi.split(";")
		#lieu = nav + ' '.join(ordi[0:-1])
		return text

	def get_cookies(self,text):
		if text:
			text_l = text.split(";")
			dic = dict()
			for part in text_l:
				if part:
					name,val = part.split("=")
					dic[name] = val
			return dic
		else:
			return dict()

	def Url_path(self,url):
		part = url.split("/")
		part = part[1:]
		L = list()
		for P in part:
			if '?' in P:
				P = P.split('?')[0]
			L.append(P)
		part = '-'.join(L)
		return part

	def get_form(self,text):
		T = text.split("?")
		if len(T)>1:
			text = T[1]
		else:
			text = str()
		text_l = text.split("&")
		dic = dict()
		for part in text_l:
			if part:
				name,val = part.split("=")
				name = ' '.join(name.split("+"))
				val = ' '.join(val.split('+'))
				if val == "Suivant":
					pass
				else:
					dic[name] = val
		req = str()
		if 'request' in dic:
			req = dic.pop("request")
		return dic,req

	def Run(self):
		self.Ac_Main.add_all()
		Obj = self.Ac_Main.Run()

		return Obj

