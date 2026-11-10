#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble trivial.html depuis trivial_template.html + les 3 paquets de questions.
Le bloc .tubebar (barre de navigation des Tubes) est repris de l'index.html déjà publié."""
import json, re, sys
sys.path.insert(0, '/workspace/defi')

from trivial_data import Q
from trivial_data2 import Q2
from trivial_mayotte import QM

ALL = Q + Q2
assert len(ALL) == 150, f"paquet général : {len(ALL)} questions"
assert len(QM) == 50, f"paquet Mayotte : {len(QM)} questions"

for name, pack in (("général", ALL), ("Mayotte", QM)):
    for q in pack:
        assert len(q["o"]) == 3, f"{name} : {q['q']} n'a pas 3 propositions"
        assert 0 <= q["r"] < 3, f"{name} : {q['q']} a un index de réponse invalide"
        assert len(set(q["o"])) == 3, f"{name} : {q['q']} a deux propositions identiques"

for cat in ("geo", "his", "art", "sci", "spo", "div"):
    n = sum(1 for q in QM if q["c"] == cat)
    assert n >= 7, f"Mayotte : seulement {n} questions en {cat} (le plateau en a besoin de 7+)"

t = open('/workspace/defi/trivial_template.html', encoding='utf-8').read()
h = t.replace('__QUESTIONS__', json.dumps(ALL, ensure_ascii=False, separators=(",", ":")))
h = h.replace('__QMAY__', json.dumps(QM, ensure_ascii=False, separators=(",", ":")))

# reprise de la barre de navigation des Tubes, déjà présente dans la version publiée
try:
    old = open('/workspace/defi/trivial.html', encoding='utf-8').read()
    m = re.search(r'(<style>\n\.tubebar.*?</nav>)', old, re.S)
    if m and 'class="tubebar"' not in h:
        h = h.replace('<body>', '<body>\n' + m.group(1), 1)
        print("tubebar reprise")
except FileNotFoundError:
    pass

h = h.replace('\U0001F5A7', '\U0001F310')   # 🖧 n'est pas rendu sur tous les appareils
open('/workspace/defi/trivial.html', 'w', encoding='utf-8').write(h)
js = re.search(r'<script>(.*?)</script>', h, re.S).group(1)
open('/tmp/vt5.js', 'w', encoding='utf-8').write(js)
print(f"OK trivial.html {len(h)} octets · {len(ALL)} + {len(QM)} questions")
