"""Complete Q3 via symmetric polar tensor, with exact Cartesian fixtures."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
import argparse, json, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, arb_poly, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/polar_third_derivative'
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from pipeline import source,load
from norms import T,U,ar,weight_poly

def H(p):
 h=sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def new(p,o):
 with Path(p).open('x') as f:json.dump(o,f,indent=2);f.write('\n')
def td(p,d):return (1-2*d*T)*p+2*T*U*p.derivative()
def third(p,d,n):
 tp=td(p,d);a=-2*d*tp+2*U*tp.derivative();b=n*(-2*d*p+2*U*p.derivative());c,rem=divmod(tp-n*n*p,T)
 assert not rem
 aa,bb,cc,dd=td(a,d+1),td(b,d+1),td(c,d+1),n*c+2*b
 assert bb==n*a-2*b and cc==a-c-n*b
 return [aa,bb,cc,dd]
def fixtures():
 import sympy as sp
 x,y,z=sp.symbols('x y z',real=True);s=x*x+y*y;rows=[]
 for n in [1,3,7]:
  m=(n-1)//2;harm=sum((-1)**((k-1)//2)*comb(n,k)*x**(n-k)*y**k for k in range(1,n+1,2))
  for d in [4,5]:
   f=harm*(1+2*s*s)/(1+s)**(d+m+2)
   cart=[sp.diff(f,x,k,y,3-k) for k in range(4)]
   pol=third(T**m*(1-2*T+3*T*T),Q(d),n)
   for xx,yy in [(Q(1,2),Q(1,2)),(Q(3),Q(4))]:
    xxsp,yysp=sp.Rational(str(xx)),sp.Rational(str(yy));ss=xx*xx+yy*yy;t=ss/(1+ss);v=1/(1+ss)
    vals=[Q(str(p.subs({x:xxsp,y:yysp}))) for p in cart]
    zr,zi=Q(1),Q(0)
    for _ in range(n):zr,zi=zr*xx-zi*yy,zr*yy+zi*xx
    checks=[]
    for k in range(4):
     # rr..theta.. tensor contraction, k radial slots and3-k angular slots.
     co=Poly([yy,xx])**k*Poly([xx,-yy])**(3-k)
     lhs=sum((co[j]*vals[j] for j in range(4)),Q(0))*ss**((n-3)//2)
     index=3-k;trig=zi if index in [0,2] else zr
     rhs=v**(d+1)*pol[index](t)*trig
     assert lhs==rhs,(n,d,xx,yy,k,lhs,rhs)
     checks.append(True)
    direct=sum((Q(comb(3,j))*a*a for j,a in enumerate(vals)),Q(0))
    polar=v**(2*d+2)/ss**n*sum((Q(mult)*p(t)**2*(zi*zi if i in [0,2] else zr*zr) for i,(mult,p) in enumerate(zip([1,3,3,1],pol))),Q(0))
    assert direct==polar
    rows.append({'n':n,'d':d,'x':str(xx),'y':str(yy),'four_tensor_projections_exact':checks,'ordered_norm_exact':True})
 assert sum((z/Q(Q(1,2)+j+1) for j,z in enumerate(Poly([1,-1]))),Q(0))==Q(4,15)
 return rows

def main():
 parser=argparse.ArgumentParser();parser.add_argument('candidate');parser.add_argument('--seconds',type=float,default=430);args=parser.parse_args()
 start=time.monotonic();ctx.prec=2048
 manifest_source=BASE/'source/MANIFEST.json';sm=json.loads(manifest_source.read_text())
 for name,rec in sm['files'].items():assert H(BASE/'source'/name)==rec['sha256']
 if args.candidate!='state131':
  calibration=BASE/'verification/state131/full.json';cc=json.loads(calibration.read_text());assert cc['complete'] and cc['reference_overlap'] and cc['code_sha256']==H(__file__)
 else:calibration=None
 fixture_rows=fixtures();print('exactfixtures',len(fixture_rows),time.monotonic()-start,flush=True)
 src=source(args.candidate);cache=ROOT/f'research/whole_plane_norms/data/{args.candidate}_D0.json.gz';assembly=ROOT/f'research/whole_plane_norms/verification/{args.candidate}_assembly.json'
 ass=json.loads(assembly.read_text());assert ass['source_sha256']==H(src) and ass['polynomial_sha256']==H(cache)
 delta=1-1/Q(json.loads(src.read_text())['cl']);raw=load(args.candidate,0)[0,0]
 assert all(k=='s' and n>0 and n%2 for ell,k,n in raw)
 modes=sorted({n for ell,k,n in raw});outdir=BASE/'verification'/args.candidate;outdir.mkdir(exist_ok=True);(outdir/'modes').mkdir(exist_ok=True)
 paths=[src,cache,assembly,Path(__file__),BASE/'PROOF.md',manifest_source,ROOT/'research/whole_plane_norms/code/pipeline.py',ROOT/'research/whole_plane_norms/code/norms.py',ROOT/'research/radial_fourier/code/radial.py']
 if calibration:paths.append(calibration)
 manifest={'candidate':args.candidate,'modes':modes,'components':len(raw),'precision_bits':ctx.prec,'weight_degree':112,'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths}}
 mp=outdir/'manifest.json'
 if mp.exists():assert json.loads(mp.read_text())==manifest
 else:new(mp,manifest)
 mh=H(mp);w,eps=weight_poly(112);w=arb_poly([ar(q) for q in w]);saved={}
 print('loaded',len(raw),'components',len(modes),'modes',time.monotonic()-start,flush=True)
 for n in modes:
  path=outdir/f'modes/mode_{n:03d}.json'
  if path.exists():
   rec=json.loads(path.read_text());assert rec['manifest_sha256']==mh and rec['mode']==n;saved[n]=rec;continue
  if time.monotonic()-start>=args.seconds:continue
  tick=time.monotonic();parts=[[],[],[],[]];identities=0;endpoints=[]
  for (ell,kind,nn),p in sorted(raw.items()):
   if nn!=n:continue
   pol=third(p,ell*delta/2,n);identities+=2
   for i,e in enumerate(pol):
    if not e:continue
    end=e(U);q=next(k for k,z in enumerate(end) if z);b=ell*delta+2*q-Q(4,5);assert b>-1
    parts[i].append((ell,q,arb_poly([ar(z) for z in list(end)[q:]])))
    endpoints.append({'part':i,'ell':ell,'q':q,'diagonal_exponent':str(b)})
  groups={};pairs=0
  for mult,rows in zip([1,3,3,1],parts):
   for i,(ell,q,p) in enumerate(rows):
    for j in range(i,len(rows)):
     ee,qq,vv=rows[j];b=(ell+ee)*delta/2+q+qq-Q(4,5);assert b>-1
     pp=p*vv*(mult*(1 if i==j else 2));groups[b]=groups.get(b,arb_poly([]))+pp;pairs+=1
  def integral(p,b):return sum((z/ar(b+k+1) for k,z in enumerate(p)),arb(0))
  s=sum((integral(p,b) for b,p in groups.items()),arb(0));t=sum((integral(p*w,b) for b,p in groups.items()),arb(0));pref=arb.pi()/2*arb(4)**ar(Q(4,5))
  lo,hi=pref*(t-ar(eps)*s),pref*t
  assert all(z>0 and z.rel_accuracy_bits()>150 for z in [s,lo,hi]),(n,s,lo,hi)
  rec={'utc':now(),'mode':n,'manifest_sha256':mh,'symmetry_identities':identities,'radial_pairs':pairs,'energy_lower_ball':lo.str(100),'energy_upper_ball':hi.str(100),'norm_lower_ball':lo.sqrt().str(90),'norm_upper_ball':hi.sqrt().str(90),'endpoints':endpoints,'elapsed_seconds':time.monotonic()-tick}
  new(path,rec);saved[n]=rec;print('mode',n,'seconds',rec['elapsed_seconds'],'total',time.monotonic()-start,flush=True)
 complete=len(saved)==len(modes);lo=sum((arb(r['energy_lower_ball']) for r in saved.values()),arb(0)).sqrt();hi=sum((arb(r['energy_upper_ball']) for r in saved.values()),arb(0)).sqrt();refpath=BASE/'source'/('state131_norms.json' if args.candidate=='state131' else 'N3_norms007_v03.json');ref=json.loads(refpath.read_text())['norms']['Q3'];assert ref['status']=='FINITE'
 overlap=False
 if complete:
  overlap=lo.union(hi).overlaps(arb(ref['norm_lower_ball']).union(arb(ref['norm_upper_ball'])));assert overlap,(lo,hi,ref['norm_lower_ball'],ref['norm_upper_ball'])
 result={'utc':now(),'candidate':args.candidate,'complete':complete,'manifest_sha256':mh,'completed_modes':sorted(saved),'missing_modes':[n for n in modes if n not in saved],'norm_lower_ball':lo.str(80),'norm_upper_ball':hi.str(80) if complete else None,'reference_lower_ball':ref['norm_lower_ball'],'reference_upper_ball':ref['norm_upper_ball'],'reference_overlap':overlap,'reference_sha256':H(refpath),'fixtures':fixture_rows,'symmetry_identities':sum(r['symmetry_identities'] for r in saved.values()),'mode_sha256':{str(n):H(outdir/f'modes/mode_{n:03d}.json') for n in saved},'code_sha256':H(__file__),'stage_elapsed_seconds':time.monotonic()-start,'status':'Complete outward calculation; OPENpeer for new polar formula' if complete else 'Partial positive mode energies only'}
 if complete:new(outdir/'full.json',result)
 else:(outdir/'progress.json').write_text(json.dumps(result,indent=2)+'\n')
 print('DONE',len(saved),'/',len(modes),'Q3',lo.str(30),hi.str(30),'reference',overlap,flush=True)
if __name__=='__main__':main()
