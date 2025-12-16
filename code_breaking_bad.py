import random
import time 

money = 30000

choix2 = (1, 2)
choix3 = (1, 2, 3)
choix4 = (1, 2, 3, 4)
choix5 = (1, 2, 3, 4, 5)
choix6 = (1, 2, 3, 4, 5, 6)

VERT = "\033[92m"
FOND_BLANC = "\033[47m"
NOIR = "\033[30m"
RESET = "\033[0m"

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

def parole(texte, delai):
    for caractere in texte:
        print(caractere, end='', flush=True)  
        time.sleep(delai)
    print()  
	
def fin_histoire():
	parole(" \n\n  --- 💸 FIN DE L'HISTOIRE 💸 ---  \n\n ", 0.05)
	print("""⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠛⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⣿⣿⠆⢸⣿⠿⢿⠿⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⣤⣄⡀⢻⣿⠀⢈⣴⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠿⠿⠃⢸⣿⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣶⣶⣶⣾⣿⣿⣶⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢰⣶⣦⠈⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢈⣉⡁⠰⣿⣟⣡⣤⡈⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⣿⠿⠀⣸⡏⢡⣶⠀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⣤⣤⣤⣶⣿⣷⣤⣴⣧⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇""")
	exit()

def sortie_GAV(money):
	money = 0
	time.sleep(1.5)
	print("\n-------------------------------")
	parole("Une fois sorti de cellule après ces quelques jours passés en garde à vue, votre femme apprend ce que vous avez fait... \nElle vous quitte et vous vire de la maison qu'elle possède !\nVous n'avez plus du tout d'argent et êtes livrer à vous mêmes pour survivre ...🦧", 0.01)
	print("-------------------------------")
	return money
	
def la_quête_du_crackhead(sachets, money):
	parole("\nTu es reçu par 6 fous du bus, chacun d'eux avec une bouteille de poliakov cassée en main.", 0.01)
	parole("Ils te demandent ce que tu viens faire ici. Au vu de leur apparence, tu prends peur et pars en courant.", 0.01)
	time.sleep(1)
	print("Tu repenses à l'argent que tu dois faire, tu choisis donc :")
	print(" 1) Retourner les voir en leur proposant d'acheter ta marchandise.")
	print(" 2) C'est une mauvaise idée de dealer avec eux et tu repars d'où tu viens.")
	réponse_crackhead = demander_choix("🔹 Que fais-tu ?", choix2)
	if int(réponse_crackhead) == 1:
		parole("\nIls semblent être partant pour t'en acheter", 0.005)
		parole("Mais l'un d'entre eux dit aux autres qu'ils ont juste à te voler.", 0.005)
		parole("Tu t'enfuies le plus vite possible, mais tu te retrouves coincé dans un cul-de-sac.", 0.005)
		time.sleep(1)
		parole("Ils te laissent le choix entre leur donner gentiment 3 sachets ou te les faire voler de force, après quoi tu leur donnes sans hésiter les sachets.", 0.005)
		parole("Avec tout le respect, ils te refilent un vieux billet tout chiffoné de 5$ pour te remercier", 0.005)
		time.sleep(1)
		sachets -= 3
		money += 5   		
		return sachets, money
	elif int(réponse_crackhead) == 2:
		parole("\nTu refuses de retourner voir le groupe, mais un des crack-head t’attend déjà sur le chemin.", 0.005)
		parole("Il insiste lourdement et finit par t'acheter 3 sachets pour 300$ d’un coup, tu acceptes volontier pour éviter les ennuis.", 0.005)
		parole("La transaction est rapide, tu prends l’argent et tu t’éclipses même si tu ne fais pas de bénéfices.", 0.005)
		time.sleep(1)
		sachets -= 3
		money += 300
		return sachets, money

def distributeur_local(sachets, money):
	time.sleep(1)
	print("\nEn rentrant dans le cartel on t'a parlé des grands dealeurs du coins en particulier CRAZY 7")
	print("Tu rends alors visite à CRAZY 7, deux gardes du corps te font rentrer après avoir bien vérifié que tu n'avais pas d'arme sur toi.")
	time.sleep(1)
	print("Tu lui proposes d'acheter ta marchandise à 1500 euros le gramme, il te répond: ")
	time.sleep(1)
	parole(" - Tu sais que le prix normal est bien plus bas que ça, t'as intérêt à baisser tes prix si tu veux repartir d'ici en un seul morceau.", 0.03)
	time.sleep(0.5)
	print("Tu lui réponds:")
	parole(" 1) - Je vends pas en dessous de ce prix même aux gens comme toi, c'est 1500$ ou rien.\n 2) - Je peux faire le prix général, 1000$ le sachet mais pas plus bas.", 0.03)
	réponse_distributeur = demander_choix("🔹 Que réponds-tu?", choix2)
	if int(réponse_distributeur) == 1:
		parole(" - T'as bien du cran pour quelqu'un de désarmé face à nous. J'aime bien ça! Payez le.", 0.03)
		time.sleep(1)
		print("Les gardes te passent 1 sac rempli de billets, tu te dépêches de partir.")
		sachets -= 3
		money += 4500
		return sachets, money
	elif int(réponse_distributeur) == 2:
		parole(" - Je te donnerai 800 euros par sachet et tu vas me remercier.", 0.03)
		print("Avant même que tu ais pu te plaindre, les 2 gardes te passent un sac et te foutent dehors")
		sachets -= 3
		money += 2400
		return sachets, money

def boîte_de_nuit(sachets, money):
	print("Tu te rends à la boîte de nuit la plus connue de la ville, et c'est un succès total.")
	time.sleep(1)
	print("T'as écoulé toute ta marchandise en moins d'un heure pour un très bon prix, 125 euros le gramme.")
	benef = 1250*sachets
	money += benef
	sachets -= sachets
	time.sleep(1)
	print(f"Tu viens de te faire {benef}$ ce soir là 💸")
	return sachets, money

def vendre_par_un_tiers(sachets, money):
	print("Tu cherches quelqu'un qui connaît le domaine pour vendre : l'ex de ta soeur était un toxico.")
	time.sleep(1)
	print("Tu l'appelles en lui proposant de vendre pour toi en échange d'un pourcentage et il accepte directement. Tu lui donnes un délai de 3 jours.")
	time.sleep(2)
	print("Après 3 jours sans nouvelles, tu décides finalement de te rendre chez lui pour comprendre ce qu'il se passe. Tu te retrouves face à lui et 4 de ses amis, tous en train de consommer ta marchandise.")
	time.sleep(1)
	print("Tu récupères rapidement les sachets qui restent et prend la fuite, il n'a pas de quoi te rembourser 2 sachets qu'il t'a consommé.")
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
	time.sleep(1)
	print(f"Vous disposez de {sachets} sachets de METH, contenant 10 grammes chacun, le prix de vente est de 100$ le gramme.")
	print("Les instructions données par le dealer sont claires, vous devez vendre tous ces sachets et rapporter 10000$ à Tuco.")
	time.sleep(1)
	print("Par contre, si vous n'êtes pas capables de ramener cet argent, ne vous attendez pas à rester en vie plus de quelques heures...")
	while sachets>0 :
		time.sleep(2)
		parole(f"\n 👉 Il vous reste {sachets} sachets à vendre, et vous avez {money}$, comment voulez-vous procéder:\n", 0.01)
		for num, (desc, _) in missions.items():
			print(f" {num}) {desc}")
		deal1 = int(input("\n🔹 Comment vends-tu ta drogue ? : "))
		if deal1 not in missions:
			print("❌ Choix invalide.")
			continue
		desc, fonction = missions[deal1]
		sachets, money = fonction(sachets, money)
		del missions[deal1]
	time.sleep(2)
	parole("\nC'est bon, vous avez tout vendu ...💰", 0.01)
	input("\n>>>Appuies sur Entrée pour rendre l'argent au Big Boss Tuco...")
	return sachets, money

def vendre(money, blue_crystal, purete, quantite):
	while True:
		parole("\n===== 💸 VENTE DE METH 💸 =====", 0.01)
		parole(f"💵 Argent : {money}$ |🧪 STOCKS TOTAL : {blue_crystal}kg | Dernière production {quantite}kg pure à {purete}%", 0.01) 
		print("\nChoisis ton type de vente :")
		print("1) Vendre 1 kg aux petits voyous ")
		print("2) Vendre 20 kg à Gus à un bon prix comme estimé selon le cours du marché")
		print("3) Vente de Blue Sky 💎(150 000$ le kg pour pureté > 90%)")
		print("4) THE BIG DEAL : 100 kg pour 2 000 000$")
		print("5) Retour au menu")
		choix = demander_choix("Ton choix : ", choix5)
		if int(choix) == 1:
			if blue_crystal < 1:
				print("\n❌ Tu n’as pas assez de METH pour cette vente.")
			elif blue_crystal >= 1:
				gain = 5000  
				blue_crystal -= 1
				money += gain
				print(f"\n💵 Tu vends 1 kg aux voyous pour {gain}$. (Ils t'ont volé sec.)")
				time.sleep(1)
				input("\n>>> Appuie pour continuer...")
		elif int(choix) == 2:
			if blue_crystal < 20:
				print("\n❌ Il faut au moins 20 kg pour vendre à Gus.")
			elif blue_crystal >= 20:
				gain = purete * 20 * 100
				blue_crystal -= 20
				money += gain
				print(f"\nGus valide la transaction des 20 kg de METH🛢️.")
				print(f"Il te donne {gain}$ pour la livraison.")
				time.sleep(1)
				input("\n>>> Appuie pour continuer...")
		elif int(choix) == 3:
			if purete < 90:
				print(f"\n❌ Ta dernière production n’est pas assez pure, seulement {purete}% (> 90% requis)")
			elif purete >= 90:
				gain = 150000*quantite  
				blue_crystal -= quantite
				quantite = 0
				purete = 0
				money += gain
				print("\n Vente premium réussie 💎 !")
				print(f"💵 Tu gagnes {gain}$.")
				time.sleep(1)
				input("\n>>> Appuie pour continuer...")
		elif int(choix) == 4:
			if blue_crystal < 100:
				print("\n❌ Il faut 200 kg pour ce deal monumental.")
			elif blue_crystal >= 200:
				gain = 2_000_000
				blue_crystal -= 200
				money += gain
				parole("\nTHE BIG DEAL RÉUSSIE 🔥", 0.01)
				print("Un acheteur fou te prend 200 kg d’un coup !")
				print(f"💵 Tu touches {gain}$ en cash.")
				time.sleep(1)
				input("\n>>> Appuie pour encaisser la somme...")
		elif int(choix) == 5:
			return money, blue_crystal, purete, quantite

