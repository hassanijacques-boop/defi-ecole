# -*- coding: utf-8 -*-
"""DÉFI ÉCOLE — défis de révision gamifiés, CP → CM2.
Chaque question : [énoncé, [3 choix], index de la bonne réponse, explication]
"""

NIVEAUX = [
 {"id":"cp",  "n":"CP",  "e":"🐣","c":"#F59E0B","d":"J'apprends à lire et à compter"},
 {"id":"ce1", "n":"CE1", "e":"🐥","c":"#22C55E","d":"Je consolide la lecture et le calcul"},
 {"id":"ce2", "n":"CE2", "e":"🦊","c":"#3B82F6","d":"Je lis couramment, j'écris seul"},
 {"id":"cm1", "n":"CM1", "e":"🦅","c":"#8B5CF6","d":"Je comprends, j'explique"},
 {"id":"cm2", "n":"CM2", "e":"🦁","c":"#EF4444","d":"Je maîtrise pour le collège"},
]

D = []
def d(id, nv, m, e, c, n, qs):
    D.append({"id":id,"nv":nv,"m":m,"e":e,"c":c,"n":n,"qs":qs})

# ══════════════ CP ══════════════
d("cp-fr","cp","Français","📖","#E0533D","Les sons et les lettres",[
 ["Quel mot contient le son [ch] ?",["chat","table","lune"],0,"« ch » chante comme dans « chat », « cheval », « niche »."],
 ["Combien de syllabes dans « chocolat » ?",["2","3","4"],1,"cho-co-lat : on frappe trois fois dans ses mains."],
 ["Le son [ou] s'écrit avec quelles lettres ?",["ou","on","oi"],0,"ou : comme dans « loup », « poule », « roue »."],
 ["Dans « le chat », le mot « le » est…",["un article","un nom","un verbe"],0,"« le », « la », « les » sont des articles : ils annoncent le nom."],
 ["Quelle phrase est correctement écrite ?",["Le chat dort.","le chat dort","Le chat dort"],0,"Une phrase commence par une majuscule et finit par un point."],
])
d("cp-ma","cp","Maths","🔢","#23618F","Les nombres jusqu'à 20",[
 ["7 + 5 = ?",["11","12","13"],1,"7 + 5 : on part de 7 et on avance de 5 → 12."],
 ["Quel nombre vient juste après 19 ?",["18","20","21"],1,"Après 19, c'est 20 : deux dizaines."],
 ["2 dizaines, c'est…",["2","12","20"],2,"1 dizaine = 10, donc 2 dizaines = 20."],
 ["15 − 6 = ?",["8","9","10"],1,"De 15 on recule de 6 → 9. On peut vérifier : 9 + 6 = 15."],
 ["Range du plus petit au plus grand : 8, 12, 5",["8, 12, 5","5, 8, 12","12, 8, 5"],1,"On compare : 5 < 8 < 12."],
])
d("cp-qm","cp","Questionner le monde","🌱","#31825A","Le temps qui passe",[
 ["Combien de jours y a-t-il dans une semaine ?",["5","7","10"],1,"Lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche : 7 jours."],
 ["Quel mois vient juste après janvier ?",["février","mars","décembre"],0,"Janvier, février, mars, avril…"],
 ["Combien y a-t-il de saisons ?",["2","3","4"],2,"Printemps, été, automne, hiver : 4 saisons."],
 ["Le matin, au réveil, on prend le…",["petit-déjeuner","déjeuner","dîner"],0,"Petit-déjeuner le matin, déjeuner à midi, dîner le soir."],
 ["Quel jour vient après lundi ?",["mercredi","mardi","dimanche"],1,"Lundi puis mardi, dans l'ordre de la semaine."],
])
d("cp-em","cp","EMC","⚖️","#65489B","Vivre ensemble",[
 ["En classe, pour prendre la parole, je…",["lève la main","crie","me lève sans rien dire"],0,"Lever la main, c'est laisser la parole aux autres aussi."],
 ["Un camarade est seul dans la cour. Je…",["l'invite à jouer","ris de lui","l'ignore"],0,"Inviter quelqu'un, c'est le premier geste contre la solitude."],
 ["Une insulte, c'est…",["interdit","permis","drôle"],0,"Les mots peuvent blesser : insulter, c'est déjà une violence."],
 ["Le respect, c'est…",["écouter l'autre","crier plus fort","se moquer"],0,"Respecter, c'est reconnaître que l'autre compte autant que moi."],
 ["J'ai fait mal à quelqu'un sans le vouloir. Je…",["m'excuse","me cache","ris"],0,"S'excuser répare ; se cacher laisse la blessure ouverte."],
])
d("cp-an","cp","Anglais","🇬🇧","#B93A73","Hello ! Les couleurs",[
 ["« red », c'est…",["rouge","bleu","vert"],0,"red = rouge."],
 ["« blue », c'est…",["jaune","bleu","noir"],1,"blue = bleu, comme le ciel."],
 ["Comment dit-on « bonjour » en anglais ?",["goodbye","hello","please"],1,"hello = bonjour ; goodbye = au revoir."],
 ["« green », c'est…",["vert","rose","gris"],0,"green = vert, comme l'herbe."],
 ["« one, two, … » : comment dit-on trois ?",["four","three","two"],1,"one, two, three, four : 1, 2, 3, 4."],
])

