import random

money = 30000
pv = 100
blue_crystal = 0
Casino = 1
Numéro_Casino = 1 
n = 0

# Introduction
print("Vous êtes Walter Black, un professeur d'informatique de lycée. En vous réveillant, vous checker vos mails et apprenait que la direction vous a virer car votre métier se fait remplacer par une intelligence artificielle")
print("Cette nouvelle vous atriste beaucoup car ces derniers vous avez quelque soucis financier ")
# Premier choix
print("Pendant que vous déprimé votre collégue vous appel car il a reçu le même mail")
print("Face à la situation vous décidez :" )
print(" 1)De sortir boire coup au bar pour vous changer les idées\n 2)D'aller manifester devant le lycée avec d'autres enseignant dans votre cas ")
reponse_1 = input("Quel choix(sélectionnez le numéro) : ")

# Branche 1
if int(reponse_1) == 1:
  print("\nUne fois au bar le moral n'est toujours pas au top vous enchaîner verres de bière et de wisky, votre collègue vous propose un plan pour se refaire aller au casino !") 
	print("Alors que l'alcool monte peit à petit vous décider " )
	print(" 1)Refuser et continuer à boire pour oublier vos problèmes\n 2)Tenter votre chance au casino")
	reponse_1_1 = input("Que choisissez-vous ? : ")
	
	# Branche 1-1 Ivre
	if int(reponse_1_1) == 1:
		print("\nVous finissez complètement arraché, torse nu dans le bar, des élèves de votre lycée vous ont filmés vous faire sortir par le videur, avec lequel vous avez démmaré un combat. Sans grande surprise, il vous bat et vous rentrez chez vous. Votre femme vous découvre complètement ivre, et sachant que vous n'avez plus de travail, elle décide de vous quitter et de vous virer de votre maison qu'elle possède.")
		print("Face à la situation vous décidez :")
		print(" 1)Vous décidez de resortir boire comme hier soir car vous en pouvez plus de votre situation\n 2)Vous décidez de reprendre votre vie en main et d'aller trouver un emploie chez pôle emploie.")
		reponse_1_1_1 = input("Quel est votre choix : ")
		if int(reponse_1_1_1) == 1:
			print("\nVous sombrez dans l'alcool, vous perdez tout ce que vous avez dans l'unique objectif de pouvoir acheter une bouteille de plus. Chaque jour devient le même, une bouteille de vodka à la main en dormant sous un pont.")
		elif int(reponse_1_1_1) == 2:
			print("\nA cause de l'essor de l'intelligence artificielle, vous avez des difficultés à trouver un travail adapter à vos compétences, vous vous résignez et partez travailler à Mcdo. Cela suffit à combler vos besoins, et sans ambitions, vous continuez votre vie ainsi jusqu'à la retraite, une vie simple en fin de compte.")
			
	# Branche 1-2 Casino
	if int(reponse_1_1) == 2:
		print("\nEt vous voilà arrivez au CASINO ! ")
		print(f"Vous disposez de {money} $, ce qui correspond à tout l'argent que vous avez de côté, y compris l'argent qui est censé rembourser vos prêts et payer les études de votre enfant. Vous décidez de tout mettre en un coup à la roulette.")
		print("Vous choisissez de mettre tout votre argent sur:\n 1)Rouge\n 2)Noir.")
		réponse_Casino = input ("Quel est votre choix?")
		Numéro_Casino = random.randint(1,2)
		if int(réponse_Casino) == Numéro_Casino:
			Casino = 1
			money = 2*money
		else:
			Casino = 2
			money=0
			print (f"\nDommage!! Vous avez perdu toutes vos économies vous n'avaez plus que {money}$")
		
		while Casino == 1:
			print(f"\nVous avez gagné!! Comme vous n'êtes pas très futé, vous décidez de remettre vos gains en jeux, c'est à dire {money} $. Choisissez à nouveau sur quelle couleur vous mettez tout votre argent:\n 1)Rouge\n 2)Noir.")
			réponse_Casino = input ("Quel est votre choix?")
			Numéro_Casino = random.randint(1,2)
			if int(réponse_Casino) == Numéro_Casino:
				Casino = 1
				money = 2*money
			else:
				Casino = 2
				money = 0
				print (f"\nDommage!! Vous avez perdu toutes vos économies vous n'avaez plus que {money}$")
			n = n+1
			if n == 4:
				print(f"\nVous venez de remporté le jackpot 5 fois d'affilé, vous êtes riche et vous disposez de {money}$!!!!!! Largement suffisant pour démarer une nouvelle vie loin de tout problèmes mais proche de toutes les babies dont vous rêvez!!!!")
				exit() 
		# Branche principale
		print("\nVous êtes dépité, viré du casino et n'avait plus un seul euros sur vous ! Un homme en capuche s'approche de vous et vous propose ce deal")
		print("Je t'ai entendu parler dans le casino, je sais que t'as plus rien et que tu t'y connais en informatique. Je te propose un nouveau travail, où tu gagneras en un mois ce que t'aurais gagné en une vie. J'étais comme toi y'a plusiseurs années, maintenant je suis plein aux as... affaire à suivre :/")
		
		

