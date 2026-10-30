"""Complete radial annuli of the selected exact Laplacian angular band."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, sys, time
from flint import arb, arb_poly, fmpq as Q, fmpq_poly as Poly, ctx
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];D=R/'research/laplacian_radial_band'
NAME='C1-N1-007-d2w-j7-e2bal';MODES=list(range(17,32,2))
sys.path.insert(0,str(R/'research/whole_plane_norms/code'))
from pipeline import source,load
from norms import ar,T,U
ctx.prec=2048

def H(path):
 h=sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def new(path,data):
 with path.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
def now():return datetime.now(timezone.utc).isoformat()
def primitive(P,b,x):
 if not x:return arb(0)
 xx=ar(x);out=arb(0)
 for j in reversed(range(len(P))):out=out*xx+P[j]/ar(b+j+1)
 return (xx**ar(b+1))*out

def main():
 start=time.monotonic();fixture=arb_poly([1,-1]);a=primitive(fixture,Q(1,2),Q(1,4));b=primitive(fixture,Q(1,2),Q(1))
 assert a.overlaps(ar(Q(17,240))) and b.overlaps(ar(Q(4,15))) and (b-a).overlaps(ar(Q(47,240)))
 src=source(NAME);cache=R/f'research/whole_plane_norms/data/{NAME}_D0.json.gz';ass=R/f'research/whole_plane_norms/verification/{NAME}_assembly.json';check=json.loads(ass.read_text())
 assert H(src)=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
 assert check['source_sha256']==H(src) and check['polynomial_sha256']==H(cache)
 c=Q(json.loads(src.read_text())['cl']);delta=1-1/c
 fullpath=R/'research/candidate007_laplacian_fast/verification/full.json';full=json.loads(fullpath.read_text());assert full['complete'] and full['completed_modes']==list(range(1,320,2))
 fullE=arb(next(w['energy'] for w in full['weights'] if w['a']=='0'))
 peerpaths={n:R/f'research/candidate007_laplacian_fast/verification/modes/mode_{n:03d}.json' for n in MODES}
 assert all(H(p)==full['mode_record_sha256'][str(n)] for n,p in peerpaths.items())
 radii=[Q(0),Q(1,4),Q(1,2),Q(1),Q(2),Q(4),Q(8),Q(16),Q(32),Q(64),None]
 edges=[1/(1+r*r) if r is not None else Q(0) for r in radii]
 paths=[src,cache,ass,fullpath,Path(__file__),D/'PROOF.md',R/'research/whole_plane_norms/code/pipeline.py',R/'research/whole_plane_norms/code/norms.py',R/'research/radial_fourier/code/radial.py']+list(peerpaths.values())
 manifest={'candidate':NAME,'modes':MODES,'radius_edges':[str(r) if r is not None else 'infinity' for r in radii],'precision_bits':ctx.prec,'inputs':{str(p.relative_to(R)):H(p) for p in paths}}
 mp=D/'verification/manifest.json'
 if mp.exists():assert json.loads(mp.read_text())==manifest
 else:new(mp,manifest)
 F=load(NAME,0)[0,0];assert all(kind=='s' and n>0 and n%2 for ell,kind,n in F)
 print('loaded',len(F),'components',time.monotonic()-start,flush=True);records={}
 for n in MODES:
  dest=D/f'verification/mode_{n:03d}.json'
  if dest.exists():
   records[n]=json.loads(dest.read_text());assert records[n]['manifest_sha256']==H(mp);continue
  tick=time.monotonic();parts=[]
  for (ell,kind,nn),P in sorted(F.items()):
   if nn!=n:continue
   d=ell*delta/2
   def td(V):return (1-2*d*T)*V+2*T*U*V.derivative()
   L,rem=divmod(td(td(P))-n*n*P,T);assert not rem
   if not L:continue
   endpoint=L(U);q=next(i for i,z in enumerate(endpoint) if z);assert ell*delta+2*q-2>0
   parts.append((ell,q,arb_poly([ar(z) for z in list(endpoint)[q:]])))
  groups={};unit=arb_poly([1,-1])
  for i,(ell,q,P) in enumerate(parts):
   for j in range(i,len(parts)):
    ell2,q2,V=parts[j];b=(ell+ell2)*delta/2+q+q2-3;assert b>-1
    groups[b]=groups.get(b,arb_poly([]))+unit*P*V*(1 if i==j else 2)
  antiderivatives=[sum((primitive(P,b,x) for b,P in groups.items()),arb(0))*arb.pi()/2 for x in edges]
  energies=[antiderivatives[i]-antiderivatives[i+1] for i in range(len(edges)-1)]
  assert all(z>0 and z.rel_accuracy_bits()>100 for z in energies),(n,[(z.str(20),z.rel_accuracy_bits()) for z in energies])
  total=sum(energies,arb(0));peer=json.loads(peerpaths[n].read_text());pe=arb(next(w['energy'] for w in peer['weights'] if w['a']=='0'))
  assert total.overlaps(pe) and total.rel_accuracy_bits()>150
  rec={'utc':now(),'mode':n,'manifest_sha256':H(mp),'groups':len(groups),'annular_energies':[z.str(85) for z in energies],'total_energy':total.str(85),'previous_mode_overlap':True,'elapsed_seconds':time.monotonic()-tick}
  new(dest,rec);records[n]=rec;print('mode',n,'seconds',rec['elapsed_seconds'],flush=True)
 sums=[sum((arb(rec['annular_energies'][i]) for rec in records.values()),arb(0)) for i in range(len(edges)-1)];band=sum(sums,arb(0))
 out={'utc':now(),'candidate':NAME,'projection_modes':MODES,'complete_for_selected_modes':len(records)==len(MODES),'manifest_sha256':H(mp),'whole_plane_full_N0':fullE.sqrt().str(65),'band_energy':band.str(65),'band_fraction_of_full_energy':(band/fullE).str(65),'annuli':[{'r0':manifest['radius_edges'][i],'r1':manifest['radius_edges'][i+1],'selected_energy':z.str(65),'fraction_of_band':(z/band).str(65),'fraction_of_full_energy_lower':(z/fullE).str(65)} for i,z in enumerate(sums)],'mode_sha256':{str(n):H(D/f'verification/mode_{n:03d}.json') for n in MODES},'elapsed_seconds':time.monotonic()-start,'status':'N4-origin OPEN independent peer'}
 new(D/'verification/full.json',out);print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
