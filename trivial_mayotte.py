# -*- coding: utf-8 -*-
"""Paquet « Spécial Mayotte » — 50 questions, réparties dans les 6 catégories.
geo 9 · his 9 · art 8 · sci 9 · spo 8 · div 7 = 50 — niveau junior (9-13 ans)."""

QM = []
def q(c, qq, opts, r, e=""):
    QM.append({"c": c, "q": qq, "o": opts, "r": r, "e": e})

# ─────────── GÉOGRAPHIE (9) ───────────
q("geo", "Combien d'îles principales compte l'archipel de Mayotte ?",
  ["Deux", "Trois", "Cinq"], 0,
  "Grande-Terre (Mahoré) et Petite-Terre (Pamanzi), entourées d'une trentaine d'îlots.")
q("geo", "Quel est le chef-lieu de Mayotte ?",
  ["Mamoudzou", "Dzaoudzi", "Koungou"], 0,
  "Mamoudzou, sur Grande-Terre, est le chef-lieu depuis 1977. Avant, c'était Dzaoudzi.")
q("geo", "Dans quel océan se trouve Mayotte ?",
  ["L'océan Indien", "L'océan Atlantique", "La mer Méditerranée"], 0,
  "Plus précisément dans le canal du Mozambique, entre Madagascar et l'Afrique de l'Est.")
q("geo", "Quel pays est le plus proche de Mayotte ?",
  ["Les Comores", "Madagascar", "Le Mozambique"], 0,
  "L'île d'Anjouan, aux Comores, n'est qu'à environ 70 km.")
q("geo", "Quel est le point culminant de Mayotte ?",
  ["Le mont Bénara", "Le mont Choungui", "Le Karthala"], 0,
  "660 mètres, au centre de Grande-Terre. Le Choungui, plus connu, culmine à 594 m ; le Karthala est un volcan des Comores.")
q("geo", "Comment passe-t-on de Mamoudzou à Petite-Terre ?",
  ["En barge", "En train", "Par un pont"], 0,
  "La barge transporte passagers et véhicules plusieurs fois par jour, en quelques minutes.")
q("geo", "En quelle année Mayotte est-elle devenue un département français ?",
  ["2011", "1946", "1848"], 0,
  "Le 31 mars 2011 : 101e département, après le référendum de 2009 (95 % de oui).")
q("geo", "Comment appelle-t-on la saison sèche et fraîche à Mayotte ?",
  ["Le kusi", "Le kashkazi", "L'hivernage"], 0,
  "Le kusi souffle de juin à septembre. Le kashkazi, c'est la saison des pluies.")
q("geo", "Combien d'habitants compte à peu près Mayotte ?",
  ["Environ 320 000", "Environ 80 000", "Environ 2 millions"], 0,
  "C'est le département le plus jeune de France : la moitié de la population a moins de 18 ans.")

# ─────────── HISTOIRE (9) ───────────
q("his", "En 1841, qui a cédé Mayotte à la France ?",
  ["Le sultan Andriantsoly", "Le sultan de Zanzibar", "Napoléon III"], 0,
  "Le traité de cession est signé le 25 avril 1841 par le sultan Andriantsoly.")
q("his", "En quelle année l'esclavage a-t-il été aboli à Mayotte ?",
  ["1846", "1789", "1946"], 0,
  "Le 27 avril 1846, deux ans avant le reste de la France (1848).")
q("his", "En 1975, quand les Comores deviennent indépendantes, que choisit Mayotte ?",
  ["Rester française", "Rejoindre les Comores", "Devenir indépendante"], 0,
  "Par référendum, les Mahorais choisissent la France à plus de 60 %, puis à 99 % en 1976.")
q("his", "Qu'est-ce que le « grand mariage » à Mayotte ?",
  ["Une fête traditionnelle très coûteuse qui marque l'entrée dans le statut d'adulte",
   "Un mariage organisé par la mairie", "Une fête religieuse du Ramadan"], 0,
  "Appelé harusi ou ada, il dure plusieurs jours et engage toute la famille.")
q("his", "Quelle est la religion très majoritaire à Mayotte ?",
  ["L'islam", "Le christianisme", "L'hindouisme"], 0,
  "Environ 95 % de la population est musulmane ; le droit local s'appuie sur des cadis.")
q("his", "Qui juge selon le droit local musulman à Mayotte ?",
  ["Le cadi", "Le maire", "Le préfet"], 0,
  "Le cadi intervient dans certains litiges civils, comme le mariage ou l'héritage.")
q("his", "Parmi ces langues, laquelle est parlée à Mayotte ?",
  ["Le shimaoré", "Le créole réunionnais", "Le malgache officiel"], 0,
  "On parle shimaoré et kibushi (proche du malgache), en plus du français, langue officielle.")
