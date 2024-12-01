#Coding:utf-8

OPT_LIST = [
	"Tableau de bord",
	"Mes Favoris",
	"Services Générals",
	#"Messageries",
	"Mes commandes",
	"Plus",
	"Profile",
	"Déconnexion"
]

LOGO_TEXT = "Le Rupin Sarl"

LOGO = "/static/general/logo.jpg"

PANIER_TEXT = "Votre Panier"
CATEGORIE_TEXT = "Catégories totals"
ARTICLE_TEXT = "Articles totals"
COMMANDE = "Vos principaux commandes"

ENCOURS = 'Commandes en cours de traitement'
REJETTER = 'Commandes rejettées'
ACCEPTER = 'Commandes acceptées'
SATISFAIT = 'Commandes satisfaits'

HISTORIQUE = "Vos activitées récentes"

MESSAGE = "Services Techniques"


SF_TEXT = "Vos services Favoris"

AC_TEXT = "Vos activitées récentes"

INFO_Perso = "Identité"

INFO_Resid = 'Résidence'

INFO_CON = 'Vos informations de connexion'

INFO_CONT = 'Vos contacts'

NO_C_MES = "Pas de commande pour le moment!"

NO_H_MES = "Pas d'activitées récentes"

NO_BF_MES = "Pas de Boutiques Favoris enrégistrées"

NO_SF_MES = "Pas de Sevices Favoris enrégistrées"

def GET_PART_INFO(part):
	P = f"Pas de '{part}' pour le moment"
	return P

ORG_REC = "Une présentation de l'organisation"

PRESENT_REC = "La présentation du programme de récrutement"

PRESENT_FORM = "Si vous souhaitez travailler pour nous, \
veillez remplir les informations qui suit."

"""
	Ici:
		but:info
"""

CV_but = "Votre CV"
prof_but = 'Profile'
mes_but = "Message"
REC_PART = {
	prof_but:"Les informations sur votre Identité",
	CV_but:"Vos informations professionelles",
	mes_but:"Un petit message d'engagement",
}

PRESENT_STATUS = "Votre demande est envoyer"

PRESENT_VAL = 'Votre demande est approuver.\
 Utiliser les informations suivantes pour vous \
connecter à votre espace de travail'

FELICITATION_PESENT = 'Félicitation à vous'.upper()

CV_INFO = "le fichier numérique de votre CV. \
(Un fichier pdf augementera votre chance)!"

SMS_INFO = "Un message de motivation montrant votre \
volonté et votre engagement pour le travail."

