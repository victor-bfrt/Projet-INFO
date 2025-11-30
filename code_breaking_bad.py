import random
import time 

money = 30000
pv = 100
blue_crystal = 0
duree_1 = 1 
duree_05 = 0.5

choix0 = (0, 1, 2)  ### Racourci pas dans le vrai code ###
choix2 = (1, 2)
choix3 = (1, 2, 3)
choix4 = (1, 2, 3, 4)

# Toutes les fonctions #

def demander_choix(texte: str, rep_possibles: tuple):
    while True:
        r = input(texte)
        if r in ("q", "Q"):
            quit()
        if not r.isdigit():
            print("\n  ❌ Erreur : entre un nombre.\n")
            continue
        r = int(r)
        if r in rep_possibles:
            return r
        else:
            print(f"\n  ❌ Erreur : choisis parmi {rep_possibles}.\n")


def parole(texte, delai):  # Fonction pour afficher le texte progressivement
    for caractere in texte:
        print(caractere, end='', flush=True)  
        time.sleep(delai)
    print()  
	

def fin_histoire():
	message = " \n\n💸 FIN DE L'HISTOIRE 💸\n\n "
	delai = 0.05
	parole(message, delai)
	exit()


def sortie_GAV():
	message = "📌 Une fois sortie de cellule après ces quelques jour passer en garde à vue, votre femme apprend ce que vous avez fait... \nElle vous quitte et vous vire de la maison qu'elle possède ! Vous n'avez plus du tout d'argent et êtes livrer à vous mêmes pour survivre ..." 
	delai = 0.02
	parole(message, delai)


def la_quête_du_crackhead(sachets, money):
	print("\nTu es reçu par 6 fous du bus, chacun d'eux avec une bouteille de poliakov cassée en main.")
	print("Ils te demandent ce que tu viens faire ici. Au vu de leur apparence tu prends peur et part en courant.")
	time.sleep(duree_1)
	print("Tu repenses à l'argent que tu dois faire, tu choisis donc :")
	print(" 1) Retourner les voir en leur proposant d'acheter ta marchandise.")
	print(" 2) C'est une mauvaise idée de dealer avec eux et tu repars d'où tu viens.")
	réponse_crackhead = demander_choix("🔹 Que fais-tu ?", choix2)
	if int(réponse_crackhead) == 1:
		print("\nIls semblent être partant pour t'en acheter au début, mais l'un d'entre eux dit aux autres qu'ils ont juste à te voler.")
		print("Tu t'enfuies le plus vite possible, mais tu te retrouvent coincés dans un cul-de-sac.")
		time.sleep(duree_1)
		print("Ils te laissent le choix entre leur donner gentiment 3 sachets ou te les faire voler de force, après quoi tu leur donnes sans hésiter les sachets.")
		print("Avec tout le respect il te refile un vieux billet tout chiffoné de 5$ pour te remercier")
		time.sleep(duree_1)
		sachets -= 3
		money += 5   		
		return sachets, money
	elif int(réponse_crackhead) == 2:
		print("\nTu refuses de retourner voir le groupe, mais un des crack-head t’attend déjà sur le chemin.")
		print("Il insiste lourdement et finit par t'acheter 3 sachets pour 300$ d’un coup, tu acceptes volontier pour éviter les ennuis.")
		print("La transaction est rapide, tu prends l’argent et tu t’éclipses même si tu n'es pas en bénéfice.")
		time.sleep(duree_1)
		sachets -= 3
		money += 300
		return sachets, money


def distributeur_local(sachets, money):
	print("\nPendant qu'on t'emmenait voir Tuco, un des membres du gang t'as présenté les traficants du coin, et tu t'es dis que tu pouvais ta chance avec l'un d'entre eux, crazy 7")
	print("Tu arrives devant une grande villa avec deux garde du corps qui te font rentrer après avoir bien vérifié que tu n'avais pas d'arme sur toi.")
	print("Tu lui proposes d'acheter ta marchandise à 1500 euros le gramme, il te répond: ")
	time.sleep(duree_1)
	message = " - Tu sais que le prix normal est bien plus bas que ça, t'as intérêt à baisser tes prix si tu veux repartir d'ici en un seul morceau."
	délai = 0.03
	parole(message, délai)
	print("Tu lui répond:")
	message = " 1) - Je vend pas en dessous de ce prix même aux gens comme toi, c'est 1500$ ou rien.\n 2) - Je peux faire le prix général, 1000$ le sachet mais pas plus bas."
	délai = 0.03
	parole(message, délai)
	réponse_distributeur = demander_choix("🔹 Que réponds-tu?", choix2)
	if int(réponse_distributeur) == 1:
		message = " - T'as bien du cran pour quelqu'un de désarmé face à nous. J'aime bien ça! Payez le."
		délai = 0.03
		parole(message, délai)
		print("Les gardes te passe 1 sac remplie de billets, tu te dépêches de partir.")
		sachets -= 3
		money += 4500
		return sachets, money
	elif int(réponse_distributeur) == 2:
		message = " - Je te donnerai 800 euros par sachet tu vas me remercier."
		délai = 0.03
		parole(message, délai)
		print("Avant même que tu ai pu te plaindre, les 2 garde te passe un sac et te foutent dehors")
		sachets -= 3
		money += 2400
		return sachets, money