# ══════════════ CE1 ══════════════
d("ce1-fr","ce1","Français","📖","#E0533D","Le verbe et le temps",[
 ["Dans « Le chien aboie », quel est le verbe ?",["le chien","aboie","le"],1,"Le verbe dit ce que fait le sujet : ici, il aboie."],
 ["« Demain, je partirai. » À quel temps est ce verbe ?",["passé","présent","futur"],2,"« Demain » + « partirai » : on parle de ce qui n'est pas encore arrivé."],
 ["Le pluriel de « cheval » est…",["chevals","chevaux","chevaus"],1,"Les mots en -al font souvent -aux : cheval → chevaux."],
 ["Le féminin de « acteur » est…",["acteuse","actrice","acteure"],1,"acteur → actrice, comme directeur → directrice."],
 ["Quelle phrase est au présent ?",["Je mange.","J'ai mangé.","Je mangerai."],0,"« Je mange » : c'est maintenant."],
])
d("ce1-ma","ce1","Maths","🔢","#23618F","Calcul et mesures",[
 ["45 + 27 = ?",["62","72","82"],1,"5 + 7 = 12 (je pose 2, je retiens 1) ; 4 + 2 + 1 = 7 → 72."],
 ["3 × 4 = ?",["7","12","34"],1,"3 × 4, c'est 3 + 3 + 3 + 3 = 12."],
 ["100 − 36 = ?",["64","74","66"],0,"De 100 on retire 36 : 100 − 30 = 70, puis − 6 = 64."],
 ["La moitié de 48, c'est…",["14","24","28"],1,"La moitié, c'est diviser par 2 : 48 ÷ 2 = 24."],
 ["1 mètre, c'est combien de centimètres ?",["10","100","1000"],1,"1 m = 100 cm ; 1 cm = 10 mm."],
])
d("ce1-qm","ce1","Questionner le monde","🌱","#31825A","Le vivant et la matière",[
 ["Que faut-il à une graine pour germer ?",["de l'eau et de la chaleur","du sucre","du sable"],0,"Eau, chaleur et air : sans eau, la graine reste en sommeil."],
 ["Un animal qui a des plumes est…",["un mammifère","un oiseau","un reptile"],1,"Plumes et bec : c'est un oiseau."],
 ["L'eau qui devient de la glace, c'est…",["la fusion","la solidification","l'évaporation"],1,"Liquide → solide = solidification (il fait froid)."],
 ["Le petit du chien s'appelle…",["le chiot","le chaton","le veau"],0,"Chien → chiot ; chat → chaton ; vache → veau."],
 ["Pourquoi se lave-t-on les mains ?",["pour enlever les microbes","pour avoir chaud","pour briller"],0,"Le savon décroche les microbes et l'eau les emporte."],
])
d("ce1-em","ce1","EMC","⚖️","#65489B","Les règles de la classe",[
 ["À quoi sert le règlement de la classe ?",["à punir","à vivre ensemble","à décorer"],1,"Un règlement protège tout le monde, pas seulement le maître."],
 ["Un camarade se moque d'un autre. Je…",["ne dis rien","le dis à un adulte","ris avec lui"],1,"Le silence laisse faire ; parler à un adulte protège."],
 ["Les droits et les devoirs…",["vont ensemble","sont séparés","n'existent pas à l'école"],0,"Mon droit au calme implique mon devoir de ne pas déranger."],
 ["On est tous différents. C'est…",["un problème","une richesse","une erreur"],1,"La différence n'empêche pas l'égalité de droits."],
 ["Qui peut être harcelé ?",["seulement les petits","n'importe qui","seulement les nouveaux"],1,"N'importe qui : le harcèlement parle de celui qui le fait, pas de celui qui le subit."],
])
d("ce1-an","ce1","Anglais","🇬🇧","#B93A73","Se présenter",[
 ["« My name is… » veut dire…",["Je m'appelle…","J'ai… ans","J'habite…"],0,"My name is = mon nom est."],
 ["« How old are you? » demande…",["ton nom","ton âge","ta couleur"],1,"How old = quel âge."],
 ["« I am eight » veut dire…",["J'ai huit ans","Je suis le huitième","Il est huit heures"],0,"I am + âge = j'ai … ans."],
 ["Comment dit-on « au revoir » ?",["hello","goodbye","thanks"],1,"goodbye = au revoir."],
 ["« Thank you » veut dire…",["s'il te plaît","merci","pardon"],1,"Thank you = merci ; please = s'il te plaît."],
])

