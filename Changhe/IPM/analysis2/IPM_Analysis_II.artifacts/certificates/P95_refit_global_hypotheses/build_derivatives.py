from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import json,sys,time
from flint import fmpq as Q
from build import recover,deriv,cheb,clean
here=Path(__file__).parent

def odd_factor(n,kind):
 C=cheb(n,'T')[1:] if kind=='c' else cheb(n-1,'U');out={}
 for h,a in enumerate(C):
  if not a:continue
  assert h%2==0
  for k in range(h//2+1):out[k]=out.get(k,Q(0))+a*Q(comb(h//2,k),2**(h//2))
 return clean(out)
def main(name):
 start=time.monotonic();c,coeff,src,sha,digest=recover(name);delta=1-1/c;out={};factors={}
 for label,axes,sign in [('u1','xyy',-1),('u2','xxy',1),('chi41','xxxxy',1),('chi32','xxxyy',1),('chi23','xxyyy',1),('chi14','xyyyy',1),('chi05','yyyyy',1)]:
  order=len(axes);shift=2 if order==3 else 3;factors[label]='cos' if axes.count('y')%2==0 else 'sin'
  for j in range(6):
   p=(3+1/c-j*delta)/2;D={('c',2*m,k):v for (jj,m,k),v in coeff.items() if jj==j}
   for d,ax in enumerate(axes):D=deriv(D,p,d,ax)
   P={}
   for (kind,n,k),v in D.items():
    assert n%2==1 and k>=shift and kind==('c' if factors[label]=='cos' else 's')
    for z,a in odd_factor(n,kind).items():P[k-shift,z]=P.get((k-shift,z),Q(0))+sign*v*a
   out[f'{label}_{j}']=[[i,k,str(v)] for (i,k),v in sorted(clean(P).items())]
  print(name,label,'done',time.monotonic()-start,flush=True)
 record={'utc':datetime.now(timezone.utc).isoformat(),'name':name,'cl':str(c),'delta':str(delta),'polynomials':out,'angular_factors':factors,'source':str(src),'source_sha256':sha,'canonical_sha256':digest,'proof_sha256':sha256((here.parent/'PROOF.md').read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
 (here/f'{name}.derivatives.json').write_text(json.dumps(record,indent=2)+'\n');print(record['utc'],'BUILT',record['seconds'],flush=True)
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'nb_d2_exact')
