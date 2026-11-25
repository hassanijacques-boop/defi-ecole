# -*- coding: utf-8 -*-
"""Ameliore le choix du 4e distracteur : similarite question + reponse."""
p = '/workspace/defi/build_trivial.py'
s = open(p, encoding='utf-8').read()
a = s.index("def _mots(")
b = s.index("def shuffle_det(")
NEW = '''def _mots(t):
    return set(w.lower() for w in _re.findall(r"[A-Za-zéèêàâîôûçÉÈÊÀÂÎÔÛÇ]{4,}", t))

ART = ("le ", "la ", "les ", "l'", "l’", "un ", "une ", "des ")

def _article(t):
    bas = t.strip().lower()
    for ar in ART:
        if bas.startswith(ar):
            return ar
    return ""

def add_fourth(qq, banque):
    """4e proposition : question proche, ou reponse proche, sinon meme article."""
    opts = list(qq["o"])
    if len(opts) >= 4:
        return qq
    deja = set(o.strip().lower() for o in opts)
    moy = sum(len(o) for o in opts) / len(opts)
    bonne = opts[qq["r"]].strip().lower()
    mq = _mots(qq["q"])
    mr = _mots(opts[qq["r"]])
    art = _article(opts[qq["r"]])
    cands = []
    for x in banque:
        if x is qq or x.get("c") != qq["c"] or not x.get("o"):
            continue
        rep = x["o"][x["r"]]
        bas = rep.strip().lower()
        if bas in deja or bas == bonne:
            continue
        if not (0.45 * moy <= len(rep) <= 2.0 * moy):
            continue
        if _re.search(r"\\d", rep) and not _re.search(r"\\d", opts[qq["r"]]):
            continue
        score = len(mq.intersection(_mots(x["q"]))) + 2 * len(mr.intersection(_mots(x["q"])))
        if art and _article(rep) == art:
            score += 1
        if score > 0:
            cands.append((score, rep))
    if cands:
        cands.sort(key=lambda t: -t[0])
        opts.append(cands[0][1])
        qq["o"] = opts
        return qq
    for x in banque:
        if x is qq or x.get("c") != qq["c"] or not x.get("o"):
            continue
        rep = x["o"][x["r"]]
        if rep.strip().lower() in deja or _re.search(r"\\d", rep):
            continue
        if _article(rep) == art and 0.6 * moy <= len(rep) <= 1.5 * moy:
            opts.append(rep)
            qq["o"] = opts
            return qq
    opts.append("Aucune de ces réponses")
    qq["o"] = opts
    return qq

'''
s = s[:a] + NEW + s[b:]
open(p, 'w', encoding='utf-8').write(s)
print("ok")
