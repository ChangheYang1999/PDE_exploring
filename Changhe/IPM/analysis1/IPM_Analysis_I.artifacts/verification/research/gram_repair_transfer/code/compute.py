from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
from flint import arb,ctx
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/gram_repair_transfer';R=B/'research/gram_conforming_repair'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
def aq(x):x=F(x);return arb(x.numerator)/x.denominator
def frac(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(x):return [frac(x.lower()),frac(x.upper())]
def ceiling(x,p):return F(x.numerator*10**p//x.denominator+1,10**p)
v=json.loads((R/'evidence/verdict.json').read_text());check(sha(R/'evidence/verdict.json')=='7b6791c636849601648b92cdf5d0fecb63f9bb920d8c646c4bc6d14dc30457d3','prior verdict');pins={}
for n,h in v['files'].items():check(sha(B/n)==h,'prior pin');pins[n]=h
summary=json.loads((R/'evidence/summary.json').read_text());records=[]
for row in summary['records']:
 N=row['independent_repaired_functions'];delta=F(row['public']['uniform_single_column_relative_broken_energy_upper']);check(N==row['M']*row['N'],'dimension');eta=(aq(N)*aq(delta)**2).sqrt();lo,hi=box(eta);gram=F(N)*(2*delta+delta**2);ep=ceiling(hi,21);gp=ceiling(gram,19);check(0<lo<=hi<ep and gram<gp,'strict outward')
 records.append({'M':row['M'],'N':N,'delta_exact':str(delta),'eta_squared_exact':str(N*delta**2),'eta_arb512':list(map(str,[lo,hi])),'eta_strict_public_upper':str(ep),'gram_perturbation_exact_upper':str(gram),'gram_strict_public_upper':str(gp),'eta_float_orientation':float(hi),'gram_float_orientation':float(gram)})
for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),R/'evidence/verdict.json',R/'evidence/summary.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ARB_SCALAR_CONSTANTS_FOR_CONDITIONAL_GRAM_TRANSFER','prior_pins_rechecked':len(v['files']),'records':records,'files':pins,'scope':'Exact scalar ceilings and general Hilbert-space theorem only; no Gram eigenvalue lower bound or operator transfer.'}
p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'records':records}))