# Branche 2 manifestation
elif int(reponse_1) == 2:
	print("\nAvec d'autres professeurs vous organiser un blocus devant le lycée et des etudiants vous rejoignent pour manifester. ")
	print("La manifestation dégénère rapidement, car de nombreux casseurs s'étaient infiltrés dans vos rangs et les CRS sont appelés. Ces derniers commence à gazer vos collègues. Révolté, vous décidez de:")
	print("1)Sortir votre paf et leur courir dessus.\n 2) Tenter un 1v1 avec un CRS malgré le fait que vous soyez moins imposant qu'un moustique.\n 3) Dire à un CRS que sa soeur est belle (mauvaise idée).\n 4)Leur jeter dessus le plus gros pavé que vous trouvez.")
	reponse_2 = input("Que choisissez-vous ?")
	if int(reponse_2) in [1, 2, 3, 4]:
		print("\nEnervez un CRS n'était pas la meilleure idée, vous vous retrouvez en garde en vue.")
		jour = 1
		for i in range (1,4):
			print(f"C'est le jour {jour} de garde à vue. Les policiers pensent que vous ne leur avez pas tout dit, ils continuent de vous poser des questions pour la journée.")
			jour = jour+1
	print("\nMalgré le fait que les policiers ont décidés d'abandonner la garde à vue, ils décident de vous faire passer un peu de temps en cellule avec des personnes très peu sympatiques...")
	print("Un de vos condétenu, un géorgien de 2m10 et 110kg de muscle avec un t-shirt et un short ufc, vous demande de lui passer vos chaussures car <<elles lui iraient très bien>>. Vous décidez de:\n 1)Vous tentez de le frapper le plus fort possible au visage, même si son menton semble plus solide que les barreaux de votre cellule.\n 2) Vous lui passez vos chaussures comme le bon toutou que vous êtes.")
	(reponse_2_1) = input("Que choisissez-vous?")
	if int(reponse_2_1) == 1:
		print("\nVous vous faites mal à la main en essayant de le frapper, il finit par vous soulever et vous lancer sur le sol de la celulle. Il récupère vos chaussures pendant que vous pleurez par terre.")
	elif int(reponse_2_1) == 2:
		print("\nContent de sa nouvelle paire de chaussures, il décide de vous laisser tranquile pour le reste du temps.")
	print("Un autre codétenu vous aborde, il vous explique qu'il est un dealer et il vous propose d'acheter ou de rentrer dans son réseau. Vous décidez de:\n 1) Acheter un peu de métamphétamine pour votre consommation personnelle, vous avez jamais testé et vous êtes curieux.\n 2) Vous acceptez son offre car vous n'avez plus rien, c'est votre seul moyen de faire de l'argent.\n 3) Vous le dénoncez au policier qui surveille votre cellule car vous savez que vous sortez avant lui")	
	reponse_2_A = input("Que choisissez-vous ?")
	
