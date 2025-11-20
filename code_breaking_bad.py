import random

money = 30000
pv = 100
blue_crystal = 0

# Introduction
print("Vous êtes Walter Black, un professeur d'informatique de lycée. En vous réveillant, vous checker vos mails et apprenait que la direction vous a viré car votre métier se fait remplacer par une intelligence artificielle")
print("Cette nouvelle vous attriste car ces derniers temps, vous avez quelques soucis financiers... ")
# Premier choix
print("Pendant que vous déprimé votre collègue vous appel car il a reçu le même mail.")
print("Face à la situation vous décidez :" )
print(" 1)De sortir boire un coup au bar pour vous changer les idées\n 2)D'aller manifester devant le lycée avec d'autres enseignants dans votre cas ")
reponse_1 = input("Quel choix(sélectionnez le numéro) : ")

# Branche 1
if int(reponse_1) == 1:
	print("\nUne fois au bar le moral n'est toujours pas au top vous enchaînez verres de bière et de whisky, votre collègue vous propose un plan pour se refaire aller au casino !") 
	print("Alors que l'alcool monte petit à petit vous décidez :" )
	print(" 1)Refuser et continuer à boire pour oublier vos problèmes\n 2)Aller tenter votre chance au casino !")
	reponse_1_1 = input("Que choisissez-vous ? : ")
	
	# Branche 1-1 Ivre
	if int(reponse_1_1) == 1:
		print("\nVous finissez complètement arraché, torse nu dans le bar, des élèves de votre lycée vous ont filmés vous faire sortir par le videur, avec lequel vous avez démmaré un combat.")
		print("Sans grande surprise, il vous bat et vous rentrez chez vous. Votre femme vous découvre complètement ivre, et sachant que vous n'avez plus de travail, elle décide de vous quitter et de vous virer de la maison qu'elle possède.")
		print("Face à la situation vous décidez :")
		print(" 1)Vous décidez de resortir boire comme hier soir car vous en pouvez plus de votre situation\n 2)Vous décidez de reprendre votre vie en main et d'aller trouver un emploie chez pôle emploie.")
		reponse_1_1_1 = input("Quel est votre choix : ")
		if int(reponse_1_1_1) == 1:
			print("\nVous sombrez dans l'alcool, vous perdez tout ce que vous avez dans l'unique objectif de pouvoir acheter une bouteille de plus. Chaque jour devient le même, une bouteille de vodka à la main en dormant sous un pont.")
		elif int(reponse_1_1_1) == 2:
			print("\nÀ cause de l'essor de l'intelligence artificielle, vous avez des difficultés à trouver un travail adapté à vos compétences, vous vous résignez et partez travailler à McDo.") 
			print("Cela suffit à combler vos besoins, et sans ambitions, vous continuez votre vie ainsi jusqu'à la retraite, une vie simple en fin de compte.")
			
	# Branche 1-2 Casino
	elif int(reponse_1_1) == 2:
		print("\nEt vous voilà arrivez au CASINO ! ")
		print(f"Vous disposez de {money}$, ce qui correspond à tout l'argent que vous avez de côté, y compris l'argent qui est censé rembourser vos prêts et payer les études de votre enfant. Vous décidez de tout mettre en un coup à la roulette.")
		tours = 0
		while tours < 5:
			print(f"\nTour {tours+1} — Mise actuelle : {money}$")
			print("Vous choisissez de mettre tout votre argent sur le :\n 1)Rouge\n 2)Noir.")
			choix_casino = input ("Quel est votre choix?")
			resultat = random.randint(1, 2)
			
			if int(choix_casino) == resultat:      # Victoire
				money = 2*money
				tours = tours + 1
				print(f"\nBravo ! Tu gagnes. Ton argent double : {money}$.")
				
				if tours == 5:
					print(f"JACKPOT ! Tu as gagné 5 fois d’affilée.")
					print(f"Tu repars avec {money}$ !!! Vous êtes riche !!! Largement suffisant pour démarer une nouvelle vie loin de tout problèmes et proche de toutes les babies dont vous rêvez!!!!")
					exit() 
				print(f"Comme vous n'êtes pas très futé, vous décidez de remettre tout vos gains en jeux, c'est à dire {money}$")
			else :  
				money = 0
				print("\nDommage ! La balle ne tombe pas sur votre couleur...")
				print(f"Vous avez perdu TOUTES vos économies vous ne disposez plus que de {money}$")
				break 

		print("\nVous êtes dépité, viré du casino et n'avait plus un seul euros sur vous ! Un homme en capuche s'approche de vous et vous propose ce deal")
		print("Je t'ai entendu parler dans le casino, je sais que t'as plus rien et que tu t'y connais en informatique. Je te propose un nouveau job, où tu gagneras en un mois ce que t'aurais gagné en une vie. J'étais comme toi y'a plusiseurs années, maintenant je suis plein aux as...")
		print("Que lui répondez vous ?")
		print(" 1) <<Au point où j'en suis je n'ai plus rien à perdre dis moi en plus>> suis  \n 2) <<Non ça ira je ne suis pas intéressé>>")
		décision = input("Votre choix : ")
		if int(décision) == 1 :
			print("\nVous acceptez sans réfléchir. L'homme vous emmène dans une voiture.")
			print("Il vous tend des sachets métanphétamine et sors un flingue en vous menaçant :")
			print("<<Tiens, ta première mission, revend tous ça d'ici la fin de semaine et ramène le fric au big boss Tuco c'est le seul moyen de faire tes preuves dans notre cartel, après ça on en aura pas fini avec toi crois moi bien!") 
			print("Trop tard pour reculer, vous n'avez pas d'autre choix que de dealer.")
		elif int(décision) == 2 :
			print("\nVous refusez et tentez de partir pour rentrer chez vous")
			print("L'homme vous rattrappe aussitôt, sors un flingue, canon sur la tempe il vous dit :")
			print("<< Je crois t'as pas bien compris petit merdeux ici c'est moi qui décide, et j'ai décidé que tu allé travailler pour moi, revend moi ces sachets de méthamphétamine d'ici la fin de semaine et ramène le fric au big boss Tuco>>")
			print("Vous êtes dans une impasse pas d'autre choix que d'obéïr aux ordres")
			
		# Début dans le cartel
		le_cartel()

