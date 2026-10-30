"""Full-plane weak probe integrals; no numerical quadrature."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib,argparse
from flint import fmpq,arb,arb_poly,fmpq_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import Radial,ar,pshift
from pipeline import source,load,digest,DATA
U=fmpq_poly([1,-1]); AU=arb_poly([1,-1]);T=fmpq_poly([0,1])

def ap(P):return arb_poly([ar(q) for q in P])
def integral(P,b):
 assert b>-1,str(b)
 return sum((v/ar(b+k+1) for k,v in enumerate(P)),arb(0))

def field_norm_sq(model,fields,p,k):
 total=arb(0);pairs=0;exponents=[]
 for field in fields:
  F,a,kind=model.fields[field];groups={}
  for (j,n),P in F.items():
   Q=pshift(P,2);groups.setdefault(n,[]).append((j,ap(Q(U))))
  for n,rows in groups.items():
   for i,(j,P) in enumerate(rows):
    for l in range(i,len(rows)):
     jj,Q=rows[l];b=a-model.p[j]-model.p[jj]+2*p-k-2
     assert k-a+4==1
     v=integral(AU*P*Q,b)
     total+=(2 if kind=='c' and n==0 else 1)*(1 if i==l else 2)*v
     pairs+=1;exponents.append(b)
 assert total>0,total
 return arb.pi()/2*total,{'pairs':pairs,'minimum_endpoint_exponent':str(min(exponents))}

def run(name,ps,bits):
 start=time.monotonic();ctx.prec=bits;path=source(name);model=Radial(path)
 D=load(name,0)[0,0]
 # Retain only the exact first angular mode, after checking its sine parity.
 rows=[]
 for (ell,kind,n),P in D.items():
  assert kind=='s'
  if n==1:rows.append((ell,ap((T*P)(U))))
 del D
 print('loaded',name,'first-mode branches',len(rows),'seconds',time.monotonic()-start,flush=True)
 boxes=[('FW-T-T4L2-sharp-v1',fmpq(1,7744),fmpq(147,200000),2**18),
        ('FW-T-T4L2-sharpw-v1',fmpq(1,5184),fmpq(1351,1000000),2**20),
        ('FW-T-T4L2-v1',fmpq(1,2**17),fmpq(1,2**14),2**18),
        ('FW-T-TB-sharp-v1',fmpq(1,8192),fmpq(43,50000),2**18),
        ('A2-D(b)',fmpq(1,2**18),fmpq(1,2**16),2**18)]
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'source_sha256':digest(path),
      'residual_sha256':digest(DATA/f'{name}_D0.json.gz'),'code_sha256':digest(Path(__file__)),'precision_bits':bits,'probes':[]}
 for p in ps:
  pairing=arb.pi()/2*sum((integral(P,ell*model.delta/2+p-3) for ell,P in rows),arb(0))
  N2=arb.pi()/ar(fmpq(2*(2*p-1)*(2*p-2)))
  A2=arb.pi()/2*integral(ap((T*((3*model.c+1)-2*model.c*p*T)**2)(U)),fmpq(2*p-3))
  B2,bmeta=field_norm_sq(model,['u1','u2'],p,0)
  C2,cmeta=field_norm_sq(model,['rho_x','rho_y'],p,1)
  N,A,B,C=[q.sqrt() for q in [N2,A2,B2,C2]];base=A+(1+2*p)*B+C
  results=[]
  for fw,s,r,w2 in boxes:
   m=ar(r)/arb(w2).sqrt();d=ar(r)/(4*arb.pi()*ar(s)*(1+ar(s))).sqrt()
   denom=base+d*N;upper=m*denom;gap=abs(pairing)-upper
   results.append({'framework':fw,'s_exact':str(s),'R_exact':str(r),'w2':w2,'m':m.str(80),'d':d.str(80),
                   'necessary_upper':upper.str(80),'gap':gap.str(80),'excluded':bool(gap>0),
                   'L2_correction_lower_at_d':(abs(pairing)/denom).str(80)})
  row={'p':p,'pairing':pairing.str(90),'N':N.str(80),'A':A.str(80),'B':B.str(80),'C':C.str(80),
       'denominator_without_d':base.str(80),'B_metadata':bmeta,'C_metadata':cmeta,'boxes':results}
  out['probes'].append(row);out['elapsed_seconds']=time.monotonic()-start
  dest=ROOT/f'research/weak_probe/verification/{name}_{bits}.json'
  dest.write_text(json.dumps(out,indent=2)+'\n')
  print('p',p,'pairing',pairing.str(18),'base',base.str(15),'all_excluded',all(q['excluded'] for q in results),
        'seconds',time.monotonic()-start,flush=True)
 print('complete',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--p',type=int,nargs='+',default=[2,3,4]);p.add_argument('--bits',type=int,default=1024)
 a=p.parse_args();assert all(i>=2 for i in a.p);run(a.candidate,a.p,a.bits)
