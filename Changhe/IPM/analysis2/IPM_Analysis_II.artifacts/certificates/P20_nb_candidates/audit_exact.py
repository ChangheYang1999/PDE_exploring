"""Independent N-B canonical, origin and tail audit; no producer imports."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,time,math
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0)
ctx.prec=512
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'13_algebraic_repair/verification'))
from audit_repair import clean,moments,audit_sectors,cosine,derivatives,add
ctx.prec=512

def run(source):
 start=time.monotonic();p=Path(source);raw=p.read_bytes();d=json.loads(raw);c=Q(d['cl']);g=1/c;delta=1-g
 assert c==Q(4076476460239181,2251799813685248)
 A={}
 for gen in d['generators']:
  j,m,s,v=gen['j'],gen['m'],gen['spec'],Q(gen['coef'])
  assert 0<=j<=5 and m>=0
  if s[0]=='mono': poly={s[1]:Q(1)}
  else:
   assert s[0]=='leg';w,n=s[1:]
   poly={w+h:Q((-1)**(n-h)*math.comb(n,h)*math.comb(n+h,h)) for h in range(n+1)}
  for h,b in poly.items():
   k=m+h;assert k>=m
   key=j,m,k;A[key]=A.get(key,Q(0))+v*b
 A=clean(A)
 center=Q(0);a0=Q(0)
 for (j,m,k),v in A.items():
  p_j=(3+g-j*delta)/2
  if k==0:strain=4*p_j*(p_j-1);slope=-16*p_j*(p_j-1)
  elif k==1 and m==0:strain=8*(p_j-1);slope=-32*(p_j-1)
  elif k==1 and m==1:strain=Q(0);slope=24*(p_j-1)
  elif k==2 and m==0:strain=Q(8);slope=Q(-32)
  elif k==2 and m==1:strain=Q(0);slope=Q(24)
  elif k==2 and m==2:strain=Q(-24);slope=Q(0)
  else:continue
  center+=v*strain;a0+=v*slope
 assert center+c==1 and a0>0
 print('canonical terms',len(A),'center normalized; a0',arb(str(a0)).str(20),flush=True)
 M=moments(A,c)
 orig=BASE/'source_audit/state131_exact.json';od=json.loads(orig.read_text())
 B={tuple(k):Q(v) for k,v in zip(od['canonical_order'],od['canonical_coefficients'])}
 OM=moments(B,c)
 assert M[0,0]==OM[0,0]
 assert all(not M[j,1] for j in (0,1))
 stationary=BASE/'10_tail_splice/verification/state131_splice.json';td=json.loads(stationary.read_text())
 C={int(n)-1:{int(m)//2:Q(v) for m,v in x['cosine_coefficients'].items()} for n,x in td['homogeneous_potential_orders'].items()}
 assert all(M[j,0]==clean(C[j]) for j in range(6))
 prim={k:v for k,v in M.items() if k[1]==0 or k[0]<=1}
 rows=audit_sectors(prim,c)
 assert all(row['zero'] for row in rows if (row['h'],row['q'])!=(6,0))
 assert g-6*delta < -2
 serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(A.items()))+'\n'
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED exact admissibility; coercivity and size OPEN','candidate':p.name,'source_sha256':hashlib.sha256(raw).hexdigest(),'canonical_sha256':hashlib.sha256(serial.encode()).hexdigest(),'generator_count':len(d['generators']),'canonical_count':len(A),'precision_bits':ctx.prec,'cl':str(c),'origin_strain':str(center),'origin_slope':str(a0),'origin_slope_ball':arb(str(a0)).str(60),'original_leading_potential_equal':True,'leading_six_potential_branches_equal_stationary':True,'first_descendant_branches_zero':[0,1],'residual_sectors':rows,'residual_decay_exponent':str(g-6*delta),'canonical_order':[list(k) for k in sorted(A)],'canonical_coefficients':[str(A[k]) for k in sorted(A)],'dependencies':{str(v.relative_to(BASE)):hashlib.sha256(v.read_bytes()).hexdigest() for v in [orig,stationary,BASE/'13_algebraic_repair/verification/audit_repair.py',HERE.parent/'PROOF.md']},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
 dest=HERE/p.stem;dest.with_suffix('.input.json').write_bytes(raw);dest.with_suffix('.audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',p.name,'seconds',out['seconds'],flush=True)
if __name__=='__main__':
 for source in sys.argv[1:]:run(source)
