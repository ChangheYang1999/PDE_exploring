"""Exact generator quotient. Standalone Python/flint; no optimizer imports."""
from pathlib import Path
from collections import defaultdict
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import argparse,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly
sys.set_int_max_str_digits(0)
T=Poly([0,1])
def digest(p):return sha256(Path(p).read_bytes()).hexdigest()
def leg(n):return Poly([(-1)**(n-k)*comb(n,k)*comb(n+k,k) for k in range(n+1)])
def recurrence(n):
 a,b=Poly([1]),2*T-1
 if n==0:return a
 for k in range(1,n):a,b=b,((2*k+1)*(2*T-1)*b-k*a)/(k+1)
 return b
def polynomial(g):
 assert set(g)<= {'j','m','spec','coef','coef_float'}
 j,m=int(g['j']),int(g['m']);assert j==g['j'] and m==g['m'] and j>=0 and m>=0
 s=g['spec'];assert s[0] in ['mono','leg'];assert len(s)==(2 if s[0]=='mono' else 3)
 assert all(int(z)==z and z>=0 for z in s[1:])
 if s[0]=='mono':return T**int(s[1])
 assert leg(int(s[2]))==recurrence(int(s[2]))
 return T**int(s[1])*leg(int(s[2]))
def subtract(v,w,a):
 out=dict(v)
 for i,x in w.items():
  out[i]=out.get(i,Q(0))-a*x
  if not out[i]:del out[i]
 return out

def canonical(gens):
 out=defaultdict(lambda:Q(0))
 for g in gens:
  for k,z in enumerate(polynomial(g)):
   if z:out[int(g['j']),int(g['m']),int(g['m'])+k]+=Q(g['coef'])*z
 return {k:v for k,v in out.items() if v}

def reduce(raw):
 gens=raw['generators'];assert raw['n_fixed']==0 and raw['n_free']==len(gens)
 c=Q(raw['cl_exact']);assert c>1;delta=1-1/c
 js=sorted({int(g['j']) for g in gens})
 for j in js:
  for k in js:
   if j<k:assert ((k-j)*delta/2).denominator!=1
 polys=[polynomial(g) for g in gens];groups=defaultdict(list)
 for i,g in enumerate(gens):groups[int(g['j']),int(g['m'])].append(i)
 pivots=[];rels=[];blocks=[]
 for (j,m),ids in sorted(groups.items()):
  ordered=sorted(ids,key=lambda i:(gens[i]['spec'][0]!='leg',polys[i].degree(),i));basis={};local=[];nulls=[]
  for index in ordered:
   pp=polys[index];vector={index:Q(1)}
   while pp:
    degree=pp.degree()
    if degree not in basis:basis[degree]=(pp,vector);local.append(index);break
    bp,bv=basis[degree];factor=pp[degree]/bp[degree];pp-=factor*bp;vector=subtract(vector,bv,factor)
   if not pp:
    assert vector[index]==1 and all(i==index or i in local for i in vector)
    assert not sum((v*polys[i] for i,v in vector.items()),Poly([]))
    rels.append((index,vector));nulls.append(index)
  assert len(local)+len(nulls)==len(ids);pivots+=local
  blocks.append({'j':j,'m':m,'rank':len(local),'original_columns':len(ids),'pivot_indices':local,'nonpivot_indices':nulls})
 assert len(set(pivots))==len(pivots) and len(pivots)+len(rels)==len(gens)
 alpha=[Q(g['coef']) for g in gens];beta={i:alpha[i] for i in pivots}
 for index,vector in rels:
  for i,v in vector.items():
   if i!=index:beta[i]-=alpha[index]*v
 new=[]
 for i in pivots:
  g=gens[i];new.append({'j':int(g['j']),'m':int(g['m']),'spec':list(g['spec']),'coef':str(beta[i]),'coef_float':float(beta[i])})
 assert canonical(new)==canonical(gens)
 return new,pivots,rels,blocks

def main():
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output_directory');ap.add_argument('--canonical-check');args=ap.parse_args();start=time.monotonic()
 src=Path(args.input).resolve();outdir=Path(args.output_directory).resolve();outdir.mkdir(parents=True,exist_ok=True)
 targets=[outdir/name for name in ['reduced_exact.json','coordinate_map.json','result.json']];assert all(not x.exists() for x in targets)
 raw=json.loads(src.read_text());new,pivots,rels,blocks=reduce(raw)
 result={'format':raw['format'],'cl_exact':raw['cl_exact'],'cl_float':float(Q(raw['cl_exact'])),'generators':new,'n_free':len(new),'n_fixed':0,'meta':{'kind':'unregistered exact coordinate representation, no new optimization','source_sha256':digest(src),'source_filename':src.name,'coordinate_policy':'independent original generators, Legendre preference','source_n_free':len(raw['generators']),'exact_equivalence_checked':True,'binary64_scope':'coef_float is rounded convenience data; no exact preservation or condition-number assertion for that rounding','constraint_setup':'rebuild all matrices and pivots for this generator list'}}
 second,pp,rr,bb=reduce(result);assert second==new and not rr and len(pp)==len(new)
 can_sha=None
 if args.canonical_check:
  cp=Path(args.canonical_check).resolve();can=json.loads(cp.read_text());assert Q(can['cl'])==Q(raw['cl_exact']);expected={tuple(map(int,k)):Q(v) for k,v in zip(can['order'],can['coefficients'])}
  assert canonical(new)==expected;can_sha=digest(cp)
 with targets[0].open('x') as f:json.dump(result,f,indent=1);f.write('\n')
 mapping={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':digest(src),'reduced_sha256':digest(targets[0]),'reduced_to_original_pivots':pivots,'kernel_relations':[{'unit_nonpivot_index':i,'coefficients':{str(k):str(v) for k,v in sorted(rel.items())}} for i,rel in rels],'blocks':blocks,'reduction_formula':'beta_i=alpha_i-sum_nonpivot_j alpha_j*r_ji; r_jj=1','embedding_formula':'put beta in the recorded original pivot positions and zero in every nonpivot position'}
 with targets[1].open('x') as f:json.dump(mapping,f,indent=1);f.write('\n')
 summary={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':digest(src),'canonical_sha256':can_sha,'code_sha256':digest(__file__),'generator_count':len(raw['generators']),'reduced_dimension':len(new),'zero_potential_dimension':len(rels),'blocks':len(blocks),'selected_legendre_count':sum(g['spec'][0]=='leg' for g in new),'selected_monomial_count':sum(g['spec'][0]=='mono' for g in new),'all_kernel_relations_exact':True,'all_potential_coefficients_preserved':True,'canonical_check_passed':can_sha is not None,'second_reduction_identical':True,'reduced_sha256':digest(targets[0]),'map_sha256':digest(targets[1]),'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent peer of this coordinate map; not conditioning, optimization or an inverse certificate'}
 with targets[2].open('x') as f:json.dump(summary,f,indent=2);f.write('\n')
 print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':main()