q("his", "Que s'est-il passé à Mayotte le 31 mars 2011 ?",
  ["Mayotte est devenue un département", "Mayotte a obtenu son indépendance",
   "Mayotte a changé de capitale"], 0,
  "Mayotte devient le 101e département français et le 5e département d'outre-mer.")
q("his", "D'où viennent les populations qui ont peuplé Mayotte ?",
  ["D'Afrique de l'Est, de Madagascar et du monde arabe", "Uniquement de France",
   "De Polynésie"], 0,
  "D'où une culture métissée, une langue bantoue et une religion venue du monde arabe.")

# ─────────── ARTS & LITTÉRATURE (8) ───────────
q("art", "Comment s'appelle la robe traditionnelle colorée portée par les femmes à Mayotte ?",
  ["Le salouva", "Le boubou", "La sape"], 0,
  "Le salouva, souvent accompagné du kishali, le grand châle porté sur la tête ou les épaules.")
q("art", "Qu'est-ce que le « debaa » ?",
  ["Un chant dansé des femmes", "Un plat traditionnel", "Un instrument de musique"], 0,
  "Un chant religieux et poétique, en cercle, qui peut durer des heures.")
q("art", "Comment s'appelle la danse traditionnelle en cercle qui rythme les fêtes ?",
  ["Le mgodro", "La biguine", "Le séga"], 0,
  "Le mgodro se danse au son des tambours, surtout pendant les grands mariages.")
q("art", "Quel écrivain mahorais a écrit « La Fille du polygame » ?",
  ["Nassur Attoumani", "Aimé Césaire", "Patrick Chamoiseau"], 0,
  "Nassur Attoumani, auteur, humoriste et metteur en scène né à Mamoudzou en 1954.")
q("art", "Comment s'appelle le masque de beauté au bois de santal des femmes mahoraises ?",
  ["Le msindzano", "Le henné", "Le khôl"], 0,
  "Une pâte de bois de santal broyé appliquée sur le visage : un soin traditionnel.")
q("art", "Quel musicien mahorais chante en shimaoré et fait connaître l'île sur scène ?",
  ["M'toro Chamou", "Youssou N'Dour", "Kassav'"], 0,
  "M'toro Chamou, figure de la musique mahoraise, entre tradition et rock.")
q("art", "Dans quelle langue sont racontés les contes traditionnels de Mayotte ?",
  ["En shimaoré ou en kibushi", "En français", "En anglais"], 0,
  "Les contes se transmettent à l'oral, le soir, dans les deux langues de l'île.")
q("art", "Quel plat traditionnel mahorais est fait de feuilles de manioc et de lait de coco ?",
  ["Le mataba", "La paella", "Le couscous"], 0,
  "Feuilles de manioc pilées, lait de coco, poisson ou viande : le plat du quotidien.")

# ─────────── SCIENCES & NATURE (9) ───────────
q("sci", "Quel animal vole la nuit à Mayotte et se nourrit de fruits ?",
  ["La roussette", "Le hibou grand-duc", "La chauve-souris vampire"], 0,
  "La roussette est une grande chauve-souris frugivore, espèce protégée.")
q("sci", "Quelle tortue vient pondre sur les plages de Mayotte ?",
  ["La tortue verte", "La tortue luth", "La tortue de Floride"], 0,
  "La tortue verte et la tortue imbriquée pondent sur les plages ; elles sont protégées.")
q("sci", "Quel grand cétacé vient dans les eaux de Mayotte entre juillet et octobre ?",
  ["La baleine à bosse", "L'orque", "Le cachalot"], 0,
  "Elle vient y mettre bas et allaiter son petit, à l'abri du lagon.")
q("sci", "Qu'est-ce qui entoure Mayotte et protège ses côtes ?",
  ["Une double barrière de corail", "Une banquise", "Une chaîne de montagnes sous-marines"], 0,
  "L'un des plus grands lagons fermés du monde, d'environ 1 500 km².")
q("sci", "De quelle fleur Mayotte tire-t-elle une essence de parfum célèbre dans le monde entier ?",
  ["L'ylang-ylang", "La lavande", "Le jasmin"], 0,
  "Mayotte est le premier producteur mondial d'essence d'ylang-ylang.")
q("sci", "Quelle forêt pousse dans l'eau salée le long des côtes ?",
  ["La mangrove", "La forêt de pins", "La savane"], 0,
  "Les palétuviers retiennent la terre et servent de nursery aux jeunes poissons.")
q("sci", "Quand s'étend la saison des cyclones dans l'océan Indien ?",
  ["De décembre à avril", "De juin à septembre", "Toute l'année"], 0,
  "C'est l'été austral : chaleur, pluies fortes et risque de cyclone.")
