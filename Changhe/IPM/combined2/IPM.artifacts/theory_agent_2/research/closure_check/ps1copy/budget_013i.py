# HF-Q budgets at P-S1 = (21/10, 1, 1/2): version 013i (theory_agent_1, 2026-11-03, for theory_v13): copy of budget_013h with
# one change, N in {0.0055546} (the Hermite upper N_(21/10) <= 0.0055545729 of AT-1431, replayed by numerical_audit exchange
# v317), at the forcing uppers 7.9613e-7 (AT-1413) and 1.2540e-6 (AT-1391); beta0 7/4 only.
# beta0 = beta_0* and b0 are stipulated numbers, not certified properties of any background.
import os, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "ps1"))
from ps1_tables import *
import ps1_tables
t0 = time.time()
P1 = Weight(1, Fr(1, 2), Fr(9619, 5000))
B0S = (Fr(55, 100), Fr(60, 100))
F2L = (Fr(79613, 10**11), Fr(12540, 10**10))
NS = (Fr(55546, 10**7),)
def row(b0, F2, ce):
    Rq = F2/beta0; R = A_(Rq); cells = []
    if ce: _, r1, r2 = P1.best_rhos(float(Rq), 0.3); cf = P1.cf_of(r1, r2); kfun = lambda M: P1.Kstar_f(float(Rq), M, cf)
    else: kfun = lambda M: float(P1.cWq)*M
    for N in NS:
        M, B, A = P1.search(b0, Rq, kfun, lambda P, M: M*(P - float(N)))
        Mr = H.rat3(M); cl = Mr > Fr(1, 2)
        if cl: Mr = Fr(1, 2)
        if ce: _, s1, s2 = P1.best_rhos(float(Rq), float(Mr)); Kb = P1.certify_K(Rq, Mr, s1, s2)
        else: Kb = P1.cWq*Mr
        Z = A_(Mr)*(P1.cap(b0, R, Kb, Mr, B, A) - A_(N)); D = Z/R**2
        if not Z > 0: cells.append("N %.7g: none (search maximum not positive)" % float(N)); continue
        cells.append("N %.7g: D %.3g, Z %.4g (M %s%s, B %s, Kbar/M %.5f)" % (float(N), float(H.lowdec(D, 3)),
                     float(H.lowdec(Z, 4)), float(Mr), " clamped" if cl else "", B, float(Kb/Mr)))
    return "b0 %s | ||F||_2 %.3g | " % (float(b0), float(F2)) + " | ".join(cells)
for beta0 in (Fr(175, 100),):
    ps1_tables.beta0 = beta0
    for ce, name in ((True, "Part CE: CE input (Theorem CE-G)"),):
        print("%s, beta0 = %s; D lower decimal; Z = D R^2 lower decimal" % (name, beta0))
        for b0 in B0S:
            for F2 in F2L: print(row(b0, F2, ce)); sys.stdout.flush()
print("done (%.1f s)" % (time.time() - t0))
