from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
r=Path('research/finite_family_interval_exclusion');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();paths={Path(__file__),r/'PROOF.md'};edges=[];sources=[]
for f,key in [('research/general_beta_spectral_fields/bindings.json','hashes'),('research/spectral_representation_bias/bindings.json','hashes'),('research/meromorphic_logarithmic_obstruction/verification/audit_bindings.json','sha256'),('research/remaining_beta_local_obstruction/bindings.json','hashes')]:
 p=Path(f);d=json.loads(p.read_text());paths.add(p)
 for file,h in d[key].items():assert sha(file)==h,(p,file);paths.add(Path(file));edges.append([str(p),file,h])
 sources.append({'manifest':f,'sha256':sha(p),'status':d.get('status'),'unique_paths':len(d[key])})
lo,hi=Q(5,2),Q(7,2);m=lambda b:b/(b-2);assert m(hi)==Q(7,3) and m(lo)==5
integers=[k for k in range(2,7) if m(hi)<=k<=m(lo)];assert integers==[3,4,5]
rows=[]
for k in integers:
 b=Q(2*k,k-1);assert lo<=b<=hi and m(b)==k
 rows.append({'m':k,'beta':str(b),'b':str(b-2),'p':str(1/b),'eta6_exponent_m_over3':str(Q(k,3)),'local_obstruction':67 if b==3 else 112})
assert [row['beta'] for row in rows]==['3','8/3','5/2']
# Equality to the beta3 formulas at rational manufactures; all powers integral in this specialization.
manufactures=[]
for x,e,s in [(Q(1,3),Q(2,5),Q(3,2)),(Q(0),Q(0),Q(1)),(Q(5),Q(7),Q(1,2))]:
 generalE=x*x+(1+(e/s)**6)**int(Q(3,3));specialE=1+x*x+(e/s)**6;assert generalE==specialE
 manufactures.append({'x':str(x),'e':str(e),'s':str(s),'E':str(specialE)})
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_DEPENDENCY_BINDINGS_AND_EXACT_PARAMETER_ENUMERATION','dependency_manifests':sources,'parameter_cases':rows,'beta3_E_manufactures':manufactures,'hashes':{str(p.resolve()):sha(p) for p in sorted(paths)},'direct_edges':edges,'scope':'Dependency integrity and exact algebra only; no rerun of analytic proofs or new candidate certificate.'};(r/'verification/checks.json').write_text(json.dumps(o,indent=2)+'\n');print(o['status'],len(o['hashes']),'unique files',len(edges),'edges')
