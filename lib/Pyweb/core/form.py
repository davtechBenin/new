#Coding:utf-8
"""
	La définition de style se fera grace à la classe de définition
	généralCss. ainsi, c'est l'objet qui sera donné comme argument
	au méthode de définition des différente partie du formulaire.
	cependant, il est aussi possible de gérer le css du formulaire
	directement grace à l'héritage de la classe 'cssSheet' via la
	classe 'balise'

	les attributs utiles pour le formulaire:
		size = permet d'agrandire le champ
		maxlenght = permet de limiter le nombre de caratères du champ
		value = permet de préremplir le champ
		placeholder = permet de donner une indication sur le contenue du champ
		autofocus = pour donner automatiquement le focus a un champ
		required = pour rendre un champ obligatoire

	les attributs possibles pour les champs nombre, date, et curseur:
		min pour indiquer la valeur minimale autorisée
		max pour indiquer la valeur maximale autorisée
		step pour spécifier le nombre de pas.


	Au niveau de la class formulaire, nous avons trois type de 
	formulaire qui nécessite un objet extra. nous avons le
	checkbox, le radiobutton et la liste déroulente.

"""
from .balises import balise,baliseOrph
class form(balise):
	def __init__(self,ident,method='GET',action="",
		bg_color = (255,255,255)):
		balise.__init__(self,'form')
		"""
			L'ident est très important dans le
			sens où il permettra d'identifier
			le but du formulaire
		"""
		self.ident = ident
		self.Set_attr('method',method)
		self.Set_attr('action',action)
		self.Field = None

		self.Set_bg_color(bg_color)

	@classmethod
	def get_style(cls,style,attrs_dic):
		if style:
			if type(style) == str:
				pass
			else:
				if 'class' in attrs_dic.keys():
					bal_name = f'.{attrs_dic["class"]}'
				elif 'id' in attrs_dic.keys():
					bal_name = f'#{attrs_dic["id"]}'
				else:
					bal_name = 'input'
				style = style.Run_css(bal_name)
			return style
		return ''

	def Begin_field(self,title,field_style = None,**inp_style):
		self.Field = balise('fieldset')
		leg = balise('legend')
		leg._No_css = True
		leg.Set_cont_obj(title)
		self.Field.Set_cont_obj(leg)
		if field_style:
			self.Field.Set_style(field_style)

	def End_field(self):
		self.Set_cont_obj(self.Field)
		self.Field = None

	def Set_input(self,Type,name,inp_style = None,
		lab_style = None,lab = True,required = True,
		**attrs_dic):
	#
		Inp = baliseOrph('input')
		Inp.Set_attr('type',Type)
		Inp.Set_attr('name',name)
		Inp.Set_attr('id',name)
		if required:
			Inp.Set_attr("required",'required')

		if Type!= 'submit' and lab == True:
			self.Set_label(name,style = lab_style,
				**{'for':name})
		Inp.Set_attrs(attrs_dic)
		if inp_style:
			Inp.Set_style(inp_style)
		if self.Field:
			self.Field.Set_cont_obj(Inp)
		else:
			self.Set_cont_obj(Inp)
