"""Independent coefficient-system partial fractions and direct 2F1 moments."""
from pathlib import Path
from datetime import datetime, timezone
import importlib.util, hashlib, json, time
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
ROOT=Path(__file__).resolve().parents[1]
V=P([0,1]);sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/arb(q.denominator)
spec=importlib.util.spec_from_file_location('n4_poles_frozen',ROOT/'source/moments.py')
peer=importlib.util.module_from_spec(spec);spec.loader.exec_module(peer)

def own_decompose(N,factors):
 merged={}
 for a,m in factors:
  a=Q(a);assert a>0 and type(m) is int and m>0
  merged[a]=merged.get(a,0)+m
 merged=sorted(merged.items());D=P([1])
 for a,m in merged:D*=(1+a*V)**m
 if not D.degree():return list(N),[],0
 basis=[];tags=[]
 for j in range(max(0,N.degree()-D.degree()+1)):
  basis.append(D*V**j);tags.append(('poly',j))
 for a,m in merged:
  for k in range(1,m+1):
   quot,rem=divmod(D,(1+a*V)**k);assert not rem
   basis.append(quot);tags.append(('pole',a,k))
 size=len(basis);assert size==max(D.degree(),N.degree()+1)
 mat=[[basis[j][i] for j in range(size)]+[N[i]] for i in range(size)]
 for col in range(size):
  piv=next(i for i in range(col,size) if mat[i][col])
  mat[col],mat[piv]=mat[piv],mat[col]
  pivot=mat[col][col];mat[col]=[x/pivot for x in mat[col]]
  for i in range(size):
   if i!=col and mat[i][col]:
    fact=mat[i][col];mat[i]=[a-fact*b for a,b in zip(mat[i],mat[col])]
 coeff=[mat[i][-1] for i in range(size)]
 assert sum((q*p for q,p in zip(coeff,basis)),P([]))==N
 pol=P([]);parts=[]
 for q,tag in zip(coeff,tags):
  if not q:continue
  if tag[0]=='poly':pol+=q*V**tag[1]
  else:parts.append((tag[1],tag[2],q))
 return list(pol),parts,size

def own_integral(b,N,factors):
 pol,parts,size=own_decompose(N,factors)
 val=sum((ar(q/(b+j+1)) for j,q in enumerate(pol)),arb(0))
 for a,k,q in parts:
  J=(-ar(a)).hypgeom_2f1(arb(k),ar(b+1),ar(b+2),bc=True,abc=True)/ar(b+1)
  assert J.is_finite();val+=ar(q)*J
 return val,size,len(parts)

def main():
 ctx.prec=2048;start=time.monotonic()
 frozen=json.loads((ROOT/'source/N4_result.json').read_text())
 assert frozen['code_sha256']==sha(ROOT/'source/moments.py')
 assert frozen['proof_sha256']==sha(ROOT/'source/N4_PROOF.md')
 fixtures=[]
 for row in frozen['fixtures']:
  fixtures.append((row['name'],Q(row['b']),P([Q(c) for c in row['numerator']]),[(Q(a),m) for a,m in row['factors']],row))
 for k in range(2,9):
  fixtures.append((f'resonance_{k}',Q(k-2),P([1,-2,1]),[(Q(99),k)],None))
 fixtures.append(('near_integrability_endpoint',Q(-999,1000),P([1,-3,2]),[(Q(99),2),(Q(9999),3)],None))
 rows=[]
 for name,b,N,factors,stored in fixtures:
  tick=time.monotonic();own,size,nparts=own_integral(b,N,factors)
  theirs,record=peer.integral(b,N,factors)
  assert own.is_finite() and own.overlaps(theirs)
  assert own.rel_accuracy_bits()>250 and theirs.rel_accuracy_bits()>250
  comparisons={'rerun_peer_overlap':True}
  if stored:
   for key in ['value','independent_value']:
    comparisons[key+'_overlap']=bool(own.overlaps(arb(stored[key])))
   assert all(comparisons.values())
  rows.append({'name':name,'b':str(b),'numerator':[str(c) for c in N],
   'factors':[[str(a),m] for a,m in factors],'coefficient_system_dimension':size,
   'principal_parts':nparts,'own':own.str(100),'peer':theirs.str(100),
   'comparisons':comparisons,'accuracy_bits':own.rel_accuracy_bits(),
   'elapsed_seconds':time.monotonic()-tick})
  print(name,'passed',time.monotonic()-tick,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,
  'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(__file__),
  'source_hashes':{p.name:sha(p) for p in sorted((ROOT/'source').iterdir()) if p.is_file()},
  'fixtures':rows,'all_passed':True,'elapsed_seconds':time.monotonic()-start,
  'verdict':'CONFIRMED scalar primitive and listed fixtures; no candidate norm claim'}
 dest=ROOT/'verification/result.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
 (ROOT/'verification/installed_hypgeom_doc.txt').write_text(arb.hypgeom_2f1.__doc__+'\n')
 print('DONE',len(rows),'fixtures',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
