#Coding:utf-8

def transform(x):
	if type(x) != str:
		if x <= 1:
			x*=100
		return (f"{x}%")
	else:
		return x

def transform_to_int(x):
	if type(x) == str:
		if 'px' in x:
			x = float(x[:-2])
		elif "%" in x:
			x = float(x[:-1])
	else:
		if x <= 1:
			x*=100
	return x

class style:
	def __init__(self,size = (100,100),
		bg_color = None,font_size = .97,
		pos = (0,0),pos_type = "absolute"):
	#
		self.cont = str()
		self.Css_dict = dict()
		self.width = 100
		self.height = 100

		
		if pos:
			self.Set_position_type(pos_type)
			self.Set_position(pos)
		self.Set_font_family('Lexend')
		self.Add_css('box-sizing','border-box')
		if bg_color:
			self.Set_bg_color(bg_color)
		else:
			self.bg_color = None
		if size:
			self.Set_size(*size)
		self.Set_font_size(font_size)

	def Init_css(self):
		self.cont = str()
		self.Css_dict = dict()

# Obtention de quelque propriété
	def Get_size(self,ind = None):
		size = (self.width,self.height)
		if type(ind) == int:
			return size[ind]
		else:
			return size

	def Get_bg_color(self,ind = None):
		if type(ind) == int:
			return self.bg_color[ind]
		else:
			return self.bg_color

	def Get_position(self,ind = None):
		if type(ind) == int:
			return self.pos[ind]
		else:
			return self.pos

	def Get_pos(self,ind = None):
		return self.Get_position(ind)

