from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/modal_graph_scaling'
def check(q,t):
 if not q:raise ValueError(t)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def hx(s):return F.from_float(float.fromhex(s))
def ih(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('+-');m,e=s.split('p');whole,tail=m[2:].split('.');return sign*F(int(whole+tail,16),16**len(tail))*F(2)**int(e)
def aa(q):return arb(q.numerator)/q.denominator
def ii(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def af(a):n,e=a.man_exp();return F(int(n))*F(2)**int(e)
def mf(a):sg,m,e,bc=a;return (-1 if sg else 1)*F(m)*F(2)**e
def rr(q):return str(q.numerator)+'/'+str(q.denominator)
raw=json.loads((B/'data_exact/modal_v2.json').read_text());M=raw['arrays']['D']['shape'][0];check(raw['arrays']['D']['shape']==[260,7],'shape');strings=[raw['scalars_hex']['k'],raw['arrays']['knots']['hex'][0],raw['arrays']['D']['hex'][(M-1)*7]];k,t,d=map(hx,strings);ki,ti,di=map(ih,strings);check((k,t,d)==(ki,ti,di),'independent exact decoders');check(d>0 and 0<k<F(1,2),'signs');c=3/k-1;ci=3/ki-1
# Method A: epsilon-Eepsilon on a homogeneous degree-five term.
old=F(json.loads((B/'research/center_obstruction/evidence/exact_modes.json').read_text())['linear_residual5_before_exp_minus_2ta'][str(2*M+3)]);pref=(1-5)*old;check(pref==-c*(M-2)*d/2,'exact inherited source formula')
# Method B: build K5 first, then apply the explicit linear center transport.
nu=2*M+1;K5highest=F(-4,8)*di;direct=ci*F(nu-5,2)*K5highest;check(pref==direct,'direct K transport coefficient')
ctx.prec=512;iv.dps=180
ba=aa(pref)*(-2*aa(t)).exp();bi=ii(direct)/(iv.exp(ii(ti))**2);alo,ahi=af(ba.lower()),af(ba.upper());ilo,ihi=map(mf,bi._mpi_);lower,upper=F('-0.000000000024'),F('-0.000000000020');check(lower<alo<=ahi<upper,'Arb strict bracket');check(lower<ilo<=ihi<upper,'iv strict bracket');check(max(alo,ilo)<=min(ahi,ihi),'independent overlap only supplementary')
files={}
for dep in ['research/center_obstruction/evidence/verdict.json','research/modal_graph_scaling/evidence/independent.json']:
 a=json.loads((B/dep).read_text())
 for n,h in a['files'].items():check(sha(B/n)==h,'dependency');check(n not in files or files[n]==h,'pin conflict');files[n]=h
 files[dep]=sha(B/dep)
for p in [D/'PROOF.md',D/'ADDENDUM.md',D/'NONZERO_IMAGE.md',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_EXACT_SCALING_IMAGE_COEFFICIENT_DERIVATIONS_ARB512_AND_IV180','frequency':2*M+3,'radial_degree':5,'coefficient_before_exp_minus_2t':rr(pref),'arb_exact_enclosure':[rr(alo),rr(ahi)],'iv_exact_enclosure':[rr(ilo),rr(ihi)],'strict_public_bracket':[rr(lower),rr(upper)],'actual_image_nonzero_requires':'NONZERO_IMAGE.md and inherited differentiated uniform center remainder theorem','files':files,'scope':'A single exact leading Fourier coefficient and analytic nonzero-image consequence, not an image norm bound or numerical inverse constant.'};p=D/'evidence/nonzero_image.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:out[n] for n in ['utc','status','frequency','radial_degree','strict_public_bracket']}))
