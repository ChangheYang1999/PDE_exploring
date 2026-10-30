import sys, json, time; sys.path.insert(0,'RUN_ROOT/numerics_N1N2/numerics/lib')
import ipm_exact as X, ipm_opt as OPT, ipm_farpart as FP
d2 = json.load(open('external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json'))
c = X.Q(d2['cl']) if isinstance(d2['cl'], str) else X.Q(float(d2['cl']))
gens = [{'m': g['m'], 'j': g['j'], 'spec': g['spec'], 'coef': g['coef']} for g in d2['generators']]
t=time.time(); terms = X.generators_to_terms(c, gens); print('d2 terms', len(terms), time.time()-t, flush=True)
t=time.time(); rep = OPT.sector_report(c, terms, qmax=2); print('sector time', time.time()-t, flush=True)
for r in rep['rows'][:14]: print(f"  exp {r['exponent']:+.4f} {r['status']:14s} maxharm {r['max_harmonic']:3d} quarter {r['quarter_L2']:.6e} full {r['full_circle_L2']:.6e}", flush=True)
t=time.time(); far = FP.report_far(c, terms, 1e4, qmax=4); print('far part d2 beyond 1e4:', far, time.time()-t, flush=True)
print('sqrt rF2_far =', far['rF2_far']**0.5 if far['rF2_far'] else None, ' (analysis2 quoted far part ~1.70e3 for ||rF||_2)', flush=True)
print('sqrt F2_far =', far['F2_far']**0.5 if far['F2_far'] else None, flush=True)
