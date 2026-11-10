# -*- coding: utf-8 -*-
"""Trivial École — 78 questions supplémentaires (niveau junior).
Porte le total à 150 questions, 25 par catégorie.
"""

Q2 = []
def q(c, qq, opts, r, e=""):
    Q2.append({"c":c, "q":qq, "o":opts, "r":r, "e":e})

# ─────────── GÉOGRAPHIE ───────────
q("geo","Quelle est la capitale de l'Italie ?",["Rome","Milan","Naples"],0,"Rome, traversée par le Tibre.")
q("geo","Quel est le plus long fleuve du monde ?",["Le Nil","L'Amazone","Le Mississippi"],0,"Environ 6 700 km. L'Amazone est le plus puissant.")
q("geo","Dans quel pays se trouve le Taj Mahal ?",["L'Inde","Le Pakistan","L'Iran"],0,"À Agra, construit par un empereur moghol.")
q("geo","Sur quel continent se trouve l'Égypte ?",["L'Afrique","L'Asie","L'Europe"],0,"Au nord-est de l'Afrique, bordée par la Méditerranée.")
q("geo","Quelle mer est la plus salée du monde ?",["La mer Morte","La mer Rouge","La Baltique"],0,"On y flotte sans effort : tellement salée que presque rien n'y vit.")
q("geo","Quelle est la capitale de l'Espagne ?",["Madrid","Barcelone","Valence"],0,"Située au centre du pays.")
q("geo","Dans quel pays se trouve la tour de Pise ?",["L'Italie","La Grèce","L'Espagne"],0,"En Toscane, célèbre pour son inclinaison.")
q("geo","Quel est le plus grand pays d'Amérique du Sud ?",["Le Brésil","L'Argentine","Le Pérou"],0,"Il couvre presque la moitié du continent.")
q("geo","Dans quel pays se trouve le Kilimandjaro ?",["La Tanzanie","Le Kenya","L'Éthiopie"],0,"Son sommet est couvert de neige malgré la chaleur.")
q("geo","Quelle est la capitale de l'Allemagne ?",["Berlin","Munich","Hambourg"],0,"Elle redevient capitale après la réunification de 1990.")
q("geo","Quel détroit sépare l'Europe de l'Asie ?",["Le Bosphore","Le détroit de Gibraltar","Le Pas de Calais"],0,"Il traverse Istanbul, en Turquie.")
q("geo","Quelle est la plus grande île du monde ?",["Le Groenland","Madagascar","La Nouvelle-Guinée"],0,"Une île immense, mais pas un continent.")
q("geo","Quelle est la capitale du Maroc ?",["Rabat","Casablanca","Marrakech"],0,"Casablanca est la plus grande ville, Rabat la capitale.")

# ─────────── HISTOIRE ───────────
q("his","Qui était Cléopâtre ?",["Une reine d'Égypte","Une impératrice romaine","Une reine de France"],0,"Le dernier grand pharaon d'Égypte.")
q("his","Qui a unifié une grande partie de la Gaule ?",["Clovis","Vercingétorix","Charlemagne"],0,"Roi des Francs, au début du VIe siècle.")
q("his","Quel roi a fait construire Chambord ?",["François Ier","Louis XIV","Henri IV"],0,"Un château de la Renaissance, en Sologne.")
q("his","Quel jour est signé l'armistice de 1918 ?",["Le 11 novembre","Le 8 mai","Le 14 juillet"],0,"À 11 heures, le 11 du 11 : d'où la date de commémoration.")
q("his","Quel savant a créé le prix qui porte son nom ?",["Alfred Nobel","Einstein","Pasteur"],0,"Inventeur de la dynamite, il crée les prix en 1901.")
q("his","Qui a été le premier homme à marcher sur la Lune ?",["Neil Armstrong","Youri Gagarine","Buzz Aldrin"],0,"Le 20 juillet 1969, mission Apollo 11.")
q("his","En quelle année l'Empire romain d'Occident s'effondre-t-il ?",["476","800","1492"],0,"Date conventionnelle de la fin de l'Antiquité.")
q("his","Quand l'euro est-il entré en circulation sous forme de pièces et billets ?",["2002","1992","2010"],0,"L'euro existait « en compte » dès 1999.")
q("his","Combien d'années a duré la guerre de Cent Ans ?",["Environ 116 ans","Exactement 100 ans","Environ 50 ans"],0,"De 1337 à 1453 : le nom est arrondi.")
q("his","Quel empire Charlemagne a-t-il fondé ?",["L'Empire carolingien","L'Empire romain","L'Empire byzantin"],0,"Couronné empereur à Rome en 800.")
q("his","Qui a écrit la Déclaration d'indépendance des États-Unis ?",["Thomas Jefferson","George Washington","Benjamin Franklin"],0,"Adoptée le 4 juillet 1776.")
q("his","Quelle reine d'Égypte a été la dernière de sa lignée ?",["Cléopâtre VII","Néfertiti","Hatchepsout"],0,"Elle se suicide après la défaite face à Rome.")
q("his","Quel mur séparait Berlin pendant la Guerre froide ?",["Le mur de Berlin","Le mur d'Hadrien","La ligne Maginot"],0,"Construit en 1961, tombé en 1989.")

