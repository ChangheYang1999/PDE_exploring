"""Lead's own reading of prediction P (analysis 14.6), not the verifier's test. The trial's density everywhere, the
velocity by the lead's modal inverse on r <= Rinv L with the two-term exterior beyond (formula continued to Rinv L).
Signed R/N_v on near-axis columns and at theta 0.818 at r = 1e3 ... 5e5 L, against the leading term q1 delta and the
third-order series of far2.py. The fields file is deleted afterwards.
usage (from work/c7): python3 ../far/ptest.py <shape.npz> <nr> <nt> <Rinv_in_L> <out.json>"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.getcwd())
from diagnose import diagnostic
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import far2

shape, nr, nt, Rinv, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
fields = out.replace('.json', '_fields.npz')
res = diagnostic(shape, nr, nt, Rinv, export=fields, tail="two-term")
z = np.load(fields)
r, th = z['r'], z['theta']; R = z['residual']; D = z['denominator']
cl_export = float(z['c_l'])
o = far2.coefficients(shape, 1 << 15)
k, L = o['k'], o['L']
rec = dict(shape=shape, nr=nr, nt=nt, Rinv_L=Rinv, cl_export=cl_export, cl_stored=o['cl'],
           drift_offset=(cl_export*k-1)/(1+k), columns=[])
nth = len(th)
for jt in [nth-2, nth-4, nth-10, int(np.argmin(np.abs(th-0.818)))]:
    t0 = float(th[jt]); i0 = int(np.argmin(np.abs(o['th']-t0)))
    q1, q2, qh, q3 = (float(o[n][i0]) for n in ('q1', 'q2', 'qh', 'q3'))
    col = dict(theta=t0, q1=q1, q2=q2, qh=qh, q3=q3, rows=[])
    print('column theta %.5f  q1 %+.5e' % (t0, q1))
    for rL in (1000, 4701, 9503, 3e4, 1e5, 3e5, 5e5, 1e6, 3e6):
        if rL > 0.9*Rinv: continue
        i = int(np.argmin(np.abs(r-rL*L))); ri = float(r[i]); d = ri**(k-1)
        meas = float(R[i, jt]/D[i, jt])
        lead = q1*d; ser = q1*d+q2*d*d+qh/ri**2+q3*d**3
        col['rows'].append(dict(r_L=ri/L, measured=meas, leading=lead, series=ser, ratio_leading=meas/lead, ratio_series=meas/ser))
        print('   r/L %9.0f  R/N_v %+.4e  leading %+.4e  series %+.4e  measured/leading %.4f  measured/series %.4f'
              % (ri/L, meas, lead, ser, meas/lead, meas/ser))
    rec['columns'].append(col)
print('c_l export %.12f  stored %.12f  drift offset in R/N_v %+.3e' % (cl_export, o['cl'], rec['drift_offset']))
json.dump(rec, open(out, 'w'), indent=1)
os.remove(fields)
