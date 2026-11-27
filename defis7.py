# -*- coding: utf-8 -*-
"""DÉFI ÉCOLE — 16 défis CE2 + 16 CM1 + 16 CM2."""

D7 = []
def d(id, nv, m, e, c, n, qs):
    D7.append({"id":id,"nv":nv,"m":m,"e":e,"c":c,"n":n,"qs":qs})

# ═══════════ CE2 ═══════════
d("ce2-fr6","ce2","Français","⏭️","#E0533D","Le futur simple",[
 ["Quel est le futur de « je chante » ?",["je chanterai","je chante","je chantais"],0,"Infinitif + ai."],
 ["Quel est le futur de « nous finissons » ?",["nous finirons","nous finissons","nous finissions"],0,"Finir + ons."],
 ["Quel est le futur de « il vient » ?",["il viendra","il vient","il venait"],0,"Venir → viendra."],
 ["Quel est le futur de « tu as » ?",["tu auras","tu as","tu avais"],0,"Avoir → auras."],
 ["Quel mot indique le futur ?",["demain","hier","autrefois"],0,"Demain."],
])
d("ce2-fr7","ce2","Français","🤝","#E0533D","L'accord sujet-verbe",[
 ["« Les enfants ___ dans la cour » : quel verbe ?",["jouent","joue","jouer"],0,"Sujet pluriel → ent."],
 ["« Marie ___ à l'école » : quel verbe ?",["va","vont","aller"],0,"Sujet singulier → va."],
 ["« Nous ___ contents » : quel verbe ?",["sommes","est","sont"],0,"Nous → sommes."],
 ["« Le chat et le chien ___ » : quel verbe ?",["dorment","dort","dormir"],0,"Deux sujets → pluriel."],
 ["Quel est le sujet dans « Les oiseaux chantent » ?",["Les oiseaux","chantent","le"],0,"Qui est-ce qui chante ?"],
])
d("ce2-ma6","ce2","Maths","➗","#23618F","La division posée",[
 ["Combien font 84 ÷ 4 ?",["21","22","20"],0,"4 × 21 = 84."],
 ["Combien font 96 ÷ 8 ?",["12","11","13"],0,"8 × 12 = 96."],
 ["Combien font 75 ÷ 5 ?",["15","14","16"],0,"5 × 15 = 75."],
 ["Dans 87 ÷ 4, quel est le reste ?",["3","2","1"],0,"4 × 21 = 84, reste 3."],
 ["Combien font 100 ÷ 4 ?",["25","20","30"],0,"4 × 25 = 100."],
])
d("ce2-ma7","ce2","Maths","🍰","#23618F","Les fractions simples",[
 ["Que représente 1/2 d'un gâteau ?",["La moitié","Le quart","Le tout"],0,"Une part sur deux."],
 ["Que représente 1/4 ?",["Le quart","La moitié","Le tiers"],0,"Un quart."],
 ["Combien font 1/2 de 20 ?",["10","5","15"],0,"20 ÷ 2."],
 ["Combien font 1/4 de 40 ?",["10","20","5"],0,"40 ÷ 4."],
 ["Que vaut 2/4 ?",["1/2","1/4","1"],0,"2/4 = 1/2."],
])
d("ce2-ma8","ce2","Maths","🔲","#23618F","Le périmètre",[
 ["Quel est le périmètre d'un carré de 5 cm de côté ?",["20 cm","10 cm","25 cm"],0,"4 × 5 = 20."],
 ["Quel est le périmètre d'un rectangle 4 × 6 ?",["20 cm","24 cm","10 cm"],0,"(4+6) × 2 = 20."],
 ["Qu'est-ce que le périmètre ?",["Le tour d'une figure","La surface","La hauteur"],0,"La longueur du contour."],
 ["Périmètre d'un triangle 3, 4, 5 cm ?",["12 cm","60 cm","15 cm"],0,"3+4+5 = 12."],
 ["Quelle unité pour un périmètre ?",["Le centimètre","Le centimètre carré","Le litre"],0,"Une longueur."],
])
d("ce2-ma9","ce2","Maths","🔢","#23618F","Les nombres décimaux",[
 ["Combien font 2,5 + 2,5 ?",["5","4,5","5,5"],0,"2,5 + 2,5 = 5."],
 ["Quel nombre est plus grand : 3,5 ou 3,45 ?",["3,5","3,45","égaux"],0,"3,50 > 3,45."],
 ["Combien font 1,2 + 0,8 ?",["2","1,10","2,2"],0,"1,2 + 0,8 = 2."],
 ["Que représente le 5 dans 4,5 ?",["Cinq dixièmes","Cinq unités","Cinquante"],0,"5/10."],
 ["Combien font 10 − 1,5 ?",["8,5","8","9,5"],0,"10 − 1,5 = 8,5."],
])
d("ce2-sc5","ce2","Sciences","🪐","#22A06B","Le système solaire",[
 ["Combien de planètes dans le système solaire ?",["8","9","7"],0,"Pluton n'en est plus une."],
 ["Quelle planète est la plus proche du Soleil ?",["Mercure","Vénus","La Terre"],0,"Mercure."],
 ["Quelle est notre planète ?",["La Terre","Mars","Vénus"],0,"La Terre."],
 ["Quel astre est au centre du système ?",["Le Soleil","La Terre","La Lune"],0,"Le Soleil, une étoile."],
 ["Quelle planète a des anneaux visibles ?",["Saturne","Mars","Vénus"],0,"Saturne."],
])
d("ce2-sc6","ce2","Sciences","💧","#22A06B","Les changements d'état",[
 ["Comment appelle-t-on le passage de solide à liquide ?",["La fusion","La solidification","L'évaporation"],0,"La glace fond."],
 ["Comment appelle-t-on le passage de liquide à gaz ?",["L'évaporation","La fusion","La condensation"],0,"L'eau bout ou s'évapore."],
 ["Comment appelle-t-on le passage de gaz à liquide ?",["La condensation","La fusion","L'évaporation"],0,"La buée."],
 ["Que devient l'eau à 0 °C ?",["De la glace","De la vapeur","Du sel"],0,"Solidification."],
 ["Que devient l'eau à 100 °C ?",["De la vapeur","De la glace","Du sable"],0,"Ébullition."],
])
d("ce2-ge5","ce2","Géographie","🗺️","#0891B2","Les régions françaises",[
 ["Combien de régions compte la France métropolitaine ?",["13","22","8"],0,"Depuis 2016."],
 ["Dans quelle région est Mayotte ?",["Mayotte est une région d'outre-mer","Provence","Bretagne"],0,"Un DROM."],
 ["Quelle région est au sud-ouest ?",["La Nouvelle-Aquitaine","La Bretagne","L'Alsace"],0,"Bordeaux."],
 ["Quelle région est une île ?",["La Corse","La Normandie","Le Jura"],0,"La Corse."],
 ["Quel océan borde la Bretagne ?",["L'Atlantique","Le Pacifique","L'Indien"],0,"L'Atlantique."],
])
d("ce2-hi4","ce2","Histoire","🏰","#B45309","La vie au Moyen Âge",[
 ["Où vivaient la plupart des gens au Moyen Âge ?",["À la campagne","En ville","Dans des châteaux"],0,"Paysans."],
 ["Qui cultivait la terre ?",["Les paysans","Les rois","Les chevaliers"],0,"Les serfs et paysans libres."],
 ["Quel bâtiment dominait le village ?",["L'église","L'usine","La gare"],0,"Le clocher."],
 ["Qu'est-ce qu'une foire au Moyen Âge ?",["Un grand marché","Une fête religieuse","Un tournoi"],0,"On y échange des marchandises."],
 ["Quel métier travaillait le fer ?",["Le forgeron","Le meunier","Le boulanger"],0,"Le forgeron."],
])
d("ce2-dm3","ce2","Découverte du monde","⛵","#0891B2","Les grandes découvertes",[
 ["Qui a atteint l'Amérique en 1492 ?",["Christophe Colomb","Magellan","Marco Polo"],0,"Il cherchait les Indes."],
 ["Qui a fait le premier tour du monde ?",["Magellan et son équipage","Colomb","Vasco de Gama"],0,"1519-1522."],
 ["Quel océan Colomb a-t-il traversé ?",["L'Atlantique","Le Pacifique","L'Indien"],0,"L'Atlantique."],
 ["Qu'est-ce qu'une caravelle ?",["Un navire","Une épice","Une boussole"],0,"Un bateau rapide."],
 ["Quel instrument aide à s'orienter en mer ?",["La boussole","Le sablier","La carte seule"],0,"La boussole."],
])
d("ce2-ma10","ce2","Maths","📏","#23618F","Les unités de mesure",[
 ["Combien de grammes dans un kilogramme ?",["1 000","100","10"],0,"1 kg = 1 000 g."],
 ["Combien de centilitres dans un litre ?",["100","10","1 000"],0,"1 L = 100 cl."],
 ["Quelle unité pour la masse ?",["Le gramme","Le litre","Le mètre"],0,"La masse se mesure en grammes."],
 ["Combien de mètres dans 3 km ?",["3 000","300","30"],0,"1 km = 1 000 m."],
 ["Quelle unité pour le volume d'eau ?",["Le litre","Le gramme","Le mètre"],0,"Le litre."],
])
d("ce2-fr8","ce2","Français","📕","#E0533D","Le dictionnaire",[
 ["Dans quel ordre sont les mots du dictionnaire ?",["Alphabétique","Par taille","Par thème"],0,"De A à Z."],
 ["Quel mot vient avant « chat » ?",["château","chien","cheval"],0,"châ… avant che…"],
 ["Que trouve-t-on dans un article de dictionnaire ?",["Le sens du mot","Une histoire","Une image seulement"],0,"Définition, classe, exemple."],
 ["Que signifie « nm » dans un dictionnaire ?",["Nom masculin","Nom commun","Nouveau mot"],0,"Nom masculin."],
 ["Quel mot vient après « pomme » ?",["pommeau","pomme de terre","pommade"],0,"pommade avant pommeau."],
])
d("ce2-em2","ce2","EMC","🗳️","#8B5CF6","Voter et décider ensemble",[
 ["Que fait-on lors d'un vote ?",["On choisit une option","On crie","On tire au sort"],0,"Chacun donne son avis."],
 ["Que signifie « majorité » ?",["Plus de la moitié","Moins de la moitié","Tout le monde"],0,"Le plus grand nombre."],
 ["Comment choisit-on les délégués de classe ?",["Par un vote","Par tirage au sort","Par le maître"],0,"Élection."],
 ["Un vote à bulletin secret garantit…",["La liberté de choix","La rapidité","Rien"],0,"Personne ne voit le bulletin."],
 ["Que fait un délégué ?",["Il représente la classe","Il donne les devoirs","Il punit"],0,"Il porte la parole."],
])
d("ce2-an3","ce2","Anglais","📅","#2563EB","Les jours et les mois",[
 ["Comment dit-on « lundi » ?",["Monday","Sunday","Tuesday"],0,"Monday."],
 ["Comment dit-on « janvier » ?",["January","June","July"],0,"January."],
 ["Comment dit-on « dimanche » ?",["Sunday","Saturday","Monday"],0,"Sunday."],
 ["Comment dit-on « aujourd'hui » ?",["today","tomorrow","yesterday"],0,"Today."],
 ["Comment dit-on « demain » ?",["tomorrow","today","yesterday"],0,"Tomorrow."],
])
d("ce2-cu3","ce2","Culture","💡","#BE185D","Les inventions du quotidien",[
 ["Qui a inventé l'ampoule électrique ?",["Edison","Bell","Watt"],0,"En 1879."],
 ["Qui a inventé le téléphone ?",["Bell","Edison","Marconi"],0,"En 1876."],
 ["Quelle invention permet de conserver les aliments au froid ?",["Le réfrigérateur","Le four","Le grille-pain"],0,"Le frigo."],
 ["Quelle invention permet de laver le linge ?",["La machine à laver","Le lave-vaisselle","L'aspirateur"],0,"La machine à laver."],
 ["Qui a inventé la télévision ?",["Plusieurs chercheurs, dont Baird","Edison seul","Bell"],0,"Dans les années 1920."],
])
d("ce2-ma11","ce2","Maths","🔎","#23618F","Calculer vite",[
 ["Combien font 25 + 25 ?",["50","45","55"],0,"50."],
 ["Combien font 100 − 25 ?",["75","85","65"],0,"75."],
 ["Combien font 30 × 3 ?",["90","60","93"],0,"90."],
 ["Combien font 60 ÷ 3 ?",["20","30","15"],0,"20."],
 ["Combien font 15 + 15 + 15 ?",["45","30","50"],0,"45."],
])
d("ce2-qm3","ce2","Questionner le monde","🌾","#22A06B","Les saisons et les cultures",[
 ["Quelle saison est la plus chaude ?",["L'été","L'hiver","L'automne"],0,"L'été."],
 ["Quand sème-t-on les graines ?",["Au printemps","En hiver","En automne"],0,"Au printemps."],
 ["Quand récolte-t-on le blé ?",["En été","En hiver","Au printemps"],0,"En été."],
 ["Que font les arbres en automne ?",["Ils perdent leurs feuilles","Ils fleurissent","Ils grandissent vite"],0,"Feuilles qui tombent."],
 ["Que faut-il pour semer ?",["De la terre et de l'eau","Du sable sec","Du vent"],0,"Un sol et de l'humidité."],
])
d("ce2-hi5","ce2","Histoire","👑","#B45309","Les rois de France",[
 ["Quel roi a fait construire Versailles ?",["Louis XIV","Louis IX","François Ier"],0,"Le Roi-Soleil."],
 ["Quel roi a été sacré à Reims en 496 ?",["Clovis","Charlemagne","Hugues Capet"],0,"Clovis."],
 ["Quel empereur a régné vers 800 ?",["Charlemagne","Napoléon","Clovis"],0,"Couronné en 800."],
 ["Quel roi a été guillotiné en 1793 ?",["Louis XVI","Louis XIV","Charles X"],0,"Louis XVI."],
 ["Quelle dynastie a régné de 987 à 1328 ?",["Les Capétiens","Les Mérovingiens","Les Bourbons"],0,"Hugues Capet."],
])
d("ce2-ma12","ce2","Maths","🧮","#23618F","Les problèmes à deux étapes",[
 ["Un livre coûte 8 €, un cahier 3 €. Total pour 2 livres ?",["16 €","11 €","22 €"],0,"8 × 2 = 16."],
 ["J'ai 20 €, j'achète 3 stylos à 2 €. Combien reste ?",["14 €","6 €","17 €"],0,"20 − 6 = 14."],
 ["12 œufs, 4 cassent. Le reste divisé en 2 ?",["4","6","8"],0,"12 − 4 = 8, ÷ 2 = 4."],
 ["3 boîtes de 6 crayons. Combien de crayons ?",["18","9","12"],0,"3 × 6 = 18."],
 ["25 élèves, 5 par table. Combien de tables ?",["5","6","4"],0,"25 ÷ 5 = 5."],
])
d("ce2-ge6","ce2","Géographie","🌦️","#0891B2","Le climat",[
 ["Quel climat a des hivers froids et des étés chauds ?",["Le climat continental","Le climat tropical","Le climat polaire"],0,"À l'est de la France."],
 ["Quel climat est chaud et humide toute l'année ?",["Le climat tropical","Le climat montagnard","Le climat océanique"],0,"Comme à Mayotte."],
 ["Quel climat a des pluies fréquentes toute l'année ?",["Le climat océanique","Le climat désertique","Le climat polaire"],0,"Près de l'Atlantique."],
 ["Quel climat trouve-t-on en montagne ?",["Le climat montagnard","Le climat océanique","Le climat tropical"],0,"Froid en altitude."],
 ["Quelle saison est la plus pluvieuse à Mayotte ?",["La saison des pluies (décembre-mars)","L'hiver","L'été"],0,"Mousson."],
])

