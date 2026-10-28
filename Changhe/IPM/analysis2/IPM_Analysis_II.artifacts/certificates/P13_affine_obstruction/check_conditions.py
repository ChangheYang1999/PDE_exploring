from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json
from flint import arb,ctx
ctx.prec=384
BASE=Path(__file__).resolve().parents[2]
def aa(q):
 q=Q(q);return arb(q.numerator)/q.denominator
out=[]
for name in ['state088','state131','n12_m4','n12_m5','n12_m10','n12_m12']:
 if name.startswith('state'):
  d=json.loads((BASE/'source_audit'/f'{name}_exact.json').read_text());c=Q(d['exact_parameters']['cl']);q=2/c-1
  E=json.loads((BASE/'05_tails/verification'/f'{name}_tail.json').read_text()) if (BASE/'05_tails/verification'/f'{name}_tail.json').exists() else None
  norm=None
 else:
  d=json.loads((BASE/'08_refits/verification'/f'{name}_audit.json').read_text());c=Q(d['cl']);q=3/c-2
  row=next(s for s in d['residual_sectors'] if s['h']==2 and s['q']==0)
  coeff=[Q(x) for x in row['coefficients'].values()];assert any(coeff)
  norm=(arb.pi()*aa(sum((x*x for x in coeff),Q(0))/4)).sqrt() / aa(1-c*q)
 assert q>1/c-1 and c*q<1 and q>-1
 out.append({'name':name,'q':str(q),'q_decimal':aa(q).str(55),'gap_over_gamma_minus_one':str(q-(1/c-1)),
  'response_denominator':str(1-c*q),'required_correction_quarter_angular_norm':norm.str(55) if norm is not None else None,
  'excludes_bounded_corrections':q>0,'excludes_N_s_corrections':True})
p=Path(__file__).with_name('conditions.json')
p.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','conditions':out},indent=2)+'\n')
print(p.read_text())