def synthèse_blue_crystal(money, blue_crystal, purete, quantite):
	purete = 0     
	quantite = 0 
	parole("\n• Étape 1 : Choix du réactif 👨‍🔬", 0.01)
	print("1) Pseudoéphédrine industrielle (500$)")
	print("2) Phénylacétone pharmaceutique (2000$)")
	print("3) Méthylamine pure (10 000$)")
	choix = demander_choix(" 🔹Ton choix : ", choix3)
	if int(choix) == 1:
		cout = 500
	if int(choix) == 2:
		cout = 2000
	if int(choix) == 3:
		cout = 10000
	if money < cout:
		print("\n❌ Tu n'as pas assez d'argent pour ces ingrédients ! Choisis autre chose")
		return money, blue_crystal, purete, quantite
	money -= cout
	if int(choix) == 1:
		purete += 13
		quantite += 3
	elif int(choix) == 2:
		purete += 19
		quantite += 4
	elif int(choix) == 3:
		purete += 33
		quantite += 5
	print("\n• Étape 2 : Mode de chauffage🔥")
	print("1) Chauffage rapide (volume +, pureté -)")
	print("2) Chauffage lent et contrôlé (pureté +++)")
	print("3) Chauffage normal")
	choix = demander_choix("🔹 Ton choix : ", choix3)
	if int(choix) == 1:
		parole("\nChauffage en cours veuillez patienter...", 0.03)
		purete += 17
		quantite += 7
		parole("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩", 0.2)
		parole("Cuisson terminée ! ☑️", 0.02)
	elif int(choix) == 2:
		parole("\nChauffage en cours veuillez patienter...", 0.03)
		purete += 33
		quantite += 5
		parole("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩", 1)
		parole("Cuisson terminée ! ☑️", 0.02)
	elif int(choix) == 3:
		parole("\nChauffage en cours veuillez patienter...", 0.03)
		purete += 27
		quantite += 10
		parole("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩", 0.5)
		parole("Cuisson terminée ! ☑️", 0.02)
	print("\n• Étape 3 : Cristallisation")
	print("1) Cristallisation simple (rapide)")
	print("2) Cristallisation sous vide (pureté +)")
	print("3) Cristallisation ultra lente (pureté +++)")
	choix = demander_choix("🔹 Ton choix : ", choix3)
	if int(choix) == 1:
		parole("Critsallisation en cours patientez...", 0.01)
		parole("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦", 0.2)
		parole("Votre métamphétamine est prête ! ✅", 0.01)
		purete += 22
		quantite += 4
	elif int(choix) == 2:
		parole("Critsallisation en cours patientez...", 0.01)
		parole("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦", 0.75)
		parole("Votre métamphétamine est prête ! ✅", 0.01)
		purete += 27
		quantite += 5
	elif int(choix) == 3:
		parole("Critsallisation en cours patientez...", 0.01)
		parole("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦", 1.5)
		parole("Votre métamphétamine est prête ! ✅", 0.01)
		purete += 33
		quantite += 2
	valeur = purete*quantite*100
	time.sleep(1)
	print("\n=== RÉSULTAT  ===")
	print(f" Quantité synthétisée : {quantite}kg")
	print(f" Pureté : {purete}%")
	print(f" Valeur estimée pour la revente, {valeur}$💰 d'après le cours du marché")
	print("\nTa METH est prête, c'est du vrai cristal bleue une pure folie 👨‍🔬!")
	blue_crystal += quantite
	return money, blue_crystal, purete, quantite

def acheter(money, inv):
	while True:
		print("\n===== INVESTISSEMENTS =====")
		parole(f"💵 Argent : {money}$ |🔫 Armes : {inv['armes']}/10 |🧍 Hommes : {inv['hommes de mains']}/5", 0.005)
		parole(f"⚖️ Avocat (Saul Goodman) : {'Oui' if inv['avocat'] else 'Non'} | Informateur police : {'Oui' if inv['informateur'] else 'Non'}", 0.005)
		print("\nQue veux-tu acheter ?")
		print("1) Une arme (35 000$)  - Max 10")
		print("2) Un homme de main (100 000$) - Max 5")
		print("3) Avocat Saul Goodman (500 000$) - Unique")
		print("4) Informateur dans la police (750 000$) - Unique")
		print("5) Retour au menu")
		choix = demander_choix("🔹 Ton choix : ", choix5)
		if int(choix) == 1:
			if inv["armes"] >= 10:
				print("\n❌ Tu as déjà le maximum d’armes (10).")
				input("\n>>> Appuie pour continuer...")
			if money < 35000:
				print("\n❌ Pas assez de cash.")
				input("\n>>> Appuie pour continuer...")
			elif money >= 35000:
				money -= 35000
				inv["armes"] += 1
				print("\nTu as acheté une arme🔫 .")
				input("\n>>> Appuie pour continuer...")
		elif int(choix) == 2:
			if inv["hommes de mains"] >= 5:
				print("\n❌ Tu as déjà le maximum d’hommes (5).")
				input("\n>>> Appuie pour continuer...")
			if money < 100000:
				print("\n❌ Pas assez de cash.")
				input("\n>>> Appuie pour continuer...")
			elif money >= 100000:
				money -= 100000
				inv["hommes de mains"] += 1
				print("\n🧍 Tu recrutes un homme de main.")
				input("\n>>> Appuie pour continuer...")
		elif int(choix) == 3:
			if inv["avocat"]:
				print("\n❌ Tu as déjà Saul Goodman.")
				input("\n>>> Appuie pour continuer...")
			if money < 500000:
				print("\n❌ Pas assez de cash.")
				input("\n>>> Appuie pour continuer...")
			elif money >= 500000 and not inv["avocat"]:
				money -= 500000
				inv["avocat"] = True
				print("\n⚖️ Saul Goodman rejoint ton organisation. « Better call Saul ! »")
				input("\n>>> Appuie pour continuer...")
		elif int(choix) == 4:
			if inv["informateur"]:
				print("\n❌ Tu as déjà un informateur.")
				input("\n>>> Appuie pour continuer...")
			if money < 750000:
				print("\n❌ Pas assez de cash.")
				input("\n>>> Appuies pour continuer...")
			elif money >= 750000 and not inv["informateur"]:
				money -= 750000
				inv["informateur"] = True
				print("\n Tu finances un informateur dans la police. Les infos vont couler… Tu ne devrais pas avoir à te soucier de la DEA")
				input("\n>>> Appuie pour continuer...")
		elif int(choix) == 5:
			return money, inv

