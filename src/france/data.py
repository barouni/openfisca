# -*- coding:utf-8 -*-
# Copyright © 2011 Clément Schaff, Mahdi Ben Jelloul

"""
openFisca, Logiciel libre de simulation du système socio-fiscal français
Copyright © 2011 Clément Schaff, Mahdi Ben Jelloul

This file is part of openFisca.

    openFisca is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    openFisca is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with openFisca.  If not, see <http://www.gnu.org/licenses/>.
"""

from core.datatable import DataTable, IntCol, EnumCol, BoolCol, AgesCol, FloatCol
from core.utils import Enum

QUIFOY = Enum(['vous', 'conj', 'pac1','pac2','pac3','pac4','pac5','pac6','pac7','pac8','pac9'])
QUIFAM = Enum(['chef', 'part', 'enf1','enf2','enf3','enf4','enf5','enf6','enf7','enf8','enf9'])
QUIMEN = Enum(['pref', 'cref', 'enf1','enf2','enf3','enf4','enf5','enf6','enf7','enf8','enf9'])
CAT    = Enum(['noncadre', 'cadre', 'fonc'])

YEAR = 2010

class InputTable(DataTable):
    '''
    Socio-economic data
    Donnée d'entrée de la simulation à fournir à partir d'une enquète ou 
    à générer avec un générateur de cas type
    '''
    noi = IntCol()

    idmen   = IntCol() # 600001, 600002,
    idfoy   = IntCol() # idmen + noi du déclarant
    idfam   = IntCol() # idmen + noi du chef de famille

    quimen  = EnumCol(QUIMEN)
    quifoy  = EnumCol(QUIFOY)
    quifam  = EnumCol(QUIFAM)
    
    type_sal = EnumCol(CAT)
    
    sali = IntCol() #(f1aj, f1bj, f1cj, f1dj, f1ej)
    choi = IntCol() # (f1ap, f1bp, f1cp, f1dp, f1ep)
    rsti = IntCol() # (f1as, f1bs, f1cs, f1ds, f1es)
    fra = IntCol() # (f1ak, f1bk, f1ck, f1dk, f1ek)

    alr = IntCol() # (f1ao, f1bo, f1co, f1do, f1eo)
    
    hsup = IntCol()
    inv = BoolCol()
    alt = BoolCol()
    cho_ld = BoolCol() # (f1ai, f1bi, f1ci, f1di, f1ei)
    ppe_tp_sa = BoolCol() # (f1ax, f1bx, f1cx, f1dx, f1qx)
    ppe_tp_ns = BoolCol() # (f5nw, f5ow, f5pw)
    ppe_du_sa = IntCol() # (f1av, f1bv, f1cv, f1dv, f1qv)
    ppe_du_ns = IntCol() # (f5nv, f5ov, f5pv)
    jour_xyz = IntCol(default = 360)
    age = AgesCol()
    agem = AgesCol()
    
    zone_apl = IntCol()
    loyer = IntCol()
    so = IntCol()
    activite = IntCol()
    boursier = BoolCol()
    code_postal = IntCol()
    
    statmarit = IntCol(default = 2)
    
    nbR = IntCol()
    nbJ = IntCol()
    nbI = IntCol()
    nbH = IntCol()
    nbG = IntCol()
    nbF = IntCol()
    nbN = IntCol()
    
    caseE = BoolCol()
    caseF = BoolCol()
    caseG = BoolCol()
    caseH = IntCol()
    caseK = BoolCol()
    caseL = BoolCol()
    caseN = BoolCol()
    caseP = BoolCol()
    caseS = BoolCol()
    caseT = BoolCol()
    caseW = BoolCol()
    
    # Rentes viagères
    f1aw = IntCol()
    f1bw = IntCol()
    f1cw = IntCol()
    f1dw = IntCol()
    
    f1tv = IntCol()
    f1uv = IntCol()
    f1tw = IntCol()
    f1uw = IntCol()
    f1tx = IntCol()
    f1ux = IntCol()
    
    # RVCM
    # revenus au prélèvement libératoire
    f2da = IntCol()
    f2dh = IntCol()
    f2ee = IntCol()

    # revenus ouvrant droit à abattement
    f2dc = IntCol()
    f2fu = IntCol()
    f2ch = IntCol()
    
    # Revenus n'ouvrant pas droit à abattement
    f2ts = IntCol()
    f2go = IntCol()
    f2tr = IntCol()
    
    # Autres
    f2cg = IntCol()
    f2bh = IntCol()
    f2ca = IntCol()
    f2ab = IntCol()    
    f2aa = IntCol()
    f2al = IntCol()
    f2am = IntCol()
    f2an = IntCol()

    # non accessible (from previous years)
    f2gr = IntCol() 
    

    
    f3vc = IntCol()
    f3vd = IntCol()
    f3ve = IntCol()
    f3vf = IntCol()    
    
    f3vl = IntCol()
    f3vi = IntCol()
    f3vm = IntCol()
    
    f3vj = IntCol()
    f3vk = IntCol()
    f3va = IntCol()
    
    # Plus values et gains taxables à 18%
    f3vg = IntCol()
    f3vh = IntCol()
    f3vt = IntCol()
    f3vu = IntCol()
    f3vv = IntCol()

    # Revenu foncier
    f4ba = IntCol()
    f4bb = IntCol()
    f4bc = IntCol()
    f4bd = IntCol()
    f4be = IntCol()
    
    # Prime d'assurance loyers impayés
    f4bf = IntCol()
    
    f4bl = IntCol()
    
    f5qm = IntCol()
    f5rm = IntCol()
    
    # Csg déductible
    f6de = IntCol()

    # Pensions alimentaires
    f6gi = IntCol()
    f6gj = IntCol()
    f6el = IntCol()
    f6em = IntCol()
    f6gp = IntCol()
    f6gu = IntCol()
    
    # Frais d'accueil d'une personne de plus de 75 ans dans le besoin
    f6eu = IntCol()
    f6ev = IntCol()
    
    # Déductions diverses
    f6dd = IntCol()
    
    # Dépenses de grosses réparations effectuées par les nus propriétaires
    f6cb = IntCol()
    f6hj = IntCol()
    
    # Sommes à rajouter au revenu imposable
    f6gh = IntCol()    
    
    # Deficit Antérieur
    f6fa = IntCol()
    f6fb = IntCol()
    f6fc = IntCol()
    f6fd = IntCol()
    f6fe = IntCol()
    f6fl = IntCol()
    
    # Dons
    f7ud = IntCol()
    f7uf = IntCol()
    f7xs = IntCol()
    f7xt = IntCol()
    f7xu = IntCol()
    f7xw = IntCol()
    f7xy = IntCol()
    
    # Cotisations syndicales des salariées et pensionnés
    f7ac = IntCol()
    f7ae = IntCol()
    f7ag = IntCol()

    # Salarié à domicile
    f7db = IntCol()
    f7df = IntCol()
    f7dq = IntCol()
    f7dg = IntCol()
    f7dl = IntCol()
    
    # Intérêt des emprunts contractés pour l'acquisition ou la construction de l'habitation principale
    f7vy = IntCol()
    f7vz = IntCol()
    f7vx = IntCol()
    f7vw = IntCol()

    # Dépenses d'accueil dans un établissement pour personnes âgées dépendantes
    f7cd = IntCol()
    f7ce = IntCol()

    # Frais de garde des enfants de moins de 6 ans
    f7ga = IntCol()
    f7gb = IntCol()
    f7gc = IntCol()
    f7ge = IntCol()
    f7gf = IntCol()
    f7gg = IntCol()

    # Enfants à charge poursuivant leurs études
    f7ea = IntCol()
    f7eb = IntCol()
    f7ec = IntCol()
    f7ed = IntCol()
    f7ef = IntCol()
    f7eg = IntCol()

    # Intérêts des prêts étudiants
    f7td = IntCol()
    f7vo = IntCol()
    f7uk = IntCol()
    
    # Primes de survies, contrat d'épargne handicap
    f7gz = IntCol()
    
    # Prestations compensatoires
    f7wm = IntCol()
    f7wn = IntCol()
    f7wo = IntCol()
    f7wp = IntCol()
    
    # Dépenses en faveur de la qualité environnementale
    f7we = IntCol()
    f7wq = IntCol()
    f7wh = IntCol()
    f7wk = IntCol()
    f7wf = IntCol()
    
    # Dépenses en faveur de l'aide aux personnes
    f7wi = IntCol()
    f7wj = IntCol()
    f7wl = IntCol()
    
    # Revenus des professions non salariées
    frag_exon = IntCol() # (f5hn, f5in, f5jn)
    frag_impo = IntCol() # (f5ho, f5io, f5jo)    
    arag_exon = IntCol() # (f5hb, f5ib, f5jb)
    arag_impg = IntCol() # (f5hc, f5ic, f5jc)
    arag_defi = IntCol() # (f5hf, f5if, f5jf)
    nrag_exon = IntCol() # (f5hh, f5ih, f5jh)
    nrag_impg = IntCol() # (f5hi, f5ii, f5ji)
    nrag_defi = IntCol() # (f5hl, f5il, f5jl)
    nrag_ajag = IntCol() # (f5hm, f5im, f5jm)

    mbic_exon = IntCol() # (f5kn, f5ln, f5mn)
    abic_exon = IntCol() # (f5kb, f5lb, f5mb)
    nbic_exon = IntCol() # (f5kh, f5lh, f5mh)
    mbic_impv = IntCol() # (f5ko, f5lo, f5mo)
    mbic_imps = IntCol() # (f5kp, f5lp, f5mp)
    abic_impn = IntCol() # (f5kc, f5lc, f5mc)
    abic_imps = IntCol() # (f5kd, f5ld, f5md)
    nbic_impn = IntCol() # (f5ki, f5li, f5mi)
    nbic_imps = IntCol() # (f5kj, f5lj, f5mj)
    abic_defn = IntCol() # (f5kf, f5lf, f5mf)
    abic_defs = IntCol() # (f5kg, f5lg, f5mg)
    nbic_defn = IntCol() # (f5kl, f5ll, f5ml)
    nbic_defs = IntCol() # (f5km, f5lm, f5mm)
    nbic_apch = IntCol() # (f5ks, f5ls, f5ms)

    macc_exon = IntCol() # (f5nn, f5on, f5pn)
    aacc_exon = IntCol() # (f5nb, f5ob, f5pb)
    nacc_exon = IntCol() # (f5nh, f5oh, f5ph)
    macc_impv = IntCol() # (f5no, f5oo, f5po)
    macc_imps = IntCol() # (f5np, f5op, f5pp)
    aacc_impn = IntCol() # (f5nc, f5oc, f5pc)
    aacc_imps = IntCol() # (f5nd, f5od, f5pd)
    aacc_defn = IntCol() # (f5nf, f5of, f5pf)
    aacc_defs = IntCol() # (f5ng, f5og, f5pg)
    nacc_impn = IntCol() # (f5ni, f5oi, f5pi)
    nacc_imps = IntCol() # (f5nj, f5oj, f5pj)
    nacc_defn = IntCol() # (f5nl, f5ol, f5pl)
    nacc_defs = IntCol() # (f5nm, f5om, f5pm)
    mncn_impo = IntCol() # (f5ku, f5lu, f5mu)
    cncn_bene = IntCol() # (f5sn, f5ns, f5os)
    cncn_defi = IntCol() # (f5sp, f5nu, f5ou, f5sr)

    mbnc_exon = IntCol() # (f5hp, f5ip, f5jp)
    abnc_exon = IntCol() # (f5qb, f5rb, f5sb)
    nbnc_exon = IntCol() # (f5qh, f5rh, f5sh)
    mbnc_impo = IntCol() # (f5hq, f5iq, f5jq)
    abnc_impo = IntCol() # (f5qc, f5rc, f5sc)
    abnc_defi = IntCol() # (f5qe, f5re, f5se)
    nbnc_impo = IntCol() # (f5qi, f5ri, f5si)
    nbnc_defi = IntCol() # (f5qk, f5rk, f5sk)

    mbic_mvct = IntCol() # (f5hu)
    macc_mvct = IntCol() # (f5iu)
    mncn_mvct = IntCol() # (f5ju)
    mbnc_mvct = IntCol() # (f5kz)

    frag_pvct = IntCol() # (f5hw, f5iw, f5jw)
    mbic_pvct = IntCol() # (f5kx, f5lx, f5mx)
    macc_pvct = IntCol() # (f5nx, f5ox, f5px)
    mbnc_pvct = IntCol() # (f5hv, f5iv, f5jv)
    mncn_pvct = IntCol() # (f5ky, f5ly, f5my)

    mbic_mvlt = IntCol() # (f5kr, f5lr, f5mr)
    macc_mvlt = IntCol() # (f5nr, f5or, f5pr)
    mncn_mvlt = IntCol() # (f5kw, f5lw, f5mw)
    mbnc_mvlt = IntCol() # (f5hs, f5is, f5js)

    frag_pvce = IntCol() # (f5hx, f5ix, f5jx)
    arag_pvce = IntCol() # (f5he, f5ie, f5je)
    nrag_pvce = IntCol() # (f5hk, f5ik, f5jk)
    mbic_pvce = IntCol() # (f5kq, f5lq, f5mq)
    abic_pvce = IntCol() # (f5ke, f5le, f5me)
    nbic_pvce = IntCol() # (f5kk, f5lk, f5mk)
    macc_pvce = IntCol() # (f5nq, f5oq, f5pq)
    aacc_pvce = IntCol() # (f5ne, f5oe, f5pe)
    nacc_pvce = IntCol() # (f5nk, f5ok, f5pk)
    mncn_pvce = IntCol() # (f5kv, f5lv, f5mv)
    cncn_pvce = IntCol() # (f5so, f5nt, f5ot)
    mbnc_pvce = IntCol() # (f5hr, f5ir, f5jr)
    abnc_pvce = IntCol() # (f5qd, f5rd, f5sd)
    nbnc_pvce = IntCol() # (f5qj, f5rj, f5sj)

# pfam only
    inactif   = BoolCol()
    partiel1  = BoolCol()
    partiel2  = BoolCol() 
    categ_inv = IntCol()
    opt_colca = BoolCol()
    empl_dir  = BoolCol() 
    ass_mat   = BoolCol()
    gar_dom   = BoolCol()

    # to remove
    wprm = FloatCol()
    etr = IntCol()     
    charges_deduc = IntCol()
    reductions = IntCol()
    rfr_cd = IntCol()
    coloc = BoolCol()
    csg_taux_plein = IntCol(default = 1)
    aer = IntCol()
    ass = IntCol()
#    birth = DateCol()
    f5sq = IntCol()