# ══════════════ CE2 ══════════════
d("ce2-fr","ce2","Français","📖","#E0533D","Passé composé et accords",[
 ["« J'ai mangé une pomme. » Le verbe est au…",["présent","passé composé","futur"],1,"avoir au présent + participe passé = passé composé."],
 ["Dans « une petite maison », l'adjectif est…",["une","petite","maison"],1,"L'adjectif qualifie le nom : petite dit comment est la maison."],
 ["Complète : « Il … un gâteau. »",["a","à","as"],0,"« a » = le verbe avoir ; « à » est une préposition (aller à Paris)."],
 ["Le sujet de « Les enfants jouent dans la cour » est…",["les enfants","jouent","la cour"],0,"On pose la question : qui est-ce qui joue ? Les enfants."],
 ["L'imparfait de « je chante » est…",["je chanterai","je chantais","j'ai chanté"],1,"Imparfait : la terminaison -ais, -ais, -ait…"],
])
d("ce2-ma","ce2","Maths","🔢","#23618F","Nombres et calculs",[
 ["Dans 3 456, le chiffre 5 est le chiffre des…",["centaines","dizaines","unités"],1,"3 milliers, 4 centaines, 5 dizaines, 6 unités."],
 ["7 × 8 = ?",["54","56","64"],1,"7 × 8 = 56. Astuce : 7 × 8 = 7 × 4 × 2 = 28 × 2."],
 ["Le quart de 20, c'est…",["4","5","10"],1,"Le quart = diviser par 4 : 20 ÷ 4 = 5."],
 ["Le périmètre d'un carré de 3 cm de côté est…",["6 cm","9 cm","12 cm"],2,"Périmètre = 4 × côté = 4 × 3 = 12 cm."],
 ["Quelle fraction représente la moitié ?",["1/4","1/2","2/1"],1,"1/2 : une part sur deux."],
])
d("ce2-sc","ce2","Sciences","🔬","#2E8B57","Le cycle de l'eau",[
 ["L'eau qui s'évapore sous l'effet de la chaleur, c'est…",["la condensation","l'évaporation","la solidification"],1,"Chauffée, l'eau liquide devient vapeur : évaporation."],
 ["La vapeur d'eau qui redevient liquide en altitude, c'est…",["la condensation","la fusion","l'infiltration"],0,"En refroidissant, la vapeur se condense en fines gouttes : les nuages."],
 ["Dans une chaîne alimentaire, la plante est…",["le prédateur","le producteur","le consommateur"],1,"La plante produit sa nourriture grâce à la lumière : c'est le producteur."],
 ["Les trois états de l'eau sont…",["solide, liquide, gazeux","chaud, froid, tiède","clair, trouble, sale"],0,"Glace (solide), eau (liquide), vapeur (gaz)."],
 ["Que devient l'eau de pluie qui s'infiltre dans le sol ?",["une nappe souterraine","du sable","de la fumée"],0,"Elle alimente les nappes phréatiques, qui donnent les sources."],
])
d("ce2-hi","ce2","Histoire","🏛️","#9B5320","La Préhistoire",[
 ["Le premier homme utilisait la pierre pour…",["couper et chasser","écrire","conduire"],0,"La pierre taillée est le premier outil : c'est l'âge de la pierre."],
 ["L'art des grottes s'appelle l'art…",["pariétal","moderne","gothique"],0,"Pariétal vient de paroi : les peintures sur les murs des grottes (Lascaux)."],
 ["La Préhistoire se termine avec l'invention…",["de l'écriture","du feu","de la roue"],0,"L'écriture marque le début de l'Histoire : il y a 5 000 ans environ."],
 ["Les hommes préhistoriques vivaient de…",["la chasse et la cueillette","l'usine","du commerce"],0,"Avant l'agriculture : chasse, pêche, cueillette, puis élevage."],
 ["Quel animal a été domestiqué en premier ?",["le chien","le cheval","le chat"],0,"Le chien accompagne l'humain depuis la Préhistoire."],
])
d("ce2-ge","ce2","Géographie","🗺️","#1F7A6C","Mon pays : la France",[
 ["Combien de régions la France métropolitaine compte-t-elle ?",["10","13","18"],1,"13 régions métropolitaines, plus 5 d'outre-mer."],
 ["Sur un plan, le nord est…",["en haut","en bas","à droite"],0,"Par convention : nord en haut, sud en bas, est à droite, ouest à gauche."],
 ["Mayotte est un département…",["d'outre-mer","de métropole","étranger"],0,"Mayotte est un DROM : département et région d'outre-mer, depuis 2011."],
 ["Le relief, c'est…",["les reliefs de montagnes et de plaines","le climat","la population"],0,"Le relief décrit les formes du terrain : plaines, plateaux, montagnes."],
 ["Quel océan borde Mayotte ?",["l'océan Indien","l'Atlantique","le Pacifique"],0,"Mayotte est dans l'océan Indien, entre Madagascar et l'Afrique."],
])
d("ce2-an","ce2","Anglais","🇬🇧","#B93A73","Les animaux et les nombres",[
 ["« a dog », c'est…",["un chat","un chien","un cheval"],1,"dog = chien ; cat = chat."],
 ["« eleven » correspond à…",["10","11","12"],1,"eleven = 11 ; twelve = 12."],
 ["« I like… » veut dire…",["J'aime…","Je n'aime pas…","Je mange…"],0,"I like = j'aime ; I don't like = je n'aime pas."],
 ["« a horse », c'est…",["un cheval","une souris","un oiseau"],0,"horse = cheval."],
 ["Comment dit-on « vingt » ?",["twelve","twenty","two"],1,"twenty = 20."],
])