def mission_finale(money, inv, name):
	parole("Tu es devenu l'un des plus grands dealeurs et fabricants de METH\nDésormais tu as le choix de décider comment mener à bien ton empire de la drogue ou bien même tout quitter ...", 0.01)
	time.sleep(1)
	while True:
		print("\n===== 🔥 MISSIONS 🔥 =====")
		print("1) Prendre ta retraite (disparaître)")
		print("2) Blanchiment d’argent")
		print("3) Déclencher une guerre contre le cartel Salamanca, qui te limite dans ta production et donc t'empêches de faire suffisamment de bénéfices")
		print("4) Retour au menu")
		choix = demander_choix("🔹 Ton choix : ", choix4)
		if int(choix) == 1:
			print("\nTu veux disparaître… changer d’identité… tout quitter et profiter de tout l'argent que tu as gagner.")
			time.sleep(1)
			print(f"Actuellement tu as accumulé au total {money}$ mais tu peux encore décider de continuer à vendre pour gagner plus\n(fais un max d'oseille avant de partir  tu risques d'en avoir besoin pour disparaître)")
			confirm = demander_choix("\n🔹 Es-tu sûr de voiloir te retirer du deal ? (action iréversible) (1)oui/(2)non : ", choix2)
			if int(confirm) == 1:
				print("\nTon histoire dans le monde de la meth s’arrête ici…")
				time.sleep(1)
				if inv["avocat"]:
					print("Ton avocat sauras surement comment te sortir de là")
					parole("\n📞 Appel de Saul Goodman...", 0.01)
					parole("  « J’ai peut-être quelqu’un… Un type qui fait disparaître les gens. C'est 500 000$  »", 0.02)
					parole("  « Tout est pris en compte ton labo sera détruis, nouvelle identité, transport, nouvelle vie ...»", 0.02)
					parole("  « Qu'en dis-tu ? »", 0.02)
					time.sleep(1)
					choix = demander_choix("🔹 Accepter (1) ou Refuser (2) :", choix2)
					if money >= 500000 and int(choix) == 1:
						money -= 500000
						print("\nTout est réglé.")
						print("Nouveau nom. Nouvelle identité. Nouveau pays.")
						time.sleep(0.5)
						print(f"Tu profites du reste de ton argent {money} $ à l'autre bout du monde")
						time.sleep(0.5)
						print("\nLa disparition parfaite🌅.")
						fin_histoire()
					elif money < 500000 and int(choix) == 1:
						print("\nTu n'as pas assez d'argent pour payer")
						parole("   « C'est regretable mon amis, je ne peux pas t'aider autrement, c'est à toi de te débrouiller »", 0.02)
					elif int(choix) == 2:
						parole("\n  « C'est regretable mon amis, je ne peux pas t'aider autrement, c'est à toi de te débrouiller »", 0.02)
				elif not inv["avocat"]:
					parole("Malheuresement tu n'as aucun contact sur qui t'aider, tu es seul sans (un avocat aurait pu t'aider à te faire disparaître ...)", 0.01)
				time.sleep(2)
				print("\nTu n’as plus le choix.🔥")
				time.sleep(0.5)
				print("Tu dois brûler ton labo pour effacer toute trace.")
				time.sleep(0.5)
				print("Produits chimiques. Gaz. METHS. Matos. Une étincelle et tout explose…")
				time.sleep(0.5)
				input("Appuies sur entrée pour tout faire pêter !🧨")
				parole("💥💥💥BOOOOM💥💥💥!!!!", 0.07)
				print("Tout ton labo part en fumer")
				time.sleep(1)
				print("Tu réalises au même moment que tes sacs de billets sont en train de partir en fumer c'est tout ton argent")
				time.sleep(1)
				if inv["informateur"]:
					parole("Tu appelles ton informateur dans la police et tu lui explique la situation")
					parole("\n  « La police est en chemin et sera la dans 5 min, je m'occupe d'effacer toute preuve pouvant t'inculper»", 0.02) 
					parole("  « À présent fuit le plus loin possible »", 0.02)
					parole("  « Pour ce qui est de ton argent, laisses le brûler, tu recevera ton dû en crypto sur un compte off-shore »", 0.02)
					time.sleep(2)
					parole("Tu prends la route avant l’arrivée des flics et prends le premier avion.", 0.02)
					time.sleep(1)
					parole(f"Tu as réussi ! Tu t'es retiré du deal et profites désormais de tes {money}$ sous les tropiques 🏝️!", 0.03)
					fin_histoire()
				if not inv["informateur"]:
					input("Appuies sur entrée pour te casser au plus vite ...")
					print("\nLe feu attire trop l’attention.")
					time.sleep(1)
					print("La police arrive trop vite👮‍♂️")
					time.sleep(0.5)
					print("Les policiers te retiennent le temps de comprendre à qui ils avaient affaire, après un petit temps ils découvrent qui tu es.")
					time.sleep(0.5)
					print("\n⛓️ Tu pars en prison")
					fin_histoire()
			elif int(confirm) == 2:
				print("\nTu changes finalement d’avis… le business continue")
				input("\n>>>Appuie sur entrée pour retourner au menu...")
		elif int(choix) == 2:
			print("\nTu veux blanchir ton argent sale sans te faire chopper")
			print("Mais chaque option a ses risques.")
			print("\nOptions possible :")
			print("1) Los Pollos Hermanos 🐔")
			print("2) Une laverie 🧼")
			print("3) Un car wash 🚗")
			choix_blanchiment = demander_choix("🔹 Ton choix : ", choix3)
			if not inv["informateur"] or not inv["avocat"]:
				print("Mauvaise idée sans aucun contact et aucune expérience dans le millieu tu te choppes un contrôle fiscale")
				time.sleep(1)
				print("Tu es démasqué et on t'arrête pour trafic de stupéfiants")
				time.sleep(1)
				print("\n⛓️ Tu pars en prison")
				fin_histoire()
			elif inv["informateur"] and inv["avocat"]:
				cout = 150000
				parole(f"💸 Investissement initial : {cout}$", 0.01)
				time.sleep(0.5)
				print("\nTu utilises une nouvelle entreprise pour blanchir ton argent")
				time.sleep(1)
				print("Ton avocat Saul Good Man s'arrange pour que la comptabilité soit géré parfaitement")
				time.sleep(1)
				print("Avec ton informateur dans la police que tu as payé tu es assuré que personne ne vienne se mêler de ton business, il t’évite tout contrôle fédéral")
				time.sleep(0.5)
				print("Flux d’argent énorme. Comptabilité béton.")
				time.sleep(0.5)
				parole(f"\n✅ Blanchiment ultra-efficace en 1 an tu parviens à te faire {money}$ d'argent propre !.", 0.01)
				time.sleep(1)
				parole("Tu es intouchable jusqu'a la fin de ta vie ! Bien joué ! ", 0.03)
				fin_histoire()
		elif int(choix) == 3:
			print("\n🔫 Tu veux déclarer la guerre aux Salamanca…")
			print("⚠️ C’est suicidaire sans préparation.")
			print("👉 Minimum conseillé : 3 hommes + 3 armes + pas mal de contacts")
			if inv["hommes de mains"] < 3 or inv["armes"] < 3:
				print("\n❌ Tu n’as PAS les moyens pour une guerre frontale.")
			elif inv["hommes de mains"] >= 3 or inv["armes"] >= 3:
				confirm = demander_choix("\n🔹 Es-tu sûr de vouloir mener cette guerre ? (action iréversible) (1)oui/(2)non : ", choix2)
				if int(confirm) == 1:
					print("\n🧠Il va falloir jouer finement si tu veux réussir à t'occuper du cartel, ils ont bien plus de troupes et d'armes que toi")
					print("Tu réfléchis à plusieurs manières de les éliminer. Tu hésites entre:")
					print(" 1)Leur proposer de se rencontrer dans un lieu isolé sous prétexte d'une potentielle collaboration et de les éliminer à l'aide d'un sniper.")
					print(" 2)Envoyer tes hommes de mains au domicile des salamanca.")
					confirm = demander_choix("🔹 Que choisis-tu?", choix2)
					if int(confirm) == 1 and not inv["informateur"]:
						parole("\n📞Tu prend contact avec Lalo Salamanca afin d'arranger un rendez-vous pour discuter business.\nCe dernier trouve que c'est une bonne idée et accepte de te rencontrer accompagner du reste du cartel.", 0.01)
						time.sleep(1)
						parole("Tu missiones l'un de tes hommes de se positionner au sommet d'une colline aux alentours, sur laquelle il aura une vue globale sur les environs.", 0.01)
						time.sleep(1)
						input("\nAppuie sur entrée pour continuer ...")
						parole("\nUne fois arrivé, tu discutes avec eux en attendant l'occasion parfaite d'en finir avec eux, lorsque tout d'un coup: ", 0.01)
						time.sleep(1)
						parole("BANG!!💥💥💥", 0.1)
						parole("Ce coup de feu te surprend car tu n'as pas donné l'ordre de tirer, et lorsque que tu regarde autour de toi, aucun des membres du cartel n'est blessé.", 0.01)
						time.sleep(2)
						parole("Vous vous demandez ce qu'il se passe avec les membres du cartel lorsque vous entendez les sirènes de police retentir.", 0.01)
						time.sleep(1)
						parole("Soudain, une voix retentit à l'aide d'un mégaphone:", 0.01)
						time.sleep(2)
						parole("   📢 <<Vous êtes cernés! Ne cherchez pas à vous enfuir>>", 0.04)
						time.sleep(1)
						parole("La DEA débarque et vous embarque tous. Vous êtes tous envoyés en prison, ce qu'un informateur dans la police aurait pu vous éviter.", 0.01)
						time.sleep(2.5)
						parole("\nVous finnissez le restant de votre vie en prison ⛓️", 0.05)
						fin_histoire()
					elif int(confirm) == 1 and inv["informateur"]:
						parole("\n📞Tu prends contact avec Lalo Salamanca pour un rendez-vous sous couvert de négociations.", 0.01)
						parole("\nAlors que tu es en train de te préparer pour partir au rendez-vous, ton homme infiltré dans la police t'informe qu'ils ont eu vent de ces négociations et qu'ils comptent arrêter tout le monde sur place.", 0.01)
						time.sleep(1)
						parole("\nIl t'explique qu'il s'arrangera pour que ton nom ne ressorte pas pendant les interrogatoires, et qu'il faut uniquement que tu fasses profil bas pendant quelque temps.", 0.01)
						time.sleep(1)
						parole("\n💵Tout ce qu'il demande est une augmentation de son salaire, ce qui ne devrait pas être un problème une fois que tu auras la main-mise sur le territoire des Salamanca.", 0.01)
						input("\n>>>Appuie sur Entrée pour continuer..")
						print("\n Tu attends nerveux depuis ton laboratoire, quand soudainn ton téléphone sonne:")
						time.sleep(1)
						parole("     <<C'est fini. On les a eu.>>", 0.06)
						parole("Tu es débarassé de tes ennemis les plus dangereux, qui remontent à l'époque où tu as tué Tuco. Plus rien ni personne ne s'oppose à l'expansion de ton empire maintenant.", 0.02)
						time.sleep(2.5)
						parole(f"Ton contrôle s'étend au cours des années, il ne se compte plus en ville mais en pays.\n\nTu seras retenu dans les mémoires de tous comme le plus grand narcotraficant de tous les temps, connu sous le nom de {name}, celui dont même les états avaient peur🥶.", 0.03)
						fin_histoire()
					elif int(confirm) == 2:
						parole("\nTu choisis d’envoyer tes hommes de main au domicile des Salamanca.", 0.01)
						time.sleep(1)
						parole("La nuit tombe. Trois véhicules sans plaques roulent lentement vers leur quartier.", 0.01)
						time.sleep(1)
						parole("L’opération est rapide, brutale, silencieuse.", 0.01)
						time.sleep(1)
						parole("🔫 Les Salamanca sont éliminés chez eux. Aucun survivant.", 0.01)
						time.sleep(1)
						parole("Pendant quelques heures, tu penses avoir gagné.", 0.01)
						input(">>>Appuie sur Entrée pour continuer...")
						parole("\nÀ l’aube, tu quittes ta planque, confiant.", 0.01)
						time.sleep(1)
						parole("Tu prend la route tranquillement pour rejoindre ton labo.", 0.01)
						time.sleep(1)
						parole("Un véhicule arrive à fond par derrière et ouvre le feu sur ta voiture. ", 0.01)
						parole("💥BAM!!!💥BAM!!!💥BAM!!!💥BAM!!!💥BAM!!!💥", 0.1)
						time.sleep(1)
						parole("\nTu es touché et tu perds le contrôle de ton véhicule.", 0.01)
						time.sleep(1.5)
						parole("\nTu es mort 😵, le cartel gagnera toujours ...", 0.04)
						fin_histoire()
				elif int(confirm) == 2:
					print("\nT'as raison, ce n'est pas une bonne idée")
			input("\n>>>Appuie sur entrée pour retourner au menu...")
		elif int(choix) == 4:
			return money, inv, name

