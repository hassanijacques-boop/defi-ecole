# -*- coding: utf-8 -*-
"""Reconstruit index.html de Defi Ecole avec tous les defis."""
import json, re, sys
sys.path.insert(0, '/workspace/defi')
import defis, defis2, defis3, defis4, defis5

D = defis.D + defis2.D2 + defis3.D3 + defis4.D4 + defis5.D5
BADGES = defis.BADGES + defis3.BADGES3

# verifications
ids = [x["id"] for x in D]
assert len(ids) == len(set(ids)), "ids en double : " + str([i for i in ids if ids.count(i) > 1])
for x in D:
    for q in x["qs"]:
        if not isinstance(q[2], int):
            q[2] = int(q[2])
    assert len(x["qs"]) >= 3, x["id"]
    for q in x["qs"]:
        assert len(q) == 4, (x["id"], q[0])
        assert len(q[1]) == 3, (x["id"], q[0])
        assert 0 <= q[2] <= 2, (x["id"], q[0])

tpl = open('/workspace/defi/template.html', encoding='utf-8').read()
html = tpl.replace("__DEFIS__", json.dumps(D, ensure_ascii=False, separators=(",", ":")))
html = html.replace("__NIVEAUX__", json.dumps(defis.NIVEAUX, ensure_ascii=False, separators=(",", ":")))
html = html.replace("__BADGES__", json.dumps(BADGES, ensure_ascii=False, separators=(",", ":")))

if 'class="tubebar"' not in html:
    old = open('/workspace/defi/index.html', encoding='utf-8').read()
    m = re.search(r'(<style>\n\.tubebar.*?</nav>)', old, re.S)
    if m:
        html = html.replace("<body>", "<body>\n" + m.group(1), 1)
if "serviceWorker" not in html:
    old = open('/workspace/defi/index.html', encoding='utf-8').read()
    m = re.search(r'(<link rel="manifest".*?</script>)', old, re.S)
    if m:
        html = html.replace("</head>", m.group(1) + "</head>", 1)

open('/workspace/defi/index.html', 'w', encoding='utf-8').write(html)
print("défis:", len(D), "| questions:", sum(len(x["qs"]) for x in D), "| badges:", len(BADGES))
import collections
print(collections.Counter(x["nv"] for x in D))
print("matières:", len(set(x["m"] for x in D)))
print("taille:", len(html))
