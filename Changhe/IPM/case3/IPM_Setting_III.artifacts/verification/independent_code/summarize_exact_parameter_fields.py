"""Summarize result164 without changing its literal field definitions."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
root=Path('research/exact_parameter_fields/verification')
src=root/'AUDIT.json'; d=json.loads(src.read_text()); assert d['status']=='COMPUTED'
mp.mp.dps=120
out={'utc':datetime.now(timezone.utc).isoformat(),'audit_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'proof_sha256':d['proof_sha256'],'manufactured':d['manufactured'],'rows':[]}
text=['# Exact exponent and normalization audit','',f"Written {out['utc']}. Independent finite-field comparisons; no profile or convergence claim.",'','A uses the literal saved binary exponent. B uses the same coefficients and exact alpha=3/10. C additionally changes four Chebyshev entries to impose c=1-ell and K=a exactly. All inputs are exact JSON; the canonical inverse is recomputed for each density.','', '| Size | Field | center defect | K-a | sampled max NF | sampled max NV | R at (6e249,8e249) |', '|---|---|---:|---:|---:|---:|---:|']
for case in d['cases']:
    fields={v['label']:v for v in case['fields']}
    ref=fields['A']['precision_rows'][-1]['points']
    for label,v in fields.items():
        pts=v['precision_rows'][-1]['points']
        nf=max((z['field'] for z in pts if z['field']['R_Nf'] is not None),key=lambda z:mp.mpf(z['R_Nf']))
        nv=max((z['field'] for z in pts if z['field']['R_Nv'] is not None),key=lambda z:mp.mpf(z['R_Nv']))
        precise=max(mp.mpf(z) for pt in v['precision_comparisons'] for z in pt.values())
        compact=[]
        for i,(a,b) in enumerate(zip(ref,pts)):
            if i>=6:continue
            compact.append({'point':case['points'][i],'delta_R':mp.nstr(mp.mpf(b['field']['R'])-mp.mpf(a['field']['R']),30),'delta_NF':None if a['field']['R_Nf'] is None else mp.nstr(mp.mpf(b['field']['R_Nf'])-mp.mpf(a['field']['R_Nf']),30)})
        row={'size':case['tag'],'field':label,'input':v['exact_input'],'input_sha256':v['exact_input_sha256'],'center_defect_exact':v['center_defect_exact'],'K_minus_a_exact':v['K_minus_a_exact'],'p_exact':v['p_exact'],'ell_p_minus_one_exact':v['ell_p_minus_one_exact'],'sampled_peak_Nf':nf,'sampled_peak_Nv':nv,'far_points':pts[-2:],'precision_error_scaled':str(precise),'compact_changes_from_A':compact}
        out['rows'].append(row)
        text.append('| '+case['tag'].split('_')[-1]+' | '+label+' | '+format(float(Fraction(v['center_defect_exact'])),'.4e')+' | '+format(float(Fraction(v['K_minus_a_exact'])),'.4e')+' | '+mp.nstr(mp.mpf(nf['R_Nf']),12)+' | '+mp.nstr(mp.mpf(nv['R_Nv']),12)+' | '+mp.nstr(mp.mpf(pts[-1]['field']['R']),9)+' |')
text+=['','Each row uses the same eight fixed points, including two N40 peak locations, two near-axis cancellation witnesses and the origin. These are selected-point maxima, not a new global grid search. In particular the N36 row is not its previous wide-grid maximum. The origin has zero R, Nf and Nv; its ratios are undefined, and it was retained explicitly.','',f"The exact projection and two independent canonical strain expressions passed {d['manufactured']['exact_checks']} rational checks in 100 manufactured cases. Two-precision comparisons use 75 and110 requested digits plus the previously validated radius/cancellation guard. No interval certification is claimed.",'','CONFIRMED: B/C have exact p=1/ell and absolutely decaying far residual O(r^(-1/5)); C also has exact center strain and K/a=1. Both preserve the original nonzero slope. Compact selected residuals change little. REFUTED: the literal exponent growth defect of A is an unavoidable obstacle to finite approximations. OPEN: optimizer stationarity, parameter/jet and domain convergence, and the SettingIII primary endpoint. Finite angular content still prevents these individual fields from being exact profiles.','', 'Absolute residuals, denominators, velocity and Cartesian derivatives, the two-term far comparison, all source hashes and exact coefficient changes are in AUDIT.json and the separate A/B/C JSON files.']
(root/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n');(root/'SUMMARY.md').write_text('\n'.join(text)+'\n')
print('\n'.join(text))