def menu_principal(money, lieu, blue_crystal, name, purete, quantite):
	tot = blue_crystal
	vendu = 0
	inv = {
		"armes": 0,
		"hommes de mains": 0,
		"avocat": False,
		"informateur": False
	}
	while True:
		print("\n===== 🔹 MENU 🔹 =====")
		parole(f"💵 Argent : {money}$  | 🧪 METH : {blue_crystal}kg ", 0.01)
		print("1) Cook de la METH")
		print("2) Vendre ta production")
		print("3) Acheter du matériel / armes")
		print("4) Partir en mission")
		print("5) Voir ton stock")
		print("6) Quitter le jeu")
		menu = demander_choix("🔹 Ton choix : ", choix6)
		if int(menu) == 1:
			money, blue_crystal, purete, quantite = synthèse_blue_crystal(money, blue_crystal, purete, quantite)
			time.sleep(1)
			tot +=quantite
			input("\n>>>Appuie sur entrée pour retourner au menu...")
		elif int(menu) == 2:
			money, blue_crystal, purete, quantite = vendre(money, blue_crystal, purete, quantite)
		elif int(menu) == 3:
			money, inv = acheter(money, inv)
		elif int(menu) == 4:
				money, inv, name = mission_finale(money, inv, name)
		elif int(menu) == 5:
			print(f"\n•🛢️ Stock actuel : {blue_crystal}kg")
			print(f"•💵 Argent : {money}$")
			print(f"•🧪 METH produite au total depuis le début : {tot}kg")
			print(f"•🔫 Armes : {inv['armes']}/10")
			print(f"•🧍 Hommes : {inv['hommes de mains']}/5")
			print(f"•⚖️ Avocat (Saul Goodman) : {'Oui' if inv['avocat'] else 'Non'}")
			print(f"•👮‍♂️ Informateur police : {'Oui' if inv['informateur'] else 'Non'}")
			input("\n>>>Appuie sur entrée pour retourner au menu...")
		elif int(menu) == 6:
			confirm = demander_choix("\n⚠️ Es-tu sûr de vouloir quitter le jeu ? (1)oui / (2)non : ", choix2)
			if int(confirm) == 1:
				fin_histoire()
			elif int(confirm) == 2:
				time.sleep(0.5)

def intervention_GUS(money, prix, lieu, name):
	print("\n🐓📞 *Un téléphone sonne au loin...*")
	time.sleep(1)
	print("\nUne voix calme et posée :")
	time.sleep(1)
	parole(f"  « Bonjour {name}. Je suis Gustavo Fring. »", 0.02)
	time.sleep(1)
	parole("  « On m’a parlé de vous… un homme intelligent mais fauché. »", 0.02)
	time.sleep(1)
	parole("  « Je tiens à vous remercier d'avoir éliminer TUCO, c'était notre plus grande menace»", 0.02)
	time.sleep(1)
	parole("  « Je peux financer votre laboratoire. En échange, je veux votre loyauté. »", 0.02)
	time.sleep(1.5)
	if money < prix :
		print("\nQue fais-tu ?")
		argent_gus = prix - money
		print(f" 1) Accepter l’offre de Gus (il te donne {argent_gus}$ mais tu lui DOIS tout)")
		print(" 2) Refuser (extrêmement dangereux…)")
		choix = demander_choix("🔹 Que choisis-tu ?", choix2)
		if int(choix) == 1:
			money = money + argent_gus
			print("\nGustavo te félicite d'avoir accepté, il finance entièrement la contruction d'un labo pour toi")
			parole("    « Vous commencez demain 9h, RDV à Los Pollos Hermanos pour que je vous file du matos de qualité. »", 0.02)
			time.sleep(0.5)
			parole("    « Ne me décevez pas. »", 0.02)
			time.sleep(1)
		elif int(choix) == 2:
			print("\nTu refuses poliment… ❌")
			time.sleep(1)
			parole("  « Je vois. C’est terriblement regrettable. »", 0.02)
			time.sleep(2)
			parole("Quelques heures plus tard, tu disparais mystérieusement.🕵️‍♂️", 0.03)
			time.sleep(2)
			parole("Ton corps est retrouvé sans vie dans un fossé lendemain ...🪦", 0.03)
			fin_histoire()
	if money > prix :
		print("\nTu as plus qu’assez d’argent pour financer le projet pourquoi accpeter ? 💼 .")
		time.sleep(1)
		parole("Gus marque un silence…", 0.03)
		time.sleep(1)
		parole("  «Intéressant. Vous n’avez pas besoin de moi… mais moi, j’ai besoin de vous. »", 0.02)
		time.sleep(1)
		print("\nQue fais-tu ?")
		print(" 1) Refuser toute collaboration (risqué mais tu restes indépendant)")
		print(" 2) Accepter quand même son 'partenariat' (tu gagnes un allié… et une menace)")
		choix = demander_choix("🔹 Que choisis-tu ?", choix2)
		if int(choix) == 1:
			print("\nTu refuses calmement la proposition de Gus.")
			time.sleep(1)
			parole("  « Très bien… Je respecte votre décision. Pour l’instant... »", 0.02)
			time.sleep(1)
			print(f"\nTu payes {prix}$ pour un {lieu} et tu restes totalement indépendant.")
			money -= prix
			print(f"Argent restant : {money}$")
			time.sleep(1)
			parole(f"Mais tu sens que cette histoire n’est pas terminée… tu continues alors l'installation de ton labo dans ton {lieu}, il te manque le matos de chimie", 0.03)
			input("\nAppuie sur Entée pour continuer...")
			print("\n Un soir alors 2 hommes en noir t'attendent à la sortie de ton {lieu}.")
			time.sleep(1)
			parole("« Mr Fring souhaite vous parler. »", 0.02)
			print("\nTu as deux choix :")
			print(" 1) Résister (Folie, mais tu peux tenter…)")
			print(" 2) Te laisser emmener")
			choix2bis = demander_choix("🔹 Que fais-tu ?", choix2)		
			if int(choix2bis) == 1:
				print("\nTu essaies de fuir en courant…")
				time.sleep(1)
				print("Mais les hommes de main de Gus sont formés, rapides, précis et sans-pitié.")
				time.sleep(1)
				parole("Un coup sec derrière la tête…", 0.02)
				time.sleep(1)
				parole("… noir complet.", 0.03)
				time.sleep(2)
				parole("\n💀 Tu as été retrouvé deux jours plus tard dans un fossé.", 0.03)
				fin_histoire()
			elif int(choix2bis) == 2:
				print("\nOn te pousse dans une voiture aux vitres teintées.")
				time.sleep(1)
				print("Gustavo Fring est là à l'intérieur.")
				time.sleep(1)
				parole("  «Je vous avais laissé une chance. Maintenant, vous travaillez pour moi.»", 0.02)
				time.sleep(0.5)
				parole(f"  «Seul vous n'y arriverez jamais. La preuve, en 1 mois, vous n'avez toujours pas installé tous votre équipement dans votre {lieu} »", 0.02)
				time.sleep(1)
				print("Vous acceptez à contre-coeur et espérez que ça ne finnisse pas comme avec Tuco")		
		elif int(choix) == 2:
			print("\nTu acceptes le partenariat de Gus… même sans avoir besoin de lui.")
			time.sleep(1)
			parole("	« Une sagesse rare. Ensemble, nous irons loin. Je m'engage à financer le matériel pour ton labo »", 0.02)
			time.sleep(1)
			print(f"Tu finances toi-même {lieu} pour {prix}$, Gus complète l’équipement avec du matériel professionnel.")
			money -= prix
			time.sleep(1)
			parole("    « Vous commencez demain 9h. Soyez ponctuel. »", 0.03)		
	return money, prix, lieu