def boîte_de_nuit(sachets, money):
	print("Tu te rends à la boîte de nuit la plus connue de la ville, et c'est un succès total.")
	time.sleep(duree_1)
	print("T'as écoulé toute ta marchandise en moins d'un heure pour un très bon prix, 125 euros le gramme.")
	money += 1250*sachets
	sachets -= sachets
	time.sleep(duree_1)
	print(f"Tu viens de te faire {sachets*1250}$ ce soir là 💸")
	return sachets, money


def vendre_par_un_tiers(sachets, money):
	print("Tu cherches quelqu'un qui connaît le domaine pour vendre, et tu rappelle que l'ex de ta soeur était un toxico.")
	time.sleep(duree_1)
	print("Tu l'appelle en lui proposant de vendre pour toi en échange d'un pourcentage et il accepte directement. Tu lui donnes un délai de 3 jours.")
	time.sleep(duree_1)
	print("Après 3 jours sans nouvelles, tu décides finalement de te rendre chez lui pour comprendre ce qu'il se passe. Tu te retrouves face à lui et 4 de ses amis, tous en train de consommer ta marchandise.")
	time.sleep(duree_1)
	print("Tu récupères rapidement les sachets qui restent et prend la fuite, car tu sais qu'il n'a pas de quoi te rembourser 2 sachets qu'il t'as consommé.")
	sachets -= 2
	return sachets, money


def mission_dealeur_1(money):
	sachets = 12
	missions = {
        1: ("Aller au contact de la clientèle, directement en proposer aux crack-head sous le pont", la_quête_du_crackhead),
        2: ("Aller voir le distributeur local dont on t'a donné l'adresse", distributeur_local),
        3: ("Aller en boîte de nuit pour vendre", boîte_de_nuit),
        4: ("Envoyer une lointaine connaissance vendre pour toi en lui promettant sa part", vendre_par_un_tiers)
    }
	print(f"Vous disposez de {sachets} sachets de métamphétamine, chacun contenant 10 grammes, sachant que ça se vend généralement à 100$ le gramme.")
	print("Les instructions donné par le deauer sont clair, vous devez vendre tous ces sachets et rapporter 10000$ à Tuco. Le reste part dans votre poche.")
	print("Par contre, si vous n'êtes pas capables de ramener cet argent, ne vous attendez pas à rester en vie plus de quelques heures...")
	while sachets>0 :
		time.sleep(duree_1)
		print(f"\n 👉 Il vous reste {sachets} sachets à vendre, et vous avez {money}$ comment voulez procéder:\n")
		for num, (desc, _) in missions.items():
			print(f" {num}) {desc}")
		deal1 = int(input("\n🔹 Comment vend tu ta drogue ? : "))
		if deal1 not in missions:
			print("❌ Choix invalide.")
			continue
		desc, fonction = missions[deal1]
		sachets, money = fonction(sachets, money)  # Appeler la fonction et mettre à jour les sachets et money
		del missions[deal1]    # Supprimer la mission pour qu'on ne puisse plus la refaire
	print("\nC'est bon vous avez tout vendu ...")
	return sachets, money


def faire_tomber_TUCO(money):
	print("\n\n🤬vengeance")
	return money