# Branche 2 manifestation
elif int(reponse_1) == 2:
	print("\nAvec d'autres professeurs vous organisez un blocus devant le lycée et des étudiants vous rejoignent pour manifester. ")
	print("La manifestation dégénère rapidement, car de nombreux casseurs s'étaient infiltrés dans vos rangs et les CRS sont appelés. Ces derniers commence à gazer vos collègues. Révolté, vous décidez de:")
	print(" 1)Sortir votre paff et leur courir dessus.\n 2) Tenter un 1v1 avec un CRS malgré le fait que vous soyez moins imposant qu'un moustique.\n 3) Dire à un CRS que sa soeur est belle (mauvaise idée).\n 4)Leur jeter dessus le plus gros pavé que vous trouvez.")
	reponse_2 = input("Que choisissez-vous ?")
	if int(reponse_2) in [1, 2, 3, 4]:
		print("\nÉnerver un CRS n'était clairement pas une bonne idée...")
		print("Vous êtes placé en garde à vue. Chaque journée semble interminable.\n")
		jour = 1
		nb_jours = 3   # durée de la garde à vue
		while jour <= nb_jours:
			input(f"Appuyez sur Entrée pour passer au jour {jour}...")
			print(f"\n📅 Jour {jour} de garde à vue")
			print("Les policiers pensent que vous cachez encore quelque chose.")
			print("Ils vous interrogent toute la journée...\n")
			jour = jour + 1
		print("La garde à vue prend fin après ces longues heures de pression.")
		print("Malgré le fait que les policiers ont décidés d'abandonner la garde à vue, ils décident de vous faire passer un peu de temps en cellule avec des personnes très peu sympatiques, le temps de gérer la partie admistrative...")
		print("\nUn de vos condétenu, un géorgien de 2m10 et 110kg de muscle avec un t-shirt et un short ufc, vous demande de lui passer vos chaussures car <<elles lui iraient très bien>>.")
		print("Vous décidez de:\n 1) Vous tentez de le frapper le plus fort possible au visage, même si son menton semble plus solide que les barreaux de votre cellule.\n 2) Vous lui passez vos chaussures comme le bon toutou que vous êtes.")
		(reponse_2_1) = input("Que choisissez-vous?")
		if int(reponse_2_1) == 1:
			print("\nVous vous faites mal à la main en essayant de le frapper, il finit par vous soulever et vous lancer sur le sol de la celulle. Il récupère vos chaussures pendant que vous pleurez par terre.")
		elif int(reponse_2_1) == 2:
			print("\nContent de sa nouvelle paire de chaussures, il décide de vous laisser tranquile pour le reste du temps.")
		print("Un autre codétenu vous aborde, il vous explique qu'il est un dealer et il vous propose d'acheter ou de rentrer dans son réseau.")
		print("Vous décidez de:\n 1) Acheter un peu de métamphétamine pour votre consommation personnelle, vous avez jamais testé et vous êtes curieux.\n 2) Vous acceptez son offre car vous n'avez plus rien, c'est votre seul moyen de faire de l'argent.\n 3) Vous le dénoncez au policier qui surveille votre cellule car vous savez que vous sortez avant lui")	
		reponse_DEAL = input("Que choisissez-vous ?")
		
		if int(reponse_DEAL) == 1 :
			print("\nVous acceptez « juste pour essayer ». Le codétenu vous glisse un petit morceau de cristal.")
			print("Vous hésitez… puis vous le prenez. Quelques minutes plus tard, un rush violent vous traverse, des sensations fortes.")
			print("Votre cœur bat à 200, vous êtes dans un état second.")
			print("Mais quand l’effet retombe, un vide énorme vous frappe.")
			input("\nAppuyez sur Entrée pour continuer...")
			print("\nLe lendemain matin, le codétenu vient vous voir :")
			print("« Alors, ça t’a plu ? J’en ai encore si tu veux… mais cette fois tu paies. »")
			print("\nVous décidez de :")
			print(" 1) Reprendre une dose (vous en voulez vraiment).")
			print(" 2) Refuser… mais vous n'avez pas de quoi payer la première dose.")
			choix_drogue = input("Votre choix ? ")
			if int(choix_drogue) == 1 :
				print("\nVous craquez. Vous en voulez encore. Vous tendez la main.")
				print("Le codétenu sourit : « Je le savais. »")
				print("Vous avalez la dose, mais cette fois votre corps ne tient pas.")
				input("\nAppuyez sur Entrée pour continuer...")
				print("Overdose. Vous ne vous relevez jamais.")
				print("La consommation de stupéfiant est dangereuse pour votre santé ceci est un message du gouvernement.")
				quit()
			elif int(choix_drogue) == 2 :
				print("\nVous refusez. « Non merci, hier c’était une erreur. »")
				print("Le codétenu change soudain de visage « Ah ouais ? Donc tu consommes gratos maintenant ? Tu crois que je fais ça par charité ? »")
				print("\nIl s’approche de vous, tout près :")
				print("« Tu vas rembourser. Et tu vas rembourser en travaillant pour moi. »")
				print("Il vous met dans la main un petit sachet : « Tu vas le refourguer discret. Si tu refuses… »")
				print("« Quand tu sortiras dehors on te retrouvera et ton fera la peau si tu nous trahi. »")
				print("\nVous êtes désormais forcé de dealer pour rembourser votre ‘dette’.")
				print("Au même instant on vous annonce que vous êtes liberé c'est la fin de votre séjour en cellulle")
		
		elif int(reponse_DEAL) == 2 :
			print("\nVous acceptez la proposition. Le codétenu hoche la tête : « Bienvenue dans l’entreprise. »")
			print("Il vous glisse discrètement trois petits sachets dans la main, c'est de la metenphétamine.")
			print("« Tu les écoules aujourd’hui. Prix simple : 500$ la dose. Tu prend 50% pour toi et le reste tu iras les données au big boss Tuco. »")
			print("Vous venez officiellement d'entrer dans la famille. Et en sortir sera presque impossible.")
			print("Au même instant on vous annonce que vous êtes liberé c'est la fin de votre séjour en cellulle")

		elif int(reponse_DEAL) == 3 :
			print("\nVous signalez discrètement le dealer au policier. En quelques secondes, il se fait attraper.")
			print("Il vous fixe avec une intensité glaçante pendant qu’on l’emmène. Vous savez que ce regard n'annonce rien de bon.")
			print("Les policiers vous félicitent : « Grâce à vous, on a attrapé un gros poisson. Vous êtes officiellement libre. »")
			print("Une fois libre Une camionnette noire s’arrête juste devant vous. Deux hommes descendent.")
			print("C’est le réseau du dealer. Ils vous attrapent sans un mot.")
			input("\nAppuyez sur Entrée pour continuer...")
			print("\nDans un hangar, ils vous expliquent les choses très clairement :")
			print("« Tu as dénoncé l’un des nôtres. Maintenant tu as deux options : »")
			print("1) Travailler pour nous. Vendre. Livrer. Fermer ta bouche.")
			print("2) Disparaître sous une dalle de béton et ne plus jamais poser de problèmes.")
			choix_final = input("Votre choix ? ")
			if int(choix_final) == 1 :
				print("\nVous baissez les yeux. Vous savez que vous n’avez aucune autre issue.")
				print("« D’accord... j’accepte. »")
				print("L’homme sourit : « Bonne décision. On aime les gens intelligents. »")
				print("Il coupe vos liens et vous tend un sac rempli de petits sachets.")
				print("« Tu commences aujourd’hui. Si tu tentes de fuir… tu connais la suite. Vend tout ces sachet pour la fin de semaine et ramène le pognoin au big boss Tuco »")
				print("Vous êtes libre… mais uniquement pour servir leur réseau.")
		
			elif int(choix_final) == 2 :
				print("\nVous refusez catégoriquement de collaborerer.")
				print("Il soupire, se relève, et fait un signe de tête.")
				input("\nAppuyez sur Entrée pour continuer...")
				print("\nUn homme s’approche derrière vous")
				print("PANNN !!")
				print("Vous êtes mort")
				quit()
				
		# Début dans le cartel
		le_cartel()


# Fonction : Début dans le cartel
def le_cartel():
	print("C'est le début de votre aventure dans le monde du narcotrafique")


	
