# -*- coding: utf-8 -*-
"""DÉFI ÉCOLE — 16 défis CP + 16 défis CE1."""

D6 = []
def d(id, nv, m, e, c, n, qs):
    D6.append({"id":id,"nv":nv,"m":m,"e":e,"c":c,"n":n,"qs":qs})

# ═══════════ CP ═══════════
d("cp-fr5","cp","Français","🅰️","#E0533D","Les voyelles",[
 ["Combien y a-t-il de voyelles en français ?",["6","5","8"],0,"a, e, i, o, u, y."],
 ["Quelle lettre est une voyelle ?",["a","b","t"],0,"a est une voyelle."],
 ["Quel mot commence par une voyelle ?",["avion","table","papa"],0,"Avion commence par a."],
 ["Quelle lettre n'est pas une consonne ?",["o","d","r"],0,"o est une voyelle."],
 ["Combien de voyelles dans « école » ?",["3","2","4"],0,"é, o, e."],
])
d("cp-ma6","cp","Maths","🔟","#23618F","Compter jusqu'à 10",[
 ["Combien font 5 + 5 ?",["10","9","11"],0,"Deux mains de cinq doigts."],
 ["Combien de doigts sur une main ?",["5","10","4"],0,"Cinq."],
 ["Quel nombre vient après 8 ?",["9","7","10"],0,"9."],
 ["Combien font 10 − 3 ?",["7","6","8"],0,"10 − 3 = 7."],
 ["Quel nombre est plus grand que 6 ?",["9","4","2"],0,"9 est plus grand."],
])
d("cp-qm5","cp","Questionner le monde","🐕","#22A06B","Les animaux de la maison",[
 ["Quel animal miaule ?",["Le chat","Le chien","Le cheval"],0,"Le chat miaule."],
 ["Quel animal aboie ?",["Le chien","Le chat","La poule"],0,"Le chien aboie."],
 ["Que mange un lapin ?",["Des carottes et de l'herbe","De la viande","Du poisson"],0,"Un herbivore."],
 ["Où vit un poisson ?",["Dans l'eau","Dans un arbre","Sous terre"],0,"Il respire avec des branchies."],
 ["Quel animal a des plumes ?",["Le canari","Le chat","Le chien"],0,"Les oiseaux ont des plumes."],
])
d("cp-em4","cp","EMC","🛡️","#8B5CF6","La sécurité",[
 ["Que fait-on avant de traverser ?",["On regarde à gauche et à droite","On court","On ferme les yeux"],0,"Et on attend le feu vert."],
 ["Que signifie un feu rouge pour les piétons ?",["On ne traverse pas","On traverse vite","On court"],0,"On attend."],
 ["Que met-on en voiture ?",["La ceinture de sécurité","Un chapeau","Des lunettes de soleil"],0,"Obligatoire."],
 ["Que ne faut-il jamais faire avec un objet pointu ?",["Jouer avec","Le ranger","Le prêter"],0,"On peut se blesser."],
 ["Qui appelle-t-on en cas d'urgence ?",["Les secours (15, 17, 18, 112)","Un ami","La maîtresse"],0,"112, le numéro européen."],
])
d("cp-qm6","cp","Questionner le monde","👕","#22A06B","Le corps et les vêtements",[
 ["Combien de bras a un être humain ?",["2","4","1"],0,"Deux bras."],
 ["Que met-on aux pieds ?",["Des chaussures","Des gants","Un chapeau"],0,"Aux pieds : chaussures ou chaussettes."],
 ["Que met-on sur la tête en hiver ?",["Un bonnet","Des chaussettes","Des lunettes"],0,"Pour avoir chaud."],
 ["Combien de doigts a une main ?",["5","4","6"],0,"Cinq."],
 ["Avec quoi voit-on ?",["Les yeux","Le nez","Les oreilles"],0,"Les yeux."],
])
d("cp-qm7","cp","Questionner le monde","🍎","#22A06B","Les aliments",[
 ["Quel aliment est un fruit ?",["La pomme","La carotte","Le pain"],0,"La pomme pousse sur un arbre."],
 ["Quel aliment est un légume ?",["La carotte","La banane","Le riz"],0,"La carotte pousse sous terre."],
 ["Que faut-il boire chaque jour ?",["De l'eau","Du soda","Du jus sucré"],0,"L'eau, surtout."],
 ["Quel aliment vient du blé ?",["Le pain","Le lait","Le poisson"],0,"Le boulanger fait le pain avec la farine de blé."],
 ["Quel aliment est un produit laitier ?",["Le fromage","La pomme","Le riz"],0,"Du lait transformé."],
])
d("cp-ma7","cp","Maths","📐","#23618F","Les formes autour de nous",[
 ["Quelle forme a un ballon ?",["Une sphère","Un cube","Un triangle"],0,"Ronde comme une boule."],
 ["Quelle forme a un dé ?",["Un cube","Une sphère","Un cercle"],0,"Six faces carrées."],
 ["Combien de côtés a un triangle ?",["3","4","5"],0,"Tri = trois."],
 ["Combien de côtés a un carré ?",["4","3","6"],0,"Quatre côtés égaux."],
 ["Quelle forme a une roue ?",["Un cercle","Un carré","Un triangle"],0,"Un cercle."],
])
d("cp-fr6","cp","Français","📖","#E0533D","Lire une phrase",[
 ["Combien de mots dans « Le chat mange. » ?",["3","4","2"],0,"Le / chat / mange."],
 ["Par quelle lettre commence une phrase ?",["Une majuscule","Une minuscule","Un chiffre"],0,"La majuscule."],
 ["Par quoi finit une phrase ?",["Un point","Une virgule","Rien"],0,"Un point."],
 ["Quel est le mot qui désigne une personne, un animal ou une chose ?",["Un nom","Un verbe","Un adjectif"],0,"Un nom."],
 ["Dans « Le chien court », quel est le verbe ?",["court","chien","le"],0,"L'action : courir."],
])
d("cp-qm8","cp","Questionner le monde","🌍","#22A06B","La Terre et le ciel",[
 ["Sur quoi vivons-nous ?",["La Terre","Le Soleil","La Lune"],0,"Une planète."],
 ["Quel astre nous éclaire le jour ?",["Le Soleil","La Lune","Mars"],0,"Le Soleil."],
 ["Que voit-on dans le ciel la nuit ?",["Des étoiles","Des nuages seulement","Rien"],0,"Étoiles et Lune."],
 ["De quelle couleur est le ciel par beau temps ?",["Bleu","Vert","Rouge"],0,"Bleu."],
 ["Quel temps fait-il quand il pleut ?",["Il y a des nuages","Il fait sec","Il neige"],0,"La pluie tombe des nuages."],
])
d("cp-ar3","cp","Arts","🎵","#D97706","Chanter et écouter",[
 ["Que fait-on avec sa voix en musique ?",["On chante","On dessine","On court"],0,"On chante."],
 ["Quel instrument frappe-t-on avec des baguettes ?",["Le tambour","La flûte","Le piano"],0,"Le tambour."],
 ["Que fait-on pour écouter une chanson ?",["On se tait","On crie","On parle"],0,"On écoute en silence."],
 ["Combien de notes dans la gamme ?",["7","5","10"],0,"do, ré, mi, fa, sol, la, si."],
 ["Que fait-on en rythme ?",["On frappe des mains ensemble","On lit","On écrit"],0,"On suit la pulsation."],
])
d("cp-cu3","cp","Culture","🎄","#BE185D","Les fêtes de l'année",[
 ["Quelle fête célèbre la naissance de Jésus ?",["Noël","Pâques","La Toussaint"],0,"Le 25 décembre."],
 ["Que mange-t-on à la Chandeleur ?",["Des crêpes","De la galette","Des œufs"],0,"La fête des crêpes."],
 ["Quelle fête célèbre la fin du Ramadan ?",["L'Aïd","Noël","Le 14 juillet"],0,"L'Aïd el-Fitr."],
 ["Quelle fête nationale française a lieu le 14 juillet ?",["La fête nationale","Noël","Pâques"],0,"Feux d'artifice et défilé."],
 ["Quand cherche-t-on les œufs en chocolat ?",["À Pâques","À Noël","En été"],0,"À Pâques."],
])
d("cp-qm9","cp","Questionner le monde","💼","#22A06B","Les métiers",[
 ["Qui soigne les malades ?",["Le médecin","Le boulanger","Le facteur"],0,"Le médecin."],
 ["Qui fait le pain ?",["Le boulanger","Le maçon","Le facteur"],0,"Le boulanger."],
 ["Qui apporte le courrier ?",["Le facteur","Le pompier","Le cuisinier"],0,"Le facteur."],
 ["Qui éteint les incendies ?",["Les pompiers","Les policiers","Les médecins"],0,"Les pompiers."],
 ["Qui construit les maisons ?",["Le maçon","Le facteur","Le boulanger"],0,"Le maçon."],
])
d("cp-ma8","cp","Maths","⚖️","#23618F","Grand, petit, lourd, léger",[
 ["Quel animal est le plus lourd ?",["L'éléphant","Le chat","La souris"],0,"L'éléphant."],
 ["Quel objet est le plus léger ?",["Une plume","Un livre","Une chaise"],0,"La plume."],
 ["Quel est le plus grand ?",["Un immeuble","Un vélo","Une fourmi"],0,"L'immeuble."],
 ["Avec quoi pèse-t-on ?",["Une balance","Une règle","Un thermomètre"],0,"La balance."],
 ["Quel contenant contient le plus d'eau ?",["Un seau","Un verre","Une cuillère"],0,"Le seau."],
])
d("cp-fr7","cp","Français","🔊","#E0533D","Entendre les sons",[
 ["Quel mot commence comme « papa » ?",["pomme","table","lune"],0,"papa, pomme : son [p]."],
 ["Quel mot finit comme « chat » ?",["sac","lune","ami"],0,"Le son [a] final."],
 ["Quel mot contient le son [ou] ?",["poule","papa","titi"],0,"[ou] dans poule."],
 ["Quel mot rime avec « roi » ?",["toit","chat","lune"],0,"roi / toit."],
 ["Combien de syllabes dans « banane » ?",["3","2","4"],0,"ba-na-ne."],
])
d("cp-em5","cp","EMC","🏫","#8B5CF6","La classe et l'école",[
 ["Que fait-on quand on a besoin d'aide ?",["On lève la main","On crie","On sort"],0,"On demande la parole."],
 ["Que range-t-on à la fin de la journée ?",["Ses affaires","Rien","Les chaises seulement"],0,"On range son matériel."],
 ["Comment se déplace-t-on dans les couloirs ?",["En marchant","En courant","En criant"],0,"Calmement."],
 ["Que fait-on si on est en retard ?",["On s'excuse et on entre","On reste dehors","On crie"],0,"On s'excuse."],
 ["Que partage-t-on avec ses camarades ?",["Le matériel","Rien","Ses affaires personnelles seulement"],0,"Le matériel de classe."],
])
d("cp-cu4","cp","Culture","🎬","#BE185D","Les dessins animés",[
 ["Quel personnage est une souris de Disney ?",["Mickey","Donald","Goofy"],0,"Mickey Mouse."],
 ["Quel est l'ami de Mickey ?",["Donald","Tintin","Astérix"],0,"Donald le canard."],
 ["Quel dessin animé parle de jouets ?",["Toy Story","Nemo","Cars"],0,"Toy Story."],
 ["Quel poisson cherche son fils dans un dessin animé ?",["Marin","Nemo","Dory"],0,"Nemo."],
 ["Quel chien est un dessin animé ?",["Snoopy","Milou au cinéma","Rex"],0,"Snoopy."],
])