# ═══════════ CM1 ═══════════
d("cm1-fr5","cm1","Français","⏳","#E0533D","Le plus-que-parfait",[
 ["Le plus-que-parfait exprime…",["Une action avant une autre au passé","Le futur","Le présent"],0,"« J'avais mangé avant qu'il arrive. »"],
 ["Quel est le plus-que-parfait de « je mange » ?",["j'avais mangé","je mangeais","j'ai mangé"],0,"Avoir à l'imparfait + participe."],
 ["Quel auxiliaire utilise « partir » ?",["Être","Avoir","Faire"],0,"J'étais parti."],
 ["Quel est le plus-que-parfait de « nous finissons » ?",["nous avions fini","nous finissions","nous avons fini"],0,"Avions + fini."],
 ["Quand utilise-t-on ce temps ?",["Pour une action antérieure","Pour le présent","Pour le futur"],0,"Le passé du passé."],
])
d("cm1-fr6","cm1","Français","🎈","#E0533D","Le conditionnel",[
 ["Le conditionnel exprime…",["Une action possible ou imaginaire","Une certitude","Un ordre"],0,"« Je viendrais si… »"],
 ["Quel est le conditionnel de « je chante » ?",["je chanterais","je chanterai","je chantais"],0,"Chanter + ais."],
 ["Quel est le conditionnel de « il est » ?",["il serait","il sera","il était"],0,"Être → serait."],
 ["Quel mot introduit souvent le conditionnel ?",["Si","Quand","Puisque"],0,"Si + imparfait."],
 ["« Je voudrais un pain » : quel temps ?",["Le conditionnel","Le futur","L'imparfait"],0,"Politesse."],
])
d("cm1-fr7","cm1","Français","🔁","#E0533D","Les pronoms",[
 ["Par quoi remplacer « le chat » dans « Le chat dort » ?",["Il","Elle","Ils"],0,"Il dort."],
 ["Par quoi remplacer « les filles » ?",["Elles","Ils","Elle"],0,"Elles."],
 ["Quel est le pronom de la 1re personne du pluriel ?",["Nous","Vous","Ils"],0,"Nous."],
 ["Que remplace « le » dans « Je le vois » ?",["Un nom masculin","Une fille","Un pluriel"],0,"Le COD."],
 ["Que remplace « y » ?",["Un lieu","Une personne","Un temps"],0,"« J'y vais » = à cet endroit."],
])
d("cm1-ma6","cm1","Maths","🔢","#23618F","Opérations sur les décimaux",[
 ["Combien font 3,5 + 4,2 ?",["7,7","7,5","8,7"],0,"3,5 + 4,2 = 7,7."],
 ["Combien font 8,4 − 2,1 ?",["6,3","6,1","5,3"],0,"8,4 − 2,1 = 6,3."],
 ["Combien font 2,5 × 2 ?",["5","4,5","6"],0,"5."],
 ["Combien font 6,6 ÷ 2 ?",["3,3","3,2","2,3"],0,"3,3."],
 ["Combien font 1,25 + 0,75 ?",["2","1,100","2,5"],0,"1,25 + 0,75 = 2."],
])
d("cm1-ma7","cm1","Maths","✖️","#23618F","Multiplier par 10, 100, 1000",[
 ["Combien font 45 × 10 ?",["450","4 500","45"],0,"On ajoute un zéro."],
 ["Combien font 3,5 × 100 ?",["350","35","3 500"],0,"La virgule se décale."],
 ["Combien font 12,4 × 10 ?",["124","1,24","1 240"],0,"124."],
 ["Combien font 7 × 1 000 ?",["7 000","700","70 000"],0,"Trois zéros."],
 ["Combien font 80 × 100 ?",["8 000","800","80 000"],0,"8 000."],
])
d("cm1-ma8","cm1","Maths","🔺","#23618F","Les polygones",[
 ["Combien de côtés a un pentagone ?",["5","6","4"],0,"Penta = cinq."],
 ["Combien de côtés a un hexagone ?",["6","5","8"],0,"Hexa = six."],
 ["Qu'est-ce qu'un polygone ?",["Une figure à plusieurs côtés","Un cercle","Une sphère"],0,"Poly = plusieurs."],
 ["Combien de côtés a un octogone ?",["8","6","10"],0,"Octo = huit."],
 ["Quel polygone a tous ses côtés égaux ?",["Le polygone régulier","Le rectangle","Le trapèze"],0,"Régulier."],
])
d("cm1-ma9","cm1","Maths","🪞","#23618F","La symétrie",[
 ["Qu'est-ce qu'un axe de symétrie ?",["Une ligne qui partage en deux moitiés identiques","Un angle","Un côté"],0,"Comme un miroir."],
 ["Combien d'axes de symétrie a un carré ?",["4","2","1"],0,"4 axes."],
 ["Combien d'axes de symétrie a un cercle ?",["Une infinité","1","4"],0,"Tous les diamètres."],
 ["Combien d'axes de symétrie a un triangle équilatéral ?",["3","1","2"],0,"3 axes."],
 ["La lettre A a-t-elle un axe de symétrie vertical ?",["Oui","Non","Parfois"],0,"Oui."],
])
d("cm1-sc5","cm1","Sciences","❤️","#22A06B","La circulation du sang",[
 ["Quel organe pompe le sang ?",["Le cœur","Les poumons","Le foie"],0,"Le cœur."],
 ["Que transporte le sang ?",["L'oxygène et les nutriments","Seulement de l'eau","De l'air"],0,"Et il emporte les déchets."],
 ["Combien de cavités a le cœur ?",["4","2","6"],0,"Deux oreillettes, deux ventricules."],
 ["Quels vaisseaux ramènent le sang au cœur ?",["Les veines","Les artères","Les nerfs"],0,"Les veines."],
 ["Quels vaisseaux partent du cœur ?",["Les artères","Les veines","Les capillaires seuls"],0,"Les artères."],
])
d("cm1-sc6","cm1","Sciences","🦊","#22A06B","Les chaînes alimentaires",[
 ["Que mange un herbivore ?",["Des plantes","De la viande","Des insectes"],0,"Herbe, feuilles."],
 ["Que mange un carnivore ?",["De la viande","Des plantes","Des fruits"],0,"D'autres animaux."],
 ["Qui est au début d'une chaîne alimentaire ?",["Les plantes","Les prédateurs","Les décomposeurs"],0,"Les producteurs."],
 ["Que se passe-t-il si on supprime un maillon ?",["Toute la chaîne est perturbée","Rien","Les plantes poussent mieux"],0,"Équilibre rompu."],
 ["Quel animal est omnivore ?",["Le sanglier","Le lapin","Le lion"],0,"Il mange de tout."],
])
d("cm1-hi4","cm1","Histoire","⚔️","#B45309","La Révolution française",[
 ["En quelle année commence la Révolution ?",["1789","1799","1815"],0,"États généraux."],
 ["Quel événement a lieu le 14 juillet 1789 ?",["La prise de la Bastille","Le sacre de Napoléon","La mort de Louis XVI"],0,"Bastille."],
 ["Quelle déclaration est adoptée en 1789 ?",["La Déclaration des droits de l'homme","Le Code civil","La Constitution de 1791"],0,"26 août."],
 ["Que devient Louis XVI en 1793 ?",["Il est guillotiné","Il devient empereur","Il s'exile"],0,"21 janvier."],
 ["Qui prend le pouvoir en 1799 ?",["Napoléon Bonaparte","Robespierre","Louis XVIII"],0,"Coup d'État du 18 Brumaire."],
])
d("cm1-ge4","cm1","Géographie","🌊","#0891B2","Les fleuves de France",[
 ["Quel fleuve traverse Paris ?",["La Seine","La Loire","Le Rhône"],0,"La Seine."],
 ["Quel est le plus long fleuve de France ?",["La Loire","La Seine","Le Rhône"],0,"1 020 km."],
 ["Quel fleuve se jette dans la Méditerranée ?",["Le Rhône","La Seine","La Loire"],0,"Le Rhône."],
 ["Quel fleuve va vers l'Atlantique à Bordeaux ?",["La Garonne","Le Rhin","La Meuse"],0,"La Garonne."],
 ["Qu'est-ce qu'un affluent ?",["Un cours d'eau qui se jette dans un autre","Un lac","Une mer"],0,"Il rejoint le fleuve."],
])
d("cm1-ge5","cm1","Géographie","🇪🇺","#0891B2","L'Union européenne",[
 ["Combien de pays compte l'Union européenne ?",["27","28","15"],0,"Depuis le Brexit."],
 ["Où siège le Parlement européen ?",["À Strasbourg","À Paris","À Londres"],0,"Aussi à Bruxelles."],
 ["Quelle monnaie utilise la plupart des pays de l'UE ?",["L'euro","Le dollar","La livre"],0,"L'euro."],
 ["Quel pays n'est pas dans l'UE ?",["La Norvège","L'Espagne","L'Italie"],0,"La Norvège."],
 ["Qu'est-ce que l'espace Schengen ?",["Une zone sans contrôle aux frontières","Un traité militaire","Une monnaie"],0,"Libre circulation."],
])
d("cm1-cu3","cm1","Culture","🌍","#BE185D","La population du monde",[
 ["Combien d'habitants compte la Terre ?",["Environ 8 milliards","1 milliard","500 millions"],0,"8 milliards."],
 ["Quel continent est le plus peuplé ?",["L'Asie","L'Afrique","L'Europe"],0,"L'Asie."],
 ["Quel pays a le plus d'habitants ?",["L'Inde","Les États-Unis","Le Brésil"],0,"Depuis 2023."],
 ["Quelle est la plus grande ville du monde ?",["Tokyo","Paris","Londres"],0,"38 millions dans l'agglomération."],
 ["Quel continent a la population qui croît le plus vite ?",["L'Afrique","L'Europe","L'Océanie"],0,"L'Afrique."],
])
d("cm1-em3","cm1","EMC","🏛️","#8B5CF6","La commune et le maire",[
 ["Qui dirige une commune ?",["Le maire","Le préfet","Le président"],0,"Élu par le conseil municipal."],
 ["Comment est élu le maire ?",["Par le conseil municipal","Par les habitants directement","Par le président"],0,"Les conseillers l'élisent."],
 ["Quel bâtiment abrite la mairie ?",["L'hôtel de ville","La préfecture","L'école"],0,"Hôtel de ville."],
 ["Que fait la commune ?",["Écoles, routes, services","La loi","La justice"],0,"Services de proximité."],
 ["Comment appelle-t-on les habitants d'une commune qui votent ?",["Les électeurs","Les députés","Les sénateurs"],0,"Électeurs inscrits."],
])
d("cm1-an4","cm1","Anglais","👕","#2563EB","Les vêtements en anglais",[
 ["Comment dit-on « un pantalon » ?",["trousers","shirt","shoes"],0,"Trousers."],
 ["Comment dit-on « une chemise » ?",["a shirt","a skirt","a hat"],0,"A shirt."],
 ["Comment dit-on « des chaussures » ?",["shoes","socks","shorts"],0,"Shoes."],
 ["Comment dit-on « un chapeau » ?",["a hat","a coat","a cap"],0,"A hat."],
 ["Comment dit-on « je porte » ?",["I wear","I have","I am"],0,"I wear."],
])
d("cm1-dm3","cm1","Découverte du monde","🌋","#0891B2","Les volcans du monde",[
 ["Quel volcan a détruit Pompéi ?",["Le Vésuve","L'Etna","Le Krakatoa"],0,"En 79."],
 ["Quel volcan domine la Sicile ?",["L'Etna","Le Vésuve","Le Stromboli"],0,"L'Etna."],
 ["Quel volcan a explosé en 1883 en Indonésie ?",["Le Krakatoa","Le Fuji","Le Mauna Loa"],0,"Krakatoa."],
 ["Quel est le plus grand volcan du système solaire ?",["Olympus Mons","L'Etna","Le Vésuve"],0,"Sur Mars."],
 ["Que rejette un volcan ?",["De la lave et des cendres","De l'eau","Du sable"],0,"Lave, gaz, cendres."],
])
d("cm1-ma10","cm1","Maths","📈","#23618F","Les graphiques",[
 ["Que montre un diagramme circulaire ?",["Des proportions","Une durée","Une distance"],0,"Des parts d'un tout."],
 ["Que lit-on sur l'axe vertical ?",["Les valeurs","Les noms","Les dates"],0,"Les valeurs."],
 ["Que lit-on sur l'axe horizontal ?",["Les catégories ou le temps","Les valeurs","Rien"],0,"Les catégories."],
 ["Que représente une courbe qui monte ?",["Une augmentation","Une baisse","Rien"],0,"Elle augmente."],
 ["Que permet un graphique ?",["De comparer visuellement","De calculer","D'écrire"],0,"Comparer."],
])
d("cm1-fr8","cm1","Français","💬","#E0533D","Le dialogue",[
 ["Comment marque-t-on les paroles dans un dialogue ?",["Par des guillemets ou un tiret","Par des parenthèses","Par des points"],0,"Guillemets ou tirets."],
 ["Que fait-on quand un personnage parle ?",["On va à la ligne","On continue","On met un point"],0,"Nouvelle ligne, tiret."],
 ["À quoi sert un dialogue ?",["À faire parler les personnages","À décrire","À résumer"],0,"Il donne vie au récit."],
 ["Quel signe suit une question ?",["Un point d'interrogation","Un point","Une virgule"],0,"?"],
 ["Quel signe suit une exclamation ?",["Un point d'exclamation","Un point","Un tiret"],0,"!"],
])
d("cm1-qm4","cm1","Questionner le monde","🌳","#22A06B","La forêt",[
 ["Qu'est-ce qu'une forêt ?",["Un grand ensemble d'arbres","Un champ","Un jardin"],0,"Un écosystème."],
 ["Que produit un arbre grâce au soleil ?",["De l'oxygène","Du sable","De l'eau"],0,"Photosynthèse."],
 ["Quel animal vit dans la forêt ?",["Le chevreuil","Le dromadaire","Le manchot"],0,"Chevreuil, sanglier, renard."],
 ["Pourquoi faut-il protéger les forêts ?",["Elles produisent de l'oxygène","Elles sont jolies","Elles cachent le soleil"],0,"Poumon de la planète."],
 ["Quel est le plus grand désert chaud du monde ?",["Le Sahara","Le Gobi","Le Kalahari"],0,"Le Sahara."],
])