def fuite(money):
	print("Tu part en sprintant en direction de la sortie, tu arrives à esquiver l'un des leurs.")
	print("Tu te retrouves dehors, et tu reconnais la voiture dans laquelle on t'avais emmené. Tu fais donc face à deux choix:")
	print("1) Aller en direction de la voiture et espérer que les clés sont restés sur le contact")
	print("2) Continuer de courir en espérant les perdre dans les ruelles voisines.")
	choix_fuite = demander_choix("🔹 Comment vous échappez vous?", choix2)
	voiture = random.randint(1,2)
	if int(choix_fuite) == 1 and voiture == 1:
		print("Gros coup de chance! Les clés sont encore là, tu t'empresses de démarrer pendant que les membres du gang sortent du batîment et commencent à te tirer dessus.")
		print("Plusieurs balles touchent la voiture, mais pas de blessures pour toi ni de disfonctionnement pour la voiture.")
		print("Tu t’éloignes et tu décides d’en finir : Tuco doit tomber.")
		faire_tomber_TUCO()
	
	elif int(choix_fuite) == 1 and voiture == 2:
		print("\nMauvaise nouvelle : la voiture est fermée...")
		print("Tu entends les pas du cartel se rapprocher.")
		print("Tu dois réagir vite :")
		print("1) Casser la vitre pour tenter de voler la voiture")
		print("2) Repartir en courant dans l’autre direction")
		
		choix_bloque = demander_choix("\n🔹Ton choix : ", choix2)
		action = random.randint(1, 2)
		
		if int(choix_bloque) == 1 and action == 1:
			print("\n💥 Tu éclates la vitre avec ton coude, ça fait un bruit énorme.")
			print("Tu montes, tu démarres… et tu parviens à t’enfuir de justesse.")
			time.sleep(duree_1)
			print("Tu t'es blessés légèrement en cassant la vitre")
			print("Après cet incident qui a faille te couter la vie tu réfléchis pour en finir avec Tuco")
			faire_tomber_TUCO(money)
		elif int(choix_bloque) == 1 and action == 2:
			print("\nTu tentes de casser la vitre mais le cartel t'attrappe avant que tu puisse partir.")
			print("Ils te frappent jusqu'à ta mort et prennent tout ce que tu as sur toi. 💀")
			fin_histoire()
		elif int(choix_bloque) == 2:
			print("\nTu t’enfuis dans une ruelle sombre.")
			print("Ils te poursuivent mais tu arrives à te cacher derrière une benne.")
			print("Tu les entends passer sans te voir. Tu as survécu. Tu décides de passer la nuit ici💤")
			time.sleep(duree_1)
			print("Le lendemain après avoir gamberger toute la nuit tu décides d’en finir : Tuco doit tomber.")
			faire_tomber_TUCO(money)
	elif int(chois_fuite) == 2:
		print("Le cartel de rattrape est commance à te frapper lourdement. Par chance Tuco arrive est ordonne qu'on arrête ton massacre")
		parole( " - Laissez le je crois qu'il compris la leçon, ici on ne me fais de coup de traite sinon voilà ce qui arrive. Maintenant pour te pardonner tu n'as pas d'autre choix que de travailler pour moi, je vais te faire découvrir notre labo et tu n'y sortiras pas tant que j'en n'aurais pas fini avec toi", 0.02)
		money = labo_de_TUCO(money)

def faible_paiement():
	print("🤨 Le montant est vraiment faible au vu de ce que tu as produits")
	rep = demander_choix("Veux tu te plaindre au près de Tuco ? \n 1)Oui c'est pas assez \n 2) Non c'est que le début il faut continuer à produire\n🔹 Ton choix : ", choix2)
	if rep == 1:
		print("\Tu te plains à Tuco du montant qu'il te donneprint\n👊 Tuco te choque contre le mur :")
		parole(" - T’AS UN PROBLÈME AVEC MA GÉNÉROSITÉ ? TU BOSSES POUR MOI, PAS POUR TON PORTE-MONNAIE !")
		trahison = True

	
