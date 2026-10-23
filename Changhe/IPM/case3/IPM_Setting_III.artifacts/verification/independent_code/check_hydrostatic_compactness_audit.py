from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
root=Path('research/hydrostatic_compactness_audit');v=root/'verification'
source=Path('evidence/q_exact_jets/R1_SUMMARY.json');d=json.loads(source.read_text());rows=[]
for N in [64,96,128,160,192]:
 r=next(r for r in d['rows']if r['tag']==f'R1C_CL3P0_N{N}');a=r['a'];b=r['physical_cubics']['b'];e=r['physical_cubics']['e'];length=(a/10)**1.5
 B=b/length**2;E=e/(a*length**2);assert abs(length**(2/3)*10/a-1)<5e-16
 rows.append(dict(N=N,a=a,dilation_length=length,B=B,E=E))
with mp.workdps(60):
 constants=[]
 for gamma in [mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4]:
  a=2**(2-gamma)*mp.gamma(gamma)*mp.gamma((3-gamma)/2)/mp.sqrt(mp.pi)
  b=2*mp.gamma(2-gamma)*mp.gamma(gamma)/mp.gamma(1-gamma/2)
  assert abs(a-b)<mp.mpf('1e-55')
  constant=-2*mp.beta(gamma,3-gamma)
  # Integer substitution removes the fractional endpoint singularity for these rational gammas.
  ref=-8*mp.quad(lambda u:u**(4*gamma-1)/(1+u**4)**3,[0,1,mp.inf])
  assert abs(ref-constant)<mp.mpf('1e-50');constants.append(dict(gamma=str(gamma),gaussian_constant=mp.nstr(-a,30),rational_constant=mp.nstr(constant,30),quadrature_difference=mp.nstr(abs(ref-constant),5)))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=11,recomputed_gauge_rows=rows,constants=constants,halfwidths_and_box_status='OPEN: producer values only in this initial audit',manifest={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [root/'PROOF.md',source,Path(__file__),*v.glob('initial_*.txt')]})
(v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