def baron_de_la_drogue(money):
	input("\n>>>Appuies sur Entrée pour construire ton empire de la drogue⚔️\n")
	print("En tant que baron de la drogue il te faut absolument un nom de narcotrafiquant")
	name = input("🔹 Quel nom veut tu porter à la place de Walter Black : ")
	parole(f"À présent les gens t'appellerons {name} 🥶", 0.03)
	time.sleep(1)
	print("\nPour commencer, il te faut investir dans un labo, un lieu sûre pour cook.")
	time.sleep(1)
	print(f"Tu disposes de {money}$ cela corespond à tout l'argent que tu as pu te faire avec la vente de drogue")
	time.sleep(1)
	print("\nOù veux-tu installer ton labo ?")
	print("1) Dans un camping-car (20 000$)")
	print("2) Dans un entrepôt abandonné (150 000$)")
	choix = demander_choix("🔹 Ton choix : ", choix2)
	if int(choix) == 1:
		prix = 20000
		lieu = "camping-car"
	elif int(choix) == 2:
		prix = 150000
		lieu = "entrepôt abandonné"
	if money < prix:
		print(f"\n❌ Tu n’as pas assez pour acheter un {lieu} ({prix}$ requis).")
		money, prix, lieu = intervention_GUS(money, prix, lieu, name)
	else :
		print("Tu te renseignes pour acheter")
		time.sleep(1)
		money, prix, lieu = intervention_GUS(money, prix, lieu, name)	
	print(f"\n----------------- Argent restant: {money} $ -----------------\n")
	print("Gus revient te voir quelques jours plus tard 🧍: ")
	time.sleep(1)
	parole(f"   « {name}… Le matériel est en place. Ton {lieu} est prêt pour commencer à produire de la METH. »", 0.03)
	time.sleep(1)
	print(f"\nTu te rends dans ton {lieu}. À l’intérieur :")
	time.sleep(0.5)
	print("• Matériel flambant neuf 🧪")
	time.sleep(0.5)
	print("• Barils de Méthylamine, Phénylacétone, Pseudoéphédrine… 🛢️☢️")
	time.sleep(1)
	print("\nTu enfiles ta combinaison jaune. Le moment est venu de cook.")
	input(">>> Appuie sur Entrée pour commencer ta première synthèse...")
	blue_crystal = 0
	purete = 0
	quantite = 0
	money, blue_crystal, purete, quantite = synthèse_blue_crystal(money, blue_crystal, purete, quantite)
	time.sleep(2)
	print("\nGustavo Fring observe le crystal bleu que tu viens de produire avec un léger sourir : ")
	parole("  — Impressionnant. Pour une première production, c’est remarquable. Continuez ainsi je compte sur vous pour batir un empire de la drogue.", 0.03)
	parole("  - La pureté de ton produit est remarquable, je m'engage à être ton revendeur", 0.03)
	time.sleep(0.5)
	input("\n>>>À présent tu gères toi-même ton business. Appuie sur Entrée pour accéder au menu de ton business...")
	money, lieu, blue_crystal, name, purete, quantite = menu_principal(money, lieu, blue_crystal, name, purete, quantite)


def faire_tomber_TUCO(money):
	time.sleep(1)
	input("\nAppuies sur Entrée...")
	print("\n-------------------------------------------------\n")
	print("Il faut faire tomber ce fdp de TUCO !Il était temps de se débarrasser de lui🤬")
	print("Tu réfléchis à la meilleure façon de t’en débarrasser définitivement.\n")
	time.sleep(1)
	print("👉 Trois plans te viennent en tête :\n")
	parole(" 1) L'empoisonner discrètement (ricin ou équivalent)", 0.001)
	parole(" 2) Fabriquer une bombe artisanale pour le piéger", 0.001)
	parole(" 3) Monter un faux deal sous une fausse identité et lui faire tester de la meth empoisonnée\n", 0.001)
	choix = demander_choix("🔹 Comment veux-tu t’y prendre ? ", choix3)
	if int(choix) == 1:
		print("\nTu optes pour un poison discret. Tu achètes une dose de Ricin sur le darkweb pour 2000$ avec l'argent que tu disposes.")
		money -= 2000
		print("Il te restes à trouver comment la lui faire ingérer...")
		time.sleep(1)
		print(" 1) Lui offrir un café 'pour discuter business'")
		print(" 2) L'ajouter à son repas lors d'un rendez-vous professionnel")
		choix = demander_choix("🔹 Que fais-tu ? ", choix2)
		if int(choix) == 1:
			print("Tuco accepte de discuter business à ta grande surprise. Tu lui verse ton poison quand il a le dos tourné.Le poison agit lentement...") 
			parole("Tuco s'effondre. Il est mort.", 0.03)
			time.sleep(1)
			parole("Tu n'as plus d'ennemis !", 0.03)   
		elif int(choix) == 2:
			print("Tu verses du poison dans son repas. Tuco crache le contenu immédiatement, te regardant avec des yeux de tueur.")
			time.sleep(1)
			print("Il te saute dessus et te tues d'une balle dans la tête sans hésiter.🔫")
			parole("PANN !!! \nTu es mort 💀", 0.04)
			fin_histoire()
	if int(choix) == 2:
		print("\n💣 Tu décides de fabriquer une bombe artisanale en regardant un tuto sur Youtube.")
		print("Tu prépares un petit explosif que tu dois placer quelque part où Tuco passera.")
		time.sleep(1)
		print("\nOù veux-tu le placer ?")
		print("1) Sous son siège de voiture")
		print("2) Dans son bureau, derrière la porte")
		choix = demander_choix("🔹 Ton choix : ", choix2)
		reussite = random.randint(1,2)
		print("\nTu attends le moment critique...")
		if reussite == 2 :
			parole("BOOOOMMM💥", 0.04)
			print("Une énorme explosion retentit. Tuco n’a pas eu le temps de comprendre.")
			print("☠️ Tu as réussi, il est mort.")
		else:
			time.sleep(0.5)
			print("Tuco te surprend en train de poser la bombe.")
			time.sleep(0.5)
			print("Il te massacre sans réfléchir et tire à bout portant")
			parole("PANN !!! \nTu es mort 💀", 0.04)
			fin_histoire()		
	if int(choix) == 3:
		print("\nTu décides de monter un faux deal.")
		print("Tu inventes une identité de dealer et fixes un rendez-vous à Tuco.")
		time.sleep(1)
		print("Ton but : lui faire tester une METH empoisonnée que tu as préparé.\n")
		print("Où veux-tu organiser le deal ?")
		print("1) Dans un parking souterrain")
		print("2) Dans un motel abandonné")
		choix = demander_choix("🔹 Ton choix : ", choix2)
		reussite = random.randint(1,3)
		print("\nTuco arrive...")
		if reussite == 3:
			print("Le jour du deal, il veut tester ta marchandise, mais te demande de gôuter en premier !")
			print("Tu te retouves piéger car c'est du poison")
			time.sleep(1)
			print("Il comprend le piège et sort son flingue.")
			parole("PANN !!! \nTu es mort 💀", 0.04)
			fin_histoire()
		else:
			print("Le jour du deal, Tuco veut tester ta marchandise")
			print("💉 La METH empoisonnée fait son effet. Tuco devient livide, tombe au sol.")
			time.sleep(1)
			print("☠️ Tu l’as eu. Tu prend vite la fuite pour éviter les représailles. C’est terminé pour lui.")
	time.sleep(1)
	print("\nTuco est mort, maintenannt c'est toi le nouveau baron de la drogue du coin !")
	print("\n----------------------------------------------\n")
	money = baron_de_la_drogue(money)

def fuite(money):
	print("Tu pars en sprintant en direction de la sortie.")
	print("Tu te retrouves dehors, tu reconnais la voiture dans laquelle on t'avais emmené.")
	print("1) Aller en direction de la voiture et espérer que les clés sont restés sur le contact 🚗")
	print("2) Continuer de courir en espérant les perdre dans les ruelles voisines🏃")
	choix_fuite = demander_choix("🔹 Comment vous échappez-vous?", choix2)
	voiture = random.randint(1,2)
	if int(choix_fuite) == 1 and voiture == 1:
		print("\nGros coup de chance! Les clés sont encore là, tu t'empresses de démarrer pendant que les membres du gang sortent du batîment et commencent à te tirer dessus.")
		print("Plusieurs balles touchent la voiture, mais pas de blessures pour toi.")
		time.sleep(1)
		print("Tu t’éloignes et tu décides d’en finir : Tuco doit tomber.")
		time.sleep(2)
		mmoney = faire_tomber_TUCO(money)	
	elif int(choix_fuite) == 1 and voiture == 2:
		print("\nMauvaise nouvelle : la voiture est fermée...")
		time.sleep(1)
		print("Tu entends les pas du cartel se rapprocher.")
		time.sleep(1)
		print("Tu dois réagir vite :")
		print("1) Casser la vitre pour tenter de voler la voiture")
		print("2) Repartir en courant dans l’autre direction")
		choix_bloque = demander_choix("\n🔹Ton choix : ", choix2)
		action = random.randint(1, 2)	
		if int(choix_bloque) == 1 and action == 1:
			print("\n💥 Tu éclates la vitre avec ton coude, ça fait un bruit énorme.")
			print("Tu montes, tu démarres… et tu parviens à t’enfuir de justesse.")
			time.sleep(1)
			print("Tu t'es blessé légèrement en cassant la vitre")
			print("Après cet incident qui a failli te coûter la vie, tu réfléchis pour en finir avec Tuco")
			time.sleep(1)
			money = faire_tomber_TUCO(money)
		elif int(choix_bloque) == 1 and action == 2:
			print("\nTu tentes de casser la vitre mais le cartel t'attrappe avant que tu puisses partir.")
			print("Ils te frappent jusqu'à ta mort et prennent tout ce que tu as sur toi. 💀")
			fin_histoire()
		elif int(choix_bloque) == 2:
			print("\nTu t’enfuis dans une ruelle sombre.")
			print("Ils te poursuivent mais tu arrives à te cacher derrière une benne.")
			time.sleep(1)
			print("Tu les entends passer sans te voir. Tu as survécu. Tu décides de passer la nuit ici💤")
			time.sleep(2)
			print("Le lendemain, après avoir gamberger toute la nuit, tu décides d’en finir : Tuco doit tomber.")
			money = faire_tomber_TUCO(money)
	elif int(choix_fuite) == 2:
		print("Le cartel te rattrape est commence à te frapper lourdement. Par chance Tuco arrive et ordonne qu'on arrête ton massacre")
		parole( " - Laissez le je crois qu'il a compris la leçon,", 0.02)
		parole( " - Ici on ne me fais de coup de traite sinon voilà ce qui arrive.", 0.02)
		parole( " - Maintenant tu n'as pas d'autre choix que de travailler pour moi, je t'emmène au labo et tu n'en sortiras pas tant que j'en aurais pas fini avec toi", 0.02)
		time.sleep(2)
		money = labo_de_TUCO(money)

