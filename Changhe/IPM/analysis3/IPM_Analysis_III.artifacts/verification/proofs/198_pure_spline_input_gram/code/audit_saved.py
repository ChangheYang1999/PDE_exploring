"""Check outward serialization and the exact-dyadic matrix certificate afresh."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from flint import arb,arb_mat,ctx
ctx.prec=768;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];ROOT=TOP.parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):
 q=F(q);return arb(q.numerator)/q.denominator

def bounds(d):return tuple(F(int(d[k][0]))*F(2)**int(d[k][1]) for k in ('lo_binary','hi_binary'))
def bb(d):
 lo,hi=bounds(d);assert lo<=hi;return aa((lo+hi)/2)+arb(0,aa((hi-lo)/2).upper())
def rowbound(M):return max(sum(abs(M[i,j]) for j in range(M.ncols())).upper() for i in range(M.nrows()))
def main():
 started=time.monotonic();inp=TOP/'evidence/gram_512_640.json';d=json.loads(inp.read_text());assert sha(TOP/'PROOF.md')==d['proof_sha256'];assert sha(TOP/'code/check.py')==d['script_sha256']
 assert sha(ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz')==d['source_sha256']
 a=[[F(x) for x in row] for row in d['angular_rational_matrix']]
 assert a[0][0]>0 and a[0][0]*a[1][1]-a[0][1]**2>0
 determinant=sum(((-1)**i*a[0][i]*(a[1][(i+1)%3]*a[2][(i+2)%3]-a[1][(i+2)%3]*a[2][(i+1)%3])*(-1)**i for i in range(3)),F(0));assert determinant>0
 r=d['runs']['S1M3'];Tfile=TOP/'evidence/S1M3_whitening.npz';assert sha(Tfile)==r['comparison']['T_file_sha256']
 Tn=np.load(Tfile,allow_pickle=False)['T'];assert hashlib.sha256(Tn.tobytes()).hexdigest()==r['comparison']['T_sha256']
 T=arb_mat([[aa(F.from_float(float(x))) for x in row] for row in Tn]);G=arb_mat([[bb(x) for x in row] for row in r['exact_scaled_input_Gram']]);n=G.nrows();assert n==52
 source=ROOT/'proofs/183_s1m3_floating_audit/evidence/parts_matrices.npz';assert sha(source)==r['floating_matrix_sha256'];idx=r['selected_new_indices'];Gn=np.load(source,allow_pickle=False)['G'][np.ix_(idx,idx)]
 GF=arb_mat([[aa(F.from_float(float(x))) for x in row] for row in Gn]);I=arb_mat(np.eye(n,dtype=int).tolist())
 e=rowbound(T.transpose()*G*T-I);dd=rowbound(T.transpose()*(GF-G)*T);assert e<1;rel=dd/(1-e);assert rel<aa(F(237,100000000))
 for tag,r in d['runs'].items():assert bb(r['maximum_relative_stored_strain_error'])<aa(F(271,10**18));assert sha(TOP/'evidence/source'/f'{tag}_meta.json')==r['metadata_sha256']
 out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','precision_bits':768,'serialized_radial_Gram_entries':26**2,'angular_rational_Sylvester':'positive','angular_determinant_exact':str(determinant),'input_relative_error_upper':rel.upper().str(50),'accepted_relative_Gram_error':'237/100000000','accepted_relative_strain_error':'271/1000000000000000000','source_gram_certificate_sha256':sha(inp),'script_sha256':sha(__file__),'proof_sha256':sha(TOP/'PROOF.md'),'seconds':time.monotonic()-started,'scope':'Exact input Gram and strain only; no image norm or complement inverse.'}
 (TOP/'evidence/audit_saved_768.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
