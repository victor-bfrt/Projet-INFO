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
print(" 1)De sortir boire coup au bar pour vous changer idées\n 2)D'aller manifester devant le lycée avec d'autres enseignant dans votre cas ")
reponse_1 = input("Quel choix(sélectionnez le numéro) : ")

# Branche 1
if int(reponse_1) == 1:
	print("Une fois au bar le moral n'est toujours pas au top vous enchaîner verres de bière et de wisky, votre collègue vous propse un plan pour se refaire aller au casino !")
	print("Alors que l'alcool monte peit à petit vous décider :")
	print(" 1)Refuser et continuer à boire pour oublier vos problèmes\n 2)Tenter votre chance au casino !")
	reponse_1_1 = input("Que choisissez-vous ? : ")

	# Branche 1-1 Ivre
	if int(reponse 1 1) == 1:
	print("Vous finissez complètement arraché, torse nu dans le bar, des élèves de votre lycée vous ont filmés vous fatre sortir par le videur, avec lequel vous vous êtes battu.")
	print("Sans grande surprise, il vous bat et vous rentrez chez vous.")
	print("Votre femme vous découvre complètement ivre, et sachant que vous n'avez plus de travail, elle décide de vous quitter et de vous virer de la maison qu'elle possède.")
	print("Face à la situation vous décidez :")
	print(" 1)Vous décidez de resortir boire comme hier soir car vous en pouvez plus de votre situation")
	print(" 2)Vous décidez de reprendre votre vie en main et d'aller trouver un emploi chez pôle emploie")
	reponse_1_1_1 = input("Quel est votre choix :")
	
	if int (reponse_1_1_1) == 1:
		print("Vous sombrez dans l'alcool, vous perdez tout ce que vous avez dans l'unique objectif de pouvoir acheter une bouteille de plus.")
		print("Chaque jour devient le même, une bouteille à la main en dormant sous un pont.")
	elif int(reponse_1_1_1) == 2:
		print("À cause de l'essor de l'intelligence artificielle, vous avez des difficultés à trouver un travail adapter à vos compétences, vous vous résignez et partez travaillez chez Mcdo. Cela suffit à combler vos besoins, et sans ambitions, vous continuez votre vie ainsi jusqu'à la retraite, une vie simple en fin de compte.")

	# Branche 1-2 Casino
	if int(reponse 1 1) == 2:
		print("Et vous voilà arrivez au CASINO ! ")
		print(f"Vous disposez de {money}$, ce qui correspond à tout l'argent que vous avez de côté, y compris l'argent qui est censé rembourser vos prêts et payer les études de votre enfant")
		print("Vous décidez de tout mettre en un coup à la roulette.")
		print("Vous choisissez de mettre tout votre argent sur:")
		print(" 1)Le Rouge")
		print(" 2)Le Noir")
		réponse_Casino = input ("Quel est votre choix?")
		Numéro_Casino = random.randint(1,2)
		if int (réponse_Casino) == Numéro_Casino:
			Casino = 1
			money = 2*money
		else:
			Casino = 2
			print ("Dommage!! Vous avez perdu toutes votres argent !")
		while Casino == 1:
			print(f"Vous avez gagné!! Comme vous n'êtes pas très futé, vous décidez de remettre vos gains en jeux, c'est à dire {money}$.")
			print("Choisissez à nouveau sur quelle couleur vous mettez votre argent: 1)Rouge 2)Noir.")")
			réponse_Casino = input ("Quel est votre choix?")
			Numéro _Casino = random. randint (1,2)
			if int(réponse_Casino) == Numéro_Casino:
				Casino = 1
				money = 2*money
			else:
				Casino = 2
				money = 0
				print ("Dommage!! Vous avez perdu toutes vos économies")
			n=n+1
			if n == 4: 
				print(f"Vous venez de remporté le jackpot 5 fois d'affilé, vous êtes riche et vous disposez de ({money}, largement suffisant pour démarer une nouvelle vie loin de tout problèmes !!! ")
				break
		# Branche principale
		print("Vous êtes dépité, viré du casino et n'avait plus un seul euros sur vous ! Un homme en capuche s'approche de vous et vous propose ce deal")