def travailler_pour_TUCO(money):
	print("Tu lance ton processus automatisé pour cook la met, quel programme veut-tu utiliser")
	print("1) Mode Sécurisé – moins rentable mais zéro risque")
	print("2) Mode Boost – production plus élevée mais risque d'erreur")
	choix = demander_choix("🔹 Ton choix : ", choix2)
	etat_trahison = False
	purete = 0
	volume = 0
	if int(choix) == 1:
		print("\n💻 Le mode sécurisé et lancer sur quel autre paramètre veux-tu influencer la synthèse de la métamphétamine ?)
		print("1) Optimiser la quantité (volume ++) ")
		print("2) Optimiser la pureté (qualité ++) ")
		programme = demander_choix("🔹 Quel paramètre t'interesses : ", choix2)
      
		if int(programme) == 1:
			volume = random.randint(9, 15)
			purete = random.randint(50, 75)
			gain = volume * purete * 100
			money += gain
			print(f"\nPas mal ce que tu as produit ! {volume} kg de MET, pureté {purete}%.")
			print(f"💰 Tuco te paye {gain}$ (c'est raisonnable mais clairement pas tout vu le prix du marché)")
			if gain < 75000 :  
				faible_paiement()
				print("🤨 Le montant est vraiment faible au vu de ce que tu as produits")
				rep = demander_choix("Veux tu te plaindre au près de Tuco ? \n 1)Oui c'est pas assez \n 2) Non c'est que le début il faut continuer à produire\n🔹 Ton choix : ", choix2)
				if rep == 1:
					print("\Tu te plains à Tuco du montant qu'il te donneprint\n👊 Tuco te choque contre le mur :")
					parole(" - T’AS UN PROBLÈME AVEC MA GÉNÉROSITÉ ? TU BOSSES POUR MOI, PAS POUR TON PORTE-MONNAIE !")
					trahison = True
			else :
				input("🧑‍🔬Appuies sur entrée pour prendre ta part et continuer à bosser ...")
		
		elif int(programme) == 2:
			purete = random.randint(80, 95)
			volume = random.randint(2, 7)
			gain = purete * 100
			money += gain
			print(f"\nMet ultra pur ! {purete}% mais volume faible.")
			print(f"💰 Tuco te donne {gain}$… il se fout de toi.")
			if gain < 35000: # pureté forte mais paiement faible → trahison
				trahison = True
 
	elif int(choix) == 2:
		print("\n Tu lances le mode boost avec ton collégue Jesse pour:")
		print("1) Ajuster les catalyseurs (qualité ++ mais moins fiable)")
		print("2) Forcer la réaction (rapidité +++ volume +++ mais risque d'explosion)")
		cuisson = demander_choix("🔹 Quel cuisson chois-tu ? : ", choix2)
		if int(cuisson) == 1:
			purete = random.randint(50, 70)
			volume = random.randint(2, 4)
			gain = purete * 5
			money += gain
			print(f"Met OK. Pureté {purete}%.")
			print(f"💰 {gain}$ reçus… Tuco t’ignore.")
			if gain < 200:  
				trahison = True

		elif int(cuisson) == 2:
            # 1 chance sur 3 de tout foirer
			if random.randint(1, 3) == 1:
				print("\n💥 Explosion dans le labo gros flop, Tuco t'engueule alors que c'est lui qui t'as enseigné, il veut que tu paye le nettoyage et lematos cassé")
				money -= 1000
				purete = 0
				volume = 0
				trahison = True
			else:
				volume = random.randint(5, 10)
				purete = random.randint(40, 60)
				gain = purete * volume
				money += gain
				print(f"Batch massif : {volume} unités.")
				print(f"💰 Tu reçois {gain}$… mais il semble que le compte n'y est par rapport au volume et prix du marché.")

	return money, etat_trahison, purete, volume


def labo_de_TUCO(money):
	input("\nAppuyer sur Entrée pour suivre Tuco dans le labo 🧑‍🔬\n")
	print("La pièce est remplie de matériel de chimie… des tubes, des câbles, des machines, des PC.")
	parole(" - On m’a dit que t’étais bon en informatique… tu vas me le prouver,tu vas travailler pour moi. Ton objectif c'est de me coder un programme qui cook la MET la plus pure ! Tu ne seras pas seul, Jesse sera ton partenaire", 0.03)
	time.sleep(duree_1)
	print("\nTuco sort et vous laisse à deux avec Jesse, il t’explique ainsi les grandes étape de la synthèse de la métanphétamine 🧪.")
	etat_trahison = False
	input("\nAppuyer sur Entrée pour commencer à cook de la met 🧑‍🔬\n")
	parole(" - Salut Walter moi c'est Jesse, ensemble on va cook de le met, le boss Tuco a besoin de toi pour que tu m'aide à programmer un système qui automatise la production de la MET la plus pure !", 0.03)
	time.sleep(duree_1)
	print("Tu t'installes est prend commnce à coder sur un PC plusieur programmes différents 👨‍💻\n Tu passes la nuit entière à coder un logiciel qui sera répondre au attente de Tuco")
	time.sleep(duree_1)
	parole("\n>>>Script exucted ... \n01101010011101110\n01100011101101010\n11010110010010010\n01100011101101010\n01101010011101110 >>>Ready to cook\n", 0.02)
	time.sleep(duree_1)
	print("Ton logiciel est prêt, à toi de choisir avec Jesse quel programme éxecuter pour cook efficacement et faire un max de fric 💰\n")
	time.sleep(duree_1)
	trahison = False
	while not trahison:
		money, etat_trahison, purete, volume = travailler_pour_TUCO(money)
		print(f"\n➡️ Ton argent total : {money}$")
		print("➡️ Le business continue… pour l’instant.")
	
	print("\n❗ Tu réalises que Tuco t’arnaque et ne te respectera jamais, tu pense donc à échapper à cela")
	

def le_cartel():
	money = 0
	input("\nAppuyez sur Entrée pour commencez à dealer...")
	message = "\n💰C'est le début de votre aventure dans le monde du narcotrafique💰\n"
	delai = 0.02
	parole(message, delai)
	time.sleep(duree_1)
	_, money = mission_dealeur_1(money)
	print("\nMaintenant il faut rendre les bénéfice de tes ventes à Tuco")
	print(f"En vendant toute la drogue tu as réussi à te faire {money}$, vous vous rendez donc au QG de Tuco pour lui ramener le fric")
	input("\n Appuies sur Entrée pour rendre l'argent au Big Boss Tuco...")
	print("\nTuco te regarde sans cligner des yeux. Son sourire nerveux t’indique que t’as pas intérêt à le décevoir.")
	time.sleep(1)
	if money < 10000:
		message = f"\n - {money}$ ?! Tu te fous de moi ? Elle est passée où toute ma cam !!? Il est où mon putain de fric ?! Tu vas le payer cher !🤬 "
		délai = 0.03
		parole(message, délai)
		print("Il attrape une batte de baseball derrière lui et commence à avancer vers toi.")
		print("\nTu n’as qu’une seule option : COURIR.")
		input("\nAppuyez sur Entrée pour COURIR !!!\n")
		money = fuite(money)
	else:
		print("\n💵 Tu tends l'argent. Tuco compte rapidement les billets, renifle, puis explose de rire.")
		message = " - Pas mal… PAS MAL DU TOUT ! "
		délai = 0.03
		parole(message, délai)
		print("Il te balance une liasse supplémentaire.")
		bonus = 100*random.randint(1, 50)
		money += bonus
		print(f"\n💰 Tuco t’offre un bonus de {bonus}$ pour ta 'motivation'. Nouveau total : {money}$")
		message = " - Maintenant que t’as prouvé que t’es pas un rigolo… on va passer aux choses sérieuses. "
		délai = 0.03
		parole(message, délai)
		print("Tuco ouvre une porte métallique derrière lui.")
		message = "\n - 🧪 Bienvenue dans le vrai business ! "
		délai = 0.03
		parole(message, délai)
		time.sleep(duree_1)
		money = labo_de_TUCO(money)
		money = faire_tomber_TUCO(money)
	
	
def introduction():
	message = "\n💸A BREAKING BAD STORY💸\n\nVous êtes Walter Black, un professeur d'informatique au lycée.👨‍💻\nEn vous réveillant, vous checker vos mails et apprenait que la direction vous a viré car votre métier se fait remplacer par une intelligence artificielle.\nCette nouvelle vous attriste car ces derniers temps, vous avez quelques soucis financiers... "
	delai = 0.005
	parole(message, delai)

	# Premier choix
	message = "Pendant que vous déprimé votre collègue vous appel car il a reçu le même mail\nFace à la situation vous décidez :\n 1)De sortir boire un coup au bar pour vous changer les idées\n 2)D'aller manifester devant le lycée avec d'autres enseignants dans votre cas "
	delai = 0.005
	parole(message, delai)
	demander_choix
	reponse_1 = demander_choix("🔹 Quel est ton choix(sélectionnez le numéro) : ", choix0)

	# Branche 1
	if int(reponse_1) == 1:
		print("\nUne fois au bar le moral n'est toujours pas au top vous enchaînez verres de bière et de whisky, votre collègue vous propose un plan pour se refaire aller au casino !") 
		print("Alors que l'alcool monte petit à petit vous décidez :" )
		print(" 1)Refuser et continuer à boire pour oublier vos problèmes\n 2)Aller tenter votre chance au casino !")
		reponse_1_1 = demander_choix("🔹 Que choisissez-vous ? : ", choix2)
	
		# Branche Ivre
		if int(reponse_1_1) == 1:
			print("\nVous finissez complètement arraché, torse nu dans le bar, des élèves de votre lycée vous ont filmés vous faire sortir par le videur, avec lequel vous avez démmaré un combat.")
			print("Sans grande surprise, il vous bat et vous rentrez chez vous. Votre femme vous découvre complètement ivre, et sachant que vous n'avez plus de travail, elle décide de vous quitter et de vous virer de la maison qu'elle possède.")
			print("Face à la situation vous décidez :")
			print(" 1)Vous décidez de resortir boire comme hier soir car vous en pouvez plus de votre situation\n 2)Vous décidez de reprendre votre vie en main et d'aller trouver un emploie chez pôle emploie.")
			reponse_1_1_1 = demander_choix("🔹 Que choisissez-vous ? : ", choix2)
			if int(reponse_1_1_1) == 1:
				print("\nVous sombrez dans l'alcool, vous perdez tout ce que vous avez dans l'unique objectif de pouvoir acheter une bouteille de plus. Chaque jour devient le même, une bouteille de vodka à la main en dormant sous un pont.")
				fin_histoire()
			elif int(reponse_1_1_1) == 2:
				print("\nÀ cause de l'essor de l'intelligence artificielle, vous avez des difficultés à trouver un travail adapté à vos compétences, vous vous résignez et partez travailler à McDo.") 
				print("Cela suffit à combler vos besoins, et sans ambitions, vous continuez votre vie ainsi jusqu'à la retraite, une vie simple en fin de compte.")
				fin_histoire()
			
		# Branche Casino
		elif int(reponse_1_1) == 2:
			money = 30000
			print("\nEt vous voilà arrivez au CASINO !🎰 ")
			time.sleep(duree_1)
			print(f"Vous disposez de {money}$, ce qui correspond à tout l'argent que vous avez de côté, y compris l'argent qui est censé rembourser vos prêts et payer les études de votre enfant. Vous décidez de tout mettre en un coup à la roulette.")
			tours = 0
			while tours < 5:
				print(f"\nTour {tours+1} — Mise actuelle : {money}$")
				print("Vous choisissez de mettre tout votre argent sur le :\n 1)Rouge\n 2)Noir.")
				choix_casino = demander_choix("🔹 Quel est votre choix?", choix2)
				resultat = random.randint(1, 2)
				time.sleep(duree_1)
				message = "\nLa roue tourne ... ♣️♦️♠️♥️"
				delai = 0.02
				parole(message, delai)
				time.sleep(duree_05)
				if int(choix_casino) == resultat:      # Victoire
					money = 2*money
					tours = tours + 1
					print(f"\nBravo ! Tu gagnes. Ton argent double : {money}$.")
					if tours == 5:
						print(f"JACKPOT ! Tu as gagné 5 fois d’affilée.")
						print(f"Tu repars avec {money}$ !!! Vous êtes riche !!! Largement suffisant pour démarer une nouvelle vie loin de tout problèmes et proche de toutes les babies dont vous rêvez!!!!")
						fin_histoire()
					time.sleep(duree_05)
					print(f"Comme vous n'êtes pas très futé, vous décidez de remettre tout vos gains en jeux, c'est à dire {money}$")
				else :  
					money = 0
					print("\nDommage ! La balle ne tombe pas sur votre couleur...")
					print(f"Vous avez perdu TOUTES vos économies vous ne disposez plus que de {money}$")
					break 
			time.sleep(duree_1)
			print("\nVous êtes dépité, viré du casino et n'avait plus un seul euros sur vous ! Un homme en capuche s'approche de vous et vous propose ce deal : ")
			message = " - Je t'ai entendu parler dans le casino, je sais que t'as plus rien et que tu t'y connais en informatique. Je te propose un nouveau job, où tu gagneras en un mois ce que t'aurais gagné en une vie. J'étais comme toi y'a plusiseurs années, maintenant je suis plein aux as..."
			délai = 0.03
			parole(message, délai)
			print("Que lui répondez vous ?")
			print(" 1) \"Au point où j'en suis je n'ai plus rien à perdre dis moi en plus\"\n 2) \"Non ça ira je ne suis pas intéressé\"")
			décision = demander_choix("🔹 Quel est votre choix?", choix2)
			if int(décision) == 1 :
				print("\nVous acceptez sans réfléchir. L'homme vous emmène dans une voiture.")
				print("Il vous tend des sachets métanphétamine et sors un flingue en vous menaçant :")
				message = " - Tiens, ta première mission, revend tous ça d'ici la fin de semaine et ramène le fric au big boss Tuco c'est le seul moyen de faire tes preuves dans notre cartel, après ça on en aura pas fini avec toi crois moi bien!" 
				délai = 0.03
				parole(message, délai)
				print("Trop tard pour reculer, vous n'avez pas d'autre choix que de dealer.")
			elif int(décision) == 2 :
				print("\nVous refusez et tentez de partir pour rentrer chez vous")
				print("L'homme vous rattrappe aussitôt, sors un flingue, canon sur la tempe il vous dit :")
				message = " - Je crois t'as pas bien compris petit merdeux ici c'est moi qui décide, et j'ai décidé que tu allé travailler pour moi, revend moi ces sachets de méthamphétamine d'ici la fin de semaine et ramène le fric au big boss Tuco !"
				délai = 0.03
				parole(message, délai)
				print("Vous êtes dans une impasse pas d'autre choix que d'obéïr aux ordres")

			le_cartel() # Début dans le cartel

	# Branche 2 Manifestation
	elif int(reponse_1) == 2:
		print("\nAvec d'autres professeurs vous organisez un blocus devant le lycée et des étudiants vous rejoignent pour manifester. ")
		print("La manifestation dégénère rapidement, car de nombreux casseurs s'étaient infiltrés dans vos rangs et les CRS sont appelés. Ces derniers commence à gazer vos collègues. Révolté, vous décidez de:")
		print(" 1) Sortir votre paff et leur courir dessus.\n 2) Tenter un 1v1 avec un CRS malgré le fait que vous soyez moins imposant qu'un moustique.\n 3) Dire à un CRS que sa soeur est belle (mauvaise idée).\n 4) Leur jeter dessus le plus gros pavé que vous trouvez.")
		reponse_2 = demander_choix("🔹 Quel est votre choix?", choix4)
		if int(reponse_2) in [1, 2, 3, 4]:
			print("\nÉnerver un CRS n'était clairement pas une bonne idée...")
			print("Vous êtes placé en garde à vue. Chaque journée semble interminable.\n")
			jour = 1
			nb_jours = 3   # durée de la garde à vue
			while jour <= nb_jours:
				time.sleep(duree_1)
				message = f"\n📅 Jour {jour} de garde à vue"
				délai = 0.05
				parole(message, délai)
				time.sleep(duree_1)
				print("Les policiers pensent que vous cachez encore quelque chose.")
				print("Ils vous interrogent toute la journée...\n")
				jour = jour + 1
			time.sleep(duree_1)
			print("La garde à vue prend fin après ces longues heures de pression.")
			print("Malgré le fait que les policiers ont décidés d'abandonner la garde à vue, ils décident de vous faire passer un peu de temps en cellule avec des personnes très peu sympatiques, le temps de gérer la partie admistrative...")
			time.sleep(duree_1)
			print("\nUn de vos condétenu, un géorgien de 2m10 et 110kg de muscle avec un t-shirt et un short ufc, vous demande de lui passer vos chaussures car \"elles lui iraient très bien\".")
			print("Vous décidez de:\n 1) Le frapper le plus fort possible au visage, même si son menton semble plus solide que les barreaux de votre cellule.\n 2) Vous lui passez vos chaussures comme le bon toutou que vous êtes.")
			(reponse_2_1) = demander_choix("🔹 Quel est votre choix?", choix2)
			if int(reponse_2_1) == 1:
				print("\nVous vous faites mal à la main en essayant de le frapper, il finit par vous soulever et vous lancer sur le sol de la celulle.\nIl récupère vos chaussures pendant que vous pleurez par terre.")
			elif int(reponse_2_1) == 2:
				print("\nContent de sa nouvelle paire de chaussures, il décide de vous laisser tranquile pour le reste du temps.")
			time.sleep(duree_1)
		
			print("Un autre codétenu vous aborde, il vous explique qu'il est un dealer et il vous propose d'acheter ou de rentrer dans son réseau.")
			print("Vous décidez de:\n 1) Acheter un peu de métamphétamine pour votre consommation personnelle.\n 2) Vous acceptez son offre car vous n'avez plus rien, c'est votre seul moyen de faire de l'argent.\n 3) Vous le dénoncez au policier qui surveille votre cellule car vous savez que vous sortez avant lui")	
			reponse_DEAL = demander_choix("🔹 Quel est votre choix?", choix3)
		
			if int(reponse_DEAL) == 1 :
				print("\nVous acceptez « juste pour essayer ». Le codétenu vous glisse un petit morceau de cristal.")
				print("Vous hésitez… puis vous le prenez. Quelques minutes plus tard, un rush violent vous traverse, des sensations fortes.")
				print("Votre cœur bat à 200, vous êtes dans un état second.")
				print("Mais quand l’effet retombe, un vide énorme vous frappe.")
				input("\nAppuyez sur Entrée pour continuer...")
				print("\nLe lendemain matin, le codétenu vient vous voir :")
				message = " - Alors, ça t’as plu ? J’en ai encore si tu veux… mais cette fois tu paies. "
				délai = 0.03
				parole(message, délai)
				print("\nVous décidez de :")
				print(" 1) Reprendre une dose .")
				print(" 2) Refuser… mais vous n'avez pas de quoi payer la première dose.")
				choix_drogue = demander_choix("🔹 Quel est votre choix?", choix2)
			
				if int(choix_drogue) == 1 :
					print("\nVous craquez. Vous en voulez encore. Vous tendez la main.")
					print("Le codétenu sourit :\n - « Je le savais. »")
					time.sleep(duree_1)
					print("Vous avalez la dose, mais cette fois votre corps ne tient pas.")
					time.sleep(duree_1)
					print("Overdose. Vous ne vous relevez jamais.")
					print("La consommation de stupéfiant est dangereuse pour votre santé ceci est un message du gouvernement.")
					fin_histoire()
				
				elif int(choix_drogue) == 2 :
					print("\nVous refusez. « Non merci, hier c’était une erreur. »")
					print("Le codétenu change soudain de visage :")
					message = " - « Ah ouais ? Donc tu consommes gratos maintenant ? Tu crois que je fais ça par charité ? »"
					délai = 0.03
					parole(message, délai)
					print("\nIl s’approche de vous, tout près :")
					message = " - Tu vas rembourser. Et tu vas rembourser en travaillant pour moi. "
					délai = 0.03
					parole(message, délai)
					print("Il vous met dans la main un petit sachet : ")
					message = " - Tu vas le refourguer discret. Si tu refuses… Quand tu sortiras dehors on te retrouvera et ton fera la peau si tu nous trahi. "
					délai = 0.03
					parole(message, délai)
					print("\nVous êtes désormais forcé dimport time e dealer pour rembourser votre ‘dette’.")
					print("Au même instant on vous annonce que vous êtes liberé c'est la fin de votre séjour en cellulle")
					sortie_GAV()

		
			elif int(reponse_DEAL) == 2 :
				print("\nVous acceptez la proposition :")
				message = " - « Bienvenue dans l’entreprise. »"
				délai = 0.03
				parole(message, délai)
				print("\nIl vous glisse discrètement une dizaine de petits sachets dans la main, c'est de la metanphétamine.\n")
				message = " - « Tu les écoules aujourd’hui. Prix simple : 500$ la dose. Tu prend 50% pour toi et le reste tu iras les données au big boss Tuco. »"
				délai = 0.03
				parole(message, délai)
				print("Vous venez officiellement d'entrer dans la famille. Et en sortir sera presque impossible.")
				print("Au même instant on vous annonce que vous êtes liberé c'est la fin de votre séjour en cellulle")
				sortie_GAV()

		
			elif int(reponse_DEAL) == 3 :
				print("\nVous signalez discrètement le dealer au policier. En quelques secondes, il se fait attraper.")
				print("Il vous fixe avec une intensité glaçante pendant qu’on l’emmène. Vous savez que ce regard n'annonce rien de bon.")
				print("Les policiers vous félicitent :")
				message = " - « Grâce à vous, on a attrapé un gros poisson. Vous êtes officiellement libre. »"
				délai = 0.03
				parole(message, délai)
				sortie_GAV(money)
				time.sleep(duree_1)
				print("Dehors une camionnette noire s’arrête juste devant vous. Deux hommes descendent.")
				print("C’est le réseau du dealer. Ils vous attrapent sans un mot.")
				input("\nAppuyez sur Entrée pour continuer...")
				print("\nDans un hangar, ils vous expliquent les choses très clairement :")
				message = " - Tu as dénoncé l’un des nôtres. Maintenant tu as deux options : \n 1) Travailler pour nous. Vendre. Livrer. Fermer ta bouche.\n 2) Disparaître sous une dalle de béton et ne plus jamais poser de problèmes. "
				délai = 0.03
				parole(message, délai)
				time.sleep(duree_1)
				choix_final = demander_choix("🔹 Quel est votre choix?", choix2)
			
				if int(choix_final) == 1 :
					print("\nVous baissez les yeux. Vous savez que vous n’avez aucune autre issue.")
					print("« J’accepte. »")
					print("L’homme sourit : ")
					message = "« - Bonne décision. On aime les gens intelligents. Tu commences aujourd’hui. Si tu tentes de fuir… tu connais la suite. Vend tout ces sachets de drogues pour la fin de semaine et ramène le fric au big boss Tuco »"
					délai = 0.03
					parole(message, délai)
					print("\nVous êtes libre… mais uniquement pour servir leur réseau.")
					sortie_GAV()
		
				elif int(choix_final) == 2 :
					print("\nVous refusez catégoriquement de collaborerer.")
					print("Il soupire, se relève, et fait un signe de tête.")
					time.sleep(duree_1)
					print("\nUn homme s’approche derrière vous")
					time.sleep(duree_1)
					print("PANNN !!")
					message = "Vous êtes mort 💀"
					délai = 0.08
					parole(message, délai)
					fin_histoire()
				
			# Début dans le cartel
			le_cartel()

	if int(reponse_1) == 0: # Racourci si on a la flemme d'afficher tout le programe pour vérifier la suite 
		le_cartel()

def jouer():
	introduction()

jouer() # Fin du code appel
	
