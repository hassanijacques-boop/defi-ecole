# -*- coding: utf-8 -*-
import re

p = '/workspace/defi/build_trivial.py'
s = open(p, encoding='utf-8').read()
a = s.index("def add_fourth(")
b = s.index("def shuffle_det(")
NEW = '''def _mots(t):
    return set(w.lower() for w in _re.findall(r"[A-Za-zéèêàâîôûçÉÈÊÀÂÎÔÛÇ]{4,}", t))

def add_fourth(qq, banque):
    """4e proposition : prise dans une question proche par le sens, sinon par longueur."""
    opts = list(qq["o"])
    if len(opts) >= 4:
        return qq
    deja = set(o.strip().lower() for o in opts)
    moy = sum(len(o) for o in opts) / len(opts)
    miens = _mots(qq["q"])
    cands = []
    for x in banque:
        if x is qq or x.get("c") != qq["c"] or not x.get("o"):
            continue
        rep = x["o"][x["r"]]
        if rep.strip().lower() in deja:
            continue
        if not (0.5 * moy <= len(rep) <= 1.9 * moy):
            continue
        score = len(miens.intersection(_mots(x["q"])))
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
        if 0.6 * moy <= len(rep) <= 1.7 * moy:
            opts.append(rep)
            qq["o"] = opts
            return qq
    opts.append("Aucune de ces réponses")
    qq["o"] = opts
    return qq

'''
s = s[:a] + NEW + s[b:]
open(p, 'w', encoding='utf-8').write(s)
print("ok build patché")

p2 = '/workspace/defi/trivial_histoire.py'
h = open(p2, encoding='utf-8').read()
h = h.replace(
 'q("pre","Quel empereur romain a fait construire le pont du Gard ?",["Les Romains de l\'Antiquité","Napoléon","Charlemagne"],0,"Un aqueduc pour alimenter Nîmes.")',
 'q("pre","Qui a construit le pont du Gard ?",["Les Romains","Les Gaulois","Les Grecs","Les Égyptiens"],0,"Un aqueduc romain pour alimenter Nîmes.")')
if "Quel peuple a fondé Marseille ?" not in h:
    h += '\nq("pre","Quel peuple a fondé Marseille ?",["Les Grecs","Les Romains","Les Phéniciens","Les Gaulois"],0,"Des marins venus de Phocée, vers 600 av. J.-C.")\n'
open(p2, 'w', encoding='utf-8').write(h)
print("ok histoire corrigée")
