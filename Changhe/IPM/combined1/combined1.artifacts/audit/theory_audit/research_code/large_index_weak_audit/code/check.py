from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict
from functools import lru_cache
import importlib.util,hashlib,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parent
helper=R/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('t4_largeK_polar',helper)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
T,V=Poly([0,1]),Poly([1,-1]);Z=Poly([])
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ap(p):return arb_poly([f.ar(x) for x in p])
def add(d,k,p):d[k]=d.get(k,Z)+p
@lru_cache(None)
def base(btext,L):
 b=Q(btext);assert b>-1 and L>=0
 return arb(L+2).gamma()*f.ar(b+1).gamma()/f.ar(L+b+3).gamma()
def integral(P,b,L):
 m=base(str(b),L);v=arb(0)
 for j,p in enumerate(P):
  v+=p*m;m*=f.ar(Q(L+j+2)/(L+j+b+3))
 return v
def integrate_groups(groups,delta,offset,L):
 return sum((integral(P,offset+ell*delta/2,L) for ell,P in groups.items()),arb(0))
def angular_energy(fields):
 groups={};pairs=0
 for field in fields:
  modes=defaultdict(list)
  for (j,n),p in field.items():modes[n].append((j,ap(p)))
  for entries in modes.values():
   for i,(j,p) in enumerate(entries):
    for u in range(i,len(entries)):
     k,q=entries[u];ell=j+k+2
     groups[ell]=groups.get(ell,arb_poly([]))+p*q*(1 if i==u else 2);pairs+=1
 return groups,pairs
def maximum(K):
 v=Poly([0,1]);P=v*v*(-3+(2*K+4)*v)
 crit=Poly([-6,9*K+18,-(2*K+4)*(K+3)])
 assert (1-v)*P.derivative()-K*P==v*crit
 disc=3*(K+2)*(11*K+6);root=arb(disc).sqrt()
 roots=[((9*K+18)-root)/(2*(2*K+4)*(K+3)),((9*K+18)+root)/(2*(2*K+4)*(K+3))]
 assert all(0<x and x<1 for x in roots)
 caps=[abs(x*x*(1-x)**K*(-3+(2*K+4)*x)) for x in roots]
 x=f.ar(Q(2,K+2));caps.append(x*x*(1-x)**K);H=Q(2,K*K)
 assert all(x<f.ar(H) for x in caps)
 return H,{'polynomial_exact':[str(x) for x in crit],'v_roots':[x.str(80) for x in roots],'amplitudes':[x.str(80) for x in caps],'H_exact':str(H),'all_strict':True}
