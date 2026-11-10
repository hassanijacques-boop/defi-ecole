# -*- coding: utf-8 -*-
"""Extension du corpus : +26 défis, +130 questions.
Même format que defis.py : [énoncé, [3 choix], index, explication]
"""

D2 = []
def d(id, nv, m, e, c, n, qs):
    D2.append({"id":id,"nv":nv,"m":m,"e":e,"c":c,"n":n,"qs":qs})

# ══════════════ CP ══════════════
d("cp-fr2","cp","Français","📖","#E0533D","Lire des mots et des phrases",[
 ["Quel mot s'écrit correctement ?",["une maison","un maison","une maison."],0,"« maison » est un nom féminin : une maison."],
 ["Dans « Papa lit un livre », qui lit ?",["Papa","le livre","personne"],0,"On demande : qui est-ce qui lit ? C'est Papa, le sujet."],
 ["Quel mot rime avec « chat » ?",["chapeau","bateau","chien"],1,"« chat » et « bateau » finissent par le même son [o]."],
 ["Que veut dire « il » dans « Il pleut » ?",["le ciel","un homme","la pluie"],0,"« il » ne remplace personne ici : c'est une façon de parler du temps."],
 ["Combien de mots dans la phrase « Le chat mange. » ?",["2","3","4"],1,"Le / chat / mange : trois mots."],
])
d("cp-ma2","cp","Maths","🔢","#23618F","Les formes et l'espace",[
 ["Quelle forme a 4 côtés égaux ?",["le carré","le triangle","le cercle"],0,"Le carré a 4 côtés de même longueur et 4 angles droits."],
 ["Combien de côtés a un triangle ?",["2","3","4"],1,"Tri = trois : 3 côtés et 3 sommets."],
 ["Sur une feuille, la souris est devant l'écran. L'écran est…",["derrière la souris","devant la souris","sous la souris"],1,"Devant et derrière dépendent du point de vue."],
 ["Quelle forme n'a aucun côté ?",["le cercle","le carré","le triangle"],0,"Le cercle est une ligne courbe fermée : pas de côté."],
 ["Je monte les escaliers. Je vais…",["en haut","en bas","de côté"],0,"Monter = aller vers le haut."],
])
d("cp-qm2","cp","Questionner le monde","🌱","#31825A","Les animaux et les plantes",[
 ["Quel animal a des plumes ?",["le chat","le pigeon","le poisson"],1,"Plumes et bec : c'est un oiseau."],
 ["Une plante a besoin de…",["d'eau et de lumière","de sucre","de bruit"],0,"Eau, lumière et terre : sans ça, elle jaunit et meurt."],
 ["Le petit de la vache s'appelle…",["le veau","le poussin","le chiot"],0,"Vache → veau ; poule → poussin ; chienne → chiot."],
 ["Quel animal a des poils et allaite ses petits ?",["la tortue","le dauphin","le lézard"],1,"Le dauphin est un mammifère : il allaite, même s'il vit dans l'eau."],
 ["Que devient une graine plantée dans la terre ?",["une plante","une pierre","de l'eau"],0,"Elle germe : une petite tige sort, puis des feuilles."],
])
d("cp-em2","cp","EMC","⚖️","#65489B","Mes émotions",[
 ["Quand je perds un jeu, je peux être…",["triste ou en colère","toujours content","fatigué"],0,"Toutes les émotions sont normales ; c'est ce qu'on en fait qui compte."],
 ["Je suis en colère. Je…",["respire et j'en parle","je tape","je crie sur tout le monde"],0,"Respirer, dire ce qu'on ressent : ça calme sans blesser."],
 ["Un camarade pleure. Je…",["lui demande ce qui ne va pas","ris","l'ignore"],0,"Demander, c'est déjà aider."],
 ["Dire « je n'aime pas ça » c'est…",["permis, si on le dit calmement","interdit","méchant"],0,"On peut refuser une chose sans insulter une personne."],
 ["Quand je n'y arrive pas, je…",["demande de l'aide","abandonne tout","me moque de moi"],0,"Demander de l'aide, c'est une force, pas une faiblesse."],
])