# ══════════════ CM1 ══════════════
d("cm1-fr","cm1","Français","📖","#E0533D","Grammaire et conjugaison",[
 ["Dans « Le chat dort sur le canapé », « sur le canapé » est…",["un complément circonstanciel","le sujet","un adjectif"],0,"Il indique où : complément circonstanciel de lieu."],
 ["Le futur de « nous finissons » est…",["nous finirons","nous finissions","nous avons fini"],0,"Futur : -rons, -rez, -ront."],
 ["Complète : « Les élèves … dans la cour. »",["joue","jouent","joues"],1,"Le sujet est pluriel (les élèves) : le verbe s'accorde → jouent."],
 ["Le COD de « Il mange une pomme » est…",["il","une pomme","mange"],1,"Il mange quoi ? Une pomme → COD."],
 ["Un synonyme de « rapide » est…",["lent","vif","lourd"],1,"Vif = qui va vite, comme rapide."],
])
d("cm1-ma","cm1","Maths","🔢","#23618F","Fractions et décimaux",[
 ["3/4, c'est…",["plus grand que 1","plus petit que 1","égal à 1"],1,"3 parts sur 4 : il manque une part pour faire 1."],
 ["2,5 + 1,5 = ?",["3","4","4,5"],1,"2 + 1 = 3 ; 0,5 + 0,5 = 1 → 4."],
 ["Un dixième s'écrit…",["0,1","0,01","1,0"],0,"1/10 = 0,1 ; 1/100 = 0,01."],
 ["Le périmètre d'un rectangle de 5 cm sur 3 cm est…",["8 cm","15 cm","16 cm"],2,"P = 2 × (L + l) = 2 × (5 + 3) = 16 cm."],
 ["456 ÷ 4 = ?",["112","114","124"],1,"4 × 114 = 456. On vérifie toujours par la multiplication."],
])
d("cm1-sc","cm1","Sciences","🔬","#2E8B57","Le corps et la Terre",[
 ["La digestion commence…",["dans la bouche","dans l'estomac","dans l'intestin"],0,"Les dents broient, la salive commence à transformer les aliments."],
 ["Le sang est propulsé par…",["le cœur","les poumons","le foie"],0,"Le cœur est une pompe : il envoie le sang dans tout le corps."],
 ["Un volcan entre en éruption quand…",["le magma remonte","il pleut","la terre tourne"],0,"La pression du magma sous la croûte le fait remonter."],
 ["Un séisme est…",["un tremblement de terre","une inondation","un orage"],0,"Les plaques de la croûte bougent et libèrent une énergie énorme."],
 ["Dans un mélange eau + sable, le sable…",["se dissout","se dépose au fond","disparaît"],1,"Il ne se dissout pas : c'est un mélange hétérogène."],
])
d("cm1-hi","cm1","Histoire","🏛️","#9B5320","Le Moyen Âge",[
 ["Charlemagne a été couronné empereur en…",["800","1000","1492"],0,"Noël 800, par le pape Léon III, à Rome."],
 ["Un château fort sert d'abord à…",["protéger et surveiller","habiter en ville","stocker du blé"],0,"Il contrôle un territoire : défense, résidence du seigneur, refuge."],
 ["Les paysans qui travaillent la terre du seigneur sont…",["des seigneurs","des serfs","des chevaliers"],1,"Ils sont attachés à la terre et doivent des redevances."],
 ["La féodalité repose sur…",["la fidélité entre seigneur et vassal","l'élection","le commerce"],0,"Le vassal sert le seigneur, le seigneur le protège."],
 ["Jeanne d'Arc a combattu pendant…",["la guerre de Cent Ans","les croisades","la Révolution"],0,"Guerre de Cent Ans (1337-1453) contre les Anglais."],
])
d("cm1-ge","cm1","Géographie","🗺️","#1F7A6C","La Terre et les continents",[
 ["Combien y a-t-il de continents ?",["5","6","7"],1,"Afrique, Amérique du Nord, Amérique du Sud, Antarctique, Asie, Europe, Océanie — on compte souvent 6 en regroupant les Amériques."],
 ["L'équateur est…",["un parallèle","un méridien","un océan"],0,"C'est le parallèle à égale distance des deux pôles."],
 ["Les lignes qui vont d'un pôle à l'autre sont…",["les parallèles","les méridiens","les tropiques"],1,"Les méridiens servent à mesurer la longitude."],
 ["Le plus grand océan est…",["l'Atlantique","le Pacifique","l'Indien"],1,"Le Pacifique couvre un tiers de la surface du globe."],
 ["Mayotte se situe dans l'hémisphère…",["nord","sud","ni l'un ni l'autre"],1,"Mayotte est au sud de l'équateur, dans l'océan Indien."],
])
d("cm1-an","cm1","Anglais","🇬🇧","#B93A73","Le présent simple",[
 ["« She … football every day. »",["play","plays","playing"],1,"À la 3e personne du singulier, le verbe prend un -s."],
 ["« I don't like fish » veut dire…",["J'aime le poisson","Je n'aime pas le poisson","Je mange du poisson"],1,"don't = do not : la négation au présent."],
 ["Comment pose-t-on une question avec « you » ?",["Do you like…?","You like…?","Are you like…?"],"0","Au présent simple : Do + sujet + verbe."],
 ["« Monday », c'est…",["lundi","mardi","dimanche"],0,"Monday = lundi."],
 ["« He is twelve » veut dire…",["Il a douze ans","Il est midi","Il est douze"],0,"He is + âge = il a … ans."],
])

