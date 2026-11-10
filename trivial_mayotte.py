# -*- coding: utf-8 -*-
"""Paquet spécial Mayotte — 50 questions, réparties dans les 6 catégories.
Niveau junior. Faits vérifiés (dates, géographie, faune, culture).
"""

QM = []
def q(c, qq, opts, r, e=""):
    QM.append({"c":c, "q":qq, "o":opts, "r":r, "e":e})

# ─────────── GÉOGRAPHIE (9) ───────────
q("geo","Dans quel océan se trouve Mayotte ?",["L'océan Indien","L'océan Atlantique","La mer Méditerranée"],0,"Entre Madagascar et la côte est de l'Afrique.")
q("geo","Depuis quelle année Mayotte est-elle un département français ?",["2011","1975","1999"],0,"Le 31 mars 2011 : Mayotte devient le 101e département.")
q("geo","Quel est le chef-lieu de Mayotte ?",["Mamoudzou","Dzaoudzi","Bandraboua"],0,"Mamoudzou, sur Grande-Terre — Dzaoudzi l'était avant 1977.")
q("geo","Quelles sont les deux îles principales de Mayotte ?",["Grande-Terre et Petite-Terre","Mohéli et Anjouan","Nosy Be et Nosy Komba"],0,"Grande-Terre (Mahoré) et Petite-Terre (Pamanzi), reliées par la barge.")
q("geo","Quel pays est le plus proche de Mayotte ?",["Les Comores","Madagascar","Le Mozambique"],0,"Anjouan est à environ 70 km.")
q("geo","Quel est le point culminant de Mayotte ?",["Le mont Bénara","Le mont Choungui","Le Karthala"],0,"Environ 660 m. Le Karthala est un volcan des Comores.")
q("geo","Comment traverse-t-on de Mamoudzou à Dzaoudzi ?",["En barge","En train","Par un pont"],0,"La barge transporte passagers et véhicules plusieurs fois par jour.")
q("geo","À quel archipel Mayotte appartient-elle ?",["L'archipel des Comores","Les Mascareignes","Les Seychelles"],0,"Quatre îles : Grande Comore, Anjouan, Mohéli et Mayotte.")
q("geo","Quelle est la superficie approximative de Mayotte ?",["Environ 374 km²","Environ 1 000 km²","Environ 5 000 km²"],0,"Petite, mais avec un lagon immense : plus grand que l'île.")

# ─────────── HISTOIRE (8) ───────────
q("his","En quelle année Mayotte est-elle devenue française ?",["1841","1897","1958"],0,"Le sultan Andriantsoly cède l'île à la France.")
q("his","En quelle année les Mahorais ont-ils voté pour rester français ?",["1974","1960","1981"],0,"Le 22 décembre 1974, Mayotte vote non à l'indépendance.")
q("his","Quel sultan a cédé Mayotte à la France ?",["Andriantsoly","Radama","Sakalava"],0,"Il régnait sur Mayotte au milieu du XIXe siècle.")
q("his","Comment s'appelle le statut de Mayotte devenu département ?",["Un DROM","Une collectivité d'outre-mer","Un TOM"],0,"Département et région d'outre-mer.")
q("his","Quel peuple a d'abord peuplé Mayotte ?",["Des populations bantoues et malgaches","Les Vikings","Les Incas"],0,"D'où deux langues : le shimaoré et le kibushi.")
q("his","Que s'est-il passé en 1975 pour l'archipel des Comores ?",["L'indépendance","Une éruption","Un cyclone"],0,"Sauf Mayotte, qui a choisi de rester française.")
q("his","Quelle est la date de la départementalisation de Mayotte ?",["Le 31 mars 2011","Le 14 juillet 2011","Le 1er janvier 2000"],0,"Mayotte devient le 101e département français.")
q("his","Quel roi malgache a régné sur Mayotte au XIXe siècle ?",["Andriantsoly","Ranavalona","Radama Ier"],0,"Il était d'origine sakalava, à Madagascar.")

# ─────────── SCIENCES & NATURE (9) ───────────
q("sci","Quel animal marin vient mettre bas dans le lagon de Mayotte ?",["La baleine à bosse","Le requin-baleine","L'orque"],0,"De juillet à octobre.")
q("sci","Quel animal est emblématique et unique à Mayotte ?",["Le maki (lémur brun)","Le koala","Le panda"],0,"Un lémur endémique, présent nulle part ailleurs.")
q("sci","Qu'est-ce qu'une mangrove ?",["Une forêt au bord de l'eau salée","Une plage de sable","Un récif corallien"],0,"C'est la nurserie des poissons et une protection contre les cyclones.")
q("sci","Quelle est la particularité du lagon de Mayotte ?",["Il a une double barrière de corail","Il est fait d'eau douce","Il gèle en hiver"],0,"L'un des plus grands lagons fermés du monde.")
q("sci","Quel risque naturel menace le plus Mayotte ?",["Les cyclones","Les avalanches","Les tempêtes de neige"],0,"Saison cyclonique de décembre à mars. Aussi les séismes.")
q("sci","Quelle fleur est cultivée à Mayotte pour le parfum ?",["L'ylang-ylang","La rose de mai","La tulipe"],0,"Son essence entre dans de nombreux parfums.")
q("sci","Quel animal pond ses œufs sur les plages de Mayotte ?",["La tortue marine","Le dauphin","Le dugong"],0,"La tortue verte et la tortue imbriquée sont protégées.")
q("sci","Le sol de Mayotte est d'origine…",["volcanique","glaciaire","désertique"],0,"Les îles sont des volcans sous-marins.")
q("sci","Que protège une réserve comme celle de N'Gouja ?",["Les tortues et le récif","Les voitures","Les cultures"],0,"On y observe des tortues qui viennent brouter l'herbe marine.")