q("sci", "Qu'a découvert une mission scientifique au large de Mayotte en 2019 ?",
  ["Un volcan sous-marin", "Une épave de pirate", "Un trésor englouti"], 0,
  "Un volcan de 800 m de haut, apparu en quelques mois, à 50 km à l'est de l'île.")
q("sci", "Quelle épice, en gousse noire, est cultivée à Mayotte ?",
  ["La vanille", "Le poivre de Sichuan", "Le safran"], 0,
  "La vanille pousse à l'ombre des arbres ; celle de Mayotte est très parfumée.")

# ─────────── SPORTS & LOISIRS (8) ───────────
q("spo", "Quel est le sport le plus populaire à Mayotte ?",
  ["Le football", "Le curling", "Le hockey sur glace"], 0,
  "Un terrain dans presque chaque village, et une ferveur énorme pour les tournois.")
q("spo", "Quel footballeur né à Mayotte a joué à l'OM et à Lens ?",
  ["Toifilou Maoulida", "Zinédine Zidane", "Didier Drogba"], 0,
  "Né à Dzaoudzi en 1979, plus de 500 matchs chez les professionnels.")
q("spo", "Quelle activité attire les visiteurs dans le lagon ?",
  ["La plongée sous-marine", "Le ski alpin", "Le surf sur la banquise"], 0,
  "Poissons multicolores, coraux, tortues : on visite le lagon masque et tuba.")
q("spo", "Quelle randonnée mène au sommet le plus célèbre du sud de Mayotte ?",
  ["Le mont Choungui", "L'Everest", "Le mont Blanc"], 0,
  "Le Choungui (594 m) offre la vue sur toute la barrière de corail.")
q("spo", "Comment les femmes pêchent-elles traditionnellement le poulpe à Mayotte ?",
  ["À pied, à marée basse", "En bateau au large", "Avec un filet depuis la plage"], 0,
  "Sur le récif découvert, avec un bâton et un sac : un savoir-faire transmis.")
q("spo", "Quel sport nautique se pratique avec une pagaie dans le lagon ?",
  ["Le kayak", "Le bobsleigh", "L'escalade"], 0,
  "Kayak et paddle permettent de longer les mangroves et les îlots.")
q("spo", "Comment appelle-t-on la petite pirogue traditionnelle de Mayotte ?",
  ["La galawa", "La gondole", "Le voilier"], 0,
  "Une pirogue à rames, héritée des marins de l'océan Indien.")
q("spo", "Sur un terrain de village, combien de joueurs compte une équipe de football ?",
  ["11", "7", "15"], 0,
  "Et autour du terrain, debout ou assis par terre, il y a souvent bien plus de monde.")

# ─────────── DIVERTISSEMENTS (7) ───────────
q("div", "Quel animal marin figure sur le logo du département de Mayotte ?",
  ["L'hippocampe", "Le requin", "La baleine"], 0,
  "L'hippocampe, présent dans le lagon, est devenu l'emblème de l'île.")
q("div", "Quelle chaîne de télévision publique émet à Mayotte ?",
  ["Mayotte la 1ère", "TF1 Mayotte", "Canal+ Océan"], 0,
  "Mayotte la 1ère fait partie du réseau Outre-mer de France Télévisions.")
q("div", "Quel hebdomadaire raconte l'actualité de Mayotte ?",
  ["Mayotte Hebdo", "Le Monde", "L'Équipe"], 0,
  "Un journal local, avec les infos des villages et la vie quotidienne de l'île.")
q("div", "Quelle fête musulmane est très attendue à Mayotte ?",
  ["L'Aïd", "Noël", "Halloween"], 0,
  "L'Aïd el-Fitr (fin du Ramadan) et l'Aïd el-Kébir rassemblent les familles.")
q("div", "Quel surnom donne-t-on à Mayotte ?",
  ["L'île aux parfums", "L'île de la Réunion", "L'île aux trésors"], 0,
  "À cause de l'ylang-ylang et de la vanille, qui parfument l'air de l'île.")
q("div", "Quel fruit à coque, très utilisé dans la cuisine mahoraise, pousse sur les palmiers ?",
  ["La noix de coco", "La noisette", "La châtaigne"], 0,
  "Lait de coco dans le mataba, coco râpée dans les desserts : il est partout.")
q("div", "Comment appelle-t-on les habitants de Mayotte ?",
  ["Les Mahorais", "Les Mahoréens", "Les Mahométans"], 0,
  "Mayotte donne Mahorais et Mahoraise. Le nom de l'île en shimaoré est Maoré.")
