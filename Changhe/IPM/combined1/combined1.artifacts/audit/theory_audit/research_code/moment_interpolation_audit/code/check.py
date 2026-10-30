from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,time,sys
from flint import arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];ctx.prec=768
hash=lambda p:sha256(p.read_bytes()).hexdigest()
ar=lambda q:arb(q.numerator)/q.denominator

def main():
 start=time.monotonic();mp=json.loads((B/'data/manifest.json').read_text());inputs={}
 for p,v in mp['sources'].items():assert hash(B/p)==v['sha256'];inputs[p]=v['sha256']
 c=Q(4076476460239181,2251799813685248);d=1-1/c;q=1/c-4;theta=d/(d+2)
 assert d==-q-3 and d>0 and 0<theta<1 and -2*theta+d*(1-theta)==0
 # Eliminate a^(d+2)=4H/(sqrt(pi) beta). The two constants are 1/2 and 1/d.
 assert Q(1,2)+1/d==(d+2)/(2*d)
 assert 2/(d+2)==1-theta
 C=ar((d+2)/(2*d))*arb.pi()**ar(theta/2)*arb(4)**ar(1-theta)
 rows=[];peer=json.loads((B/'source/review_results.json').read_text())
 for num in [7,13,14]:
  name=f'{num:03d}';raw=json.loads((B/'data'/f'{name}_endpoint.json').read_text())
  assert Q(raw['c'])==c
  dec=lambda key:{int(n):Q(v) for n,v in raw[key].items()}
  A,P=dec('F12'),dec('P');dot=lambda a,b:sum((v*b.get(n,Q(0)) for n,v in a.items()),Q(0))
  pp=dot(P,P);ap=dot(A,P);aa=dot(A,A);lam=ap/pp
  assert pp>0 and lam==Q(raw['lambda'])
  residual={n:A.get(n,Q(0))-lam*P.get(n,Q(0)) for n in set(A)|set(P)}
  assert dot(residual,P)==0 and dot(residual,residual)==aa-ap*ap/pp>0
  m=-arb.pi()*ar(lam);norm=(arb.pi()*ar(aa)).sqrt();orth=(arb.pi()*ar(dot(residual,residual))).sqrt()
  assert m>98306 and m<98308
  pd=peer['C']['endpoint'][name]
  float_matches={key:abs(float(value)-pd[key])<1e-8 for key,value in [('mstar',m),('norm_A',norm),('norm_A_perp_d',orth)]}
  assert all(float_matches.values())
  lower_bounds={}
  for label,beta in [('scalar_rounded_ceiling',Q(3793,10**9)),('original_graded_ceiling',Q(25,54684))]:
   Hmin=(m/(C*ar(beta)**ar(theta)))**ar(1/(1-theta));lower_bounds[label]={'beta_exact':str(beta),'H_lower_for_minimizing_moment':Hmin.str(100)}
  rows.append({'candidate':num,'lambda_exact':str(lam),'mstar':m.str(100),'norm_A':norm.str(100),'norm_A_perp':orth.str(100),'orthogonality_exact':True,'FLOAT_peer_values_agree':float_matches,'conditional_H_bounds':lower_bounds})
 for p in [Path(__file__),B/'PROOF.md',B/'data/manifest.json']:inputs[str(p)]=hash(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'q_exact':str(q),'d_exact':str(d),'theta_exact':str(theta),'theta':ar(theta).str(100),'Csplit':C.str(100),'rows':rows,'inputs':inputs,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED interpolation and exponent optimality; exact endpoint projection. FLOAT bump costs not certified; complete annular residual comparison OPEN'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['theta'],out['Csplit'],out['elapsed_seconds'])
if __name__=='__main__':main()