def main():
 ctx.prec=2048;start=time.monotonic();src=R/'taylor_projection/source/canonical007.json'
 c,delta,rho,stream=f.fields(json.loads(src.read_text()))
 peerresult=json.loads((B/'source/N4_result.json').read_text());peerrows={}
 for row in peerresult['rows']:
  p=B/'source'/Path(row['path']).name;assert sha(p)==row['sha256']
  d=json.loads(p.read_text());peerrows[d['K']]=d
 n1=json.loads((B/'source/N1_007_far_weak.json').read_text());n1rows={r['k']:r for r in n1['rows']}
 ownpairpath=R/'full_far_pairing/verification/result.json';ownpair=json.loads(ownpairpath.read_text());ownrows={r['K']:r for r in ownpair['rows']}
 assert sha(src) in ownpair['inputs'].values()
 Dr={(j,n):f.td(p,(j+1)*delta/2,1) for (j,n),p in rho.items()}
 Ds={(j,n):f.td(p,(j+1)*delta/2,2) for (j,n),p in stream.items()}
 def modes(K):
  g=(2*K+1)-(2*K+4)*T;out={(0,1):2*c+1+c*g}
  for (j,n),p in stream.items():
   add(out,(j+1,1+n),(Ds[j,n]-n*p*g)/2)
   m=1-n
   if m:add(out,(j+1,abs(m)),(1 if m>0 else -1)*(-Ds[j,n]-n*p*g)/2)
  return out
 M0=modes(0);temp=modes(1);M1={k:temp[k]-p for k,p in M0.items()}
 byn=defaultdict(list)
 for (ell,n),p in M0.items():byn[n].append((ell,ap(p),ap(M1[ell,n])))
 E0,E1,E2={},{},{};mpairs=0
 for entries in byn.values():
  for i,(j,p0,p1) in enumerate(entries):
   for u in range(i,len(entries)):
    k,q0,q1=entries[u];ell=j+k;mult=1 if i==u else 2
    for out,p in [(E0,p0*q0),(E1,p0*q1+p1*q0),(E2,p1*q1)]:out[ell]=out.get(ell,arb_poly([]))+mult*p
    mpairs+=1
 density={k:ap(p) for k,p in rho.items()};deriv={k:ap(p) for k,p in Dr.items()};Cs={};cpairs=0
 for (i,n),p in density.items():
  for (j,m),q in density.items():
   ac=2*(n==m)-(abs(n-m)==2)+(n+m==2)
   bc=2*(n==m)-(abs(n-m)==2)-(n+m==2)
   if ac or bc:
    ell=i+j+2;Cs[ell]=Cs.get(ell,arb_poly([]))+deriv[i,n]*deriv[j,m]*ac+p*q*(n*m*bc);cpairs+=1
 Bs,bpairs=angular_energy([{(j,n):n*p for (j,n),p in stream.items()},Ds])
 Cenvs,cepairs=angular_energy([{(j,n):n*p for (j,n),p in rho.items()},Dr])
 P0,P1={},{};ipairs=0
 for (j,n),p in density.items():
  for (ell,m),q in M0.items():
   if n!=m:continue
   key=j+1+ell
   P0[key]=P0.get(key,arb_poly([]))-p*ap(q)
   P1[key]=P1.get(key,arb_poly([]))-p*ap(M1[ell,m]);ipairs+=1
 print('BUILT','M',mpairs,'C',cpairs,'Benv',bpairs,'Cenv',cepairs,'parts',ipairs,'seconds',time.monotonic()-start,flush=True)
 rows=[]
 for K,peer in sorted(peerrows.items()):
  tick=time.monotonic();L=2*K
  Ms={ell:E0[ell]+K*E1[ell]+K*K*E2[ell] for ell in E0}
  M2=arb.pi()/2*integrate_groups(Ms,delta,1,L)
  C2=arb.pi()/8*integrate_groups(Cs,delta,1,L)
  I=-arb(0)+arb.pi()/2*integrate_groups({ell:P0[ell]+K*P1[ell] for ell in P0},delta,-1,K)
  weight=ap(5+(2*K-4)*V)
  Benv2=arb.pi()/2*integrate_groups({ell:p*weight*weight for ell,p in Bs.items()},delta,1,L)
  Cenv2=arb.pi()/2*integrate_groups(Cenvs,delta,1,L)
  lin=ap((2*c+1)+c*((2*K+1)-(2*K+4)*T))
  A2=arb.pi()/2*integral(lin*lin,Q(1),L)
  energies=[M2,C2,Benv2,Cenv2,A2]
  assert all(x>0 and x.rel_accuracy_bits()>150 for x in energies)
  assert abs(I)>0 and I.rel_accuracy_bits()>150
  M,C=M2.sqrt(),C2.sqrt();D=M+C;H,sup=maximum(K)
  radius=2*abs(I)/(D+(D*D+4*f.ar(H)*abs(I)).sqrt())
  values={'pairing':I,'pairing_t_endpoint':I,'pairing_by_parts':I,'M2':M2,'M2_t_endpoint':M2,'C2':C2,'C2_t_endpoint':C2,'M':M,'C':C,'D':D,'radius':radius,'A2':A2,'A':A2.sqrt(),'Benv2':Benv2,'Benv':Benv2.sqrt(),'Cenv2':Cenv2,'Cenv':Cenv2.sqrt()}
  checks={key:value.overlaps(arb(peer[key])) for key,value in values.items()}
  checks['own_full_residual_direct']=I.overlaps(arb(ownrows[K]['I_direct']))
  checks['own_full_residual_parts']=I.overlaps(arb(ownrows[K]['I_parts']))
  assert all(checks.values()),(K,checks)
  assert H==Q(peer['H_upper_exact']) and f.ar(Q(peer['strict_lower_exact']))<radius
  assert M<values['A']+values['Benv'] and C<values['Cenv']
  comparisons={}
  if K in n1rows:
   for key,oldkey in [('Benv','B_k_est'),('Cenv','C_k_est')]:
    z=values[key];estimate=Q(*float(n1rows[K][oldkey]).as_integer_ratio());ratio=f.ar(estimate)/z;err=abs(f.ar(estimate)-z)/z
    old=peer['N1_matching_envelope_comparisons'][key]
    assert ratio.overlaps(arb(old['estimate_over_full'])) and err.overlaps(arb(old['absolute_relative_error']))
    comparisons[key]={'estimate_exact_binary64':str(estimate),'estimate_over_full':ratio.str(100),'absolute_relative_error':err.str(100),'strictly_below_full':bool(ratio<1),'strictly_above_full':bool(ratio>1)}
  row={'K':K,**{k:v.str(100) for k,v in values.items()},'checks':checks,'gradient_certificate':sup,'strict_lower_exact':peer['strict_lower_exact'],'strict_floor_verified':True,'minimum_energy_accuracy_bits':min(x.rel_accuracy_bits() for x in energies),'N1_matching_envelope_comparisons':comparisons,'elapsed_seconds':time.monotonic()-tick}
  rows.append(row);print('K',K,'I',I.str(20),'M',M.str(20),'C',C.str(20),'radius',radius.str(25),'seconds',row['elapsed_seconds'],flush=True)
 paths=[src,helper,Path(__file__),B/'PROOF.md',ownpairpath,R/'full_far_pairing/PROOF.md',R/'full_far_pairing/code/check.py',*sorted((B/'source').iterdir())]
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in paths if p.is_file()},'method':'Independent polar angular products and whole-plane Beta recurrence; matched polar norm envelopes','precision_bits':ctx.prec,'pair_counts':{'M':mpairs,'C':cpairs,'Benv':bpairs,'Cenv':cepairs,'I_parts':ipairs},'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED independent candidate-level reproduction of the finite N4-216 records'}
 with (B/'verification/result.json').open('x') as fobj:json.dump(out,fobj,indent=2);fobj.write('\n')
 print('DONE',out['utc'],'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