# Définition des style
	def Set_style(self,Obj_css):
		self.Css_dict.update(Obj_css.Css_dict)

	def Add_css(self,propriete,value):
		self.Css_dict[propriete] = value

	def Set_mult_css(self,dic):
		for pro in dic:
			self.Add_css(pro,dic[pro])

	def Set_min_width(self,value):
		self.Add_css('min-width',value)

	def Set_min_height(self,value):
		self.Add_css('min-height',value)

	def Set_max_width(self,value):
		self.Add_css('max-width',value)

	def Set_max_height(self,value):
		self.Add_css('max-height',value)

	def Set_width(self,value):
		self.width = transform_to_int(value)
		if type(value) in (int,float):
			value = transform(value)
		self.Add_css('width',value)

	def Set_height(self,value):
		self.height = transform_to_int(value)
		if type(value) in (int,float):
			value = transform(value)
		self.Add_css('height',value)

	def Set_size(self,width,height):
		self.Set_width(width)
		self.Set_height(height)

	def Set_overflow(self,value = 'scroll'):
		"""
			Cette méthode est utiliser lorsque l'on veut adapter
			le contenue d'une boite a la taille de la boite. 
			Normalement, cette méthode est utiliser seulement si 
			la largeur et la hauteur de la balise sont définies
			le value possible de value sont:
				-> scroll pour cacher le contenue restant mais afficher
					une barre de défillement
				-> visible pour rendre tout simplement visible tout 
					le contenue
				-> hidden permet de cacher le contenue débordente
				-> auto pour laisser le navigateur choisir quoi faire.
		"""
		self.Add_css('overflow',value)

	def Set_display(self,value):
		"""
			Les valeurs de display sont entre autre:
				block : permet convertir un élément en type block
				inline: permet de convertir un élément en type inline
				none: permet de cacher un élément
		"""
		self.Add_css('display',value)

	def Set_position(self,pos):
		x,y = pos
		
		x_ = transform_to_int(x)
		y_ = transform_to_int(y)
		if type(x) == str:
			X = x
		else:
			X = transform(x)
		if type(y) == str:
			Y = y
		else:
			Y = transform(y)

		self.pos = x_,y_
		self.Add_css("left",X)
		self.Add_css("top",Y)

	def Set_position_type(self,typ = 'absolute'):
		self.Add_css('position',typ)

	def Set_font_size(self,value,Type = "em"):
		# Type peut être 'em' 'px' '%'
		self.Txt_size = value
		value = f'{value}{Type}'
		self.Add_css('font-size',value)

	def Set_font_family(self,*nom_police):
		"""
			avec la possibilité de mettre plusieurs nom de police à la
			foi, on utilise une liste d'argument non définie.
		"""
		nm = str()
		for i in nom_police:
			nm += f"'{i}', "
		nm = nm[:-2]
		self.Add_css('font-family',nm)

	def Set_font_style(self,value):
		# value doit être soit normal ou italic
		self.Add_css('font-style',value)

	def Set_font_weight(self,value):
		# la value varie de 100 à 900
		self.Add_css('font-weight',value)

	def Set_text_decoration(self,value):
		# la value doit être entre 'underline', 'line-through','none'
		self.Add_css('text-decoration',value)

	def Set_underline(self,val = True):
		if val == True:
			self.Add_css('text-decoration','underline')
		else:
			self.Add_css('text-decoration','none')

	def Set_text_align(self,value):
		# value doit être entre 'left', 'center','right','justify'
		self.Add_css('text-align',value)

	def Set_text_color(self,value,Type = 'rgb'):
		#type peut être 'rgb', 'rgba', '#' ou str()
		if Type == '#':
			value = f"#{value}"
		elif Type:
			value = f'{Type}{value}'
		else:
			value = value
		self.Add_css('color',value)

	def Set_bg_color(self,value,Type = 'rgb'):
		self.bg_color = value
		#type peut être 'rgb', 'rgba', '#' ou str()
		if Type == '#':
			value = f"#{value}"
		elif Type:
			value = f'{Type}{value}'
		else:
			value = value
		self.Add_css('background-color',value)

	def Set_bg_image(self,link,bg_option = dict()):
		"""
		https://developer.mozilla.org/fr/docs/Web/CSS/background pour en savoir plus
			bg_option est un dictionnaire avec les clés suivants:
				attachment value(fixed,scroll,local)
				size value(cover)
				position value(top,bottom,left,center,right)
				origin value(border-box,padding-box,content-box)
				repeat value(no-repeat,repeat-x,repeat,space,round)
				clip value(border-box,padding-box,content-box,text)
		"""
		opt_di = {
			'attachment':'background-attachment',
			'size':'background-size',
			'position':'background-position',
			'origin':'background-origin',
			'repeat':'background-repeat',
			'clip':'background-clip'
		}
		link = f'url({link})'
		self.Add_css('background-image',link)
		for op in bg_option:
			self.Add_css(opt_di[op],bg_option[op])

	def Set_bg_gradient(self,color_stops,direction,color_Type = 'rgb'):
		"""
			color_stops doit être une liste de code. au minimum 2.
			baleur possible de direction:
				180deg -> pour converger vers le bas
				0deg -> pour converger vers le haut
				90deg -> pour converger vers la droite
		"""
		colors = str()
		for color in color_stops:
			if color_Type =='#':
				color = f"#{color}"
			elif color_Type:
				color = f"{color_Type}{color}"
			else:
				color = color
			colors+=f'{color}, '
		colors = colors[:-2]
		value = f"linear-gradient({direction},{colors})"
		self.Add_css('background-image',value)

	def Set_opacity(self,value):
		# value est comprise entre 0 et 1
		self.Add_css('opacity',value)

# border
	def Set_border(self,value,typ = 'solid',
		color = (0,0,0)):
		#la valeur est en pixel
		self.Add_css('border-width',f"{value}px")
		self.Add_css('border-style',typ)
		self.Add_css('border-color',f"rgb{color}")

	def Set_top_border(self,value,typ = 'solid',
		color = (0,0,0)):
		#la valeur est en pixel
		self.Add_css('border-top-width',f"{value}px")
		self.Add_css('border-top-style',typ)
		self.Add_css('border-top-color',f"rgb{color}")

	def Set_bottom_border(self,value,typ = 'solid',
		color = (0,0,0)):
		#la valeur est en pixel
		self.Add_css('border-bottom-width',f"{value}px")
		self.Add_css('border-bottom-style',typ)
		self.Add_css('border-bottom-color',f"rgb{color}")

	def Set_right_border(self,value,typ = 'solid',
		color = (0,0,0)):
		#la valeur est en pixel
		self.Add_css('border-right-width',f"{value}px")
		self.Add_css('border-right-style',typ)
		self.Add_css('border-right-color',f"rgb{color}")

	def Set_left_border(self,value,typ = 'solid',
		color = (0,0,0)):
		#la valeur est en pixel
		self.Add_css('border-left-width',f"{value}px")
		self.Add_css('border-left-style',typ)
		self.Add_css('border-left-color',f"rgb{color}")

