"""All38 exact S1J1 input columns, from original rational knots and exponents."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from math import prod
from datetime import datetime,timezone
import ast,hashlib,json,importlib.util,time,shutil
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3];TOP=Path(__file__).resolve().parents[1];E=TOP/'evidence'
SRC=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz';MOD=SRC.parent.parent/'src/modal_fit.py'
RUN=ROOT.parent/'s2-num/work/runs/S1J1'
sp=importlib.util.spec_from_file_location('verified_radial_moments',ROOT/'proofs/198_pure_spline_input_gram/code/check.py');r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
aa=r.aa;pack=r.pack;sha=r.sha;ctx.threads=1

def solve(A,b):
 n=len(b);M=[list(a)+[v] for a,v in zip(A,b)]
 for j in range(n):
  p=next(i for i in range(j,n) if M[i][j]);M[j],M[p]=M[p],M[j]
  q=M[j][j];M[j]=[v/q for v in M[j]]
  for i in range(n):
   if i!=j:
    q=M[i][j];M[i]=[x-q*y for x,y in zip(M[i],M[j])]
 ans=[M[i][-1] for i in range(n)];assert all(sum(x*y for x,y in zip(a,ans))==v for a,v in zip(A,b));return ans

def finite(knots,pieces,method):
 G=[[arb(0) for j in range(30)] for i in range(30)];C=[arb(0) for i in range(30)];count=0
 for ci,ps0 in enumerate(pieces):
  a,b=knots[ci+7:ci+9];width=b-a;cuts=[a]+([F(0)] if a<0<b else [])+[b]
  for lo,hi in zip(cuts,cuts[1:]):
   count+=1;h=hi-lo;ps={i:r.transform(p,(lo-a)/width,h/width) for i,p in ps0.items() if i<30}
   lam=F(-1,2) if hi<=0 else F(27,4);ms=r.moments(lam*h,14,method);cs=r.moments(2*h,7,method)
   pre=aa(h)*aa(lam*lo).exp();cpre=aa(h)*aa(2*lo).exp()
   for i,p in ps.items():
    C[i]+=cpre*sum((aa(v)*cs[j] for j,v in enumerate(p)),arb(0))
    for j,q in ps.items():G[i][j]+=pre*sum((aa(v)*ms[n] for n,v in enumerate(r.mul(p,q))),arb(0))
 assert count==28;return G,C

def main():
 start=time.monotonic();assert sha(SRC)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 data=np.load(SRC,allow_pickle=False);assert int(data['p'])==7
 fine=list(map(r.rat,data['knots']));k=r.rat(data['k']);tm,tp=fine[0],fine[-1];tj=tp+1
 assert tm<0<tp<tj and fine[:8]==[tm]*8 and fine[-8:]==[tp]*8
 knots=[tm]*8+fine[8:-8][::60]+[tp]*8;assert len(knots)-8==34
 pieces=[];replay=[];checks=0
 for span in range(7,len(knots)-8):
  ps=r.cox(knots,span);ds={};total=[F(0)]*8
  for i,p in ps.items():
   ds[i]=r.db.deboor_poly(knots,[F(i==j) for j in range(34)],7,span);assert ds[i]==p;checks+=1;total=r.padd(total,p)
  assert total==[F(1)]+[F(0)]*7;pieces.append(ps);replay.append(ds)
 assert len(pieces)==27 and checks==216
 for ci in range(26):
  w1=knots[ci+8]-knots[ci+7];w2=knots[ci+9]-knots[ci+8]
  for i in range(34):assert r.db.jets(pieces[ci].get(i,[F(0)]*8),w1,True)==r.db.jets(pieces[ci+1].get(i,[F(0)]*8),w2,False)
 ex=[F(2*j) for j in range(1,8)];V=[[x**n for x in ex[:4]] for n in range(4)];D=[];jetchecks=0
 for i in range(4):
  jets=r.db.jets(pieces[0][i],knots[8]-knots[7],False)[:4];d=solve(V,jets)+[F(0)]*3;D.append(d)
  assert [sum(dj*x**n for dj,x in zip(d,ex)) for n in range(4)]==jets;jetchecks+=4
 for q in range(4,7):
  d=[-prod((ex[q]-ex[l])/(ex[j]-ex[l]) for l in range(4) if l!=j) for j in range(4)]+[F(int(j==q)) for j in range(4,7)]
  assert [sum(dj*x**n for dj,x in zip(d,ex)) for n in range(4)]==[0]*4;D.append(d);jetchecks+=4
  assert solve(V,[ex[q]**n for n in range(4)])==[-v for v in d[:4]]
 for i in range(30):assert r.db.jets(pieces[-1].get(i,[F(0)]*8),knots[-8]-knots[-9],True)[:4]==[0]*4
 for i in range(4,30):assert r.db.jets(pieces[0].get(i,[F(0)]*8),knots[8]-knots[7],False)[:4]==[0]*4
 RI=[[sum(di*dj/(x+y-F(1,2)) for di,x in zip(D[i],ex) for dj,y in zip(D[j],ex)) for j in range(7)] for i in range(7)]
 CI=[sum(v/(2+x) for v,x in zip(d,ex)) for d in D]
 # Original finite literal list, without executing the producer.
 pairs=None
 for node in ast.parse(MOD.read_text()).body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='OUTER_JL' for t in node.targets):pairs=ast.literal_eval(node.value)
 assert pairs==[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
 al=[k-3-j*(1-k)-2*l for j,l in pairs];BO=[]
 assert len(set(al[1:]))==9 and max(F(27,4)+x+y for x in al[1:] for y in al[1:])<0
 for q in range(5,10):
  b=[F(0)]*10;b[q]=1
  for i in range(1,5):b[i]=-prod((al[q]-al[j])/(al[i]-al[j]) for j in range(1,5) if j!=i)
  assert [sum(bi*x**n for bi,x in zip(b,al)) for n in range(4)]==[0]*4;BO.append(b)
 RO=[[sum(BO[q][i]*BO[v][j]/(-F(27,4)-al[i]-al[j]) for i in range(1,10) for j in range(1,10)) for v in range(5)] for q in range(5)]
 CO=[sum(bi/(-2+x*-1) for bi,x in zip(b,al)) for b in BO]
 # Exact original reconstruction matches235 rational inputs, a dependency check only.
 oldexact=json.loads((ROOT/'proofs/235_shifted_outer_input/evidence/exact_inputs.json').read_text())
 assert RO==[[F(v) for v in row] for row in oldexact['radial_Gram']]
 assert BO==[[F(v) for v in row] for row in oldexact['B']]
 meta=json.loads((RUN/'meta.json').read_text());labels=[f'sp{i}+in' for i in range(4)]+[f'in{i}' for i in range(5,8)]+[f'sp{i}' for i in range(4,30)]+[f'out{i}' for i in range(5,10)]
 assert meta['new']==[['rem',label,1] for label in labels];assert meta['cells_expected']==list(range(1569)) and meta['n_new']==38 and meta['NMAX']==530 and meta['k']==str(k)
 assert meta['settings']['out_shift']=='1' and meta['settings']['drop']=='+out' and meta['settings']['vm']=='exact_template'
 scales=[]
 for label in labels:
  ids=[i for i,x in enumerate(meta['labels']) if x==label];assert len(ids)==2
  assert sorted(meta['col_m'][i] for i in ids)==[0,1] and meta['column_scales'][ids[0]]==meta['column_scales'][ids[1]]
  scales.append(r.rat(meta['column_scales'][ids[0]]))
 assert all(s>0 for s in scales)
 hashes={'fsec_producer_frozen.py':'e9300283cfb0118acba28675fcbdad56fde2ee1cd9ea43cfbd6a6c1c5f3b67fc','basis_producer_frozen.py':'1ecb37102ff55e44aff34b6ad6a4ebc53e75a1d72006150dc0dc27d7abf3e7ee'}
 for name,digest in hashes.items():assert sha(RUN/name)==digest
 outs=[];grams=[];strains=[]
 for prec,method,pp in [(512,'taylor',pieces),(640,'antiderivative',replay)]:
  ctx.prec=prec;RF,CF=finite(knots,pp,method);G=[[arb(0) for _ in range(38)] for _ in range(38)];C=[arb(0) for _ in range(38)]
  K=8*aa(F(3,2)).gamma()*aa(F(1,4)).gamma()/aa(F(7,4)).gamma();Kalt=arb(16)/3/(2*arb.pi()).sqrt()*aa(F(1,4)).gamma()**2;assert K.overlaps(Kalt) and K>0
  fi={i:i for i in range(4)}|{i:i-3 for i in range(7,33)}
  for i,bi in fi.items():
   C[i]+=CF[bi]
   for j,bj in fi.items():G[i][j]+=RF[bi][bj]
  for i in range(7):
   C[i]+=aa(2*tm).exp()*aa(CI[i])
   for j in range(7):G[i][j]+=aa(-tm/2).exp()*aa(RI[i][j])
  for i in range(5):
   C[i+33]=aa(2*tj).exp()*aa(CO[i])
   for j in range(5):G[i+33][j+33]=aa(F(27,4)*tj).exp()*aa(RO[i][j])
  C=[aa(F(3,8))*x/aa(s) for x,s in zip(C,scales)]
  G=[[K*x/aa(scales[i]*scales[j]) for j,x in enumerate(row)] for i,row in enumerate(G)]
  assert all(G[i][i]>0 for i in range(38));assert all(G[i][j]==G[j][i] for i in range(38) for j in range(38))
  assert all(G[i][j].is_zero() for i in range(33) for j in range(33,38))
  errors=[abs(aa(r.rat(f))-c) for f,c in zip(meta['cvec'],C)]
  rel=[abs(aa(r.rat(f))/c-1) for f,c in zip(meta['cvec'],C) if not c.contains(0)]
  outs.append({'precision_bits':prec,'moment_method':method,'angular_constant':pack(K),'scaled_input_Gram':[[pack(x) for x in row] for row in G],'exact_scaled_strain':list(pack(x) for x in C),'maximum_stored_strain_absolute_error':pack(max(x.upper() for x in errors)),'maximum_stored_nonzero_strain_relative_error':pack(max(x.upper() for x in rel))})
  grams.append(G);strains.append(C)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'precision':prec,'method':method,'seconds':time.monotonic()-start}),flush=True)
 assert all(grams[0][i][j].overlaps(grams[1][i][j]) for i in range(38) for j in range(38))
 assert all(strains[0][i].overlaps(strains[1][i]) for i in range(38))
 old=json.loads((ROOT/'proofs/235_shifted_outer_input/evidence/check.json').read_text())
 for i in range(5):
  assert strains[1][i+33].overlaps(r.unpack(old['runs'][1]['exact_scaled_strain'][i]))
  for j in range(5):assert grams[1][i+33][j+33].overlaps(r.unpack(old['runs'][1]['scaled_input_Gram'][i][j]))
 deps=[ROOT/'proofs/198_pure_spline_input_gram/code/check.py',ROOT/'proofs/04_modal_scalar/code/recompute.py',ROOT/'proofs/198_pure_spline_input_gram/PROOF.md',ROOT/'proofs/235_shifted_outer_input/PROOF.md',ROOT/'proofs/235_shifted_outer_input/AUDIT_CLARIFICATIONS.md',ROOT/'proofs/235_shifted_outer_input/evidence/exact_inputs.json',ROOT/'proofs/235_shifted_outer_input/evidence/check.json']
 for p in [SRC,MOD,RUN/'meta.json',RUN/'PRODUCER_SHA256.txt']+[RUN/n for n in hashes]:shutil.copyfile(p,E/'source'/p.name)
 exact={'coarse_knots':list(map(str,knots)),'k':str(k),'inner_exponents':list(map(str,ex)),'inner_coefficients':[[str(x) for x in row] for row in D],'inner_radial_Gram':[[str(x) for x in row] for row in RI],'inner_radial_strain':list(map(str,CI)),'outer_exponents':list(map(str,al)),'outer_B':[[str(x) for x in row] for row in BO],'outer_radial_Gram':[[str(x) for x in row] for row in RO],'outer_radial_strain':list(map(str,CO)),'labels':labels,'scales':list(map(str,scales))}
 (E/'exact_inputs.json').write_text(json.dumps(exact,indent=2)+'\n')
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_INPUT_ONLY','source_sha256':sha(SRC),'pair_source_sha256':sha(MOD),'script_sha256':sha(__file__),'proof_sha256':sha(TOP/'PROOF.md'),'metadata_sha256':sha(RUN/'meta.json'),'exact_inputs_sha256':sha(E/'exact_inputs.json'),'producer_sha256':hashes,'dependencies':{str(p.relative_to(ROOT)):sha(p) for p in deps},'source_files':{p.name:sha(p) for p in sorted((E/'source').iterdir())},'n':38,'coarse_spans':27,'integration_pieces':28,'active_polynomial_checks':checks,'exact_C6_column_joins':884,'inner_jet_checks':jetchecks,'overlap_Gram_checks':38**2,'overlap_strain_checks':38,'block_sizes':[33,5],'runs':outs,'seconds':time.monotonic()-start,'scope':'Exact input and strain only; no output matrix, finite inverse or complement bound.'}
 (E/'check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('runs','source_files','dependencies')},indent=2),flush=True)
if __name__=='__main__':main()
