from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
import json,math,struct
from mpmath import iv
ROOT=Path(__file__).resolve().parents[1];ctx.prec=320;iv.dps=100
full=json.loads((ROOT/'sources/full_g4.json').read_text());l4=json.loads((ROOT/'sources/lobe_g4.json').read_text());l6=json.loads((ROOT/'sources/lobe_g6.json').read_text())
assert l4['piece']==l6['piece']==[625,965] and l4['t_range']==l6['t_range']
assert l4['g']==4 and l6['g']==6 and full['piece']==[0,1918]
names=['K = rho~ - X.grad rho~','eps~','eps~ - X.grad eps~','rho~']
def independent_q(x):
 b=int.from_bytes(struct.pack('>d',x),'big');sign=b>>63;e=b>>52&2047;m=b&((1<<52)-1);assert e!=2047
 n=m if e==0 else m+(1<<52);a=-1074 if e==0 else e-1075;n=-n if sign else n
 return n*(1<<max(a,0)),1<<max(-a,0)
def exact_arb(q):return arb(q.numerator)/q.denominator
def exact_iv(q):return iv.mpf(q.numerator)/q.denominator
out=[]
for name in names+['ratio K/F']:
 if name=='ratio K/F':q=F(full['norm2'][names[0]]['all'])/F(full['norm2'][names[2]]['all'])
 else:q=F(full['norm2'][name]['all']);n,d=independent_q(full['norm2'][name]['all']);assert q==F(n,d)
 assert q>0
 A=exact_arb(q).sqrt();I=iv.sqrt(exact_iv(q));n=math.floor(math.sqrt(float(q))*10**8)
 low=F(n-1,10**8);high=F(n+2,10**8)
 assert 0<=low<=high and low*low<=q<=high*high
 assert A>exact_arb(low) and A<exact_arb(high)
 assert bool(I>exact_iv(low)) and bool(I<exact_iv(high))
 out.append({'name':name,'square_input':str(q),'window':[str(low),str(high)],'arb':str(A),'iv':str(I),'exact_square_check':True})
changes=[]
for name in names:
 a=F(l4['norm2'][name]['all']);b=F(l6['norm2'][name]['all']);assert a>0
 # Independently use the direct integer cross-product formula.
 an,ad=independent_q(l4['norm2'][name]['all']);bn,bd=independent_q(l6['norm2'][name]['all'])
 relative=abs(b-a)/a;assert relative==F(abs(bn*ad-an*bd),bd*an)
 changes.append({'name':name,'relative_squared_norm_change':str(relative),'approx':float(relative)})
f=names[2];den=F(l4['norm2'][f]['all'])
shares=[str(F(p)/den) for p in l4['parts_norm2'][f]['all']]
res={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_LITERAL_SCALARS_ONLY','square_root_windows':out,'lobe_squared_norm_changes':changes,'lobe_F_part_shares_exact':shares,'lobe_F_part_shares_approx':[float(F(v)) for v in shares],'omitted_radial_regions':['0<r<1e-4','r>1e7'],'scope':'Literal positive saved scalars; not an integral or physical norm certificate.'}
(ROOT/'evidence/scalars.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
