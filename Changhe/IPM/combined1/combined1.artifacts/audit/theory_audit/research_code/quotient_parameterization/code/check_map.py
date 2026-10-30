"""Independently multiply out the supplied quotient identities; no elimination."""
from pathlib import Path
from collections import defaultdict
from datetime import datetime,timezone
from math import comb
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q,fmpq_poly as P
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];S=B/'source';T=P([0,1])
def H(p):return sha256(p.read_bytes()).hexdigest()
def poly(g):
 s=g['spec']; assert s[0] in ('mono','leg')
 w=int(s[1]);assert w>=0 and w==s[1]
 if s[0]=='mono':return T**w
 n=int(s[2]);assert n>=0 and n==s[2]
 return T**w*P([(-1)**(n-k)*comb(n,k)*comb(n+k,k) for k in range(n+1)])
def canon(gs):
 out=defaultdict(Q)
 for g in gs:
  for k,v in enumerate(poly(g)):
   if v:out[g['j'],g['m'],g['m']+k]+=Q(g['coef'])*v
 return {k:v for k,v in out.items() if v}
def main():
 start=time.monotonic()
 src=json.loads((S/'original007.json').read_text());new=json.loads((S/'reduced_exact.json').read_text());mp=json.loads((S/'coordinate_map.json').read_text());can=json.loads((S/'canonical007.json').read_text());summary=json.loads((S/'N4_QUOTIENT_result.json').read_text())
 assert H(S/'original007.json')==mp['source_sha256']==summary['source_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
 assert H(S/'reduced_exact.json')==mp['reduced_sha256']==summary['reduced_sha256']
 assert H(S/'coordinate_map.json')==summary['map_sha256']
 assert H(S/'canonical007.json')==summary['canonical_sha256']=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
 assert Q(src['cl_exact'])==Q(new['cl_exact'])==Q(can['cl'])
 gs=src['generators'];ns=new['generators'];pivots=mp['reduced_to_original_pivots'];relations=mp['kernel_relations']
 assert len(gs)==2982 and len(ns)==len(pivots)==1922 and len(relations)==1060
 assert len(set(pivots))==1922 and all(type(i)==int and 0<=i<2982 for i in pivots)
 pset=set(pivots);polys=list(map(poly,gs));beta={i:Q(gs[i]['coef']) for i in pivots};nonp=set()
 for row in relations:
  j=row['unit_nonpivot_index'];assert type(j)==int and 0<=j<2982 and j not in pset and j not in nonp;nonp.add(j)
  cf={int(i):Q(v) for i,v in row['coefficients'].items()};assert cf[j]==1 and set(cf)<=pset|{j}
  assert all((gs[i]['j'],gs[i]['m'])==(gs[j]['j'],gs[j]['m']) for i in cf)
  total=P([])
  for i,v in cf.items():
   total+=v*polys[i]
   if i!=j:beta[i]-=Q(gs[j]['coef'])*v
  assert not total
 assert pset|nonp==set(range(2982))
 for g,i in zip(ns,pivots,strict=True):
  assert all(g[k]==gs[i][k] for k in ('j','m','spec'))
  assert Q(g['coef'])==beta[i]
 exact={tuple(k):Q(v) for k,v in zip(can['order'],can['coefficients'],strict=True)}
 assert canon(gs)==canon(ns)==exact
 # RE=I follows from unit insertion and the absence of other nonpivot indices;
 # rank1922 is independently established by T4-195 and recorded in the proof.
 result={'utc':datetime.now(timezone.utc).isoformat(),'method':'closed-form polynomial expansion of each supplied relation; no pivot elimination','original_columns':2982,'selected_columns':1922,'verified_unit_nonpivot_relations':1060,'selected_shapes_equal':True,'transformed_coefficients_equal':True,'whole_canonical_maps_equal':True,'rank_dependency':'T4-195 independent exact rank1922','proof_sha256':H(B/'PROOF.md'),'code_sha256':H(Path(__file__)),'inputs':{p.name:H(p) for p in [S/'original007.json',S/'reduced_exact.json',S/'coordinate_map.json',S/'canonical007.json',S/'N4_QUOTIENT_result.json']},'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-175 exact coordinate map and representation; no condition-number claim'}
 with (B/'verification/map_result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