# ══════════════ CE1 ══════════════
d("ce1-fr2","ce1","Français","📖","#E0533D","Le pluriel et le féminin",[
 ["Le pluriel de « un jeu » est…",["des jeux","des jeus","des jeu"],0,"Les mots en -eu font -eux : jeu → jeux."],
 ["Le féminin de « un cousin » est…",["une cousine","une cousin","une cousines"],0,"On ajoute un -e : cousin → cousine."],
 ["Complète : « Les filles … contentes. »",["est","sont","es"],1,"Le sujet est pluriel : elles sont."],
 ["Le pluriel de « un animal » est…",["des animals","des animaux","des animaus"],1,"Les mots en -al font souvent -aux : animal → animaux."],
 ["« Un cheval » et « une jument » : lequel est le mâle ?",["le cheval","la jument","les deux"],0,"Cheval = mâle ; jument = femelle."],
])
d("ce1-ma2","ce1","Maths","🔢","#23618F","Problèmes et monnaie",[
 ["J'achète un pain à 2 € et un fromage à 3 €. Je paie…",["5 €","6 €","4 €"],0,"2 + 3 = 5 €."],
 ["1 euro, c'est combien de centimes ?",["10","100","1000"],1,"1 € = 100 centimes ; 50 c + 50 c = 1 €."],
 ["J'ai 10 € et j'achète un livre à 7 €. Il me reste…",["2 €","3 €","4 €"],1,"10 − 7 = 3 €."],
 ["Un paquet de 6 gâteaux coûte 6 €. Un gâteau coûte…",["0,50 €","1 €","2 €"],1,"6 € pour 6 gâteaux : 6 ÷ 6 = 1 €."],
 ["Le double de 15, c'est…",["25","30","35"],1,"Le double, c'est 2 × 15 = 30."],
])
d("ce1-qm2","ce1","Questionner le monde","🌱","#31825A","Le temps long et l'espace",[
 ["Un siècle, c'est…",["10 ans","100 ans","1000 ans"],1,"1 siècle = 100 ans ; 1 millénaire = 1000 ans."],
 ["Sur un plan de l'école, la cour est…",["un espace extérieur","une salle","un couloir"],0,"Un plan vu du dessus montre les espaces et leur place."],
 ["« Autrefois », c'est…",["avant maintenant","demain","jamais"],0,"Autrefois = il y a longtemps ; aujourd'hui = maintenant."],
 ["L'ordre des saisons est…",["printemps, été, automne, hiver","été, hiver, printemps, automne","automne, hiver, été, printemps"],0,"En France métropolitaine : printemps, été, automne, hiver."],
 ["Pour situer un événement, on utilise…",["une frise chronologique","une balance","un thermomètre"],0,"La frise place les événements dans l'ordre du temps."],
])
d("ce1-an2","ce1","Anglais","🇬🇧","#B93A73","Les nombres et les jours",[
 ["« fifteen », c'est…",["5","15","50"],1,"fifteen = 15 ; fifty = 50."],
 ["« Tuesday », c'est…",["mardi","jeudi","lundi"],0,"Monday lundi, Tuesday mardi, Wednesday mercredi."],
 ["Comment dit-on « dix » ?",["ten","teen","tenth"],0,"ten = 10."],
 ["« I have two brothers » veut dire…",["J'ai deux frères","J'ai deux sœurs","Je suis deux frères"],0,"brothers = frères ; sisters = sœurs."],
 ["« Sunday » est…",["dimanche","samedi","lundi"],0,"Sunday = dimanche."],
])