# ─────────── ARTS & LITTÉRATURE ───────────
q("art","Qui a écrit « Roméo et Juliette » ?",["Shakespeare","Molière","Victor Hugo"],0,"Une tragédie anglaise de la fin du XVIe siècle.")
q("art","Qui a peint « Guernica » ?",["Picasso","Dalí","Miró"],0,"En réaction au bombardement d'une ville espagnole en 1937.")
q("art","Qui a écrit « L'Avare » ?",["Molière","Racine","Corneille"],0,"Harpagon et sa cassette d'or.")
q("art","Qui a composé « La Flûte enchantée » ?",["Mozart","Beethoven","Bach"],0,"Un opéra créé en 1791.")
q("art","Qui a créé « Le Petit Nicolas » ?",["Sempé et Goscinny","Hergé","Uderzo"],0,"Dessins de Sempé, textes de Goscinny.")
q("art","Qui a peint la série des « Nymphéas » ?",["Claude Monet","Renoir","Cézanne"],0,"Peinte dans son jardin de Giverny.")
q("art","Qui a écrit « L'Odyssée » ?",["Homère","Virgile","Sophocle"],0,"Le retour d'Ulysse après la guerre de Troie.")
q("art","Qui a conçu la tour Eiffel ?",["Gustave Eiffel","Le Corbusier","Viollet-le-Duc"],0,"Pour l'Exposition universelle de 1889.")
q("art","Qui a écrit « Charlie et la chocolaterie » ?",["Roald Dahl","J.K. Rowling","Lewis Carroll"],0,"Willy Wonka et sa fabrique.")
q("art","Combien de touches compte un piano standard ?",["88","61","100"],0,"52 blanches et 36 noires.")
q("art","Qui a peint la voûte de la chapelle Sixtine ?",["Michel-Ange","Raphaël","Léonard de Vinci"],0,"Notamment la Création d'Adam, au Vatican.")
q("art","Quel est le style de la cathédrale de Chartres ?",["Gothique","Roman","Baroque"],0,"Reconnue pour ses vitraux bleus.")
q("art","Qui a écrit « Alice au pays des merveilles » ?",["Lewis Carroll","Roald Dahl","Perrault"],0,"Publié en 1865.")

# ─────────── SCIENCES & NATURE ───────────
q("sci","Quelle est la plus grande planète du système solaire ?",["Jupiter","Saturne","Neptune"],0,"Elle pourrait contenir plus de 1 300 Terres.")
q("sci","Combien de pattes a une araignée ?",["8","6","10"],0,"Huit pattes : ce n'est pas un insecte (qui en a six).")
q("sci","Quel organe filtre le sang ?",["Les reins","Le foie","Le cœur"],0,"Ils produisent aussi l'urine.")
q("sci","Quel est le plus grand mammifère terrestre ?",["L'éléphant d'Afrique","La girafe","Le rhinocéros"],0,"Jusqu'à 6 tonnes.")
q("sci","Combien de temps met la lumière du Soleil pour nous parvenir ?",["Environ 8 minutes","8 secondes","8 heures"],0,"150 millions de km à 300 000 km/s.")
q("sci","Quel est le symbole chimique du fer ?",["Fe","Fr","Fi"],0,"Du latin ferrum.")
q("sci","Quel animal change de peau en muant ?",["Le serpent","Le chat","Le dauphin"],0,"La mue permet de grandir.")
q("sci","Quelle planète est appelée la planète rouge ?",["Mars","Vénus","Mercure"],0,"À cause de l'oxyde de fer de son sol.")
q("sci","Quel gaz les plantes absorbent-elles pour fabriquer leur nourriture ?",["Le dioxyde de carbone","L'oxygène","L'azote"],0,"Elles rejettent de l'oxygène.")
q("sci","Quelle partie de la plante absorbe l'eau du sol ?",["Les racines","Les feuilles","Les fleurs"],0,"Les poils absorbants des racines.")
q("sci","Combien de dents de lait un enfant a-t-il ?",["20","32","24"],0,"Elles tombent entre 6 et 12 ans.")
q("sci","Quel est l'organe de la respiration ?",["Les poumons","Le foie","L'estomac"],0,"Ils échangent l'oxygène et le dioxyde de carbone.")
q("sci","Quelle est l'unité de mesure de la température ?",["Le degré Celsius","Le mètre","Le litre"],0,"0 °C = eau gelée, 100 °C = eau bouillante.")

