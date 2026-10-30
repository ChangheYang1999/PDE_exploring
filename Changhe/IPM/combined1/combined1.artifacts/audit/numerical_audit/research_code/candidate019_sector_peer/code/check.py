"""All cutoff-selected 018 field maps from N4 raw homogeneous Cartesian algebra."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import importlib.util,json,sys,time
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/candidate019_sector_peer'
sys.set_int_max_str_digits(0)
spec=importlib.util.spec_from_file_location('n4_independent019sectors',ROOT/'research/generator_sector_audit/code/direct.py')
D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def enc(d):return {str(k):str(v) for k,v in sorted(d.items()) if v}
def dec(d):return {int(k):Q(v) for k,v in d.items() if Q(v)}
def ar(q):return arb(q.numerator)/q.denominator
def main():
 tick=time.monotonic();ctx.prec=768;dest=BASE/'verification/result.json';assert not dest.exists()
 inputs={};manifestpath=BASE/'source/MANIFEST.json';manifest=json.loads(manifestpath.read_text())
 def bind(p,h=None):
  p=Path(p);actual=sha(p)
  if h is not None:assert actual==h,(str(p),actual,h)
  inputs[str(p.relative_to(ROOT))]=actual
  return p
 bind(manifestpath)
 for name,v in manifest['files'].items():bind(BASE/'source'/name,v['sha256'])
 peer=json.loads((BASE/'source/T4_result.json').read_text());exactpath=BASE/'source/T4_exact_sectors.json';exact=json.loads(exactpath.read_text())
 assert sha(exactpath)==peer['exact_sectors_sha256']
 def raw(ident):
  directory=next((ROOT/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'))
  man=bind(directory/'MANIFEST.json');m=json.loads(man.read_text());assert len(m['coefficient_files'])==1
  sums=bind(directory/'SHA256SUMS')
  for line in sums.read_text().splitlines():
   h,n=line.split(None,1);n=n.lstrip('*');assert Path(n).name==n;bind(directory/n,h)
  p=bind(directory/m['coefficient_files'][0]['name'],m['coefficient_files'][0]['sha256'])
  return directory.name,p,json.loads(p.read_text())
 name,rawpath,data=raw('019');assert name==peer['candidate']==exact['candidate']
 assert sha(rawpath)==exact['raw_sha256']=='ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419'
 c=Q(data['cl_exact']);gamma=1/c;delta=1-gamma;assert c==Q(4076476460239181,2251799813685248)
 alpha,C,G,E,grouped,summary=D.sectors(data,qmax=2,hmax=9)
 omitted=Q(summary['omitted_exponent_upper_bound']);assert omitted==max(gamma-6,gamma-10*delta)<Q(-7,2)
 keys=sorted([k for k in E if alpha(*k)>=Q(-7,2)],key=lambda k:alpha(*k),reverse=True)
 assert len(keys)==len(set(alpha(*k) for k in keys))==16
 rows={(r['K']-1,r['L']):r for r in exact['sectors']};assert set(keys)==set(rows)
 _,basepath,baseline=raw('007');ba,bC,bG,_,_,_=D.sectors(baseline,qmax=1,hmax=0)
 earlierpath=bind(ROOT/'research/generator_sector_audit/verification'/f'{name}_direct.json')
 earlier=json.loads(earlierpath.read_text());assert earlier['generator_sha256']==sha(rawpath)
 previous={Q(r['exponent']):r for r in earlier['sectors']};assert len(set(previous)&set(alpha(*k) for k in keys))==13
 output=[];checks=0;count=0;nonzero=[]
 for key in keys:
  h,q=key;a=alpha(*key);s=a+3;row=rows[key]
  density=G.get(key,{});psi=D.dy(D.dx(C.get(key,{}),s,'c'),s-1,'c');F=E[key]
  assert Q(row['exponent_exact'])==a;checks+=1
  maps={'density':density,'stream':psi,'residual':F}
  for field,value in maps.items():
   assert value==dec(row[field]),(key,field);checks+=1;count+=len(value)
  lhs={n:((a+1)**2-n*n)*v for n,v in psi.items() if ((a+1)**2-n*n)*v}
  rhs={n:-v for n,v in D.dx(density,a,'s').items() if v};assert lhs==rhs and row['poisson_exact'];checks+=1
  assert (not F)==row['residual_zero'];checks+=1
  norm=(arb.pi()*ar(sum((v*v for v in F.values()),Q(0)))).sqrt();assert norm.overlaps(arb(row['angular_norm']));checks+=1
  if F:assert norm>0;nonzero.append([h+1,q])
  if a in previous:
   er=previous[a];assert F==dec(er['sine_coefficients']) and bool(not F)==er['exact_zero'] and norm.overlaps(arb(er['full_circle_norm']));checks+=3
  if h<4 and q==0:
   bs=ba(h,0)+3;bpsi=D.dy(D.dx(bC[h,0],bs,'c'),bs-1,'c')
   assert density==bG[h,0] and psi==bpsi;checks+=2
  encoded={f:enc(v) for f,v in maps.items()}
  output.append({'K':h+1,'L':q,'exponent_exact':str(a),'density_modes':len(density),'stream_modes':len(psi),'residual_modes':len(F),'all_three_maps_equal_peer':True,'Poisson_identity_exact':True,'zero':not F,'norm':norm.str(100),'coefficient_maps_sha256':sha256(json.dumps(encoded,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
 assert nonzero==[[4,1],[9,0],[5,1],[1,2],[10,0]]==peer['nonzero_sectors']
 assert sum(r['zero'] for r in output)==11==peer['zero_sectors'];assert alpha(3,1)==4*gamma-5>omitted
 assert peer['all_scaled_generators_have_Q4_R50'] and peer['all_13_common_exact_coefficient_maps_agree_N4']
 for p in [Path(__file__),BASE/'PROOF.md',ROOT/'research/generator_sector_audit/code/direct.py',ROOT/'research/generator_sector_audit/PROOF.md',ROOT/'research/generator_sector_audit/PROOF_CANDIDATES.md',ROOT/'research/multiscale_generators/code/moments.py',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/multiscale_generators/PROOF.md',ROOT/'research/sector_audit/code/sectors_flint.py']:bind(p)
 assert all(sha(ROOT/p)==h for p,h in inputs.items())
 record={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(rawpath),'precision_bits':ctx.prec,'inputs':inputs,'all_peer_input_bindings_prechecked':manifest['peer_input_bindings_checked'],'complete_cutoff':'-7/2','omitted_exponent_upper_bound':str(omitted),'rectangular_computed_rows':len(E),'cutoff_rows':len(keys),'exact_coefficients_compared':count,'checks':checks,'sectors':output,'nonzero_sector_set':nonzero,'zero_sector_count':11,'all_three_additional_exact_maps_compared':True,'first_four_density_stream_profiles_equal007':True,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED T4-355 complete exact sector and leading-profile claims, including the three maps previously compared only with publisher FLOAT norms.'}
 with dest.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
 print(record['utc'],'CONFIRMED',count,'coefficients',checks,'checks',record['elapsed_seconds'],'seconds',sha(dest),flush=True)
if __name__=='__main__':main()
