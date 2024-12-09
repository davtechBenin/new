#Coding:utf-8
Img_l = [
	("static/1.png","Page de connexion"),
	("static/2.png","Paramètre de l'admin"),
	("static/2_.png","Page d'accueil"),
	("static/3.png","Interface de la vente"),
	("static/4.png","Interface de la gestion de stock"),
	("static/5.png","Interface de la gestion des clients"),
	("static/6.png","Interface de la gestion financière"),
]

MENUS = ["Téléchargement","Installation","Utilisation"]

ACCUEIL = {
	"Commercio":'''Commercio est un ensemble de logiciel \
permettant la gestion complet d'une entreprise. Il couvre \
les domaines de la gestion de stock, la vente, la gestion \
des finances, la gestion du personel et la gestion des \
clients. Commercio est par défaut multi-utilisateurs, \
mutli-postes. Avec une interface simple et intuitive, Il \
se veut être l'un des meilleurs choix pour la gestion \
de votre activitée commerciale.\
'''
}
TELECHARGEMENT = {
	'Standart':(""" La version standart concerne particulièrement \
les utilisateurs qui désire avoir juste un système pour \
l'automatisation des factures. Il comprend essentiellement \
la gestion de stock et celui de la facturation.\
""",'20 000F CFA',"https://1drv.ms/u/c/9b8909ba9b8541f6/EelhAn3JbpZNnopeajc0hVABqwCGtrYVmYQt9DG6b_s6tA?e=WcQrTS"),
	'Pro':(""" Elle comprend le système de règlement de 
factures, donc la gestion des clients. Avec cette version, 
vous avez la possibilité de gérer votre stock, la vente \
a part entière et aussi les clients.\
""",'40 000F CFA',"https://1drv.ms/u/c/9b8909ba9b8541f6/EeBTx9gqUtRLomMAJr8rbfwBnwOIxufELInH1h7hB3qXZw?e=E0cPaG"),
	'VIP':(""" Le choix Premium, elle concerne la gestion \
du stock, la gestion de la vente, la gestion des clients \
la gestion des finances et aussi la gestion du personel. \
C'est le meilleur choix pour une gestion complète de votre \
entreprise.\
""",'50 000F CFA',"https://1drv.ms/u/c/9b8909ba9b8541f6/EYNNoQriDmhIm5L3esy8wikBPju6wtIU15LFKv2TT4cZYQ?e=dlrbHk"),
}
INFO_TEL = "Veillez choisir un Pack selon vos besoins"

INSTALLATION = {
	"Étape 1":('Installation du Serveur',"""Le serveur 
est le logiciel qui permet la gestion de la communication 
entre Commercio et la base de donnée. Si vous êtes 
en réseau Local, elle doit être installer et exécuter 
uniquement sur l'ordinateur Hôte. Mais vous avez 
un poste unique, installer le sur votre poste 
avant l'intallation de Commercio.
"""),
	"Étape 2":('Installation de Commercio',"""Une 
fois l'installation du serveur terminé, vous puvez à
présent installer le logiciel commercio en elle-même.
"""),
	
}
INFO_INSTALLATION = """\
Pour une prise en charge globale de notre politique 
multi postes, nous avons séparer le programme Commercio 
de son gestionnaire de base de donnée. Ainsi, pour 
son utilisation, vous aurez besoin d'installer 
les deux logiciels sur votre ordinateur mère.<br><br> 
Une fois le téléchargement terminer, veillez dézipper 
le fichier puis procéder comme suite: 
"""


UTILISATION = {
	"1. <b>Démarrage du serveur</b>":"""
Le Seveur doit être démarrer sur l'ordinateur 
hôte ou votre ordinateur unique avant le démarage 
de Commercio. Sinon, vous aurez simplement une erreur 
de connexion.
	""",
	"2. <b>Démarrage de Commercio</b>":"""
Une fois le serveur démarrer, vous pouvez à présent 
démarrer Commercio sans problème. Si c'est votre 
première utilisation, vous devez donc vous inscrire 
pour pour continuer mais dans le cas contraires, il 
faudra vous authentifier avant de pouvoir continuer.
	""",
}

INFO_UTILISATION = """\
A chaque utilisation, vous devez passer par les 
étapes Suivantes: 
"""