# ─────────── SPORTS & LOISIRS ───────────
q("spo","Combien de joueurs compte une équipe de volley-ball sur le terrain ?",["6","5","7"],0,"Six contre six, avec rotation.")
q("spo","Quel sport pratique Teddy Riner ?",["Le judo","La boxe","La lutte"],0,"Multiple champion olympique et mondial.")
q("spo","Dans quelle ville se joue le tournoi de Wimbledon ?",["Londres","Paris","New York"],0,"Le plus ancien tournoi de tennis, sur gazon.")
q("spo","Combien de temps dure un match de football ?",["90 minutes","60 minutes","120 minutes"],0,"Deux mi-temps de 45 minutes.")
q("spo","Quel sport se joue avec un volant ?",["Le badminton","Le tennis","Le squash"],0,"Le volant est plus léger qu'une balle.")
q("spo","Combien de joueurs compte une équipe de rugby à XV ?",["15","13","11"],0,"Quinze joueurs sur le terrain.")
q("spo","Dans quel pays le judo est-il né ?",["Le Japon","La Chine","La Corée"],0,"Créé par Jigoro Kano à la fin du XIXe siècle.")
q("spo","Quel sport enchaîne natation, vélo et course ?",["Le triathlon","Le décathlon","Le pentathlon"],0,"Trois disciplines, un seul enchaînement.")
q("spo","Combien de sets faut-il gagner pour remporter Roland-Garros messieurs ?",["3","2","4"],0,"Match en trois sets gagnants.")
q("spo","Quel sport a rendu Zinédine Zidane célèbre ?",["Le football","Le basket","Le handball"],0,"Champion du monde en 1998.")
q("spo","Quel sport consiste à faire tomber des quilles avec une boule ?",["Le bowling","Le curling","Le golf"],0,"Sur une piste, en visant les quilles.")
q("spo","Tous les combien d'années ont lieu les Jeux olympiques d'hiver ?",["Tous les 4 ans","Tous les 2 ans","Tous les 5 ans"],0,"En alternance avec ceux d'été, décalés de deux ans.")
q("spo","Combien de joueurs compte une équipe de handball ?",["7","6","8"],0,"Six joueurs de champ et un gardien.")

# ─────────── DIVERTISSEMENTS ───────────
q("div","Comment s'appelle le héros de Dragon Ball ?",["Sangoku","Naruto","Luffy"],0,"Son nom japonais est Son Goku.")
q("div","Qui a créé Mickey Mouse ?",["Walt Disney","Charlie Chaplin","Walt Whitman"],0,"Apparu en 1928 dans un dessin animé.")
q("div","Dans quel dessin animé Bob l'éponge vit-il dans un ananas ?",["Bob l'éponge","Les Simpson","Scooby-Doo"],0,"Sous la mer, à Bikini Bottom.")
q("div","Quel studio a produit « Toy Story » ?",["Pixar","Disney","DreamWorks"],0,"Le premier film entièrement en images de synthèse (1995).")
q("div","Combien de cases compte le plateau du Monopoly français ?",["40","30","50"],0,"Dont quatre coins et des rues à acheter.")
q("div","Quel super-héros se déplace en lançant des toiles ?",["Spider-Man","Batman","Superman"],0,"Spiderman, l'homme-araignée.")
q("div","Quel jeu de société consiste à ruiner ses adversaires en achetant des rues ?",["Le Monopoly","Le Cluedo","Le Scrabble"],0,"Le but : faire faillite aux autres.")
q("div","Quel manga raconte l'histoire de pirates en quête d'un trésor ?",["One Piece","Naruto","Bleach"],0,"Luffy cherche le One Piece.")
q("div","Quelle fête tombe le 25 décembre ?",["Noël","La Toussaint","Pâques"],0,"Et le 24 au soir, le réveillon.")
q("div","Quel personnage de dessin animé est un chat paresseux et gourmand ?",["Garfield","Tom","Sylvestre"],0,"Il déteste les lundis.")
q("div","Dans quel jeu doit-on deviner qui a commis un meurtre dans un manoir ?",["Le Cluedo","Le Risk","Les petits chevaux"],0,"Avec le colonel Moutarde et d'autres suspects.")
q("div","Quel est le nom du cirque le plus célèbre au monde ?",["Le Cirque du Soleil","Le cirque Pinder","Le cirque d'hiver"],0,"Fondé au Québec en 1984.")
q("div","Combien de joueurs compte une équipe de e-sport dans un match de football virtuel ?",["11","5","6"],0,"Comme au football réel : onze par équipe.")