def faible_paiement(gain, trahison):
	print(f"Tuco te paye {gain}$, le montant est vraiment faible par rapport à la quantité produite 🤨")
	time.sleep(1)
	rep = demander_choix("Veux tu te plaindre au près de Tuco ? \n 1) Oui c'est pas assez \n 2) Non, c'est que le début il faut continuer à produire\n🔹 Ton choix : ", choix2)
	if rep == 1:
		print("\nTu te plains à Tuco du montant qu'il te donne.\n👊 Tuco te choque contre le mur :")
		time.sleep(1)
		parole(" - T’AS UN PROBLÈME AVEC MA GÉNÉROSITÉ ? TU BOSSES POUR MOI, PAS POUR TON PORTE-MONNAIE !", 0.03)
		trahison = True
	elif rep == 2:
		print("\nTu n’apprécies pas… mais tu continues pour l’instant.")
		input(">>>Appuies sur entrée pour prendre ta part et continuer à bosser 🧑‍🔬 ...")
	return trahison
	
def travailler_pour_TUCO(money, trahison):
	print("\nQuel programme veut-tu utiliser pour synthétiser de la METH 🧪")
	print("1) Mode Sécurisé – moins rentable mais zéro risque")
	print("2) Mode Boost – production plus élevée mais risque d'erreur")
	choix = demander_choix("🔹 Ton choix : ", choix2)
	purete = 0
	volume = 0
	if int(choix) == 1:
		print("\n💻 Le mode sécurisé est lancé, sur quel autre paramètre veux-tu influencer la synthèse de la métamphétamine ?")
		print(" 1) Optimiser la quantité (volume ++) ")
		print(" 2) Optimiser la pureté (qualité ++) ")
		programme = demander_choix("🔹 Quel paramètre t'intéresses ? ", choix2)  
		if int(programme) == 1:
			volume = random.randint(9, 15)
			purete = random.randint(50, 75)
			gain = volume * purete * 75
			money += gain
			parole(f"\nPas mal ce que tu as produit ! {volume} kg de MET, pureté {purete}%.", 0.005)
			time.sleep(1)
			if gain < 50000 :  
				trahison = faible_paiement(gain, trahison)
			else :
				parole(f"Tuco te paye {gain}$ (c'est raisonnable mais clairement pas assez vu le prix du marché)", 0.005)
				input("\n>>>Appuies sur entrée pour prendre ta part et continuer à bosser 🧑‍🔬 ...")
		elif int(programme) == 2:
			purete = random.randint(80, 95)
			volume = random.randint(2, 6)
			gain = purete * 50
			money += gain
			parole(f"\nMeth ultra pur ! {purete}% mais volume faible seulement {volume} kg.", 0.005)
			time.sleep(1)
			if gain < 20000: 
				trahison = faible_paiement(gain, trahison)
			else :
				parole(f"Tuco te paie {gain}$ c'est très peu, il doit se faire de grosses marges pour lui💰\n)", 0.005)
				time.sleep(1)
				input(">>>Appuies sur entrée pour prendre ta part et continuer à bosser 🧑‍🔬 ...")			
	elif int(choix) == 2:
		print("\nTu lances le mode boost avec ton collégue Jesse pour synthétiser une METH d'exception, quel facteur souhaite-tu ajuster ?:")
		print("1) Ajuster les catalyseurs (qualité +++ mais volume moindre)")
		print("2) Forcer la réaction (rapidité +++ volume +++ mais risque d'explosion)")
		cuisson = demander_choix("🔹 Quel paramètre chois-tu ? : ", choix2)
		if int(cuisson) == 1:
			purete = random.randint(90, 99)
			volume = random.randint(4, 9)
			gain = purete * volume * 150
			money += gain
			parole(f"EXCEPTIONNEL une METH pure à {purete}%, c'est digne des plus grands narcotrafiquants !!!", 0.01)
			time.sleep(1)
			print(f"Tuco te félicites et te paie {gain}$ pour ta came (ça mérite beaucoup plus !) 💸 ")
			time.sleep(1)
			rep = demander_choix("Demander une augmentation ?\n 1) Oui \n 2) Non\n🔹Ton choix : ", choix2)
			if rep == 1:
				print("👊 Tuco te choque contre le mur :")
				parole("- Commences pas à te plaindre, la prochaine fois tu seras mieux payé prends pas la confiance avec moi.", 0.02)
				time.sleep(1)
				print("Tu comprends que Tuco abuse de toi et qu'il ne te paieras jamais suffisamment")
				trahison = True
			if rep == 2:
				print("Tu n’apprécies pas… mais tu continues pour l’instant c'est que le début.")
				time.sleep(1)
				input(">>>Appuies sur entrée pour prendre ta part et continuer à bosser 🧑‍🔬 ...")	
		elif int(cuisson) == 2:
			if random.randint(1, 2) == 1:
				parole("\n💥💥BOOOOM !!!!💥💥", 0.07)
				time.sleep(1)
				print("\nGrosse explosion dans le labo énorme flop ! \nTuco t'engueule, il veut que tu paye le nettoyage et le matos cassé pour un montant de 5000$")
				if money <= 5000:
					print("Tu n'as pas assez d'argent pour rembourser Tuco.\n Il se rend compte que tu ne lui est pas utile et décide de se débarasser de toi.")
					print("Tu disparais mystérieusement sans laiser de trace...")
					fin_histoire()
				else :
					money -= 5000
					time.sleep(2)
					parole("Travailler pour Tuco ne va pas être une mince affaire ...", 0.01)
					trahison = True
			else :
				volume = random.randint(25, 35)
				purete = random.randint(50, 70)
				gain = purete * volume*50
				money += gain
				parole(f"INCROYABLE: {volume} kg de METH pure à {purete}% !!!", 0.01)
				time.sleep(1)
				print(f"Tuco est impressioné par ta recette il te paie {gain}$… mais il semble que le compte n'y est pas par rapport au volume et au prix du marché.💰")
				input("\n>>>Appuies sur entrée pour prendre ta part et continuer à bosser 🧑‍🔬 ...")
	return money, trahison

def labo_de_TUCO(money):
	input("\n>>>Appuyer sur Entrée pour suivre Tuco dans le labo 🧑‍🔬\n")
	parole(" - On m’a dit que t’étais bon en informatique… tu vas me le prouver,tu vas travailler pour moi. Ton objectif c'est de me coder un programme qui cook la METH la plus pure ! Tu ne seras pas seul, Jesse sera ton partenaire", 0.01)
	time.sleep(1.5)
	print("\nTuco sort et vous laisse à deux avec Jesse, il t’explique ainsi les grandes étapes de la synthèse de la métanphétamine 🧪.")
	time.sleep(1)
	parole(" - Salut Walter moi c'est Jesse, ensemble on va cook de la METH, le boss Tuco a besoin de toi pour que tu m'aides à programmer un système qui automatise la production de la METH !", 0.01)
	time.sleep(1)
	input("\n>>>Appuyer sur Entrée pour commencer à cook de la METH 🧑‍🔬\n")
	print("Tu t'installes, commences à coder sur un PC plusieur programmes différents 👨‍💻\nTu passes la nuit entière à coder un logiciel...")
	time.sleep(1)
	parole(VERT + "\n>>>Script executed ... \n011011010101011101010110\n011001000101111101101011\n110110110010110010010010\n010101011001011101101010\n101101010101010011101110\n>>>Ready to cook\n" + RESET, 0.015)
	time.sleep(1)
	print("Ton logiciel est prêt✅, à toi de choisir avec Jesse quel programme éxecuter pour cook efficacement et faire un max de fric 💰")
	time.sleep(1)
	trahison = False
	while not trahison:
		money, trahison = travailler_pour_TUCO(money, trahison)
		time.sleep(1)
		if trahison:
			break 
		print(f"\n  Ton argent total : {money}$ 💸")
		print("  Le business continue pour l’instant ... 🚀")
		time.sleep(1)
	parole("\nTuco t’arnaque et ne te respectera jamais, tu penses donc à le faire tomber ❗", 0.01)
	money = faire_tomber_TUCO(money)

def le_cartel(money):
	input("\nAppuyez sur Entrée pour commencez à dealer...")
	parole("\n----------------------------------------------\n", 0.0002)
	parole("💰C'est le début de votre aventure dans le monde du narcotrafique💰\n", 0.02)
	time.sleep(1)
	_, money = mission_dealeur_1(money)
	print(f"En vendant toute la drogue tu as réussi à te faire {money}$, vous vous rendez donc au QG de Tuco pour lui ramener le fric")
	print("Tuco te regarde sans cligner des yeux. Son sourire nerveux t’indique que t’as pas intérêt à le décevoir.")
	time.sleep(2)
	if money < 10000:
		parole(f"  - {money}$ ?! Tu te fous de moi ? Elle est passée où toute ma cam !!? \n  - Il est où mon putain de fric ?! Tu vas le payer cher !🤬 ", 0.03)
		time.sleep(1)
		print("Il attrape une batte de baseball derrière lui et commence à avancer vers toi.")
		time.sleep(1)
		print("\nTu n’as qu’une seule option : COURIR 🏃")
		input(">>>Appuyez sur Entrée pour COURIR !!!\n")
		money = fuite(money)
	else:
		print("Tu tends l'argent💵. Tuco compte rapidement les billets, renifle, puis explose de rire.")
		parole("\n - Pas mal… PAS MAL DU TOUT ! C'est du bon boulot gamin !\n", 0.03)
		print("Il te balance une liasse supplémentaire.")
		bonus = 100*random.randint(1, 50)
		money += bonus-10000
		print(f"Tuco t’offre un bonus de {bonus}$ pour ta 'motivation'. Nouveau total : {money}$💰")
		time.sleep(1)
		parole(" - Maintenant que t’as prouvé que t’es pas un rigolo… on va passer aux choses sérieuses. ", 0.03)
		print("Tuco ouvre une porte métallique derrière lui, son labo.")
		time.sleep(2)
		money = labo_de_TUCO(money)
	