# ─────────── ARTS & LITTÉRATURE (7) ───────────
q("art","Qu'est-ce que le « m'sindzano » ?",["Un masque de beauté au bois de santal","Un plat","Une danse"],0,"Une peinture traditionnelle appliquée sur le visage.")
q("art","Quelle est la langue la plus parlée à Mayotte ?",["Le shimaoré","Le français uniquement","Le malgache uniquement"],0,"Le shimaoré, proche du comorien, et le kibushi d'origine malgache.")
q("art","Qu'est-ce que le « deba » ?",["Des chants et danses traditionnels","Un instrument","Un conte écrit"],0,"Une tradition orale transmise entre générations.")
q("art","Comment dit-on « marahaba » en shimaoré ?",["Bienvenue","Au revoir","Merci beaucoup"],0,"On le dit aussi pour accueillir quelqu'un avec joie.")
q("art","Quel tissu porte-t-on traditionnellement en écharpe à Mayotte ?",["Le lamba","Le kimono","Le kilt"],0,"Un pagne coloré, porté aussi en écharpe sur l'épaule.")
q("art","Quel conte oral raconte souvent les aventures d'un animal rusé ?",["Un conte populaire transmis oralement","Un roman de Victor Hugo","Une pièce de Molière"],0,"La tradition orale est très vivante à Mayotte.")
q("art","Quel instrument traditionnel accompagne les chants mahorais ?",["Le tambour","Le piano","La guitare électrique"],0,"Les percussions rythment les danses communautaires.")

# ─────────── SPORTS & LOISIRS (8) ───────────
q("spo","Quel est le sport le plus pratiqué à Mayotte ?",["Le football","Le hockey","Le ski"],0,"Très populaire dans les villages et les écoles.")
q("spo","Quelle est la discipline de combat traditionnelle de Mayotte ?",["Le moringue","Le karaté","La boxe thaïe"],0,"Un art martial local, aussi pratiqué à La Réunion.")
q("spo","Quel type de course nautique est traditionnel à Mayotte ?",["La course de pirogues","La voile olympique","L'aviron"],0,"Des pirogues à balancier, héritées de la tradition malgache.")
q("spo","Quel sport permet de découvrir les fonds du lagon ?",["La plongée sous-marine","Le curling","Le ski nautique"],0,"Le récif et ses coraux attirent des plongeurs du monde entier.")
q("spo","Quel sport de raquette se joue beaucoup à Mayotte ?",["Le tennis de table","Le squash","Le hockey sur gazon"],0,"Les tables de ping-pong sont partout dans les écoles.")
q("spo","Quelle activité permet de découvrir la forêt de Mayotte ?",["La randonnée","Le ski","Le patinage"],0,"De nombreux sentiers mènent au mont Choungui ou au Bénara.")
q("spo","Quel sport se joue sur un terrain en herbe avec un ballon ovale ?",["Le rugby","Le basket","La natation"],0,"Il se développe à Mayotte, notamment chez les jeunes.")
q("spo","Quelle activité de plage est très pratiquée le week-end ?",["La baignade et le snorkeling","Le ski","Le hockey sur glace"],0,"Masque et tuba pour observer les poissons du lagon.")

# ─────────── DIVERTISSEMENTS (9) ───────────
q("div","Quel est le plat typique de Mayotte à base de feuilles de manioc ?",["Le mataba","La pizza","Le couscous"],0,"Cuit avec du lait de coco, souvent avec du poisson.")
q("div","Quelle monnaie utilise-t-on à Mayotte ?",["L'euro","Le franc comorien","La roupie"],0,"Mayotte est en France : on paie en euros.")
q("div","Quel est l'indicatif téléphonique de Mayotte ?",["+262","+33","+261"],0,"Le +262 couvre La Réunion et Mayotte.")
q("div","Quel fruit est très utilisé dans la cuisine mahoraise ?",["La noix de coco","La pomme","La cerise"],0,"Lait de coco, coco râpée : la base de nombreux plats.")
q("div","Comment dit-on « bonjour » en shimaoré ?",["Kwezi","Hello","Salam"],0,"« Kwezi » est le salut courant.")
q("div","Quelle grande fête religieuse est très suivie à Mayotte ?",["Le Maoulida","Noël uniquement","Halloween"],0,"La commémoration de la naissance du Prophète, avec chants et repas.")
q("div","Quel arbre donne le « fruit à pain » ?",["L'arbre à pain","Le baobab","Le manguier"],0,"Un aliment de base, cuisiné comme un légume.")
q("div","Quelle spécialité sucrée est faite à partir de noix de coco ?",["Le dessert au coco râpé","Le croissant","La crêpe"],0,"Mélangé à du sucre, parfois cuit dans la banane.")
q("div","Quel récit est raconté le soir aux enfants à Mayotte ?",["Des contes traditionnels","Des matchs de foot","Le journal télévisé"],0,"La transmission orale reste très forte.")
