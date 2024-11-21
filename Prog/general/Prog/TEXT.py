#Coding:utf-8
Con = '''Un texte pour inciter
'''
EMAIL = "Email"
PASS = 'password'
VALIDER = 'Connexion'

SERVICE = 'Nos services'

Serv_dic = {
	"Agronomie":'/static/general/agron.jpg',
	"BTP":'/static/general/btp.jpg',
	"Enseignement":'/static/general/ensei.jpg',
	"Finance":'/static/general/finan.jpg',
	"Le Droit":'/static/general/juri.jpg',
	"Services mobiliers":'/static/general/mobil.jpeg',
	"La Santée":'/static/general/sante.jpg',
	"Sécurité":'/static/general/securi.jpg',
	"Service social":'/static/general/social.jpg',
	"Stylisme":'/static/general/style.jpg',
	"Location de voiture (VTC)":'/static/general/vtc.jpg',
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

