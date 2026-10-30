"""Accept independent actual-025 point, origin and complete-prefix checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time,gzip
from flint import fmpq as Q,arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate025_peer'
sys.set_int_max_str_digits(0);ctx.prec=2048
def contents(p):
 p=Path(p);b=p.read_bytes();return gzip.decompress(b) if p.suffix==".gz" else b
sha=lambda p:sha256(contents(p)).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def dec(d):return {int(k):Q(v) for k,v in d.items() if Q(v)}
def enc(d):return {str(k):str(v) for k,v in sorted(d.items()) if v}
def main():
 start=time.monotonic();inputs={};checks={};frozen={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(p,actual,h)
  inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(contents(bind(p,h)))
 manifest=read(B/'source/MANIFEST.json');bind(B/'PROOF.md',manifest['proof_sha256']);bind(Path(__file__))
 for rel in ['research/generator_sector_audit/code/direct.py','research/generator_sector_audit/PROOF.md','research/generator_sector_audit/PROOF_CANDIDATES.md','research/multiscale_generators/code/moments.py','research/multiscale_generators/code/cartesian.py','research/multiscale_generators/PROOF.md','research/sector_audit/code/sectors_flint.py']:
  bind(R/rel)

 for original,entry in manifest['files'].items():
  p=R/entry['local'];assert sha256(p.read_bytes()).hexdigest()==entry['stored_sha256'];frozen[original]=bind(p,entry['sha256'])
 peers={}
 for topic,fn in [('candidate025_point','results.json'),('candidate025_origin','result.json'),('candidate025_sectors','result.json')]:
  p=frozen[str(R.parent/'c1-t4/research'/topic/'verification'/fn)];data=read(p);peers[topic]=data
  for rel,h in data['inputs'].items():
   original=Path(rel) if Path(rel).is_absolute() else R.parent/'c1-t4/research'/topic/rel
   assert str(original) in frozen,original;bind(frozen[str(original)],h)
 def raw(ident):
  ds=list((R/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'));assert len(ds)==1;d=ds[0]
  m=read(d/'MANIFEST.json');assert len(m['coefficient_files'])==1;e=m['coefficient_files'][0];p=bind(d/e['name'],e['sha256']);return d.name,p,read(p)
 name,rawp,data=raw('025');assert name=='C1-N1-025-combined-heldin1e16'
 assert sha(rawp)=='3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17'
 old=read(R/f'research/generator_sector_audit/verification/{name}_direct.json');assert old['generator_sha256']==sha(rawp)
 c=Q(data['cl_exact']);gamma=1/c;delta=1-gamma;assert c==Q(4076476460239181,2251799813685248)
 for pr in peers.values():assert pr['candidate']==name
 # Complete point comparison and independent necessary-inequality evaluation.
 pr=peers['candidate025_point'];pc={};assert pr['point']==old['point']==['1/10','73/100'] and Q(pr['c_exact'])==c
 assert set(pr['fields'])==set(old['fields'])=={'rho','u1','u2','rho_x','rho_y','residual','velocity_norm','gradient_norm'}
 f={k:arb(v) for k,v in old['fields'].items()}
 for k,v in f.items():pc['field_'+k]=v.is_finite() and v.overlaps(arb(pr['fields'][k]))
 x,y=map(Q,pr['point']);vx=ar(c*x)+f['u1'];vy=ar(c*y)+f['u2'];I=abs(f['residual'])
 pc['residual_identity']=(vx*f['rho_x']+vy*f['rho_y']-f['rho']).overlaps(f['residual'])
 pc['velocity_identity']=(vx*vx+vy*vy).sqrt().overlaps(f['velocity_norm'])
 pc['gradient_identity']=(f['rho_x']**2+f['rho_y']**2).sqrt().overlaps(f['gradient_norm'])
 pc['peer_fields']=all(pr['field_overlaps'].values())
 theta=(f['gradient_norm']-f['rho_y'])/2;pc['theta']=theta.overlaps(arb(pr['theta'])) and (theta-ar(c-1)).overlaps(arb(pr['theta_minus_c_minus_one']))
 specs=[('A2-Db','1/262144','1/65536'),('FW-T-TB-rebal-v1','1/65536','3/32768'),('FW-T-TB-sharp-v1','1/8192','43/50000'),('T4-019-no-H','1/131072','1/16384'),('FW-T-T4L2-sharp-v1','1/7744','147/200000'),('FW-T-T4L2-sharpw-v1','1/5184','1351/1000000')]
 assert len(pr['ball_exclusions'])==len(old['ball_exclusions'])==6;roots={}
 for spec,row,ownrow in zip(specs,pr['ball_exclusions'],old['ball_exclusions'],strict=True):
  label,ss,rr=spec;s=Q(ss);rad=ar(rr);C0=1/(4*arb.pi()*ar(1+s)).sqrt();C1=1/(8*arb.pi()*ar(s*(1+s))).sqrt()
  D=C1*f['velocity_norm']+C0*(1+f['gradient_norm']);up=rad*D+C0*C1*rad*rad;gap=I-up;root=2*I/(D+(D*D+4*C0*C1*I).sqrt())
  pc[label+'_exact_spec']=(row['framework'],row['s'],row['radius'])==spec==(ownrow['framework'],ownrow['s'],ownrow['radius'])
  for key,z in [('upper',up),('gap',gap),('necessary_H2s_radius_lower',root)]:pc[label+'_'+key]=z.is_finite() and z.overlaps(arb(row[key])) and (key not in ownrow or z.overlaps(arb(ownrow[key])))
  pc[label+'_strict']=gap>0 and root>rad;roots[label]=root.str(100)
 b0=ar(Q(50,651))/(28248*4*arb.pi()).sqrt();b1=ar(Q(25,217))/(8*arb.pi()).sqrt();up=b1*f['velocity_norm']+b0*(1+f['gradient_norm'])+b0*b1
 pc['graded_bound']=up.overlaps(arb(pr['uniform_graded_upper'])) and up.overlaps(arb(old['uniform_graded_upper']))
 gap=I-up;pc['graded_gap']=gap>0 and gap.overlaps(arb(pr['uniform_graded_gap'])) and gap.overlaps(arb(old['uniform_graded_gap']))
 assert all(pc.values()),{k:v for k,v in pc.items() if not v}
 point={'verdict':'CONFIRMED N4-362 point exclusions via independent T4 actual025 point','checks':pc,'check_count':len(pc),'residual':f['residual'].str(100),'graded_gap':gap.str(100),'necessary_radii':roots}
 # Own homogenized-Legendre origin recurrence versus independent shifted expansion.
 code=bind(R/'research/generator_sector_audit/code/direct.py');spec=importlib.util.spec_from_file_location('actual025_own_algebra',code);D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
 pr=peers['candidate025_origin'];origin=D.origin(data);sums=[Q(0)]*3;touched=terms=0
 for g in data['generators']:
  m=int(g['m']);w,n,q,scale=D.spec_parts(g['spec'])
  if m+w>2:continue
  touched+=1;terms+=min(n,2-m-w)+1;p=(3+gamma-int(g['j'])*delta)/2;sums[m]+=Q(g['coef'])*D.origin_radial(p,m,g['spec'],2-m)[2-m]
 b0,b1,b2=sums;quartic={'x4':b0+b1+b2,'x2y2':2*b0-6*b2,'y4':b0-b1+b2}
 oc={k:v==Q(old['origin'][k])==Q(pr['origin'][k]) for k,v in origin.items()}
 oc.update({'quartic_'+k:v==Q(pr['quartic_coefficients'][k]) for k,v in quartic.items()})
 oc['normalization']=c+origin['strain']==Q(pr['c_plus_strain'])==1
 oc['positive_slope']=origin['a0']>0 and pr['a0_positive']
 oc['counts']=len(data['generators'])==pr['raw_count']==2918 and touched==pr['contributing_generators']==24 and terms==pr['contributing_summands']==24
 oc['jet_identities']=origin['strain']==4*quartic['x2y2'] and origin['a0']==-4*quartic['x2y2']-24*quartic['y4']
 oc['slope_ball']=ar(origin['a0']).overlaps(arb(pr['a0_arb'])) and ar(origin['a0']).overlaps(arb(old['a0_arb']))
 oc['peer_flags']=all(pr['N4_exact_comparisons'].values());assert all(oc.values()),oc
 org={'verdict':'CONFIRMED N4-362 exact origin via independent T4 actual025 origin','checks':oc,'check_count':len(oc),'origin':{k:str(v) for k,v in origin.items()},'quartic_coefficients':{k:str(v) for k,v in quartic.items()},'slope':ar(origin['a0']).str(100),'contributing_generators':touched,'contributing_summands':terms}
 # Recompute every exact map through the full -7/2 cutoff, including new rows.
 pr=peers['candidate025_sectors'];exactp=frozen[str(R.parent/'c1-t4/research/candidate025_sectors/data/exact_sectors.json')];exact=read(exactp,pr['exact_sectors_sha256']);assert exact['candidate']==name and exact['raw_sha256']==sha(rawp)
 alpha,C,G,E,grouped,summary=D.sectors(data,qmax=2,hmax=9);omitted=Q(summary['omitted_exponent_upper_bound']);assert omitted==max(gamma-6,gamma-10*delta)<Q(-7,2)
 keys=sorted([k for k in E if alpha(*k)>=Q(-7,2)],key=lambda k:alpha(*k),reverse=True);assert len(keys)==len(set(alpha(*k) for k in keys))==16
 rows={(r['K']-1,r['L']):r for r in exact['sectors']};assert set(rows)==set(keys)
 _,basep,baseline=raw('007');ba,bC,bG,_,_,_=D.sectors(baseline,qmax=1,hmax=0)
 previous={Q(r['exponent']):r for r in old['sectors']};assert len(set(previous)&set(alpha(*k) for k in keys))==13
 scount=0;ccount=0;records=[];nonzero=[]
 for key in keys:
  h,q=key;a=alpha(*key);s=a+3;row=rows[key];density=G.get(key,{});psi=D.dy(D.dx(C.get(key,{}),s,'c'),s-1,'c');F=E[key]
  assert Q(row['exponent_exact'])==a;scount+=1;maps={'density':density,'stream':psi,'residual':F}
  for kind,value in maps.items():assert value==dec(row[kind]),(key,kind);scount+=1;ccount+=len(value)
  lhs={n:((a+1)**2-n*n)*v for n,v in psi.items() if ((a+1)**2-n*n)*v};rhs={n:-v for n,v in D.dx(density,a,'s').items() if v};assert lhs==rhs and row['poisson_exact'];scount+=1
  assert bool(not F)==row['residual_zero'];scount+=1;norm=(arb.pi()*ar(sum((v*v for v in F.values()),Q(0)))).sqrt();assert norm.overlaps(arb(row['angular_norm']));scount+=1
  if F:assert norm>0;nonzero.append([h+1,q])
  if a in previous:
   er=previous[a];assert F==dec(er['sine_coefficients']) and bool(not F)==er['exact_zero'] and norm.overlaps(arb(er['full_circle_norm']));scount+=3
  if h<4 and q==0:
   bs=ba(h,0)+3;bpsi=D.dy(D.dx(bC[h,0],bs,'c'),bs-1,'c');assert density==bG[h,0] and psi==bpsi;scount+=2
  records.append({'K':h+1,'L':q,'exponent_exact':str(a),'all_three_maps_equal':True,'Poisson_identity':True,'residual_zero':not F,'angular_norm':norm.str(100),'coefficient_maps_sha256':sha256(json.dumps({k:enc(v) for k,v in maps.items()},sort_keys=True,separators=(',',':')).encode()).hexdigest()})
 assert nonzero==[[4,1],[9,0],[5,1],[1,2],[10,0]]==pr['nonzero_sectors'];assert sum(r['residual_zero'] for r in records)==pr['zero_sectors']==11
 assert alpha(3,1)==4*gamma-5>omitted and pr['all_scaled_generators_have_Q4_and_R25_R50_R100'] and pr['all_13_common_exact_coefficient_maps_agree_N4']
 sec={'verdict':'CONFIRMED independent T4 actual025 full-prefix full prefix and leading density/stream profiles','checks':scount,'coefficient_count':ccount,'sectors':records,'complete_cutoff':'-7/2','omitted_exponent_upper_bound':str(omitted),'nonzero_sector_set':nonzero,'zero_sectors':11}
 for rel in ['research/generator_sector_audit/PROOF.md','research/generator_sector_audit/PROOF_CANDIDATES.md','research/multiscale_generators/code/moments.py','research/multiscale_generators/code/cartesian.py','research/multiscale_generators/PROOF.md','research/sector_audit/code/sectors_flint.py']:bind(R/rel)
 assert all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':now(),'candidate':name,'raw_sha256':sha(rawp),'precision_bits':ctx.prec,'inputs':inputs,'point':point,'origin':org,'sectors':sec,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED actual025 independent point/origin/full-prefix acceptance'}
 dest=B/'verification/result.json'
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED',len(pc),len(oc),scount,ccount,'bindings',len(inputs),'seconds',out['elapsed_seconds'],'SHA256',sha(dest),flush=True)
if __name__=='__main__':main()