def dessin():
	print(FOND_BLANC + NOIR + """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠖⣀⠉⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣶⣶⣦⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣛⡟⠛⠛⠛⠛⠛⣛⠛⠛⣟⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⣀⣀⡉⣁⣘⣀⣀⡛⠀⠉⠀⠀⠉⠉⠳⢽⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠉⠡⠤⠤⢄⡀⠉⠉⡿⣷⣆⠀⠀⡇⠈⣿⡇⢈⣛⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⣀⣀⣠⣶⣀⣀⣀⣀⣀⣠⣷⡎⢿⣄⣴⣧⣴⣿⣿⣿⣿⣿⣿⣎⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⣯⣝⢿⣿⣶⣤⣤⣴⣿⣥⣼⠟⢻⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠁⢤⡈⣿⠈⠛⢿⣿⣿⡷⠿⠻⣿⣿⣿⡟⠁⣼⡏⠙⣿⣿⣿⣿⡏⢹⣿⣿⣿⣿⡿⢾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⣶⣷⢻⡀⠀⠸⡆⢹⡇⠀⠈⠙⠛⠋⠃⣨⡿⠀⠀⣿⣿⣿⣿⣿⡄⢨⣿⡿⠋⢀⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠃⢸⣇⠀⠀⠻⣾⣇⠀⠀⠀⠀⣀⣴⡿⠁⠀⠀⠸⣿⣿⣿⣿⣿⣬⣁⣤⣴⣞⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡟⢷⣼⣿⠀⠀⠀⠀⠉⠛⠓⠛⢛⢛⣭⠄⠀⠀⠀⡀⢹⣿⣿⣧⣤⡈⢻⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡶⣽⣿⡾⠂⠀⡀⠀⠀⠀⠀⣴⡿⠳⣤⣤⣤⣤⣽⣾⣿⣿⣿⣿⣿⣄⣯⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⢿⣷⠀⠀⠿⠂⠀⠀⢸⣿⣠⣴⣿⣿⣦⣿⣿⣿⣟⣿⣿⣿⣯⣿⣟⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠰⢲⠄⣦⣤⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⡀⣼⠀⢸⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡏⢷⣼⡄⠈⢸⣿⣿⣿⠋⠀⠀⣀⣤⣤⣤⣤⣴⣿⣿⣿⣿⣟⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⢀⣴⣾⣿⣿⣿⡇⠈⠻⣿⡀⢸⣿⣿⣿⣿⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⡟⠀⠃⠈⠁
⢀⣀⠀⠀⠀⢀⣀⡀⠀⢠⣍⣉⣴⣿⣿⣿⣿⣿⣿⣇⠀⠀⠈⠻⣾⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠋⠉⣉⡉⠉⠉⠉⣉⡩⠯⠉⠁⣄⣤⠀⠀⠀⠀⠀⠀⠀
⣁⣠⣄⣠⣤⣤⣤⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣤⣴⣶⣄⡉⢿⠶⠁⣠⣶⡆⠀⠀⠀⠀⠀⠀⣠
⣬⣿⣏⣹⣿⣭⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⢹⣿⣿⣿⣼⣿⣯⠉⠉⠀⣠⣴⣷⣿⣿⣿⡟⠀⠀⢀⣉⢀⡀⠛
⣁⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣾⣿⣿⣿⠙⣿⣿⣷⣤⣾⡿⣿⣿⣿⣿⣿⣿⣿⡄⢀⡀⠈⠛⠛
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⣸⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⡇⢙⡿⣿⣿⣿⣷⣜⣿⣦⡀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣄⣸⣿⣿⡿⠀⣾⣿⣿⡏⠀⢠⣿⣿⣿⣿⣿⡏⢼⣿⣿⣿⣿⣿⣿⣿⣶⣯⡔⣽⣟⠿⣿⣿⣛⢷⡄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣉⠉⠉⢉⣛⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⣿⣷⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣛⠛⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""" + RESET)
	