# ══════════════ CE2 ══════════════
d("ce2-fr2","ce2","Français","📖","#E0533D","Imparfait et futur",[
 ["L'imparfait de « nous chantons » est…",["nous chanterons","nous chantions","nous avons chanté"],1,"Imparfait : -ions, -iez, -aient."],
 ["Le futur de « je finis » est…",["je finirai","je finissais","je finis"],0,"Futur : -rai, -ras, -ra."],
 ["« Quand j'étais petit, je jouais. » Ces verbes sont à…",["l'imparfait","au futur","au présent"],0,"Ils décrivent une action longue dans le passé."],
 ["Complète : « Demain, nous … à la piscine. »",["allons","irons","allions"],1,"« Demain » appelle le futur : nous irons."],
 ["« Il a mangé » est au…",["passé composé","imparfait","futur"],0,"Avoir au présent + participe passé = passé composé."],
])
d("ce2-fr3","ce2","Français","📖","#E0533D","La phrase : sujet, verbe, complément",[
 ["Dans « Le facteur apporte une lettre », le COD est…",["le facteur","une lettre","apporte"],1,"Il apporte quoi ? Une lettre → COD."],
 ["Le complément circonstanciel de lieu de « Nous jouons dans la cour » est…",["nous","jouons","dans la cour"],2,"Il répond à la question « où ? »."],
 ["Une phrase négative est…",["« Je ne veux pas partir. »","« Je veux partir. »","« Veux-tu partir ? »"],0,"« ne … pas » marque la négation."],
 ["Quelle phrase est interrogative ?",["Tu viens.","Tu viens ?","Viens !"],1,"Le point d'interrogation et l'inversion marquent la question."],
 ["Le verbe de « Les oiseaux chantent le matin » est…",["les oiseaux","chantent","le matin"],1,"Le verbe exprime l'action : chantent."],
])
d("ce2-ma2","ce2","Maths","🔢","#23618F","Multiplication et division",[
 ["24 ÷ 6 = ?",["3","4","5"],1,"6 × 4 = 24, donc 24 ÷ 6 = 4."],
 ["8 × 7 = ?",["54","56","58"],1,"8 × 7 = 56."],
 ["Dans 45, combien de fois 9 ?",["4","5","6"],1,"9 × 5 = 45."],
 ["Le double de 35, c'est…",["60","70","75"],1,"2 × 35 = 70."],
 ["35 ÷ 5 = ?",["6","7","8"],1,"5 × 7 = 35."],
])
d("ce2-ma3","ce2","Maths","🔢","#23618F","Les mesures",[
 ["1 kg, c'est…",["100 g","1 000 g","10 000 g"],1,"1 kg = 1 000 g."],
 ["1 km, c'est…",["100 m","1 000 m","10 000 m"],1,"1 km = 1 000 m."],
 ["Une heure, c'est…",["30 minutes","60 minutes","100 minutes"],1,"1 h = 60 min ; 1 min = 60 s."],
 ["1 litre, c'est…",["10 cl","100 cl","1 000 cl"],1,"1 L = 100 cl = 1 000 ml."],
 ["Un match commence à 14 h et dure 45 minutes. Il finit à…",["14 h 30","14 h 45","15 h"],1,"14 h + 45 min = 14 h 45."],
])
d("ce2-sc2","ce2","Sciences","🔬","#2E8B57","La matière",[
 ["Un mélange où l'on ne voit plus le sucre est…",["homogène","hétérogène","solide"],0,"Le sucre se dissout : le mélange est homogène (une seule phase)."],
 ["L'eau qui gèle devient…",["de la vapeur","de la glace","du sel"],1,"À 0 °C, l'eau liquide devient solide : la glace."],
 ["L'air est…",["de la matière","du vide","de l'eau"],0,"L'air est un mélange de gaz : il a une masse et occupe un volume."],
 ["Que se passe-t-il si on chauffe de l'eau à 100 °C ?",["elle bout et s'évapore","elle gèle","elle durcit"],0,"À 100 °C (au niveau de la mer), l'eau bout et devient vapeur."],
 ["Le sable dans l'eau, c'est un mélange…",["hétérogène","homogène","invisible"],0,"On distingue encore le sable et l'eau."],
])
d("ce2-ge2","ce2","Géographie","🗺️","#1F7A6C","Villes et paysages",[
 ["Une ville a…",["beaucoup d'habitants et de bâtiments","seulement des champs","aucune route"],0,"Densité de population, bâtiments, services : c'est ce qui définit la ville."],
 ["Un paysage de bord de mer s'appelle un paysage…",["littoral","montagnard","rural"],0,"Littoral = bord de mer ; montagnard = montagne ; rural = campagne."],
 ["La campagne est un paysage…",["rural","urbain","industriel"],0,"Rural vient de « rural » : les champs, les fermes, les villages."],
 ["Un fleuve se jette dans…",["la mer","une montagne","un désert"],0,"Un fleuve finit sa course dans la mer ; une rivière se jette dans un fleuve."],
 ["Mayotte se trouve près de…",["Madagascar","l'Australie","le Canada"],0,"Mayotte est dans l'archipel des Comores, près de Madagascar."],
])

