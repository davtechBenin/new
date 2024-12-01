#Coding:utf-8
'''
	Base pour abriter les fonctions d'utilisation
	basic au niveau du module des base de données
'''

from lib.DAV_BASE import MyData

def Transforme_qts(Best_sellers):
	S = sum([tup[1] for tup in Best_sellers])
	B_trans = list()
	for ind,qts in Best_sellers:
		tup = ind,(qts/S)
		B_trans.append(tup)
	return B_trans

def get_ten_colors():
	
	c5 = 128,128,0
	c6 = 128,0,128
	c7 = 0,128,128
	c8 = 255,0,128
	c9 = 128,255,0
	c10 = 0,128,255
	return c5,c6,c7,c8,c9,c10

def GET_KEY_LIST(d1,d2,keys_liste):
	this_keys = list()
	keys_liste = [MyData.TODAY(i) for i in keys_liste]
	d1 = MyData.TODAY(d1)
	d2 = MyData.TODAY(d2)
	or_list = keys_liste
	keys_liste.reverse()
	if keys_liste:
		if d1 == d2:
			date0 = keys_liste[0]
			if (d1 in keys_liste):
				return [d1.date__]
			else:
				return list()
		else:
			for date in keys_liste:
				if date <= d2:
					if date >= d1:
						this_keys.append(date)
				elif d1>date:
					break

	this_keys = [i.date__ for i in this_keys]
	return this_keys