# ══════════════ CM2 ══════════════
d("cm2-fr","cm2","Français","📖","#E0533D","Passé simple et accords",[
 ["« Il partit très tôt. » Le verbe est au…",["passé composé","passé simple","imparfait"],1,"Passé simple : action brève et achevée dans un récit écrit."],
 ["Complète : « Les lettres que j'ai … »",["écrit","écrites","écrits"],1,"Avec avoir, le participe s'accorde avec le COD placé avant : les lettres (fém. pluriel) → écrites."],
 ["« Qu'il vienne » est au…",["subjonctif","indicatif","impératif"],0,"« qu'il » + verbe : c'est le subjonctif."],
 ["Dans « Le livre que tu lis est passionnant », la proposition relative est…",["que tu lis","le livre","est passionnant"],0,"Elle complète le nom « livre » : c'est une subordonnée relative."],
 ["« Leur » ou « leurs » ? « Ils ont rangé … cahiers. »",["leur","leurs","leur's"],1,"Plusieurs cahiers → accord au pluriel : leurs."],
])
d("cm2-ma","cm2","Maths","🔢","#23618F","Proportionnalité et aires",[
 ["3 stylos coûtent 6 €. Combien coûtent 5 stylos ?",["8 €","10 €","12 €"],1,"1 stylo = 2 €, donc 5 × 2 = 10 €."],
 ["L'aire d'un rectangle de 6 cm sur 4 cm est…",["10 cm²","20 cm²","24 cm²"],2,"Aire = longueur × largeur = 6 × 4 = 24 cm²."],
 ["25 % de 80, c'est…",["20","25","40"],0,"25 % = le quart : 80 ÷ 4 = 20."],
 ["La moyenne de 10, 12 et 14 est…",["11","12","13"],1,"(10 + 12 + 14) ÷ 3 = 36 ÷ 3 = 12."],
 ["Un robinet remplit 3 seaux en 6 minutes. Combien de seaux en 10 minutes ?",["4","5","6"],1,"1 seau toutes les 2 min → 5 seaux en 10 min."],
])
d("cm2-sc","cm2","Sciences","🔬","#2E8B57","La Terre et l'énergie",[
 ["Dans le système solaire, les planètes tournent autour…",["de la Lune","du Soleil","de la Terre"],1,"Le Soleil est l'étoile centrale : tout le système tourne autour."],
 ["Une énergie renouvelable est une énergie…",["qui se renouvelle vite","qui coûte cher","qui vient du pétrole"],0,"Soleil, vent, eau : elles se renouvellent en permanence."],
 ["L'énergie ne disparaît pas : elle…",["se transforme","s'annule","s'évapore"],0,"Un panneau solaire transforme la lumière en électricité."],
 ["La photosynthèse permet à la plante de…",["fabriquer sa nourriture","respirer la nuit","boire de l'eau"],0,"Lumière + eau + CO₂ → matière organique + oxygène."],
 ["Le tri des déchets sert à…",["recycler la matière","les brûler tous","les enterrer"],0,"Trier permet de réutiliser le verre, le papier, le plastique."],
])
d("cm2-hi","cm2","Histoire","🏛️","#9B5320","Les guerres mondiales",[
 ["La Première Guerre mondiale a lieu de…",["1914 à 1918","1939 à 1945","1870 à 1871"],0,"Quatre ans de guerre de tranchées."],
 ["La Seconde Guerre mondiale se termine en Europe en…",["1943","1945","1948"],1,"8 mai 1945 : capitulation de l'Allemagne."],
 ["La Shoah est…",["le génocide des Juifs","une bataille","un traité"],0,"Six millions de Juifs assassinés par l'Allemagne nazie."],
 ["La Révolution française commence en…",["1789","1848","1917"],0,"Prise de la Bastille : 14 juillet 1789."],
 ["L'Europe s'est construite après 1945 pour…",["éviter une nouvelle guerre","faire la guerre","partager les colonies"],0,"La CECA (1951) puis la CEE (1957) : rapprocher les économies."],
])
d("cm2-em","cm2","EMC","⚖️","#65489B","La République et ses valeurs",[
 ["La devise de la France est…",["Liberté, Égalité, Fraternité","Un pour tous, tous pour un","Dieu et le Roi"],0,"Elle figure sur les bâtiments publics."],
 ["La laïcité, c'est…",["la neutralité de l'État","l'interdiction des religions","une religion d'État"],0,"L'État ne favorise aucune religion et garantit la liberté de croire ou de ne pas croire."],
 ["Le droit de vote des femmes date de…",["1944","1848","1968"],0,"Les femmes votent pour la première fois en 1945."],
 ["Un enfant a droit à…",["l'éducation et la protection","rien de particulier","seulement le jeu"],0,"La Convention internationale des droits de l'enfant (1989)."],
 ["Le harcèlement, c'est…",["une violence répétée","une plaisanterie","un conflit unique"],0,"La répétition et le rapport de force le distinguent d'une dispute."],
])
d("cm2-an","cm2","Anglais","🇬🇧","#B93A73","Décrire et comparer",[
 ["« taller than », c'est…",["le comparatif","le superlatif","le passé"],0,"-er / more … than = comparatif : plus grand que."],
 ["« the biggest » est…",["le comparatif","le superlatif","un adverbe"],1,"the + -est = superlatif : le plus grand."],
 ["« I have lived here for two years » est au…",["present perfect","prétérit","futur"],0,"have + participe passé : present perfect."],
 ["Comment dit-on « hier » ?",["yesterday","tomorrow","today"],0,"yesterday = hier ; tomorrow = demain."],
 ["« What does she look like? » demande…",["son apparence","son âge","son adresse"],0,"look like = à quoi elle ressemble."],
])

