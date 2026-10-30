"""Complete polar derivative moments, plus independent Laplacian identities."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/remaining_derivative_norms'
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from pipeline import load,source
from norms import ar,T,U

def H(p):
 h=sha256()
 with Path(p).open('rb') as s:
  for block in iter(lambda:s.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def new(p,obj):
 with p.open('x') as s:json.dump(obj,s,indent=2);s.write('\n')
def ball(row,low='norm_lower_ball',high='norm_upper_ball'):
 return arb(row[low]).union(arb(row[high]))

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--seconds',type=float,default=430);args=parser.parse_args()
 name='C1-N1-007-d2w-j7-e2bal';ctx.prec=2048;start=time.monotonic()
 src=source(name);cache=ROOT/f'research/whole_plane_norms/data/{name}_D0.json.gz'
 assembly=ROOT/f'research/whole_plane_norms/verification/{name}_assembly.json'
 assembled=json.loads(assembly.read_text());assert assembled['source_sha256']==H(src) and assembled['polynomial_sha256']==H(cache)
 peerpath=BASE/'source/N3_components.json';peer=json.loads(peerpath.read_text())
 sm=json.loads((BASE/'source/MANIFEST.json').read_text());assert H(peerpath)==sm['files']['N3_components.json']['sha256']
 auditpath=ROOT/f'research/candidate_audits/verification/{name}.json';audit=json.loads(auditpath.read_text())
 assert peer['source_sha256']==audit['generator_sha256'] and audit['canonical_sha256']==H(src)
 napath=ROOT/'research/candidate007_laplacian_fast/verification/N3_comparison_v01.json'
 gpath=ROOT/f'research/polar_derivative_norms/verification/{name}/full.json'
 delta=1-1/Q(json.loads(src.read_text())['cl']);F=load(name,0)[0,0]
 assert all(kind=='s' and n>0 and n%2 for ell,kind,n in F)
 modes=sorted({n for ell,kind,n in F});assert len(modes)==160 and modes==list(range(1,320,2))
 dest=BASE/'verification'/name;dest.mkdir(exist_ok=True);(dest/'modes').mkdir(exist_ok=True)
 paths=[src,cache,assembly,auditpath,peerpath,BASE/'source/MANIFEST.json',napath,gpath,Path(__file__),BASE/'PROOF.md',ROOT/'research/whole_plane_norms/code/pipeline.py',ROOT/'research/whole_plane_norms/code/norms.py',ROOT/'research/radial_fourier/code/radial.py']
 manifest={'candidate':name,'modes':modes,'components':len(F),'precision_bits':ctx.prec,'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths}}
 mp=dest/'manifest.json'
 if mp.exists():assert json.loads(mp.read_text())==manifest
 else:new(mp,manifest)
 mh=H(mp);unit=arb_poly([1,-1]);saved={};fresh=0
 print('loaded',len(F),'components',len(modes),'modes','seconds',time.monotonic()-start,flush=True)
 def form(E,ell):
  if not E:return None
  end=E(U);q=next(i for i,z in enumerate(end) if z)
  return ell,q,arb_poly([ar(z) for z in list(end)[q:]])
 def integrate(bucket,offset,power,multiplicities):
  groups={};ends=[]
  for part,rows0 in enumerate(bucket):
   rows=[r for r in rows0 if r is not None]
   for ell,q,P in rows:
    b=ell*delta+2*q+offset;assert b>-1
    ends.append({'part':part,'ell':ell,'q':q,'diagonal_exponent':str(b)})
   for i,(ell,q,P) in enumerate(rows):
    for j in range(i,len(rows)):
     ell2,q2,V=rows[j];b=(ell+ell2)*delta/2+q+q2+offset;assert b>-1
     prod=P*V*((1 if i==j else 2)*multiplicities[part])
     if power:prod*=unit**power
     groups[b]=groups.get(b,arb_poly([]))+prod
  energy=arb.pi()/2*sum((sum((z/ar(b+j+1) for j,z in enumerate(P)),arb(0)) for b,P in groups.items()),arb(0))
  assert energy>0 and energy.rel_accuracy_bits()>150
  return energy,ends,len(groups)
 for n in modes:
  p=dest/f'modes/mode_{n:03d}.json'
  if p.exists():
   r=json.loads(p.read_text());assert r['mode']==n and r['manifest_sha256']==mh;saved[n]=r;continue
  if time.monotonic()-start>=args.seconds:continue
  tick=time.monotonic();gradient=[[],[]];hessian=[[],[],[]];trace=[[]];identities=0
  for (ell,kind,nn),P in sorted(F.items()):
   if nn!=n:continue
   d=ell*delta/2
   def td(V):return (1-2*d*T)*V+2*T*U*V.derivative()
   TP=td(P);A=-2*d*TP+2*U*TP.derivative();B=n*(-2*d*P+2*U*P.derivative());C,rem=divmod(TP-n*n*P,T)
   assert not rem and T*(A+C)==td(TP)-n*n*P;identities+=1
   for bucket,V in zip(gradient,[TP,n*P]):bucket.append(form(V,ell))
   for bucket,V in zip(hessian,[A,B,C]):bucket.append(form(V,ell))
   trace[0].append(form(A+C,ell))
  rows={};endpoints={}
  for label,buckets,offset,power,multiplicities in [('D2',hessian,Q(-1),1,[1,2,1]),('rD2',hessian,Q(-2),2,[1,2,1]),('Pw1',gradient,Q(-9,5),0,[1,1]),('Delta',trace,Q(-1),1,[1])]:
   energy,ends,ngroups=integrate(buckets,offset,power,multiplicities)
   rows[label]={'energy_ball':energy.str(100),'norm_ball':energy.sqrt().str(90),'relative_accuracy_bits':energy.rel_accuracy_bits(),'groups':ngroups};endpoints[label]=ends
  assert arb(rows['D2']['energy_ball']).overlaps(arb(rows['Delta']['energy_ball']))
  rec={'utc':now(),'mode':n,'manifest_sha256':mh,'trace_identities':identities,'unweighted_hessian_laplacian_overlap':True,'norms':rows,'endpoints':endpoints,'elapsed_seconds':time.monotonic()-tick}
  new(p,rec);saved[n]=rec;fresh+=1
  print('mode',n,'seconds',rec['elapsed_seconds'],'total',time.monotonic()-start,flush=True)
 complete=len(saved)==len(modes);norms={}
 for label in ['D2','rD2','Pw1','Delta']:
  energy=sum((arb(r['norms'][label]['energy_ball']) for r in saved.values()),arb(0))
  norms[label]={'energy_ball':energy.str(100),'norm_ball':energy.sqrt().str(90),'complete':complete}
 out={'utc':now(),'candidate':name,'complete':complete,'source_sha256':H(src),'raw_source_sha256':audit['generator_sha256'],'manifest_sha256':mh,'completed_modes':sorted(saved),'missing_modes':[n for n in modes if n not in saved],'norms':norms,'mode_sha256':{str(n):H(dest/f'modes/mode_{n:03d}.json') for n in saved},'stage_elapsed_seconds':time.monotonic()-start,'status':'partial lower bounds only'}
 if complete:
  compare={label:arb(norms[label]['norm_ball']).overlaps(ball(peer['norms'][label],'norm_lower','norm_upper')) for label in ['D2','rD2','Pw1']};assert all(compare.values()),compare
  na=json.loads(napath.read_text());gr=json.loads(gpath.read_text());assert na['complete_modes']==160 and gr['complete']
  assert na['source_sha256']==audit['generator_sha256'] and gr['candidate']==name
  vals=[arb(r['own_norm']) for r in na['rows'] if Q(r['a'])==1];assert len(vals)==1
  G1=ball(gr['norms']['G1']);identity=vals[0]**2-arb(norms['D2']['energy_ball'])+2*G1**2
  assert identity>0 and identity.overlaps(arb(norms['rD2']['energy_ball']))
  out.update({'N3_norm_comparisons':compare,'weighted_identity_energy_ball':identity.str(100),'weighted_identity_overlap':True,'all_modal_unweighted_identities':all(r['unweighted_hessian_laplacian_overlap'] for r in saved.values()),'status':'complete independent polar integration agrees with N3 Cartesian intervals'})
  new(dest/'full.json',out)
 else:(dest/'progress.json').write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',len(saved),'/',len(modes),'complete',complete,'seconds',time.monotonic()-start,flush=True)
 for label,row in norms.items():print(label,row['norm_ball'][:65],flush=True)
if __name__=='__main__':main()
