from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,time,re
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];t=time.monotonic();ctx.prec=256
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for path,h in m['inputs'].items():assert sha(B/path)==h,path
p=json.loads((B/'data/parameters.json').read_text());text=(B/'source/THEORY_FINAL.md').read_text()
assert len(text.splitlines())==1655
assert sha(B/'source/THEORY_FINAL.md')=='febf6c09e19a2e6b585c5263348250017d4af86fca9aa731db89fbc6d6106b40'
assert sha(B/'source/accepted_draft24.md')=='5a6419c1671826ff8486e27dbb7721a4a1b1819d8b836d6db3579875b1589e84'
assert len((B/'source/changes.diff').read_text().splitlines())==989
ceilings=list(map(Q,p['ceilings']));rows=[];checks=[]
def require(name,test,value=None):
 assert test,name
 checks.append({'claim':name,'value':str(value) if value is not None else None})
for line in text.splitlines():
 if not line.startswith('| '):continue
 v=[a.strip() for a in line.strip('|').split('|')]
 if len(v)!=6 or not re.match(r'^(?:d2|Mpen2|0\d\d)$',v[0]) or v[2]=='-':continue
 floor=Q(v[1].split()[0]);out=[]
 for k,c in enumerate(ceilings):
  ratio=floor/c;printed=Q(v[k+2]);require(v[0]+' ratio '+str(k),ratio>printed,ratio);out.append({'exact':str(ratio),'lower':str(printed)})
 rows.append({'candidate':v[0],'floor':str(floor),'ratios':out})
assert len(rows)==19,len(rows)
new=[]
for row in p['new_rows']:
 out=[]
 for c,lo in zip(ceilings,row['ratios']):
  ratio=Q(row['floor'])/c;require(row['candidate']+' new ratio '+lo,ratio>Q(lo),ratio);out.append({'exact':str(ratio),'lower':lo})
 new.append(dict(row,comparisons=out))
x={k:Q(v) for k,v in p['sharpw'].items()};assert x['s']==Q(1,72**2)
rate=x['mu']-x['C']*x['s']-x['cU']*x['r']*72
require('exact high rate',rate==Q(63092119,405000000),rate)
require('rounded high rate',rate>Q(1557,10000))
require('inverse display valid with exact rate',1/rate<Q('6.4226'),1/rate)
slack=x['r']-x['eta']/Q(1557,10000)
require('lower-rate self map slack',slack==Q(7,1557000000),slack)
require('exact-rate self map',x['r']-x['eta']/rate>0,x['r']-x['eta']/rate)
def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
cs=1/(2*(arb.pi()*ar(x['s'])*(1+ar(x['s']))).sqrt())
contraction=cs*ar(x['r'])/ar(x['betaL'])
require('contraction display',contraction<ar('0.0137200'),contraction)
b=(2*ar(x['mu'])/3)*(ar(x['mu'])/(3*ar(x['C']))).sqrt()/(ar(x['cU'])*ar(x['w2']).sqrt())
require('family upper bound',b<ar('0.0000028496'),b)
require('007 original ratio',ar('0.004769166867')/b>1673,ar('0.004769166867')/b)
C=Q(397)*Q(125,97)**3/1673**2
require('C exact identity',C==Q(775390625,2554506927217),C)
require('C display',C<Q('0.000304'))
require('fixed ball L2 radius',x['r']/1024==Q('0.0000013193359375'),x['r']/1024)
require('normalization preserved','c[h] = 0' in text)
require('zero-K case preserved','if K = 0 the majorant is linear' in text)
require('radial shape separated from cutoff','cutoff-radius form of the test and are necessary, not sufficient' in text)
require('explicit grad condition on comparison','for L0 <= R <= r_grad, independently of H, E, V and t' in text)
require('no existence claim','No exact solution near any candidate has been shown to exist.' in text)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-t,'precision_bits':ctx.prec,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'source_sha256':sha(B/'source/THEORY_FINAL.md'),'table_rows':len(rows),'table':rows,'new_rows':new,'check_count':len(checks),'checks':checks,'verdict':'CONFIRMED changed mathematical content under stated hypotheses; explicit status and quantifier repairs in PROOF.md','foreign_code_executed':False,'candidate_integrals_repeated':False}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print('PASS',r['check_count'],'checks;',len(rows),'table rows;',r['utc'],'elapsed',r['elapsed_s'])
