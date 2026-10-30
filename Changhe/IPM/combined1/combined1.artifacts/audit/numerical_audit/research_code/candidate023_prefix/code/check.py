"""All actual-023 homogeneous sectors at exponent at least -7/2."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import arb,ctx,fmpq as Q
R=Path(__file__).resolve().parents[3];B=R/'research/candidate023_prefix'
sys.path.insert(0,str(R/'research/generator_sector_audit/code'))
from direct import sectors,dx,dy
from cartesian import ar,spec_parts
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();ctx.prec=1536;inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);s=sha(p);assert h is None or h==s,(str(p),h,s);inputs[str(p.relative_to(R))]=s;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 hold=read(R/'research/candidate023_holdout/verification/result.json');name=hold['candidate'];assert hold['generator_count']==2426
 for p,h in hold['inputs'].items():bind(R/p,h)
 direct=read(R/'research/generator_sector_audit/verification'/f'{name}_direct.json')
 for p,h in direct['dependency_sha256'].items():bind(R/p,h)
 d=R/'research/candidate_audits/data'/name;m=read(d/'MANIFEST.json');rawp=bind(d/m['coefficient_files'][0]['name'],hold['raw_sha256']);raw=read(rawp);assert direct['generator_sha256']==sha(rawp)
 a,C,G,E,grouped,summary=sectors(raw,qmax=2,hmax=9);assert Q(summary['omitted_exponent_upper_bound'])<Q(-7,2) and summary['all_forbidden_zero'];checks['complete_prefix_bound']=True
 selected=sorted([key for key in E if a(*key)>=Q(-7,2)],key=lambda k:a(*k),reverse=True);assert len(selected)==len({a(*key) for key in selected})==16
 def stream(C,key,alpha):
  return dy(dx(C.get(key,{}),alpha+3,'c'),alpha+2,'c')
 def ser(poly):return {str(k):str(v) for k,v in sorted(poly.items()) if v}
 rows=[]
 for key in selected:
  alpha=a(*key);g=G.get(key,{});psi=stream(C,key,alpha);lap={n:((alpha+1)**2-n*n)*v for n,v in psi.items()};want={n:-v for n,v in dx(g,alpha,'s').items()};assert ser(lap)==ser(want)
  residual=E[key];norm=(arb.pi()*ar(sum((v*v for v in residual.values()),Q(0)))).sqrt()
  rows.append({'K':key[0]+1,'L':key[1],'exponent_exact':str(alpha),'density':ser(g),'stream':ser(psi),'residual':ser(residual),'residual_zero':not residual,'stream_identity_exact':True,'full_circle_norm':norm.str(100)})
 nonzero=[(x['K'],x['L']) for x in rows if not x['residual_zero']];assert nonzero==[(4,1),(9,0),(5,1),(1,2),(10,0)] and sum(x['residual_zero'] for x in rows)==11;checks['exact11_zero5_nonzero']=True
 previous={Q(x['exponent']):x for x in direct['sectors']};common=0
 for row in rows:
  if Q(row['exponent_exact']) in previous:
   prev=previous[Q(row['exponent_exact'])];assert row['residual']==prev['sine_coefficients'] and arb(row['full_circle_norm']).overlaps(arb(prev['full_circle_norm']));common+=1
 assert common==13;checks['all13_previous_sectors_reproduced']=True
 olddir=R/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal';oldman=read(olddir/'MANIFEST.json');entry=oldman['coefficient_files'][0];old=read(olddir/entry['name'],entry['sha256']);assert old.get('cl_exact',old.get('cl'))==raw['cl_exact']
 aa,CC,GG,_,_,_=sectors(old,qmax=1,hmax=0);matches=[]
 for j in range(4):
  key=(j,0);assert C[key]==CC[key] and G[key]==GG[key] and stream(C,key,a(*key))==stream(CC,key,aa(*key));matches.append({'j':j,'potential_equal':True,'density_equal':True,'stream_equal':True})
 checks['four_leading_profiles_equal007']=True
 count=0
 for g in raw['generators']:
  w,n,q,scale=spec_parts(g['spec'])
  if scale!=1:assert scale in [25,100] and q==4;count+=1
 assert count==504;checks['all504_scaled_terms_start_at_q4']=True
 for p in [R/'research/generator_sector_audit/code/direct.py',R/'research/multiscale_generators/code/moments.py',R/'research/multiscale_generators/code/cartesian.py',R/'research/sector_audit/code/sectors_flint.py',R/'research/multiscale_generators/PROOF.md',R/'research/generator_sector_audit/PROOF.md']:bind(p)
 assert all(checks.values()) and all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(rawp),'precision_bits':ctx.prec,'threshold_exact':'-7/2','omitted_exponent_upper_bound':summary['omitted_exponent_upper_bound'],'rows':rows,'leading_profile_matches':matches,'previous_sector_count':common,'scaled_q4_count':count,'checks':checks,'inputs':inputs,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED own complete exact prefix; OPEN independent actual023 sector review'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'023_PREFIX',len(rows),'checks',len(checks),'inputs',len(inputs),'seconds',out['elapsed_seconds'],'sha',sha(p),flush=True)
if __name__=='__main__':main()