# Radius
	def Set_border_radius(self,value,
		typ = "em"):
		if type(value) in (float,int):
			value = f"{int(value)}{typ}"
		self.Add_css('border-top-left-radius',value)
		self.Add_css('border-top-right-radius',value)
		self.Add_css('border-bottom-left-radius',value)
		self.Add_css('border-bottom-right-radius',value)

	def Set_border_top_left_radius(self,value,
		typ = "em"):
		if type(value) in (float,int):
			value = f"{int(value)}{typ}"
		self.Add_css('border-top-left-radius',value)

	def Set_border_top_right_radius(self,value,
		typ = "em"):
		if type(value) in (float,int):
			value = f"{int(value)}{typ}"
		self.Add_css('border-top-right-radius',value)

	def Set_border_bottom_left_radius(self,value,
		typ = "em"):
		if type(value) in (float,int):
			value = f"{int(value)}{typ}"
		self.Add_css('border-bottom-left-radius',value)

	def Set_border_bottom_right_radius(self,value,
		typ = "em"):
		if type(value) in (float,int):
			value = f"{int(value)}{typ}"
		self.Add_css('border-bottom-right-radius',value)

# Padding
	def Set_padding(self,value,typ = 'em'):
		self.Add_css("padding",f"{value}{typ}")

	def Set_padding_top(self,value,typ = 'em'):
		self.Add_css("padding-top",f"{value}{typ}")

	def Set_padding_left(self,value,typ = 'em'):
		self.Add_css("padding-left",f"{value}{typ}")

	def Set_padding_right(self,value,typ = 'em'):
		self.Add_css("padding-right",f"{value}{typ}")

	def Set_padding_bottom(self,value,typ = 'em'):
		self.Add_css("padding-bottom",f"{value}{typ}")

# Margin
	def Set_margin(self,value,typ = 'em'):
		self.Add_css("margin",f"{value}{typ}")

	def Set_margin_top(self,value,typ = 'em'):
		self.Add_css("margin-top",f"{value}{typ}")

	def Set_margin_left(self,value,typ = 'em'):
		self.Add_css("margin-left",f"{value}{typ}")

	def Set_margin_right(self,value,typ = 'em'):
		self.Add_css("margin-right",f"{value}{typ}")

	def Set_margin_bottom(self,value,typ = 'em'):
		self.Add_css("margin-bottom",f"{value}{typ}")

#Shadow
	def Set_box_shadow(self,rayon_flou,color,
		rayon_detalement = .3,colortype='rgb',
		inset = False,
		unit_typ = "px",off_x = 0,off_y = 0):

		pr = f'box-shadow'
		if colortype =='#':
			color = f'#{color}'
		elif colortype:
			color = f'{colortype}{color}'
		value = f"{off_x}{unit_typ} {off_y}{unit_typ} {rayon_flou}{unit_typ} \
{rayon_detalement}{unit_typ} {color}"
		if inset:
			value = "inset "+value
		self.Add_css(pr,value)

# Runs
	def Run_css(self,select):
		self.cont = self.Run_css_only()
		cont = f"""{select}"""
		cont+="{"
		cont+=f'{self.cont}'
		cont+='}'
		return cont

	def Run(self):
		return self.Run_css_only()

	def Run_css_(self,select):
		return self.Run_css(select)

	def Run_css_only(self):
		self.cont = str()
		for key,val in self.Css_dict.items():
			self.cont+=f'\n\t{key}: {val};'
		self.cont+='\n'
		return self.cont

	def Set_grid_column(self,start,end):
		self.Add_css('grid-column',f"{start} / {end}")

	def Set_grid_row(self,start,end):
		self.Add_css('grid-row',f"{start} / {end}")


