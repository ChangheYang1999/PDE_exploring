"""Exact synthetic-tail strain moments with Arb and mpmath.iv checks."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/x3_tail_fit_conditioning';ctx.prec=384;iv.dps=140
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def ff(v):
 need(type(v) is float and math.isfinite(v),'finite binary64 input');return F.from_float(v)
def aa(x):return arb(x.numerator)/arb(x.denominator)
def ii(x):return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def ep(t):
 s,m,e,b=t;need(b>=0,'finite iv endpoint');return (-1)**s*F(m)*F(2)**e
def result(q,av,ivv):
 lo,hi=F(str(av.lower().fmpq())),F(str(av.upper().fmpq()));il,ih=map(ep,ivv._mpi_);need(lo<=q<=hi and il<=q<=ih,'both engines contain exact rational');return {'exact':str(q),'arb':[str(lo),str(hi)],'iv':[str(il),str(ih)],'display':float(q)}
v=load(D/'evidence/diagnostic.json');c=load(D/'evidence/independent_check.json');pins=dict(c['files']);need(c['status']=='PASS_EXACT_LAST_SPAN_POLYNOMIAL_AND_FLOATING_SOURCE_DIAGNOSTIC','actual second representation check')
for n,h in pins.items():need(sha(B/n)==h,'input pin')
mom={};records=[];ar={};ivs={}
for rec in v['fits']:
 name=rec['name'];q=list(map(ff,rec['powers']));A=[ff(row[0]) for row in rec['fitted_coefficients']];need(all(y<0 for y in q),'integrable synthetic powers');m=sum((x/(-y) for x,y in zip(A,q)),F(0))/2;av=sum((aa(x)/(-aa(y)) for x,y in zip(A,q)),arb(0))/2;ivv=sum((ii(x)/(-ii(y)) for x,y in zip(A,q)),iv.mpf(0))/2;mom[name]=m;ar[name]=av;ivs[name]=ivv
 records.append({'name':name,'outer_radius_exact':str(ff(rec['outer_radius'])),'moment':result(m,av,ivv),'floating_evaluation_exact':str(ff(rec['fitted_exterior_c_moment'])),'floating_minus_exact':str(ff(rec['fitted_exterior_c_moment'])-m)})
need(len(records)==5,'five fits');R={r['name']:r['outer_radius_exact'] for r in records};changes=[];base=load(B/'research/x3_closure_diagnostics/sources/lead/base.json');ulp=ff(v['ulp_of_saved_c'])
for n in ['td05','td20','tp_lead']:
 need(R[n]==R['base'],'same exact outer radius');q=mom[n]-mom['base'];saved=load(B/'research/x3_closure_diagnostics/sources/lead'/f'{n}.json');delta=ff(saved['c'])-ff(base['c']);changes.append({'name':n,'synthetic_change':result(q,ar[n]-ar['base'],ivs[n]-ivs['base']),'saved_full_grid_c_change_exact':str(delta),'difference_synthetic_minus_saved_exact':str(q-delta),'synthetic_change_in_saved_c_ulps_exact':str(q/ulp)})
n='tp_none';q=-mom['base'];saved=load(B/'research/x3_closure_diagnostics/sources/lead/tp_none.json');delta=ff(saved['c'])-ff(base['c']);changes.append({'name':n,'synthetic_change':result(q,-ar['base'],-ivs['base']),'saved_full_grid_c_change_exact':str(delta),'difference_synthetic_minus_saved_exact':str(q-delta),'synthetic_change_in_saved_c_ulps_exact':str(q/ulp)})
for pp in [Path(__file__),D/'RECORDED_MOMENT_PROOF.md',D/'evidence/independent_check.json',D/'evidence/independent_check.log']:pins[str(pp.relative_to(B))]=sha(pp)
for n,h in pins.items():need(sha(B/n)==h,'unchanged pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SYNTHETIC_TAIL_MOMENTS_ONLY','moments':records,'same_radius_changes':changes,'exact_quantities':9,'interval_enclosures':18,'files':dict(sorted(pins.items())),'scope':'Exact synthetic-tail strain moments of recorded binary64 coefficients and powers only. No accuracy relative to true X3 source, error of the full-grid c, or IPM endpoint.'}
with (D/'evidence/moments.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'changes':[{ 'name':r['name'],'synthetic_change':r['synthetic_change']['display'],'saved_change':float(F(r['saved_full_grid_c_change_exact'])),'synthetic_minus_saved':float(F(r['difference_synthetic_minus_saved_exact'])),'synthetic_ulps':float(F(r['synthetic_change_in_saved_c_ulps_exact']))} for r in changes]},indent=2))
