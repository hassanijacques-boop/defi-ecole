#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconstruit trivial.html avec 4 paquets de questions."""
import json, re, sys, random, hashlib
sys.path.insert(0, '/workspace/defi')
import trivial_data as T1, trivial_data2 as T2, trivial_data3 as T3, trivial_data4 as T4
import trivial_mayotte as TM, trivial_mayotte2 as TM2
import trivial_histoire as TH, trivial_sciences as TS

def shuffle_det(qq):
    """Mélange les options de façon déterministe (stable, mais réparti)."""
    seed = int(hashlib.md5(qq["q"].encode("utf-8")).hexdigest()[:8], 16)
    idx = [0, 1, 2]
    random.Random(seed).shuffle(idx)
    qq["o"] = [qq["o"][i] for i in idx]
    qq["r"] = idx.index(qq["r"])
    return qq

CAT6 = [
 {"id":"geo","n":"Géographie","e":"🌍","c":"#1E6FD9"},
 {"id":"his","n":"Histoire","e":"🏛️","c":"#E8B31C"},
 {"id":"art","n":"Arts & Littérature","e":"🎨","c":"#A855F7"},
 {"id":"sci","n":"Sciences & Nature","e":"🔬","c":"#22A06B"},
 {"id":"spo","n":"Sports & Loisirs","e":"⚽","c":"#F97316"},
 {"id":"div","n":"Divertissements","e":"🎬","c":"#E8456B"},
]
HIS6 = [
 {"id":"pre","n":"Préhistoire et Gaule","e":"🪨","c":"#8B6F47"},
 {"id":"moy","n":"Moyen Âge","e":"🏰","c":"#7C5C3E"},
 {"id":"ren","n":"Renaissance et Roi-Soleil","e":"👑","c":"#B8860B"},
 {"id":"rev","n":"Révolution et Empire","e":"⚔️","c":"#B91C1C"},
 {"id":"dix","n":"XIXe siècle","e":"🏭","c":"#1F6FB2"},
 {"id":"vin","n":"XXe siècle","e":"🕊️","c":"#0F766E"},
]
SCI6 = [
 {"id":"viv","n":"Le vivant","e":"🌿","c":"#22A06B"},
 {"id":"ter","n":"Terre et espace","e":"🌍","c":"#1E6FD9"},
 {"id":"mat","n":"Matière et chimie","e":"⚗️","c":"#7C3AED"},
 {"id":"cor","n":"Corps humain","e":"🫀","c":"#E8456B"},
 {"id":"inv","n":"Inventions","e":"💡","c":"#E8B31C"},
 {"id":"rec","n":"Records","e":"🏆","c":"#F97316"},
]

PAQUETS = [
 {"id":"culture","nom":"Culture générale","em":"🎲","desc":"Le paquet classique, tous sujets","cats":CAT6,
  "q":T1.Q+T2.Q2+T3.Q3+T4.Q4},
 {"id":"mayotte","nom":"Spécial Mayotte","em":"🌴","desc":"L'île, l'océan Indien, la faune, la culture","cats":CAT6,
  "q":TM.QM+TM2.QM2},
 {"id":"histoire","nom":"Histoire de France","em":"🏰","desc":"De la Gaule à la Ve République","cats":HIS6,
  "q":TH.QH},
 {"id":"sciences","nom":"Sciences","em":"🔬","desc":"Le vivant, la Terre, la matière, le corps","cats":SCI6,
  "q":TS.QS},
]

tpl = open('/workspace/defi/trivial_template.html', encoding='utf-8').read()

# 1) remplacer le bloc de démarrage (boutons)
old_btn = re.search(r'<button class="play" id="go">.*?</p>\s*</div>', tpl, re.S)
NEW_BTN = '''<div id="pakList" style="display:grid;gap:9px;margin-top:6px"></div>
    <p style="font-size:11.5px;color:var(--ink2);font-weight:600;margin:10px 0 0">Quatre paquets, le même plateau : seules les questions et les couleurs changent.</p>
  </div>'''
if old_btn:
    tpl = tpl[:old_btn.start()] + NEW_BTN + tpl[old_btn.end():]

# 2) remplacer le script
new_js = open('/workspace/defi/trivial_paquets.js', encoding='utf-8').read()
tpl = re.sub(r'<script>.*?</script>', '<script>\n' + new_js + '\n</script>', tpl, flags=re.S)

# 3) injecter les données
PAQ = []
for p in PAQUETS:
    qs = [shuffle_det({"c":x["c"],"q":x["q"],"o":list(x["o"]),"r":x["r"],"e":x.get("e","")}) for x in p["q"]]
    PAQ.append({"id":p["id"],"nom":p["nom"],"em":p["em"],"desc":p["desc"],"cats":p["cats"],"q":qs})
html = tpl.replace("__PAQUETS__", json.dumps(PAQ, ensure_ascii=False, separators=(",",":")))

# conserver la barre de navigation
old = open('/workspace/defi/trivial.html', encoding='utf-8').read()
m = re.search(r'(<style>\n\.tubebar.*?</nav>)', old, re.S)
if m and 'class="tubebar"' not in html:
    html = html.replace("<body>", "<body>\n" + m.group(1), 1)

open('/workspace/defi/trivial.html','w',encoding='utf-8').write(html)
print("total questions:", sum(len(p["q"]) for p in PAQ))
for p in PAQ: print(" -", p["nom"], ":", len(p["q"]), "questions,", len(p["cats"]), "catégories")
from collections import Counter
dist = Counter(x["r"] for p in PAQ for x in p["q"])
tot = sum(dist.values())
print("répartition des bonnes réponses:", {k: f"{v} ({round(100*v/tot)}%)" for k,v in sorted(dist.items())})
print("taille:", len(html))