# ══════════════ CM1 ══════════════
d("cm1-fr2","cm1","Français","📖","#E0533D","Accords et homophones",[
 ["Complète : « Ils … partis tôt. »",["son","sont","s'on"],1,"« sont » = verbe être ; « son » = possessif (son sac)."],
 ["« Les fleurs que j'ai … »",["cueilli","cueillies","cueillis"],1,"Avec avoir, accord avec le COD placé avant : fleurs (fém. plur.) → cueillies."],
 ["Complète : « Il … à Paris. »",["va","vas","vont"],0,"« il » → 3e personne du singulier : il va."],
 ["« Ce » ou « se » ? « Il … lave. »",["ce","se","ses"],1,"« se » accompagne un verbe pronominal : il se lave."],
 ["Complète : « Elles … très contentes. »",["est","sont","es"],1,"Sujet féminin pluriel : elles sont."],
])
d("cm1-fr3","cm1","Français","📖","#E0533D","Le lexique",[
 ["Un synonyme de « maison » est…",["demeure","jardin","toit"],0,"Demeure = maison, en plus soutenu."],
 ["Le contraire de « généreux » est…",["avare","riche","gentil"],0,"Avare = qui ne donne pas."],
 ["« Nuit » et « obscurité » sont…",["synonymes","contraires","homonymes"],0,"Les deux renvoient au manque de lumière."],
 ["La famille du mot « terre » comprend…",["terrain, enterrer, terrestre","mer, marin","ciel, aérien"],0,"Même racine : terr-."],
 ["Un mot qui a plusieurs sens est…",["un polysème","un synonyme","un antonyme"],0,"« Fraise » : le fruit, ou l'outil du dentiste."],
])
d("cm1-ma2","cm1","Maths","🔢","#23618F","Proportionnalité",[
 ["4 cahiers coûtent 8 €. 7 cahiers coûtent…",["12 €","14 €","16 €"],1,"1 cahier = 2 €, donc 7 × 2 = 14 €."],
 ["Si 5 kg coûtent 15 €, 1 kg coûte…",["2 €","3 €","5 €"],1,"15 ÷ 5 = 3 €."],
 ["Un robinet remplit 12 L en 3 minutes. En 5 minutes…",["18 L","20 L","24 L"],1,"4 L par minute × 5 = 20 L."],
 ["Un tableau de proportionnalité sert à…",["trouver une valeur manquante","dessiner","mesurer un angle"],0,"On multiplie ou divise toute la ligne par le même nombre."],
 ["3 stylos pour 6 €, c'est le même prix que…",["1 stylo pour 2 €","1 stylo pour 3 €","2 stylos pour 6 €"],0,"6 ÷ 3 = 2 € le stylo."],
])
d("cm1-ma3","cm1","Maths","🔢","#23618F","Géométrie",[
 ["Deux droites qui ne se croisent jamais sont…",["parallèles","sécantes","perpendiculaires"],0,"Parallèles : même écart, jamais de point commun."],
 ["Un angle droit mesure…",["45°","90°","180°"],1,"L'angle droit vaut 90°, comme le coin d'une feuille."],
 ["Un angle plus petit qu'un angle droit est…",["aigu","obtus","plat"],0,"Aigu < 90° ; obtus > 90°."],
 ["L'axe de symétrie d'un carré : combien y en a-t-il ?",["2","4","1"],1,"Deux médianes et deux diagonales : 4 axes."],
 ["Le périmètre d'un triangle de côtés 3, 4 et 5 cm est…",["12 cm","20 cm","60 cm"],0,"On additionne les côtés : 3 + 4 + 5 = 12 cm."],
])
d("cm1-sc2","cm1","Sciences","🔬","#2E8B57","L'énergie et l'électricité",[
 ["Un circuit électrique a besoin de…",["une pile, des fils et une lampe","de l'eau","du sable"],0,"Générateur, conducteurs, récepteur : le circuit doit être fermé."],
 ["Le plastique est un…",["isolant","conducteur","générateur"],0,"Il ne laisse pas passer le courant : d'où les gaines des fils."],
 ["Une énergie renouvelable est…",["le solaire","le pétrole","le charbon"],0,"Le soleil se renouvelle en permanence ; le pétrole, non."],
 ["Une lampe brille quand le circuit est…",["fermé","ouvert","coupé"],0,"Si le circuit est ouvert, le courant ne passe pas."],
 ["L'énergie se…",["transforme","perd totalement","crée de rien"],0,"Un vélo transforme l'énergie du corps en mouvement."],
])
d("cm1-ge2","cm1","Géographie","🗺️","#1F7A6C","Relief et climats",[
 ["Le point le plus haut de la Terre est…",["l'Everest","le Mont Blanc","le Kilimandjaro"],0,"Everest : 8 849 m, dans l'Himalaya."],
 ["Un climat où les étés sont chauds et secs est…",["méditerranéen","océanique","polaire"],0,"Été sec, hiver doux et humide : le climat méditerranéen."],
 ["La France métropolitaine a un relief…",["varié (plaines, plateaux, montagnes)","uniquement plat","uniquement montagneux"],0,"Plaines au nord, massifs anciens, Alpes et Pyrénées."],
 ["Le climat de Mayotte est…",["tropical","polaire","désertique"],0,"Chaud et humide, avec une saison des pluies."],
 ["Une carte de relief utilise des couleurs pour…",["montrer l'altitude","la population","la langue"],0,"Vert = plaines, marron = montagnes."],
])