# ═══════════ CM2 ═══════════
d("cm2-fr6","cm2","Français","🎩","#E0533D","Les registres de langue",[
 ["Quel registre est familier ?",["« Ça caille ! »","« Il fait froid »","« La température est basse »"],0,"Familier."],
 ["Quel registre est soutenu ?",["« Je vous prie de m'excuser »","« Pardon »","« Désolé »"],0,"Soutenu."],
 ["Quel registre est courant ?",["« Il fait froid »","« Ça caille »","« Il gèle à pierre fendre »"],0,"Courant."],
 ["Que fait-on avec le registre familier ?",["On l'utilise entre proches","On l'écrit à l'école","On l'utilise en justice"],0,"Entre amis."],
 ["Pourquoi adapter son registre ?",["Selon la personne à qui on parle","Pour être drôle","Par hasard"],0,"Le contexte."],
])
d("cm2-fr7","cm2","Français","🔄","#E0533D","Voix active et passive",[
 ["« Le chat mange la souris » est à la voix…",["active","passive","neutre"],0,"Le sujet fait l'action."],
 ["« La souris est mangée par le chat » est à la voix…",["passive","active","neutre"],0,"Le sujet subit."],
 ["Comment passe-t-on à la voix passive ?",["Avec être + participe passé","Avec avoir","Sans auxiliaire"],0,"Être + participe."],
 ["Qui fait l'action à la voix passive ?",["Le complément d'agent","Le sujet","Personne"],0,"« par le chat »."],
 ["« La maison a été construite » : quelle voix ?",["Passive","Active","Neutre"],0,"Passive."],
])
d("cm2-ma6","cm2","Maths","📊","#23618F","La moyenne",[
 ["Moyenne de 10, 12 et 14 ?",["12","13","11"],0,"36 ÷ 3 = 12."],
 ["Moyenne de 8 et 12 ?",["10","9","11"],0,"20 ÷ 2 = 10."],
 ["Comment calcule-t-on une moyenne ?",["Somme ÷ nombre de valeurs","Somme × nombre","Le plus grand"],0,"Total divisé."],
 ["Moyenne de 5, 10, 15, 10 ?",["10","9","11"],0,"40 ÷ 4 = 10."],
 ["Moyenne de 20 et 10 ?",["15","12","18"],0,"30 ÷ 2 = 15."],
])
d("cm2-ma7","cm2","Maths","🔗","#23618F","La règle de trois",[
 ["Si 3 kg coûtent 12 €, 1 kg coûte…",["4 €","3 €","6 €"],0,"12 ÷ 3 = 4."],
 ["Si 2 m coûtent 10 €, 5 m coûtent…",["25 €","20 €","15 €"],0,"Le mètre = 5 € ; 5 × 5 = 25."],
 ["Si 4 stylos coûtent 8 €, 7 stylos coûtent…",["14 €","12 €","16 €"],0,"1 stylo = 2 € ; 7 × 2 = 14."],
 ["Si 5 kg coûtent 20 €, 3 kg coûtent…",["12 €","15 €","10 €"],0,"1 kg = 4 € ; 3 × 4 = 12."],
 ["Si 6 livres coûtent 18 €, 2 livres coûtent…",["6 €","9 €","3 €"],0,"1 livre = 3 €."],
])
d("cm2-ma8","cm2","Maths","📐","#23618F","Aires et volumes",[
 ["Aire d'un carré de 4 cm de côté ?",["16 cm²","8 cm²","12 cm²"],0,"4 × 4 = 16."],
 ["Aire d'un rectangle 5 × 3 ?",["15 cm²","8 cm²","16 cm²"],0,"5 × 3 = 15."],
 ["Volume d'un cube de 2 cm ?",["8 cm³","6 cm³","4 cm³"],0,"2 × 2 × 2 = 8."],
 ["Que mesure une aire ?",["Une surface","Une longueur","Un volume"],0,"En cm²."],
 ["Combien de cm² dans 1 m² ?",["10 000","100","1 000"],0,"100 × 100."],
])
d("cm2-sc5","cm2","Sciences","👶","#22A06B","La reproduction humaine",[
 ["Combien de chromosomes a une cellule humaine ?",["46","23","64"],0,"23 paires."],
 ["Où se développe le bébé pendant la grossesse ?",["Dans l'utérus","Dans l'estomac","Dans le cœur"],0,"L'utérus."],
 ["Combien de temps dure une grossesse ?",["Environ 9 mois","3 mois","18 mois"],0,"9 mois."],
 ["De quoi est composé un être humain au départ ?",["D'une cellule-œuf","D'un os","D'un muscle"],0,"La fécondation."],
 ["Que transmet l'ADN ?",["Les caractères héréditaires","La nourriture","L'air"],0,"L'hérédité."],
])
d("cm2-sc6","cm2","Sciences","⚡","#22A06B","Les formes d'énergie",[
 ["Quelle énergie vient du Soleil ?",["L'énergie solaire","L'énergie hydraulique","L'énergie éolienne"],0,"Le solaire."],
 ["Quelle énergie vient du vent ?",["L'éolienne","Le solaire","La géothermie"],0,"L'éolien."],
 ["Quelle énergie est fossile ?",["Le pétrole","Le soleil","Le vent"],0,"Pétrole, charbon, gaz."],
 ["Que fait un panneau solaire ?",["Il transforme la lumière en électricité","Il chauffe l'eau seulement","Il stocke le vent"],0,"Photovoltaïque."],
 ["Quelle énergie est renouvelable ?",["L'hydraulique","Le charbon","Le pétrole"],0,"L'eau des barrages."],
])
d("cm2-hi4","cm2","Histoire","🇪🇺","#B45309","La construction européenne",[
 ["Quand le traité de Rome est-il signé ?",["1957","1945","1992"],0,"La CEE."],
 ["Quel traité crée l'Union européenne ?",["Le traité de Maastricht","Le traité de Rome","Le traité de Versailles"],0,"1992."],
 ["Combien de pays fondateurs ?",["6","12","27"],0,"France, Allemagne, Italie, Benelux."],
 ["Quand l'euro entre-t-il en circulation ?",["2002","1999","2010"],0,"Pièces et billets."],
 ["Pourquoi l'Europe s'est-elle construite ?",["Pour éviter une nouvelle guerre","Pour le tourisme","Pour la monnaie seule"],0,"La paix."],
])
d("cm2-hi5","cm2","Histoire","🌍","#B45309","La décolonisation",[
 ["Qu'est-ce que la décolonisation ?",["L'indépendance des colonies","La colonisation","Une guerre mondiale"],0,"Après 1945."],
 ["Quand l'Inde devient-elle indépendante ?",["1947","1962","1939"],0,"Gandhi."],
 ["Quand l'Algérie devient-elle indépendante ?",["1962","1958","1945"],0,"Accords d'Évian."],
 ["Quel pays a colonisé une grande partie de l'Afrique ?",["La France et le Royaume-Uni","Le Japon","La Russie"],0,"Empires coloniaux."],
 ["Quel principe guide la décolonisation ?",["Le droit des peuples à disposer d'eux-mêmes","Le commerce","La guerre"],0,"L'ONU."],
])
d("cm2-ge4","cm2","Géographie","🏛️","#0891B2","Les institutions françaises",[
 ["Qui est le chef de l'État ?",["Le président de la République","Le Premier ministre","Le maire"],0,"Élu pour 5 ans."],
 ["Qui gouverne et dirige le gouvernement ?",["Le Premier ministre","Le président seul","Le Sénat"],0,"Nommé par le président."],
 ["Où siège l'Assemblée nationale ?",["Au Palais Bourbon","À l'Élysée","Au Sénat"],0,"Paris."],
 ["Qui vote la loi ?",["Le Parlement","Le président seul","Les maires"],0,"Assemblée + Sénat."],
 ["Quel est le rôle du Conseil constitutionnel ?",["Vérifier la conformité des lois","Gouverner","Voter le budget"],0,"Il contrôle."],
])
d("cm2-em3","cm2","EMC","🌱","#8B5CF6","Le développement durable",[
 ["Qu'est-ce que le développement durable ?",["Développer sans épuiser les ressources","Produire plus vite","Consommer plus"],0,"Répondre aux besoins sans compromettre l'avenir."],
 ["Que signifie « recycler » ?",["Transformer les déchets en nouveaux objets","Jeter","Brûler"],0,"Réutilisation."],
 ["Quel geste économise l'eau ?",["Fermer le robinet","Laisser couler","Arroser à midi"],0,"Petits gestes."],
 ["Que sont les énergies renouvelables ?",["Soleil, vent, eau","Pétrole","Charbon"],0,"Inépuisables."],
 ["Pourquoi trier ses déchets ?",["Pour les recycler","Pour les cacher","Pour les brûler"],0,"Recyclage."],
])
d("cm2-cu4","cm2","Culture","🌐","#BE185D","Le monde d'aujourd'hui",[
 ["Que signifie ONU ?",["Organisation des Nations unies","Ordre nouveau universel","Organisation neutre unique"],0,"Créée en 1945."],
 ["Combien de pays membres à l'ONU ?",["193","50","27"],0,"Presque tous."],
 ["Quel est le rôle de l'ONU ?",["Maintenir la paix","Voter les lois françaises","Gérer l'euro"],0,"Paix et coopération."],
 ["Où siège l'ONU ?",["À New York","À Genève seule","À Paris"],0,"New York."],
 ["Que fait l'UNESCO ?",["Protège le patrimoine mondial","Gère les armées","Vote les impôts"],0,"Éducation, culture."],
])
d("cm2-dm4","cm2","Découverte du monde","🧭","#0891B2","Explorer la Terre",[
 ["Qui a atteint le pôle Sud en premier ?",["Amundsen","Scott","Shackleton"],0,"En 1911."],
 ["Qui a exploré l'Afrique centrale au XIXe ?",["Livingstone","Magellan","Colomb"],0,"Livingstone."],
 ["Quel océan est le plus profond ?",["Le Pacifique","L'Atlantique","L'Indien"],0,"Fosse des Mariannes."],
 ["Quel est le plus grand désert froid ?",["L'Antarctique","Le Sahara","Le Gobi"],0,"Désert de glace."],
 ["Qui a marché sur la Lune en 1969 ?",["Armstrong","Gagarine","Aldrin seul"],0,"Apollo 11."],
])
d("cm2-an4","cm2","Anglais","⏪","#2563EB","Le passé en anglais",[
 ["Comment dit-on « j'ai joué » ?",["I played","I play","I playing"],0,"Verbe + ed."],
 ["Quel est le passé de « go » ?",["went","goed","gone"],0,"Irrégulier."],
 ["Quel est le passé de « see » ?",["saw","seed","seen"],0,"Saw."],
 ["Comment dit-on « hier » ?",["yesterday","tomorrow","today"],0,"Yesterday."],
 ["Quel auxiliaire pour le passé composé anglais ?",["have/has","be","do"],0,"Have + participe."],
])
d("cm2-ma9","cm2","Maths","🧮","#23618F","Problèmes de la vie courante",[
 ["Un article de 80 € est soldé à −25 %. Prix ?",["60 €","55 €","65 €"],0,"80 × 0,75 = 60."],
 ["3 kg à 4 €/kg. Combien ?",["12 €","7 €","16 €"],0,"3 × 4 = 12."],
 ["Un trajet de 240 km à 80 km/h dure…",["3 h","2 h","4 h"],0,"240 ÷ 80 = 3."],
 ["J'ai 50 €, j'achète 3 articles à 12 €. Reste ?",["14 €","24 €","16 €"],0,"50 − 36 = 14."],
 ["Une recette pour 4, il faut doubler pour…",["8 personnes","6 personnes","10 personnes"],0,"8."],
])
d("cm2-fr8","cm2","Français","🔗","#E0533D","Les connecteurs logiques",[
 ["Quel connecteur exprime la cause ?",["parce que","donc","mais"],0,"La cause."],
 ["Quel connecteur exprime la conséquence ?",["donc","car","puisque"],0,"La conséquence."],
 ["Quel connecteur exprime l'opposition ?",["mais","et","donc"],0,"Mais."],
 ["Quel connecteur exprime le temps ?",["ensuite","car","mais"],0,"Ensuite."],
 ["À quoi servent les connecteurs ?",["À organiser les idées","À décorer","À compter"],0,"Structure du texte."],
])
d("cm2-sc7","cm2","Sciences","🔬","#22A06B","Le corps et la santé",[
 ["Pourquoi faut-il dormir ?",["Pour récupérer et mémoriser","Pour grandir seulement","Pour rien"],0,"Le sommeil consolide."],
 ["Combien de temps de sommeil pour un enfant ?",["9 à 11 heures","5 heures","14 heures"],0,"9-11h."],
 ["Que faut-il manger chaque jour ?",["Des fruits et légumes","Des bonbons","Que des féculents"],0,"Équilibré."],
 ["Pourquoi bouger chaque jour ?",["Pour la santé du cœur et des muscles","Pour maigrir seulement","Pour rien"],0,"Activité physique."],
 ["Que provoque le tabac ?",["Des maladies graves","Rien","De l'énergie"],0,"Danger."],
])
d("cm2-qm5","cm2","Questionner le monde","🌍","#22A06B","La biodiversité",[
 ["Qu'est-ce que la biodiversité ?",["La variété des êtres vivants","Une forêt","Un animal"],0,"La diversité du vivant."],
 ["Pourquoi la biodiversité diminue-t-elle ?",["À cause des activités humaines","À cause des saisons","Naturellement seulement"],0,"Déforestation, pollution."],
 ["Quel animal a disparu à cause de l'homme ?",["Le dodo","Le chien","Le chat"],0,"Espèce éteinte."],
 ["Que protège un parc naturel ?",["Les espèces et les milieux","Les voitures","Les usines"],0,"Protection."],
 ["Que peut-on faire pour aider ?",["Planter, trier, protéger","Rien","Consommer plus"],0,"Agir."],
])
d("cm2-cu5","cm2","Culture","🎨","#BE185D","Les grands courants artistiques",[
 ["Qu'est-ce que l'impressionnisme ?",["Un courant de peinture de la lumière","Un style de musique","Une architecture"],0,"Monet, Renoir."],
 ["Qui a peint les Nymphéas ?",["Monet","Picasso","Dalí"],0,"Monet."],
 ["Qu'est-ce que le cubisme ?",["Un art qui décompose les formes","Un art antique","Un art japonais"],0,"Picasso, Braque."],
 ["Qui a peint « Guernica » ?",["Picasso","Van Gogh","Monet"],0,"Picasso."],
 ["Quel courant utilise des taches de couleur pure ?",["Le fauvisme","Le classicisme","Le baroque"],0,"Matisse."],
])
d("cm2-em4","cm2","EMC","⚖️","#8B5CF6","La laïcité",[
 ["Que garantit la laïcité ?",["La liberté de conscience","Une religion d'État","L'interdiction des religions"],0,"Neutralité de l'État."],
 ["Quelle loi sépare les Églises et l'État ?",["La loi de 1905","La loi de 1881","La loi de 1789"],0,"1905."],
 ["Que signifie « neutre » pour l'État ?",["Il ne favorise aucune religion","Il n'a pas d'avis","Il interdit tout"],0,"Neutralité."],
 ["Peut-on croire ou ne pas croire en France ?",["Oui, c'est un droit","Non","Seulement croire"],0,"Liberté de conscience."],
 ["Où la laïcité s'applique-t-elle ?",["À l'école publique et à l'État","Aux familles","Aux magasins"],0,"École et services publics."],
])