# ═══════════ CE1 ═══════════
d("ce1-fr5","ce1","Français","🌿","#E0533D","Les familles de mots",[
 ["Quel mot est de la même famille que « terre » ?",["terrain","table","mer"],0,"Terrain, territoire, terrestre."],
 ["Quel mot est de la même famille que « lait » ?",["laitier","laine","lien"],0,"Laitier, laiterie."],
 ["Quel mot est de la même famille que « jardin » ?",["jardinier","jaune","jambe"],0,"Jardinier, jardinage."],
 ["Quel mot est de la même famille que « nager » ?",["nageoire","nuage","noix"],0,"Nageoire, nageur."],
 ["Quel mot est de la même famille que « bois » ?",["boisage","boire","bouche"],0,"Boisage, boiserie."],
])
d("ce1-fr6","ce1","Français","↔️","#E0533D","Les contraires",[
 ["Quel est le contraire de « grand » ?",["petit","haut","gros"],0,"Grand / petit."],
 ["Quel est le contraire de « chaud » ?",["froid","tiède","doux"],0,"Chaud / froid."],
 ["Quel est le contraire de « rapide » ?",["lent","vite","fort"],0,"Rapide / lent."],
 ["Quel est le contraire de « ouvrir » ?",["fermer","pousser","tirer"],0,"Ouvrir / fermer."],
 ["Quel est le contraire de « joyeux » ?",["triste","content","gai"],0,"Joyeux / triste."],
])
d("ce1-ma6","ce1","Maths","➕","#23618F","L'addition posée",[
 ["Combien font 25 + 13 ?",["38","35","48"],0,"25 + 13 = 38."],
 ["Combien font 46 + 27 ?",["73","63","83"],0,"46 + 27 = 73 (avec retenue)."],
 ["Combien font 58 + 35 ?",["93","83","103"],0,"58 + 35 = 93."],
 ["Dans 34 + 28, la retenue est…",["1","2","0"],0,"4 + 8 = 12, on retient 1."],
 ["Combien font 100 + 250 ?",["350","305","450"],0,"350."],
])
d("ce1-ma7","ce1","Maths","✖️","#23618F","Les tables de 2 et de 5",[
 ["Combien font 2 × 7 ?",["14","12","16"],0,"Le double de 7."],
 ["Combien font 5 × 6 ?",["30","25","35"],0,"5 × 6 = 30."],
 ["Combien font 5 × 9 ?",["45","40","50"],0,"5 × 9 = 45."],
 ["Combien font 2 × 9 ?",["18","16","20"],0,"Le double de 9."],
 ["Combien font 5 × 8 ?",["40","35","45"],0,"5 × 8 = 40."],
])
d("ce1-ma8","ce1","Maths","🔷","#23618F","Les figures géométriques",[
 ["Combien de côtés a un rectangle ?",["4","3","5"],0,"Quatre, comme le carré."],
 ["Quelle figure a 3 côtés ?",["Le triangle","Le carré","Le cercle"],0,"Triangle."],
 ["Que n'a pas un cercle ?",["De côté","De centre","De rayon"],0,"Le cercle n'a pas de côté droit."],
 ["Quelle figure a tous ses côtés égaux ?",["Le carré","Le rectangle","Le triangle"],0,"Le carré."],
 ["Combien de sommets a un triangle ?",["3","4","2"],0,"Trois sommets, trois angles."],
])
d("ce1-qm4","ce1","Questionner le monde","🦷","#22A06B","Les dents et l'alimentation",[
 ["Combien de dents de lait a un enfant ?",["20","32","16"],0,"20 dents de lait."],
 ["Combien de fois par jour faut-il se brosser les dents ?",["2 fois","1 fois par semaine","Jamais"],0,"Matin et soir."],
 ["Quel aliment abîme les dents ?",["Les bonbons","Les pommes","L'eau"],0,"Le sucre."],
 ["Quel est le rôle des dents ?",["Mâcher les aliments","Parler seul","Respirer"],0,"Elles broient les aliments."],
 ["Que faut-il faire après avoir mangé ?",["Se brosser les dents","Dormir","Courir"],0,"Se brosser les dents."],
])
d("ce1-qm5","ce1","Questionner le monde","🌊","#22A06B","L'eau dans la nature",[
 ["Où trouve-t-on de l'eau douce ?",["Dans les rivières","Dans la mer","Dans le désert"],0,"Rivières, lacs, nappes."],
 ["Que devient l'eau quand elle chauffe ?",["De la vapeur","De la glace","Du sable"],0,"Évaporation."],
 ["Que se passe-t-il quand l'eau gèle ?",["Elle devient solide","Elle disparaît","Elle bout"],0,"La glace."],
 ["D'où vient la pluie ?",["Des nuages","De la mer directement","Du sol"],0,"Les nuages se condensent."],
 ["Pourquoi faut-il économiser l'eau ?",["Elle est rare et précieuse","Elle est sale","Elle coûte cher seulement"],0,"C'est une ressource limitée."],
])
d("ce1-hi2","ce1","Histoire","🏫","#B45309","L'école autrefois",[
 ["L'école était-elle obligatoire il y a 150 ans ?",["Non","Oui","Seulement pour les filles"],0,"Elle le devient en 1882."],
 ["Qui a rendu l'école gratuite et obligatoire ?",["Jules Ferry","Napoléon","Charlemagne"],0,"En 1881-1882."],
 ["Avec quoi écrivait-on autrefois ?",["Une plume et de l'encre","Un stylo à bille","Un ordinateur"],0,"Plume, encre et buvard."],
 ["Les filles et les garçons étaient-ils dans la même classe ?",["Non, souvent séparés","Oui","Cela dépendait"],0,"Séparés jusqu'au XXe siècle."],
 ["Que faisait-on à l'école en plus de lire et écrire ?",["De la morale et du calcul","Du sport seulement","De la musique seulement"],0,"Lecture, écriture, calcul, morale."],
])
d("ce1-em4","ce1","EMC","🇫🇷","#8B5CF6","Les symboles de la France",[
 ["Quelles sont les couleurs du drapeau français ?",["Bleu, blanc, rouge","Bleu, blanc, vert","Rouge, blanc, noir"],0,"Le tricolore."],
 ["Quel est l'hymne national ?",["La Marseillaise","L'Internationale","Le Chant des partisans"],0,"Écrite en 1792."],
 ["Quel personnage symbolise la République ?",["Marianne","Jeanne d'Arc","Napoléon"],0,"Marianne au bonnet phrygien."],
 ["Quelle devise a la France ?",["Liberté, Égalité, Fraternité","Un pour tous","Vive la France"],0,"Depuis 1848."],
 ["Quel jour est la fête nationale ?",["Le 14 juillet","Le 11 novembre","Le 1er mai"],0,"Prise de la Bastille."],
])
d("ce1-an4","ce1","Anglais","🔢","#2563EB","Les nombres en anglais",[
 ["Comment dit-on « trois » ?",["three","tree","free"],0,"Three."],
 ["Comment dit-on « cinq » ?",["five","four","nine"],0,"Five."],
 ["Comment dit-on « dix » ?",["ten","two","teen"],0,"Ten."],
 ["Comment dit-on « sept » ?",["seven","eleven","six"],0,"Seven."],
 ["Comment dit-on « un » ?",["one","on","un"],0,"One."],
])
d("ce1-cu3","ce1","Culture","🌏","#BE185D","Les contes du monde",[
 ["Quel conte vient d'Allemagne ?",["Hansel et Gretel","Le Petit Poucet","Cendrillon"],0,"Des frères Grimm."],
 ["Qui a écrit « Le Petit Poucet » ?",["Charles Perrault","Grimm","Andersen"],0,"En 1697."],
 ["Quel conte a une petite fille aux souliers rouges ?",["Le Magicien d'Oz","Cendrillon","Blanche-Neige"],0,"Dorothy."],
 ["Quel conte parle d'un soldat de plomb ?",["Un conte d'Andersen","Perrault","Grimm"],0,"Andersen."],
 ["Quel conte a un miroir magique ?",["Blanche-Neige","Le Chat botté","Cendrillon"],0,"« Miroir, mon beau miroir »."],
])
d("ce1-ma9","ce1","Maths","🧩","#23618F","Les problèmes simples",[
 ["Léa a 12 bonbons, elle en mange 4. Combien reste-t-il ?",["8","16","9"],0,"12 − 4 = 8."],
 ["Un stylo coûte 2 €. Combien coûtent 3 stylos ?",["6 €","5 €","8 €"],0,"2 × 3 = 6."],
 ["Il y a 15 élèves, 7 partent. Combien restent ?",["8","9","7"],0,"15 − 7 = 8."],
 ["Un paquet a 6 œufs. Combien pour 2 paquets ?",["12","8","10"],0,"6 × 2 = 12."],
 ["Tom a 10 €, il achète un livre à 6 €. Combien reste ?",["4 €","5 €","3 €"],0,"10 − 6 = 4."],
])
d("ce1-qm6","ce1","Questionner le monde","🐝","#22A06B","Les animaux et leur milieu",[
 ["Où vit le poisson ?",["Dans l'eau","Dans l'air","Sous terre"],0,"Milieu aquatique."],
 ["Où vit le lion ?",["Dans la savane","Dans la mer","Dans la forêt polaire"],0,"La savane africaine."],
 ["Où vit le manchot ?",["En Antarctique","Dans le désert","Dans la jungle"],0,"Au froid."],
 ["Où vit le chameau ?",["Dans le désert","Dans l'eau","Dans la forêt"],0,"Il résiste à la sécheresse."],
 ["Où vit le ver de terre ?",["Dans le sol","Dans l'air","Dans l'eau"],0,"Sous la terre."],
])
d("ce1-ar4","ce1","Arts","🖼️","#D97706","Voir et décrire une œuvre",[
 ["Que voit-on d'abord dans un tableau ?",["Le sujet principal","Le cadre","La signature"],0,"Le sujet."],
 ["De quoi parle un portrait ?",["D'une personne","D'un paysage","D'un objet"],0,"Un portrait représente une personne."],
 ["Qu'est-ce qu'un paysage en peinture ?",["Une vue de la nature","Un visage","Un objet"],0,"Campagne, mer, montagne."],
 ["Que sont les couleurs chaudes ?",["Rouge, orange, jaune","Bleu, vert","Noir, blanc"],0,"Elles réchauffent."],
 ["Que sont les couleurs froides ?",["Bleu, vert, violet","Rouge, orange","Jaune, brun"],0,"Elles apaisent."],
])
d("ce1-ma10","ce1","Maths","📊","#23618F","Les doubles et les moitiés",[
 ["Quel est le double de 15 ?",["30","25","35"],0,"15 + 15 = 30."],
 ["Quelle est la moitié de 20 ?",["10","12","5"],0,"20 ÷ 2 = 10."],
 ["Quel est le double de 25 ?",["50","45","55"],0,"25 + 25 = 50."],
 ["Quelle est la moitié de 40 ?",["20","25","10"],0,"40 ÷ 2 = 20."],
 ["Quel est le double de 8 ?",["16","18","14"],0,"8 + 8 = 16."],
])
d("ce1-fr7","ce1","Français","❓","#E0533D","La phrase négative",[
 ["Comment rend-on « Je mange » négatif ?",["Je ne mange pas","Je mange non","Pas je mange"],0,"Ne… pas."],
 ["Quelle phrase est négative ?",["Il ne court pas","Il court","Il court vite"],0,"Ne… pas."],
 ["Quel mot accompagne « ne » ?",["Pas","Plus jamais seul","Rien"],0,"Ne… pas, ne… plus, ne… jamais."],
 ["Comment dit-on « Il vient » au négatif ?",["Il ne vient pas","Il vient pas non","Non il vient"],0,"Ne… pas."],
 ["Où place-t-on « ne » ?",["Avant le verbe","Après le verbe","À la fin"],0,"Ne + verbe + pas."],
])
d("ce1-cu4","ce1","Culture","🏛️","#BE185D","Les monuments célèbres",[
 ["Où se trouve la tour Eiffel ?",["À Paris","À Lyon","À Marseille"],0,"Paris."],
 ["Quel monument est en Égypte ?",["Les pyramides","Le Colisée","La tour de Pise"],0,"Gizeh."],
 ["Où se trouve le Colisée ?",["À Rome","À Athènes","À Paris"],0,"Rome."],
 ["Quel monument est à Londres ?",["Big Ben","La tour Eiffel","Le Parthénon"],0,"Big Ben."],
 ["Quel monument est en Grèce ?",["Le Parthénon","Le Colisée","La Sagrada Família"],0,"Athènes."],
])
