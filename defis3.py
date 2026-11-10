# -*- coding: utf-8 -*-
"""Culture scolaire et générale : arts, découverte du monde, culture générale.
3 nouveaux défis par niveau + 3 badges.
"""

D3 = []
def d(id, nv, m, e, c, n, qs):
    D3.append({"id":id,"nv":nv,"m":m,"e":e,"c":c,"n":n,"qs":qs})

# ══════════════ CP ══════════════
d("cp-ar","cp","Arts","🎨","#E879A6","Couleurs et peintures",[
 ["Quelles sont les trois couleurs primaires ?",["rouge, bleu, jaune","vert, orange, violet","noir, blanc, gris"],0,"En peinture, on obtient les autres couleurs en mélangeant ces trois-là."],
 ["Bleu + jaune donne…",["du vert","du violet","du marron"],0,"Le vert naît du bleu et du jaune."],
 ["Où peut-on voir des tableaux très anciens ?",["dans un musée","à la boulangerie","dans un stade"],0,"Le musée conserve et montre les œuvres."],
 ["Un tableau, c'est…",["une peinture sur une surface","une chanson","un livre"],0,"Un tableau est une œuvre peinte, souvent sur toile ou sur bois."],
 ["Quelle couleur est celle du soleil sur un dessin ?",["le jaune","le bleu","le noir"],0,"Mais dans un coucher de soleil, il devient orange puis rouge !"],
])
d("cp-cu","cp","Culture","📚","#7C4DFF","Les contes que tout le monde connaît",[
 ["Dans « Le Petit Chaperon rouge », qui rencontre-t-elle dans la forêt ?",["le loup","un ours","une sorcière"],0,"Le conte de Perrault et des frères Grimm."],
 ["Combien sont les petits cochons de l'histoire ?",["2","3","4"],1,"Trois petits cochons, trois maisons."],
 ["Dans « Cendrillon », que perd-elle en fuyant ?",["sa pantoufle","son chapeau","son sac"],0,"Une pantoufle de verre."],
 ["Qui mange la grand-mère dans « Le Petit Chaperon rouge » ?",["le loup","le bûcheron","la mère"],0,"Le loup, avant de prendre sa place dans le lit."],
 ["Un conte se termine souvent par…",["« Ils vécurent heureux »","une recette","une carte"],0,"La formule finale du conte est un rituel de l'histoire racontée."],
])
d("cp-dm","cp","Découverte du monde","🌍","#0EA5E9","Les animaux du monde",[
 ["Où vit le manchot ?",["au pôle Sud","dans le désert","en forêt"],0,"Le manchot vit dans l'Antarctique ; le pingouin, lui, vit dans l'hémisphère Nord."],
 ["Quel est le plus grand animal du monde ?",["la baleine bleue","l'éléphant","la girafe"],0,"La baleine bleue peut atteindre 30 mètres."],
 ["Le dromadaire vit dans…",["le désert","la banquise","la forêt tropicale"],0,"Sa bosse stocke de la graisse : il résiste longtemps sans eau."],
 ["Quel animal est le roi de la savane africaine ?",["le lion","le tigre","l'ours"],0,"Le lion vit en Afrique ; le tigre vit en Asie."],
 ["Le caméléon a la particularité de…",["changer de couleur","voler","parler"],0,"Il change de couleur selon son humeur et la température."],
])

# ══════════════ CE1 ══════════════
d("ce1-ar","ce1","Arts","🎨","#E879A6","Les instruments de musique",[
 ["Quel instrument a des cordes et un archet ?",["le violon","la flûte","le tambour"],0,"Le violon se joue avec un archet qui frotte les cordes."],
 ["Le piano est un instrument…",["à cordes frappées","à vent","de percussion pure"],0,"Des marteaux frappent les cordes à l'intérieur."],
 ["Quel instrument se joue en soufflant ?",["la trompette","le violoncelle","la harpe"],0,"Les cuivres et les bois se jouent avec le souffle."],
 ["Le tambour fait partie des…",["percussions","cordes","vents"],0,"On le frappe : c'est une percussion."],
 ["Combien de cordes a une guitare classique ?",["4","6","12"],1,"Six cordes, de la plus grave à la plus aiguë."],
])
d("ce1-dm","ce1","Découverte du monde","🌍","#0EA5E9","Pays et capitales",[
 ["La capitale de la France est…",["Paris","Lyon","Marseille"],0,"Paris est la capitale depuis des siècles."],
 ["La capitale de l'Italie est…",["Rome","Venise","Milan"],0,"Rome, ville du Colisée et du Vatican."],
 ["La capitale de l'Espagne est…",["Madrid","Barcelone","Séville"],0,"Barcelone est une grande ville, mais pas la capitale."],
 ["Quel pays a la forme d'une botte ?",["l'Italie","le Portugal","la Grèce"],0,"La péninsule italienne ressemble à une botte."],
 ["Mayotte appartient à quel pays ?",["la France","Madagascar","les Comores"],0,"Mayotte est un département français depuis 2011."],
])
d("ce1-cu","ce1","Culture","📚","#7C4DFF","Les monuments célèbres",[
 ["La tour Eiffel se trouve à…",["Paris","Londres","New York"],0,"Construite pour l'Exposition universelle de 1889."],
 ["Les pyramides de Gizeh sont en…",["Égypte","Grèce","Chine"],0,"Près du Caire, elles servaient de tombeaux aux pharaons."],
 ["La Grande Muraille se trouve en…",["Chine","Inde","Japon"],0,"Elle mesure des milliers de kilomètres."],
 ["La statue de la Liberté a été offerte par…",["la France","l'Espagne","l'Italie"],0,"Offerte par la France aux États-Unis en 1886."],
 ["Le Colisée est un monument…",["romain","grec","égyptien"],0,"Un amphithéâtre de Rome, où combattaient les gladiateurs."],
])

