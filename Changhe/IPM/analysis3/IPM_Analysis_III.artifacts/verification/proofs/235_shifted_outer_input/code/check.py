"""Independent exact shifted outer input and regularity check. No output certificate."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import prod
import ast,json,hashlib,shutil,time
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3];TOP=Path(__file__).resolve().parents[1];E=TOP/'evidence'
SRC=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
MOD=SRC.parent.parent/'src/modal_fit.py';RUN=ROOT.parent/'s2-num/work/runs/S1J1'
ctx.threads=1

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def pack(x):
 def dy(x):n,e=x.mid().man_exp();return [str(n),int(e)]
 return {'ball':x.str(44),'lo_binary':dy(x.lower()),'hi_binary':dy(x.upper())}
def rank(rows):
 a=[r[:] for r in rows];nr=len(a);nc=len(a[0]);r=0
 for c in range(nc):
  j=next((j for j in range(r,nr) if a[j][c]),None)
  if j is None:continue
  a[r],a[j]=a[j],a[r];d=a[r][c];a[r]=[v/d for v in a[r]]
  for j in range(nr):
   if j!=r:
    d=a[j][c];a[j]=[x-d*y for x,y in zip(a[j],a[r])]
  r+=1
  if r==nr:break
 return r,a

def main():
 start=time.monotonic();assert sha(SRC)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 z=np.load(SRC,allow_pickle=False);k=F.from_float(float(z['k']));tp=F.from_float(float(z['knots'][-1]));tj=tp+1
 pairs=None
 for node in ast.parse(MOD.read_text()).body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='OUTER_JL' for t in node.targets):pairs=ast.literal_eval(node.value)
 assert pairs==[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
 a=[k-3-j*(1-k)-2*l for j,l in pairs];assert 0<k<F(1,4) and tj>0 and len(set(a[1:]))==9 and max(a[1:])==a[1]
 assert max(F(27,4)+x+y for x in a[1:] for y in a[1:])<0
 B=[];jets=[];laplace_checks=0
 for q in range(5,10):
  b=[F(0)]*10;b[q]=1
  for i in range(1,5):b[i]=-prod((a[q]-a[j])/(a[i]-a[j]) for j in range(1,5) if j!=i)
  jj=[sum(b[i]*a[i]**n for i in range(1,10)) for n in range(9)]
  pq=prod(a[q]-a[i] for i in range(1,5));assert jj[:4]==[0]*4 and jj[4]==pq!=0
  e1=sum(a[1:5]);h2=sum(a[i]*a[j] for i in range(1,5) for j in range(i,5))
  assert jj[5]==pq*(a[q]+e1) and jj[6]==pq*(a[q]**2+e1*a[q]+h2)
  # Check the full rational identity via ten rational values. Numerator degree <=4, so five would suffice.
  for s in range(10):
   assert sum(b[i]/(F(s)-a[i]) for i in range(1,10))==pq/prod(F(s)-a[i] for i in [1,2,3,4,q]);laplace_checks+=1
  B.append(b);jets.append(jj)
 J=[[jets[q][n] for q in range(5)] for n in range(4,9)];assert [rank(J[:n])[0] for n in range(1,6)]==[1,2,3,4,5]
 R=[[sum(B[q][i]*B[r][j]/(-F(27,4)-a[i]-a[j]) for i in range(1,10) for j in range(1,10)) for r in range(5)] for q in range(5)]
 L=[[F(i==j) for j in range(5)] for i in range(5)];D=[]
 for i in range(5):
  d=R[i][i]-sum(L[i][j]**2*D[j] for j in range(i));assert d>0;D.append(d)
  for r in range(i+1,5):L[r][i]=(R[r][i]-sum(L[r][j]*L[i][j]*D[j] for j in range(i)))/d
 assert all(R[i][j]==sum(L[i][v]*D[v]*L[j][v] for v in range(5)) for i in range(5) for j in range(5))
 meta=json.loads((RUN/'meta.json').read_text());assert meta['k']==str(k);assert meta['mode']=='S1' and meta['n_new']==38 and meta['NMAX']==530
 assert meta['settings']['out_shift']=='1' and meta['settings']['drop']=='+out' and meta['settings']['vm']=='exact_template'
 assert meta['cells_expected']==list(range(1569));sels=[];scales=[]
 for i,new in enumerate(meta['new']):
  if new[1].startswith('out'):
   kind,label,m=new;assert kind=='rem' and m==1
   partners=[j for j,l in enumerate(meta['labels']) if l==label];assert len(partners)==2
   j0=next(j for j in partners if meta['col_m'][j]==0);jm=next(j for j in partners if meta['col_m'][j]==m)
   assert meta['column_scales'][j0]==meta['column_scales'][jm]
   assert meta['labels'][j0]==meta['labels'][jm]==label and meta['col_m'][j0]==0 and meta['col_m'][jm]==1
   sels.append(i);scales.append(F.from_float(float(meta['column_scales'][jm])))
 assert [meta['new'][i][1] for i in sels]==['out5','out6','out7','out8','out9'];assert all(s>0 for s in scales)
 expected={'fsec_producer_frozen.py':'e9300283cfb0118acba28675fcbdad56fde2ee1cd9ea43cfbd6a6c1c5f3b67fc','basis_producer_frozen.py':'1ecb37102ff55e44aff34b6ad6a4ebc53e75a1d72006150dc0dc27d7abf3e7ee'}
 for name,digest in expected.items():assert sha(RUN/name)==digest
 outputs=[];matrices=[]
 for prec in (512,640):
  ctx.prec=prec
  K=8*aa(F(3,2)).gamma()*aa(F(1,4)).gamma()/aa(F(7,4)).gamma()
  Kalt=arb(16)/3/(2*arb.pi()).sqrt()*aa(F(1,4)).gamma()**2;assert K.overlaps(Kalt) and K>0
  pre=aa(F(27,4)*tj).exp();G=[[K*pre*aa(R[q][r])/aa(scales[q]*scales[r]) for r in range(5)] for q in range(5)]
  C=[]
  for q in range(5):
   sr=sum(B[q][i]/(-2-a[i]) for i in range(1,10));qq=q+5
   assert sr==prod(a[qq]-a[i] for i in range(1,5))/prod(-2-a[i] for i in [1,2,3,4,qq])
   C.append(aa(F(3,8)*sr)*aa(2*tj).exp()/aa(scales[q]))
  matrices.append(G);outputs.append({'precision_bits':prec,'angular_constant':pack(K),'scaled_input_Gram':[[pack(x) for x in row] for row in G],'exact_scaled_strain':[pack(x) for x in C]})
 assert all(matrices[0][i][j].overlaps(matrices[1][i][j]) for i in range(5) for j in range(5))
 for p in [SRC,MOD,RUN/'meta.json',RUN/'PRODUCER_SHA256.txt']+[RUN/n for n in expected]:shutil.copyfile(p,E/'source'/p.name)
 exact={'k':str(k),'t_plus':str(tp),'t_join':str(tj),'outer_jl':pairs,'alphas':list(map(str,a)),'B':[[str(x) for x in row] for row in B],'jets_0_to_8':[[str(x) for x in row] for row in jets],'radial_Gram':[[str(x) for x in row] for row in R],'LDL_diagonal':list(map(str,D)),'scales':list(map(str,scales))}
 (E/'exact_inputs.json').write_text(json.dumps(exact,indent=2)+'\n')
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_INPUT_ONLY','original_trial_sha256':sha(SRC),'original_pair_source_sha256':sha(MOD),'proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(__file__),'exact_input_sha256':sha(E/'exact_inputs.json'),'metadata_sha256':sha(RUN/'meta.json'),'producer_sha256':expected,'selected_new_indices':sels,'high_input_dimension':3,'high_graph_dimension':2,'jump_constraint_ranks':[1,2,3,4,5],'laplace_identity_checks':laplace_checks,'runs':outputs,'source_files':{p.name:sha(p) for p in sorted((E/'source').iterdir())},'scope':'Exact input Gram and joins only. No output certificate, high-norm singular value or continuum inverse.','seconds':time.monotonic()-start}
 (E/'check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('runs','source_files')},indent=2),flush=True)
if __name__=='__main__':main()
