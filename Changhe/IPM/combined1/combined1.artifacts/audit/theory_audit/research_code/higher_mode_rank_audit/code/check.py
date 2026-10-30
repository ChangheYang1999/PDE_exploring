"""Independent exact Legendre recurrence and abstract higher-mode shape audit."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import comb
import json,hashlib,sys,time
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
def add(a,b):
 o=[Q(0)]*max(len(a),len(b))
 for i,x in enumerate(a):o[i]+=x
 for i,x in enumerate(b):o[i]+=x
 return o
def mul(a,b):
 o=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 return o
def scale(a,c):return [c*x for x in a]
def val(a,v):
 s=Q(0)
 for x in reversed(a):s=s*v+x
 return s
def main():
 start=time.monotonic();manifest=read(B/'data/manifest.json');inputs={}
 for p,d in manifest['files'].items():assert sha(B/p)==d['sha256'];inputs[p]=d['sha256']
 assert sha(B/'PROOF.md')==manifest['proof_sha256']
 old=read(B/'data/old_basis.json');parent=read(B/'data/parent016.json')
 peer=read(B/'source/N4_result.json');abstract=read(B/'source/N4_shapes.json');prior=read(B/'source/T4_joint_result.json')
 assert prior['verdict'].startswith('CONFIRMED') and prior['potential_dimension']==prior['density_dimension']==2426
 for p,h in prior['inputs'].items():assert sha(Path(p))==h;inputs[p]=h
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
 oldshapes=list(map(shape,old['generators']));parents=list(map(shape,parent['generators']))
 assert len(oldshapes)==len(set(oldshapes))==1922 and len(parents)==len(set(parents))==2174
 prefix=[(j,m,('legqs',0,N,4,25)) for j in [1,2,3] for m in range(9,16) for N in range(12)]
 assert set(parents[:1922])==set(oldshapes) and parents[1922:]==prefix
 assert set(parents)==set(oldshapes+prefix)
 blocks=[(1,m) for m in range(16,20)]+[(j,m) for j in [2,3] for m in range(16,24)]
 present={(j,m) for j,m,sp in parents};bylaunch=[(j,m) for j in [1,2,3] for m in range(16,24) if (j,m) in present]
 assert bylaunch==blocks and len(blocks)==20
 new=[(j,m,('legqs',0,N,4,25)) for j,m in blocks for N in range(12)]
 declared=oldshapes+[(j,m,('legqs',0,N,4,25)) for j in [1,2,3] for m in range(9,20 if j==1 else 24) for N in range(12)]
 actual=parents+new
 assert actual==list(map(shape,abstract['generators'])) and set(actual)==set(declared)
 assert len(actual)==len(set(actual))==2414 and len(new)==240
 launch=(B/'source/N1_chain022.sh').read_text()
 assert 'export IPM_ADD_LEGQS="1,2,3:16:23:25:12"' in launch and 'unset IPM_ADD_LEGQS' in launch
 desc=read(B/'source/N4_launch_sources.json');assert sha(B/'source/N1_chain022.sh')==desc['files']['N1_chain022.sh']['sha256']
 c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma
 ps=[(3+gamma-j*delta)/2 for j in range(8)];diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert all(q.denominator!=1 for q in ps+diffs)
 assert list(map(str,ps))==peer['branch_exponents'] and list(map(str,diffs))==peer['noninteger_differences']
 assert 3+gamma<4 and gamma-1<0
 a=Q(624);v0=-1/a;L=[Q(1),a];znum=[Q(1),-Q(626)]
 # U_N(v)=L(v)^N P_N(znum(v)/L(v)).
 numerators=[[Q(1)],znum]
 for n in range(1,11):numerators.append(scale(add(scale(mul(znum,numerators[-1]),2*n+1),scale(mul(mul(L,L),numerators[-2]),-n)),Q(1,n+1)))
 pw={(d['m'],d['N']):d for d in peer['Laurent_witnesses']}
 ow={(d['m'],d['N']):d for d in prior['witnesses'] if d['scale']==25}
 witnesses=[]
 for m in range(9,24):
  tpoly=[Q((-1)**k*comb(m,k)) for k in range(m+1)]
  for N in range(12):
   numerator=[Q(0)]*4+scale(mul(tpoly,numerators[N]),625**4)
   value=val(numerator,v0)/a**(4+N)
   formula=625**4*v0**4*comb(2*N,N)*(1-v0)**(m+N)/a**(4+N)
   assert value==formula==Q(pw[m,N]['coefficient']) and value!=0
   if m<=15:assert value==Q(ow[m,N]['coefficient'])
   witnesses.append({'m':m,'N':N,'pole_order':4+N,'coefficient':str(value),'full_numerator_formula_equal':True,'peer_equal':True,'old_equal':True if m<=15 else None})
 coefficient=4*33*32*(ps[1]-16-Q(4,625));assert coefficient!=0 and coefficient==Q(peer['density31_origin_coefficient'])
 support=sorted({2*m+s for j,m in blocks for s in [-1,1]});assert support==list(range(31,48,2))==peer['density_new_mode_support']
 assert peer['potential_dimension']==peer['density_dimension']==2414 and peer['actual_candidate_shape_match'] is None
 for p in [B/'PROOF.md',Path(__file__),B/'data/manifest.json']:inputs[str(p)]=sha(p)
 result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'potential_dimension':2414,'density_dimension':2414,'actual_candidate_shape_match':None,'proposed_shape_list_equal':True,'new_blocks':blocks,'new_count':240,'all_scaled_count':492,'branch_exponents':list(map(str,ps)),'noninteger_differences':list(map(str,diffs)),'Laurent_witnesses':witnesses,'growth_exponent':str(3+gamma),'fourth_derivative_exponent':str(gamma-1),'density_new_mode_support':support,'density31_origin_coefficient':str(coefficient),'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-294 abstract rank, density injectivity and new-mode endpoint; actual candidate remains unbound','publisher_code_executed':False}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(witnesses),result['elapsed_seconds'],sha(B/'verification/result.json'))
if __name__=='__main__':main()