# ══════════════ CM2 ══════════════
d("cm2-fr2","cm2","Français","📖","#E0533D","Vocabulaire et styles",[
 ["« Il est fort comme un lion » est…",["une comparaison","une métaphore","une hyperbole"],0,"« comme » introduit la comparaison."],
 ["« Cette nouvelle m'a glacé le sang » est…",["une métaphore","une comparaison","un proverbe"],0,"Pas de « comme » : l'image est directe."],
 ["Un synonyme de « courageux » est…",["vaillant","craintif","paresseux"],0,"Vaillant = brave."],
 ["Le champ lexical de l'école comprend…",["crayon, tableau, élève","mer, vague, sable","route, voiture, pont"],0,"Ils renvoient tous au même thème."],
 ["« Énorme » est plus fort que « grand » : c'est…",["une gradation","un contraire","un homonyme"],0,"Les mots d'un même champ peuvent être classés par intensité."],
])
d("cm2-fr3","cm2","Français","📖","#E0533D","La phrase complexe",[
 ["Une phrase avec deux verbes conjugués est…",["complexe","simple","nominale"],0,"Deux verbes conjugués = au moins deux propositions."],
 ["Dans « Je pense que tu as raison », la subordonnée est…",["que tu as raison","je pense","raison"],0,"Elle complète le verbe penser : subordonnée complétive."],
 ["Dans « Le chat dort et le chien aboie », les deux propositions sont…",["juxtaposées","coordonnées","subordonnées"],1,"« et » est une conjonction de coordination : les deux propositions sont coordonnées."],
 ["Une proposition subordonnée relative commence souvent par…",["qui, que, dont, où","et, ou, mais","car, donc, or"],0,"Ce sont les pronoms relatifs."],
 ["« Quand il pleut, je reste. » La subordonnée exprime…",["le temps","la cause","le but"],0,"« quand » indique le moment."],
])
d("cm2-ma2","cm2","Maths","🔢","#23618F","Problèmes à étapes",[
 ["Un livre coûte 12 €. J'en achète 3 et je paie avec 50 €. On me rend…",["12 €","14 €","16 €"],1,"3 × 12 = 36 ; 50 − 36 = 14 €."],
 ["Un pull à 40 € est soldé à −25 %. Il coûte…",["25 €","30 €","35 €"],1,"25 % de 40 = 10 €, donc 40 − 10 = 30 €."],
 ["Un train part à 8 h 45 et roule 2 h 30. Il arrive à…",["10 h 75","11 h 15","11 h 45"],1,"8 h 45 + 2 h = 10 h 45, + 30 min = 11 h 15."],
 ["3 ouvriers font un mur en 6 jours. 6 ouvriers mettront…",["3 jours","6 jours","12 jours"],0,"Deux fois plus d'ouvriers : deux fois moins de temps."],
 ["J'ai 5 billes, j'en gagne 3, j'en perds 4. J'en ai…",["4","5","6"],0,"5 + 3 = 8 ; 8 − 4 = 4."],
])
d("cm2-ma3","cm2","Maths","🔢","#23618F","Solides et volumes",[
 ["Le volume d'un cube de 3 cm d'arête est…",["9 cm³","27 cm³","6 cm³"],1,"V = côté × côté × côté = 3 × 3 × 3 = 27 cm³."],
 ["Un cube a combien de faces ?",["4","6","8"],1,"6 faces carrées, 12 arêtes, 8 sommets."],
 ["La formule du volume d'un pavé droit est…",["L × l × h","L + l + h","2 × (L + l)"],0,"Longueur × largeur × hauteur."],
 ["1 dm³ correspond à…",["1 litre","10 litres","1 ml"],0,"1 dm³ = 1 L : pratique pour les contenances."],
 ["Une sphère n'a…",["aucune arête","6 arêtes","12 arêtes"],0,"Une surface courbe : ni arête ni sommet."],
])
d("cm2-sc2","cm2","Sciences","🔬","#2E8B57","Le corps humain et la santé",[
 ["Le nombre d'os d'un adulte est d'environ…",["106","206","306"],1,"206 os ; le bébé en a plus, qui fusionnent en grandissant."],
 ["Le sang est pompé par…",["le cœur","les reins","l'estomac"],0,"Le cœur envoie le sang dans tout le corps."],
 ["La respiration sert à…",["apporter de l'oxygène au sang","digérer","transpirer"],0,"Les poumons échangent O₂ et CO₂ avec le sang."],
 ["Une alimentation équilibrée contient…",["des fruits, légumes, protéines et féculents","uniquement des sucres","uniquement des graisses"],0,"La variété est la règle : chaque famille d'aliments a son rôle."],
 ["Se laver les mains limite…",["la transmission des microbes","la croissance","la fatigue"],0,"L'eau et le savon décrochent les microbes."],
])
d("cm2-ge2","cm2","Géographie","🗺️","#1F7A6C","La France dans le monde",[
 ["Combien de départements d'outre-mer compte la France ?",["3","5","10"],1,"Guadeloupe, Martinique, Guyane, La Réunion, Mayotte."],
 ["La France est membre de…",["l'Union européenne","l'OPEP","le Mercosur"],0,"Depuis 1957 (Traité de Rome), elle est un membre fondateur."],
 ["L'outre-mer français représente…",["une part importante de la zone maritime","aucun espace maritime","seulement des îles sans population"],0,"Grâce à l'outre-mer, la France a le 2e domaine maritime mondial."],
 ["La population de la France est d'environ…",["38 millions","68 millions","98 millions"],1,"Environ 68 millions d'habitants."],
 ["Mayotte est devenue département en…",["2011","1995","2020"],0,"Le 31 mars 2011, Mayotte devient le 101e département."],
])
d("cm2-hi2","cm2","Histoire","🏛️","#9B5320","Révolution et XIXe siècle",[
 ["La prise de la Bastille a eu lieu le…",["14 juillet 1789","14 juillet 1790","4 août 1789"],0,"Symbole du début de la Révolution française."],
 ["Napoléon devient empereur en…",["1799","1804","1815"],1,"Sacré empereur le 2 décembre 1804."],
 ["L'abolition définitive de l'esclavage en France date de…",["1789","1848","1905"],1,"1848, sous l'impulsion de Victor Schœlcher."],
 ["La IIIe République commence en…",["1848","1870","1914"],1,"Après la défaite de 1870 et la chute du Second Empire."],
 ["La loi de séparation des Églises et de l'État date de…",["1881","1905","1946"],1,"1905 : c'est le fondement de la laïcité française."],
])
