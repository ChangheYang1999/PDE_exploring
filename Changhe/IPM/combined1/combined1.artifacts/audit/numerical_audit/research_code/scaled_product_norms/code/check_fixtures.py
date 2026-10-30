"""Coefficient-level verification before full-candidate Laurent products."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,time,random,sys
from flint import fmpq as Q,fmpq_poly as Poly
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/scaled_product_norms';sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).resolve().parent));import packed as P
Rat=P.Rat
spec=importlib.util.spec_from_file_location('own_synthetic_leibniz_check',ROOT/'research/n3_synthetic_field_audit/code/check.py');H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()

def ownref(field):return {key:Rat(A.P,A.powers) for key,A in field.items()}
def direct(C,S):
 out={}
 for (ell,kind,n),A in C.items():
  for (ell2,kind2,n2),D in S.items():
   for k,m,q in H.products(kind,n,kind2,n2):P.add(out,(ell+ell2,k,m),A*D*q)
 return out

def equal(A,C):
 assert set(A)==set(C),(set(A)^set(C))
 for key in A:assert A[key]==C[key],key
 return len(A)

def main():
 started=time.monotonic();out=B/'verification/fixtures.json';assert not out.exists();checks=[];rng=random.Random(908271)
 for case in range(24):
  fields=[]
  for kind in ['c','s']:
   field={}
   for ell in [0,1,3]:
    for n in ([0,1,4] if kind=='c' else [1,3,6]):
     powers=tuple(rng.randrange(3) if i in [0,1] else 0 for i in range(4));poly=Poly([Q(rng.randint(-7,7),rng.randint(1,11)) for k in range(1+rng.randrange(5))]);P.add(field,(ell,kind,n),Rat(poly,powers))
   fields.append(field)
  C,S=fields;new=P.product(C,S);old=direct(C,S);count=equal(new,old);checks.append({'label':f'manufactured_{case}','exact_component_count':count,'all_denominator_identities':True})
 rawpath=ROOT/'research/n3_synthetic_field_audit/data/synthetic.json';raw=json.loads(rawpath.read_text());jet=P.J.ScaledRadial(raw);F,Bg=P.residual(jet);D=P.all_derivatives(F,jet.delta,2)
 ownD,ownBg=H.own_fields(H.J.ScaledRadial(raw))
 for key,field in ownD.items():checks.append({'label':f'synthetic_F_derivative_{key}','exact_component_count':equal(D[key],ownref(field)),'all_denominator_identities':True})
 for label,field in ownBg.items():checks.append({'label':f'synthetic_{label}','exact_component_count':equal(Bg[label],ownref(field)),'all_denominator_identities':True})
 # Degenerate empty factors have no exceptional branch or center.
 assert P.product({},Bg['rho_x'])=={} and P.product(Bg['u1'],{})=={}
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS exact Laurent products and compact derivatives on manufactured fields and complete six-generator fixture; production candidate norms OPEN','manufactured_fields':24,'checks':checks,'exact_component_count':sum(r['exact_component_count'] for r in checks),'elapsed_seconds':time.monotonic()-started,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in [B/'PROOF.md',B/'code/packed.py',Path(__file__),rawpath,ROOT/'research/n3_synthetic_field_audit/code/check.py',ROOT/'research/n3_synthetic_field_audit/verification/result.json',ROOT/'research/joint_scaled_factored_weak/code/fields_joint.py']}}
 accepted=json.loads((ROOT/'research/n3_synthetic_field_audit/verification/result.json').read_text())
 for rel,h in accepted['inputs'].items():assert sha(ROOT/rel)==h;result['inputs'][rel]=h
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('FIXTURES_PASS',len(checks),result['exact_component_count'],'seconds',result['elapsed_seconds'],'utc',result['utc'],'sha256',sha(out),flush=True)
if __name__=='__main__':main()
