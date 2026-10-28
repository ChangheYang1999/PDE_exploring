"""Input-only exact strain-hyperplane certificate. No output matrix is read."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time
import mpmath as mp
from flint import arb,arb_mat,ctx
ctx.prec=640
ctx.threads=1
mp.mp.dps=75
TOP=Path(__file__).resolve().parents[1]
ROOT=TOP.parents[1]
E=TOP/'evidence'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator
def bb(d):
 lo,hi=[F(int(d[k][0]))*F(2)**int(d[k][1]) for k in ('lo_binary','hi_binary')]
 assert lo<=hi
 return aa((lo+hi)/2)+arb(0,aa((hi-lo)/2).upper())
def ff(x):
 n,e=x.mid().man_exp();return F(int(n))*F(2)**int(e)
def mm(x):
 x=F(x);return mp.mpf(x.numerator)/x.denominator
def mf(x):
 s,m,e,_=x._mpf_;return F((-1)**s*int(m))*F(2)**int(e)
def pack(x):
 def dy(v):n,e=v.mid().man_exp();return [str(n),int(e)]
 return {'ball':x.str(45),'lo_binary':dy(x.lower()),'hi_binary':dy(x.upper())}
def norm(x): return sum(x[i,0]**2 for i in range(x.nrows())).sqrt()
def rowbound(x): return max(sum(abs(x[i,j]) for j in range(x.ncols())).upper() for i in range(x.nrows()))
def main():
 start=time.monotonic()
 certp=ROOT/'proofs/239_s1j1_full_input/evidence/check.json'
 conp=ROOT/'proofs/240_s1j1_high_intersections/evidence/exact_constraints.json'
 metap=ROOT/'proofs/242_s1j1_completed_audit/evidence/source/meta.json'
 src=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
 assert sha(certp)=='c6d2e2c862f5023e90f24bb8ec550e655ea75e153ba9ccf22abb9f2599079858'
 assert sha(conp)=='96f271d72ec6190011166d747dff391d783cedff8203b97eb31a87f49bc05344'
 cert=json.loads(certp.read_text());con=json.loads(conp.read_text());meta=json.loads(metap.read_text())
 assert sha(metap)==cert['metadata_sha256'];assert sha(src)==cert['source_sha256']
 G=arb_mat([[bb(v) for v in row] for row in cert['runs'][1]['scaled_input_Gram']])
 a=arb_mat([[bb(v)] for v in cert['runs'][1]['exact_scaled_strain']])
 bq=[F.from_float(float(v)) for v in meta['cvec']]
 b=arb_mat([[aa(v)] for v in bq])
 assert a[13,0]>0 and bq[13]>0
 assert 'sp10' in str(meta['new'][13])
 out={};whiteners={}
 for name,n in [('whole',38),('high_input',32),('high_graph',29)]:
  if name=='whole':q=[[F(i==j) for j in range(38)] for i in range(38)]
  else:
   qr=[[F(v) for v in row] for row in con[name]['basis_columns']]
   q=[list(v) for v in zip(*qr)]
   assert len(q)==38 and len(q[0])==n
   # The exact jump rows vanish on the pure column sp10.
   for row in con[name]['matrix']:assert F(row[13])==0
  Q=arb_mat([[aa(v) for v in row] for row in q])
  GW=Q.transpose()*G*Q;av=Q.transpose()*a;bv=Q.transpose()*b
  gm=mp.matrix([[mm(ff(GW[i,j])) for j in range(n)] for i in range(n)])
  Tm=(mp.cholesky(gm)**-1).T
  tq=[[mf(Tm[i,j]) for j in range(n)] for i in range(n)]
  T=arb_mat([[aa(v) for v in row] for row in tq])
  I=arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
  eps=rowbound(T.transpose()*GW*T-I);assert eps<1
  D=norm(T.transpose()*(av-bv))/(1-eps).sqrt()
  A=norm(T.transpose()*av)/(1+eps).sqrt();assert A>0
  delta=D.upper()/A.lower();assert delta<1
  out[name]={'n':n,'exact_c_kernel_dimension':n-1,'binary_c_kernel_dimension':n-1,'whitening_defect':pack(eps),'functional_error_upper':pack(D.upper()),'functional_norm_lower':pack(A.lower()),'relative_projection_error_upper':pack(delta.upper()),'projection_minimum_norm_factor_lower':pack((1-delta**2).sqrt().lower())}
  whiteners[name]=[[str(v) for v in row] for row in tq]
 (E/'dyadic_whiteners.json').write_text(json.dumps(whiteners)+'\n')
 deps={str(p.relative_to(ROOT)):sha(p) for p in [certp,conp,metap]}
 ans={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CERTIFIED_INPUT_HYPERPLANE_COMPARISON_ONLY','proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(__file__),'original_archive_sha256':sha(src),'dependencies':deps,'positive_reference_column':13,'exact_reference_strain':pack(a[13,0]),'binary_reference_strain':str(bq[13]),'spaces':out,'whiteners_sha256':sha(E/'dyadic_whiteners.json'),'precision_bits':640,'seconds':time.monotonic()-start,'scope':'Exact input constraints only. No output matrix read, no operator or singular-value certificate.'}
 (E/'check.json').write_text(json.dumps(ans,indent=2)+'\n')
 print(json.dumps({'date':ans['date'],'seconds':ans['seconds'],'spaces':{k:{t:v[t] if isinstance(v[t],int) else v[t]['ball'] for t in ('n','exact_c_kernel_dimension','functional_error_upper','functional_norm_lower','relative_projection_error_upper')} for k,v in out.items()}}),flush=True)
if __name__=='__main__':main()