##
	def Set_text_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('text',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_email_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('email',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_url_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('url',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_tel_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('email',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_number_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('number',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_range_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('range',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_file_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('file',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_date_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('date',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_password_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('password',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_time_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('time',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_week_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('week',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_month_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('month',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_search_input(self,name,inp_style = None,
		lab_style = None,**attrs_dic):
		self.Set_input('search',name,inp_style = inp_style
			,lab_style = lab_style,**attrs_dic)

	def Set_textarea(self,name,style=None,**attrs_dic):
		'''
			On peut utiliser les attributs:
				rows pour définir le nombre de ligne à afficher
				cols pour définir le nombre de colonnes à afficher
		'''
		tex = balise('textarea')
		attrs_dic["name"] = name
		tex.Set_attrs(attrs_dic)
		tex.Set_style(style)
		if self.Field:
			self.Field.Set_cont_obj(tex)
		else:
			self.Set_cont_obj(tex)
#
	def Set_label(self,cont,style = None,**attrs_dic):
		lab = balise('label')
		lab.Set_cont_obj(cont)
		lab.Set_attrs(attrs_dic)
		if style:
			lab.Set_style(style)
		if self.Field:
			self.Field.Set_cont_obj(lab)
		else:
			self.Set_cont_obj(lab)

	def Set_checkbox(self,obj_checkbox):
		"""
			Cette méthode est utiliser pour insérer un objet de
			type checkbox au formulaire. un checkbox est au préalable 
			définie par un objet checkbox avant d'être ajouter 
			au formulaire. 
		"""
		if self.Field:
			self.Field.Set_cont_obj(obj_checkbox)
		else:
			self.Set_cont_obj(obj_checkbox)

	def Set_radio(self,obj_radio):
		"""
			Cette méthode est utiliser pour insérer un objet de
			type radioButton au formulaire. un radioButton est au 
			préalable définie par un objet radioButton avant d'être 
			ajouter au formulaire. 
		"""
		if self.Field:
			self.Field.Set_cont_obj(obj_radio)
		else:
			self.Set_cont_obj(obj_radio)

	def Set_form_list(self,list_obj):
		"""
			Cette méthode est utiliser pour insérer un objet de type
			formList au formulaire. cet type permet de définir une 
			liste déroulente. Il doit être au préalable définie
			par l'objet formList.
		"""
		if self.Field:
			self.Field.Set_cont_obj(list_obj)
		else:
			self.Set_cont_obj(list_obj)

	def End_form(self,submit_name = 'Send',
		Submit_style = None,**attrs_dic):
		attrs_dic['value'] = submit_name
		self.Set_input('submit',self.ident,Submit_style,**attrs_dic)

'''
class checkBox(balise):
	def __init__(self):
		balise.__init__('p')

	def Set_title(self,cont,style = None):
		self.Set_cont_obj(cont)
		if style:self.Set_style(style)

	def Add_box(self,name,label = '',style = None,lab_style = None):
		"""
			Lorsque le label est définie à None, alors le checkbox
			n'aura pas de valeur d'indication.

			Si cette partie est laissée à la valeur par défaut, 
			alors, le label prend le nom du checkbox

			ici, l'utilisateur peut choisir plusieurs options
			qui seront envoyés plus tard au gestionnaires de 
			formulaire sous forme de liste.
		"""
		inp = baliseOrph('input')
		inp.Set_type("checkbox")
		inp.Set_attr('name',name)
		inp.Set_attr('id',name)
		if style:
			if type(style) == str:inp.Set_style(style)
			else: inp.Set_style(style.Run_css(f"#{name}"))
		if label != None:
			lab = balise('label')
			lab.Set_attr('for',name)
			if lab_style:
				if type(lab_style) == str:lab.Set_style(lab_style)
				else:
					lab.Set_attr('id',f'lab{name}')
					lab.Set_style(lab_style.Run_css(f"#lab{name}"))
			if label == '':
				lab.Set_cont_obj(name)
			else:
				lab.Set_cont_obj(label)
		self.Set_cont_obj(inp)
		self.Set_cont_obj(lab)

class radioButton(balise):
	def __init__(self,name):
		balise.__init__(self,'p')
		"""
			Pour cette partie, le nom est unique et utiliser 
			pour toutes les box mais la valeur diffère
		"""
		self.name = name

	def Set_title(self,cont,style = None):
		self.Set_cont_obj(cont)
		if style:self.Set_style(style)

	def Add_box(self,value,label ='',style=None,lab_style=None):
		inp = baliseOrph('input')
		inp.Set_type("radio")
		inp.Set_attr('name',self.name)
		inp.Set_attr('value',value)
		inp.Set_attr('id',value)
		if style:
			if type(style) == str:inp.Set_style(style)
			else: inp.Set_style(style.Run_css(f"#{value}"))
		if label != None:
			lab = balise('label')
			lab.Set_attr('for',value)
			if lab_style:
				if type(lab_style) == str:
					lab.Set_style(lab_style)
				else:
					lab.Set_attr('id',f'lab{value}')
					lab.Set_style(lab_style.Run_css(f"#lab{value}"))
			if label == '':
				lab.Set_cont_obj(value)
			else:
				lab.Set_cont_obj(label)
		self.Set_cont_obj(inp)
		self.Set_cont_obj(lab)

class formList(balise):
	def __init__(self,name):
		balise.__init__(self,'p')
		self.name = name

	def Set_title(self,titre,style = None):
		lab = balise('label')
		lab.Set_attr('for',self.name)
		if style:
			if type(style) == str: lab.Set_style(style)
			else:
				lab.Set_attr('id',f'lab{self.name}')
				lab.Set_style(style.Run_css(f'#lab{self.name}'))
		self.Set_cont_obj(lab)

	def Begin_option(self):
		self.Sel = balise('select')
		self.Sel.Set_attr('name',self.name)
		self.Sel.Set_attr('id',self.name)

	def Add_option(self,value,label = ''):
		op = balise('option')
		if label: 
			op.Set_cont_obj(label) 
		else:
			op.Set_cont_obj(value)
		op.Set_attr('value',value)
		self.Sel.Set_cont_obj(op)

	def End_option(self):
		self.Set_cont_obj(self.Sel)
		del self.Sel



'''