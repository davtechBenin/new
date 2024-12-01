#Coding:utf-8
Con = '''Un texte pour inciter
'''
EMAIL = "Email"
PASS = 'password'
VALIDER = 'Connexion'

SERVICE = 'Nos services'
LOGO = "/static/general/logo.jpg"

Serv_dic = {
	"Agronomie":LOGO,
	"BTP":LOGO,
	"Enseignement":LOGO,
	"Finance":LOGO,
	"Le Droit":LOGO,
	"Services mobiliers":LOGO,
	"La Santée":LOGO,
	"Sécurité":LOGO,
	"Service social":LOGO,
	"Stylisme":LOGO,
	"Location de voiture (VTC)":LOGO,
}

Cont_text = 'Services Technique'

Contact_dict = {
	"Whatsapp":'Numéro Whatsapp officiel',
	"Tel":'Numéro N° de tel officiel',
	"Page Fb":'Numéro Page Fb officiel',
	"Page Tiktok":'Numéro Page Tiktok officiel',
}

inscription_info = [
	((1,"Vos informations de Connexion"),("Email",
		"Mot de pass","Répéter le mot de pass")),

	((2,"Votre Identité"),("Nom","Prénom",
		"Date de naissance",'Genre')),

	((3,"Vos informations de Résidence"),("Pays",
		"Ville","Province",'Rue N°')),

	((4,"Vos Contacts"),("Téléphone","Whatsapp")),
]

CLIENT_NEW = """"""

CONN_ERROR = 'Email ou mot de pas Erronée'