# ══════════════ CE2 ══════════════
d("ce2-ar","ce2","Arts","🎨","#E879A6","Les grands peintres",[
 ["Qui a peint « La Nuit étoilée » ?",["Van Gogh","Monet","Picasso"],0,"Vincent Van Gogh, peintre néerlandais du XIXe siècle."],
 ["Monet est le chef de file de…",["l'impressionnisme","le cubisme","le surréalisme"],0,"Son tableau « Impression, soleil levant » a donné son nom au mouvement."],
 ["Picasso a peint…",["Guernica","La Joconde","Les Tournesols"],0,"Guernica dénonce le bombardement d'une ville espagnole en 1937."],
 ["« Les Tournesols » est une œuvre de…",["Van Gogh","Monet","Cézanne"],0,"Une série de tableaux peints à Arles."],
 ["Un autoportrait est…",["un portrait de l'artiste par lui-même","un paysage","une nature morte"],0,"L'artiste se représente lui-même."],
])
d("ce2-dm","ce2","Découverte du monde","🌍","#0EA5E9","Océans et continents",[
 ["Combien y a-t-il d'océans ?",["3","5","7"],1,"Pacifique, Atlantique, Indien, Arctique, Antarctique."],
 ["Le plus grand océan est…",["le Pacifique","l'Atlantique","l'Indien"],0,"Il couvre environ un tiers du globe."],
 ["Mayotte se baigne dans…",["l'océan Indien","l'Atlantique","la Méditerranée"],0,"Entre Madagascar et la côte africaine."],
 ["Le continent le plus peuplé est…",["l'Asie","l'Europe","l'Afrique"],0,"Plus de la moitié de l'humanité y vit."],
 ["Le désert du Sahara se trouve en…",["Afrique","Asie","Amérique"],0,"Le plus grand désert chaud du monde."],
])
d("ce2-cu","ce2","Culture","📚","#7C4DFF","Les inventions",[
 ["Qui a inventé l'imprimerie en Europe ?",["Gutenberg","Edison","Pasteur"],0,"Vers 1450 : les livres deviennent reproductibles."],
 ["Qui a inventé l'ampoule électrique pratique ?",["Edison","Newton","Einstein"],0,"Thomas Edison, à la fin du XIXe siècle."],
 ["Qui a réalisé le premier vol en avion ?",["les frères Wright","les frères Lumière","Lindbergh"],0,"En 1903, aux États-Unis."],
 ["Les frères Lumière ont inventé…",["le cinéma","le téléphone","la radio"],0,"Leur première projection publique date de 1895."],
 ["La roue a été inventée…",["à la Préhistoire","au XXe siècle","au Moyen Âge"],0,"Une des plus anciennes inventions de l'humanité."],
])