def introduction(money):
	parole("\n            --- 💸 A BREAKING BAD STORY 💸 --- ", 0.03)
	dessin()
	input(">>> Appuies sur Entrée pour jouer...")
	parole("Vous êtes Walter Black, un professeur d'informatique au lycée.👨‍💻\nEn vous réveillant, vous checkez vos mails et apprenez que la direction vous a viré car votre métier se fait remplacer par une intelligence artificielle.", 0.01)
	parole("Cette nouvelle vous attriste car ces derniers temps, vous avez quelques soucis financiers... ", 0.01)
	time.sleep(1)
	parole("\nPendant que vous déprimez, votre collègue vous appelle car il a reçu le même mail\nFace à la situation vous décidez :\n 1)De sortir boire un coup au bar pour vous changer les idées\n 2)D'aller manifester devant le lycée avec d'autres enseignants dans votre situation ", 0.01)
	reponse_1 = demander_choix("🔹 Quel est ton choix(sélectionnez le numéro) : ", choix2)
	if int(reponse_1) == 1:
		parole("\nUne fois au bar, le moral n'est toujours pas au top, vous enchaînez verres de bière et de whisky, votre collègue vous propose un plan pour se refaire, aller au casino !", 0.01) 
		time.sleep(1)
		parole("Alors que l'alcool monte petit à petit vous décidez :", 0.01)
		time.sleep(1)
		print(" 1) Refuser et continuer à boire pour oublier vos problèmes\n 2) Aller tenter votre chance au casino !")
		reponse_1_1 = demander_choix("🔹 Que choisissez-vous ? : ", choix2)
		if int(reponse_1_1) == 1: # Branche Ivre
			print("\nVous finissez complètement arraché, torse nu dans le bar, des élèves de votre lycée vous ont filmés vous faire sortir par le videur, avec lequel vous avez démmaré un combat.")
			time.sleep(1.5)
			print("Sans grande surprise, il vous bat et vous rentrez chez vous. Votre femme vous découvre complètement ivre, et sachant que vous n'avez plus de travail, elle décide de vous quitter et de vous virer de la maison qu'elle possède.")
			time.sleep(1.5)
			print("Face à la situation vous décidez :")
			print(" 1)Vous décidez de sortir à nouveau boire comme hier soir car vous en pouvez plus de votre situation\n 2)Vous décidez de reprendre votre vie en main et d'aller trouver un travail chez pôle emploie.")
			reponse_1_1_1 = demander_choix("🔹 Que choisissez-vous ? : ", choix2)
			if int(reponse_1_1_1) == 1:
				parole("\nVous sombrez dans l'alcool, vous perdez tout ce que vous avez dans l'unique objectif de pouvoir acheter une bouteille de plus. Chaque jour devient le même, une bouteille de vodka à la main en dormant sous un pont.", 0.01)
				fin_histoire()
			elif int(reponse_1_1_1) == 2:
				parole("\nÀ cause de l'essor de l'intelligence artificielle, vous avez des difficultés à trouver un travail adapté à vos compétences, vous vous résignez et partez travailler à McDo.", 0.01) 
				time.sleep(1)
				parole("Cela suffit à combler vos besoins, et sans ambitions, vous continuez votre vie ainsi jusqu'à la retraite, une vie simple en fin de compte.", 0.01)
				fin_histoire()
		elif int(reponse_1_1) == 2: # Branche Casino
			parole("\nEt vous voilà arrivé au CASINO !🎰 ", 0.01)
			time.sleep(1)
			print(f"Vous disposez de {money}$, ce qui correspond à tout l'argent que vous avez de côté, y compris l'argent qui est censé rembourser vos prêts et payer les études de votre enfant. Vous décidez de tout mettre en un coup à la roulette.")
			time.sleep(1)
			tours = 0
			while tours < 5:
				print(f"\nTour {tours+1} — Mise actuelle : {money}$")
				print("Vous choisissez de mettre tout votre argent sur le :\n 1)Rouge🔴\n 2)Noir⚫️")
				choix_casino = demander_choix("🔹 Quel est votre choix?", choix2)
				resultat = random.randint(1, 2)
				time.sleep(1)
				parole("\nLa roue tourne ... ♣️♦️♠️♥️", 0.03)
				time.sleep(0.5)
				if int(choix_casino) == resultat:
					money = 2*money
					tours = tours + 1
					parole(f"\nBravo ! Tu gagnes. Ton argent double : {money}$.", 0.01)
					if tours == 5:
						parole(f"JACKPOT ! Tu as gagné 5 fois d’affilée.", 0.01)
						print(f"Tu repars avec {money}$ !!! Vous êtes riche !!! Largement suffisant pour démmarer une nouvelle vie loin de tout problème et proche de toutes les babies dont vous rêvez!!!!")
						fin_histoire()
					time.sleep(1)
					print(f"Comme vous n'êtes pas très futé, vous décidez de remettre tout vos gains en jeux, c'est à dire {money}$")
				else :  
					money = 0
					parole("\nDommage ! La balle ne tombe pas sur votre couleur...", 0.01)
					time.sleep(1)
					print(f"Vous avez perdu TOUTES vos économies vous ne disposez plus que de {money}$")
					break 
			time.sleep(2)
			print("\nVous êtes dépité, viré du casino et n'avait plus un seul euros sur vous ! Un homme en capuche s'approche de vous et vous propose ce deal : ")
			time.sleep(1)
			parole(" - Je t'ai entendu parler dans le casino, t'as plus rien et tu t'y connais en informatique. Je te propose un nouveau job, où tu gagneras en un mois ce que t'aurais gagné en une vie. J'étais comme toi, maintenant je suis plein aux as...", 0.02)
			time.sleep(1)
			print("Que lui répondez vous ?")
			print(" 1) \"Au point où j'en suis, je n'ai plus rien à perdre, dis moi en plus\"\n 2) \"Non ça ira, je ne suis pas intéressé\"")
			décision = demander_choix("🔹 Quel est votre choix ?", choix2)
			if int(décision) == 1 :
				print("\nVous acceptez sans réfléchir. L'homme vous emmène dans une voiture.")
				print("Il vous tend des sachets de métanphétamine et sors un flingue en vous menaçant :")
				parole" - Tiens, ta première mission, revend tout ça d'ici la fin de la semaine et ramène le fric au big boss Tuco, c'est le seul moyen de faire tes preuves dans notre cartel, après ça on en aura pas fini avec toi, crois moi bien!", 0.03)
				print("Trop tard pour reculer, vous n'avez pas d'autre choix que de dealer.")
			elif int(décision) == 2 :
				print("\nVous refusez et tentez de partir pour rentrer chez vous.")
				print("L'homme vous rattrappe aussitôt, sors un flingue, canon sur la tempe il vous dit :")
				parole("\n - Je crois que t'as pas bien compris petit merdeux, ici c'est moi qui décide, et j'ai décidé que tu allez travailler pour moi, revend moi ces sachets de méthamphétamine d'ici la fin de semaine et ramène le fric au big boss Tuco !", 0.02)
				time.sleep(1)
				print("\n Vous êtes dans une impasse pas d'autre choix que d'obéir aux ordres")
				time.sleep(1)
			money = le_cartel(money) # Début dans le cartel
	elif int(reponse_1) == 2: 
		print("\nAvec d'autres professeurs, vous organisez un blocus devant le lycée et des étudiants vous rejoignent pour manifester. ")
		time.sleep(0.75)
		print("La manifestation dégénère rapidement, car de nombreux casseurs s'étaient infiltrés dans vos rangs et les CRS sont appelés. Ces derniers commence à gazer vos collègues. Révoltés, vous décidez de:")
		print(" 1) Sortir votre paff et leur courir dessus.\n 2) Tenter un 1v1 avec un CRS malgré le fait que vous soyez moins imposant qu'un moustique.\n 3) Dire à un CRS que sa soeur est belle (mauvaise idée).\n 4) Leur jeter dessus le plus gros pavé que vous trouvez.")
		reponse_2 = demander_choix("🔹 Quel est votre choix?", choix4)
		if int(reponse_2) in [1, 2, 3, 4]:
			print("\nÉnerver un CRS n'était clairement pas une bonne idée...")
			print("Vous êtes placé en garde à vue. Chaque journée semble interminable.\n")
			jour = 1
			nb_jours = 3   # durée de la garde à vue
			while jour <= nb_jours:
				time.sleep(0.75)
				parole(f"\n📅 Jour {jour} de garde à vue", 0.04)
				time.sleep(0.75)
				print("Les policiers pensent que vous cachez encore quelque chose.")
				print("Ils vous interrogent toute la journée...\n")
				jour = jour + 1
			time.sleep(1)
			print("La garde à vue prend fin après ces longues heures de pression.")
			print("Malgré le fait que les policiers ont décidés d'abandonner la garde à vue, ils décident de vous faire passer un peu de temps en cellule avec des personnes très peu sympatiques, le temps de gérer la partie admistrative...")
			time.sleep(2)
			print("\nUn de vos condétenus, un géorgien de 2m10 et 110kg de muscle avec un t-shirt et un short ufc, vous demande de lui passer vos chaussures car <<elles lui iraient très bien>>.") 
			print("Vous décidez de:\n 1) Le frapper le plus fort possible au visage, même si son menton semble plus solide que les barreaux de votre cellule.\n 2) Vous lui passez vos chaussures comme le bon toutou que vous êtes.")
			(reponse_2_1) = demander_choix("🔹 Quel est votre choix?", choix2)
			if int(reponse_2_1) == 1:
				print("\nVous vous faites mal à la main en essayant de le frapper, il finit par vous soulever et vous lancer sur le sol de la celulle.\nIl récupère vos chaussures pendant que vous pleurez par terre.")
			elif int(reponse_2_1) == 2:
				print("\nContent de sa nouvelle paire de chaussures, il décide de vous laisser tranquile pour le reste du temps.")
			time.sleep(2)
			parole("\nUn autre codétenu vous aborde, il vous explique qu'il est un dealer et il vous propose d'acheter ou de rentrer dans son réseau.", 0.01)
			parole("Vous décidez de:\n 1) Acheter un peu de métamphétamine pour votre consommation personnelle.\n 2) Vous acceptez son offre car vous n'avez plus rien, c'est votre seul moyen de faire de l'argent.\n 3) Vous le dénoncez au policier qui surveille votre cellule car vous savez que vous sortez avant lui", 0.01)	
			reponse_DEAL = demander_choix("🔹 Quel est votre choix?", choix3)
			if int(reponse_DEAL) == 1 :
				print("\nVous acceptez « juste pour essayer ». Le codétenu vous glisse un petit morceau de crystal.")
				time.sleep(0.5)
				print("Vous hésitez… puis vous le prenez. Quelques minutes plus tard, un rush violent vous traverse, des sensations fortes.")
				time.sleep(0.5)
				print("Votre cœur bat à 200, vous êtes dans un état second.")
				time.sleep(0.5)
				print("Mais quand l’effet retombe, un vide énorme vous frappe.")
				time.sleep(0.5)
				input("\nAppuyez sur Entrée pour continuer...")
				print("\nLe lendemain matin, le codétenu vient vous voir :")
				parole(" - Alors, ça t’as plu ? J’en ai encore si tu veux… mais cette fois tu paies. ", 0.03)
				time.sleep(1)
				print("\nVous décidez de :")
				print(" 1) Reprendre une dose .")
				print(" 2) Refuser… mais vous n'avez pas de quoi payer la première dose.")
				choix_drogue = demander_choix("🔹 Quel est votre choix?", choix2)
				if int(choix_drogue) == 1 :
					print("\nVous craquez. Vous en voulez encore. Vous tendez la main.")
					print("Le codétenu sourit :")
					parole("- « Je le savais. »", 0.03)
					time.sleep(1)
					print("Vous avalez la dose, mais cette fois votre corps ne tient pas.")
					time.sleep(1)
					print("Overdose. Vous ne vous relevez jamais.")
					parole("\nLa consommation de stupéfiant est dangereuse pour votre santé, ceci est un message du gouvernement.", 0.03)
					fin_histoire()
				elif int(choix_drogue) == 2 :
					print("\nVous refusez. « Non merci, hier c’était une erreur. »")
					print("Le codétenu change soudain de visage :")
					time.sleep(1)
					parole(" - « Ah ouais ? Donc tu consommes gratos maintenant ? Tu crois que je fais ça par charité ? »", 0.03)
					print("\nIl s’approche de vous, tout près :")
					parole(" - Tu vas rembourser. Et tu vas me rembourser en travaillant pour moi. ", 0.03)
					print("Il vous met dans la main un petit sachet : ")
					parole(" - Tu vas le refourguer discret. Si tu refuses… Quand tu sortiras dehors on te retrouvera et on te fera la peau si tu nous trahis. ", 0.03)
					print("\nVous êtes désormais forcé de dealer pour rembourser votre ‘dette’.")
					print("Au même instant, on vous annonce que vous êtes liberé, c'est la fin de votre séjour en celulle")
					money = sortie_GAV(money)
			elif int(reponse_DEAL) == 2 :
				print("\nVous acceptez la proposition :")
				parole(" - « Bienvenue dans l’entreprise. »", 0.03)
				print("\nIl vous glisse discrètement une dizaine de petits sachets dans la main, c'est de la metanphétamine.\n")
				parole(" - « Tu les écoules aujourd’hui. Prix simple : 500$ la dose. Tu prend 10% pour toi et le reste tu iras les données au big boss Tuco. »", 0.03)
				time.sleep(1)
				print("Vous venez officiellement d'entrer dans la famille. Et en sortir sera presque impossible.")
				time.sleep(1)
				print("Au même instant on vous annonce que vous êtes liberé, c'est la fin de votre séjour en cellulle")
				money = sortie_GAV(money)
			elif int(reponse_DEAL) == 3 :
				print("\nVous signalez discrètement le dealer au policier. En quelques secondes, il se fait attraper.")
				print("Il vous fixe avec une intensité glaçante pendant qu’on l’emmène. Vous savez que ce regard n'annonce rien de bon.")
				time.sleep(1)
				print("Les policiers vous félicitent :")
				parole(" - « Grâce à vous, on a attrapé un gros poisson. Vous êtes officiellement libre. »", 0.03)
				money = sortie_GAV(money)
				time.sleep(1)
				print("\nDehors une camionnette noire s’arrête juste devant vous. Deux hommes descendent.")
				print("C’est le réseau du dealer. Ils vous attrapent sans un mot.")
				input("\nAppuyez sur Entrée pour continuer...")
				print("\nDans un hangar, ils vous expliquent les choses très clairement :")
				parole(" - Tu as dénoncé l’un des nôtres. Maintenant tu as deux options : \n 1) Travailler pour nous. Vendre. Livrer. Fermer ta bouche.\n 2) Disparaître sous une dalle de béton et ne plus jamais poser de problèmes. ", 0.03)
				time.sleep(1)
				choix_final = demander_choix("🔹 Quel est votre choix?", choix2)
				if int(choix_final) == 1 :
					print("\nVous baissez les yeux. Vous savez que vous n’avez aucune autre issue.")
					time.sleep(1)
					parole("« J’accepte. »", 0.02)
					print("L’homme sourit : ")
					parole(" - « Bonne décision. On aime les gens intelligents. Tu commences aujourd’hui. Si tu tentes de fuir… tu connais la suite. Vend tout ces sachets de drogue pour la fin de semaine et ramène le fric au big boss Tuco »", 0.03)
					time.sleep(1)
					print("\nVous êtes libre… mais uniquement pour servir leur réseau.")
				elif int(choix_final) == 2 :
					print("\nVous refusez catégoriquement de collaborer.")
					print("Il soupire, se relève, et fait un signe de tête.")
					time.sleep(1)
					print("\nUn homme s’approche derrière vous")
					time.sleep(1)
					parole("PANNN !!", 0.1)
					parole("Vous êtes mort 💀", 0.1)
					fin_histoire()
			money = le_cartel(money)

def jouer(money):
	introduction(money)

jouer(money)