BADGES = [
 {"id":"first","n":"Premier pas","e":"🎯","d":"Terminer un premier défi"},
 {"id":"perfect","n":"Sans faute","e":"⭐","d":"Réussir un défi 5/5"},
 {"id":"three","n":"Trois étoiles","e":"🌟","d":"Obtenir 3 étoiles sur un défi"},
 {"id":"streak3","n":"Trois jours","e":"🔥","d":"Jouer 3 jours de suite"},
 {"id":"streak7","n":"Une semaine","e":"🚀","d":"Jouer 7 jours de suite"},
 {"id":"ten","n":"Dix défis","e":"🏅","d":"Terminer 10 défis"},
 {"id":"cp","n":"Maître du CP","e":"🐣","d":"3 étoiles à tous les défis du CP"},
 {"id":"ce1","n":"Maître du CE1","e":"🐥","d":"3 étoiles à tous les défis du CE1"},
 {"id":"ce2","n":"Maître du CE2","e":"🦊","d":"3 étoiles à tous les défis du CE2"},
 {"id":"cm1","n":"Maître du CM1","e":"🦅","d":"3 étoiles à tous les défis du CM1"},
 {"id":"cm2","n":"Maître du CM2","e":"🦁","d":"3 étoiles à tous les défis du CM2"},
 {"id":"lecture","n":"Champion de lecture","e":"📖","d":"3 étoiles à 3 défis de français"},
 {"id":"calcul","n":"As du calcul","e":"🔢","d":"3 étoiles à 3 défis de maths"},
 {"id":"hist","n":"Explorateur du temps","e":"🏛️","d":"3 étoiles à 2 défis d'histoire"},
 {"id":"sci","n":"Petit savant","e":"🔬","d":"3 étoiles à 2 défis de sciences"},
 {"id":"eng","n":"Hello!","e":"🇬🇧","d":"3 étoiles à 2 défis d'anglais"},
 {"id":"xp500","n":"500 points","e":"💎","d":"Atteindre 500 XP"},
 {"id":"xp1500","n":"1 500 points","e":"👑","d":"Atteindre 1 500 XP"},
]