# ══════════════ CM1 ══════════════
d("cm1-ar","cm1","Arts","🎨","#E879A6","Art et courants",[
 ["Les peintures des grottes de Lascaux datent d'environ…",["17 000 ans","500 ans","2 000 ans"],0,"Art pariétal du Paléolithique, en Dordogne."],
 ["L'impressionnisme est né en…",["France","Italie","Espagne"],0,"Autour de Monet, Renoir, Degas, dans les années 1870."],
 ["Une sculpture en ronde-bosse est…",["visible de tous les côtés","plate","peinte sur un mur"],0,"Par opposition au bas-relief, taillé sur une face."],
 ["Le cubisme consiste à…",["décomposer les formes","peindre uniquement en noir","copier la réalité"],0,"Picasso et Braque cassent les perspectives."],
 ["L'art pariétal désigne…",["l'art des parois des grottes","l'art de la rue","l'art numérique"],0,"Pariétal vient de « paroi »."],
])
d("cm1-cu","cm1","Culture","📚","#7C4DFF","Les grandes dates",[
 ["L'invention de l'écriture marque le début de…",["l'Histoire","la Préhistoire","le Moyen Âge"],0,"Il y a environ 5 000 ans, en Mésopotamie."],
 ["L'imprimerie de Gutenberg date d'environ…",["1450","1750","1050"],0,"Elle bouleverse la diffusion des idées."],
 ["Les premiers pas de l'homme sur la Lune datent de…",["1969","1945","1981"],0,"Apollo 11, 20 juillet 1969, Neil Armstrong."],
 ["La chute du mur de Berlin a eu lieu en…",["1989","1968","1999"],0,"Le 9 novembre 1989."],
 ["Les Jeux olympiques modernes ont été relancés en…",["1896","1948","1900"],0,"À Athènes, à l'initiative de Pierre de Coubertin."],
])
d("cm1-dm","cm1","Découverte du monde","🌍","#0EA5E9","Capitales et drapeaux",[
 ["La capitale du Royaume-Uni est…",["Londres","Manchester","Dublin"],0,"Londres, sur la Tamise."],
 ["La capitale de l'Allemagne est…",["Berlin","Munich","Francfort"],0,"Berlin redevient capitale après 1990."],
 ["La capitale de Madagascar est…",["Antananarivo","Toamasina","Nosy Be"],0,"Antananarivo, au centre des hauts plateaux."],
 ["Le drapeau français a trois bandes…",["bleu, blanc, rouge","rouge, blanc, bleu","bleu, rouge, blanc"],0,"Toujours du côté du mât : bleu, blanc, rouge."],
 ["Le drapeau européen porte…",["12 étoiles","27 étoiles","1 étoile"],0,"Douze étoiles, symbole d'unité — pas le nombre de pays."],
])

# ══════════════ CM2 ══════════════
d("cm2-cu","cm2","Culture","📚","#7C4DFF","Institutions et monde d'aujourd'hui",[
 ["L'ONU a été créée en…",["1945","1919","1989"],0,"Après la Seconde Guerre mondiale, pour préserver la paix."],
 ["La Déclaration universelle des droits de l'homme date de…",["1948","1789","1958"],0,"Adoptée par l'ONU le 10 décembre 1948."],
 ["L'Union européenne est née avec le traité de…",["Maastricht","Versailles","Rome"],0,"1992 : le traité de Maastricht crée l'UE et la citoyenneté européenne."],
 ["L'UNESCO protège…",["le patrimoine mondial","les routes","les banques"],0,"Elle classe des sites « patrimoine mondial de l'humanité »."],
 ["Le programme de l'ONU pour les enfants s'appelle…",["UNICEF","OTAN","OMS"],0,"UNICEF : Fonds des Nations unies pour l'enfance."],
])
d("cm2-ar","cm2","Arts","🎨","#E879A6","Chefs-d'œuvre et patrimoine",[
 ["« La Joconde » a été peinte par…",["Léonard de Vinci","Michel-Ange","Raphaël"],0,"Elle est exposée au musée du Louvre."],
 ["La Vénus de Milo est…",["une sculpture grecque","un tableau","un monument"],0,"Découverte en Grèce, exposée au Louvre."],
 ["La cathédrale Notre-Dame de Paris est de style…",["gothique","romain","moderne"],0,"Arcs brisés, voûtes sur croisées d'ogives, rosaces."],
 ["La grotte de Lascaux se trouve en…",["Dordogne","Bretagne","Provence"],0,"Découverte en 1940 par des adolescents."],
 ["Le château de Versailles a été agrandi par…",["Louis XIV","Napoléon","François Ier"],0,"Le Roi-Soleil y installe la cour en 1682."],
])
d("cm2-dm","cm2","Découverte du monde","🌍","#0EA5E9","Records du monde",[
 ["Le plus haut sommet du monde est…",["l'Everest","le Mont Blanc","le Kilimandjaro"],0,"8 849 m, dans l'Himalaya."],
 ["Le plus long fleuve d'Afrique est…",["le Nil","le Congo","le Niger"],0,"Environ 6 700 km."],
 ["Le plus grand désert chaud du monde est…",["le Sahara","le Gobi","l'Atacama"],0,"Plus de 9 millions de km²."],
 ["La fosse la plus profonde des océans est…",["la fosse des Mariannes","la fosse du Japon","le golfe du Mexique"],0,"Près de 11 000 m de profondeur."],
 ["Le pays le plus peuplé du monde est…",["l'Inde","la Chine","le Brésil"],0,"L'Inde a dépassé la Chine en 2023."],
])

BADGES3 = [
 {"id":"curieux","n":"Curieux du monde","e":"🌍","d":"3 étoiles à 2 défis de découverte du monde"},
 {"id":"artiste","n":"Œil d'artiste","e":"🎨","d":"3 étoiles à 2 défis d'arts"},
 {"id":"culture","n":"Culture générale","e":"📚","d":"3 étoiles à 2 défis de culture"},
 {"id":"sansfaute5","n":"Cinq sans-faute","e":"💫","d":"Réussir 5 défis à 5/5"},
]
