"""Independent completed S1J1 accounting and exact input-form comparison only."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import fsum
import json,hashlib,shutil,time
import numpy as np
import mpmath as mp
from flint import arb,arb_mat,ctx
ctx.prec=640;ctx.threads=1;mp.mp.dps=70
TOP=Path(__file__).resolve().parents[1];ROOT=TOP.parents[1];NUM=ROOT.parent/'s2-num';RUN=NUM/'work/runs/S1J1';E=TOP/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator
def bb(d):
 lo,hi=[F(int(d[k][0]))*F(2)**int(d[k][1]) for k in ('lo_binary','hi_binary')];assert lo<=hi
 return aa((lo+hi)/2)+arb(0,aa((hi-lo)/2).upper())
def af(x):
 n,e=x.mid().man_exp();return F(int(n))*F(2)**int(e)
def mf(x):
 s,m,e,b=x._mpf_;return F((-1)**s*int(m))*F(2)**int(e)
def mm(x):
 x=F(x);return mp.mpf(x.numerator)/x.denominator
def pack(x):
 def dy(v):n,e=v.mid().man_exp();return [str(n),int(e)]
 return {'ball':x.str(45),'lo_binary':dy(x.lower()),'hi_binary':dy(x.upper())}
def am(x):return arb_mat([[aa(F.from_float(float(v))) for v in row] for row in x])
def rowbound(x):return max(sum(abs(x[i,j]) for j in range(x.ncols())).upper() for i in range(x.nrows()))
def mpfromfloat(x):return mp.matrix([[mm(F.from_float(float(v))) for v in row] for row in x])
def section(g,b,q,labels,tag):
 gg=q.T*g*q;bbm=q.T*b*q
 gg=(gg+gg.T)/2;bbm=(bbm+bbm.T)/2
 ll=mp.cholesky(gg);li=ll**-1;ww=li*bbm*li.T;wf=np.array(ww.tolist(),dtype=float);wf=(wf+wf.T)/2
 ev,v=np.linalg.eigh(wf);assert ev[0]>0,(tag,ev[0])
 xx=q*li.T*mp.matrix(v[:,0].tolist());x=np.array([float(z) for z in xx]);x/=np.linalg.norm(x);inds=np.argsort(-abs(x))[:10]
 return {'n':q.cols,'floating_singular_values':np.sqrt(ev[:8]).tolist(),'weakest_scaled_coefficients':x.tolist(),'largest_coefficients':[[labels[i],float(x[i])] for i in inds],'method':'70-digit pair restriction and whitening, symmetric double eigen-solve; output uncertified'}
def main():
 start=time.monotonic();parts=sorted(RUN.glob('part_*.npz'));assert len(parts)==4,'Four final parts are required; no completed-run claim from checkpoints.'
 assert not list(RUN.glob('base_*.npz'))
 meta_path=RUN/'meta.json';meta=json.loads(meta_path.read_text());new=meta['new'];assert len(new)==38
 certpath=ROOT/'proofs/239_s1j1_full_input/evidence/check.json';assert sha(certpath)=='c6d2e2c862f5023e90f24bb8ec550e655ea75e153ba9ccf22abb9f2599079858';cert=json.loads(certpath.read_text())
 assert sha(meta_path)==cert['metadata_sha256'];assert meta['NMAX']==530 and meta['settings']['vm']=='exact_template' and meta['settings']['out_shift']=='1' and meta['settings']['drop']=='+out'
 for name,h in cert['producer_sha256'].items():assert sha(RUN/name)==h,name
 src=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz';assert sha(src)==cert['source_sha256']
 expected=meta['cells_expected'];assert expected==list(range(1569));seen=set();rows=[];gm=[];bm=[]
 for path in parts:
  with np.load(path,allow_pickle=False) as z:
   ids=list(map(int,z['done']));diag=json.loads(str(z['diag']));assert len(ids)==len(set(ids));assert len(ids)==diag['cells'];assert not seen.intersection(ids);seen.update(ids)
   g=z['GZ'];b=z['BY'];assert g.shape==b.shape==(38,38);assert np.isfinite(g).all() and np.isfinite(b).all();gm.append(g.copy());bm.append(b.copy())
   wid=int(path.stem.split('_')[1]);assert ids==expected[wid::4]
  rows.append({'name':path.name,'sha256':sha(path),'cells':len(ids),'done':ids});shutil.copyfile(path,E/'source'/path.name)
 assert seen==set(expected)
 G=np.array([fsum(v) for v in zip(*(x.ravel() for x in gm))]).reshape(38,38);B=np.array([fsum(v) for v in zip(*(x.ravel() for x in bm))]).reshape(38,38)
 asym={'G':float(np.max(abs(G-G.T))),'B':float(np.max(abs(B-B.T)))};G=(G+G.T)/2;B=(B+B.T)/2
 ckpts=[]
 for path in sorted(RUN.glob('ckpt_*.npz')):
  with np.load(path,allow_pickle=False) as z:
   ids=list(map(int,z['done']));wid=int(path.name.split('_')[1]);assert ids==expected[wid::4][:len(ids)];assert set(ids)<=seen
  ckpts.append({'name':path.name,'sha256':sha(path),'duplicate_prefix_cells':len(ids)})
 logpath=NUM/'logs/s1j1_prod.log';log=logpath.read_text();assert 'sampling: 1569 cells over 4 workers' in log;assert 'resume:' not in log
 for wid in range(4):assert f'worker {wid} done: {len(expected[wid::4])} cells' in log
 GA=arb_mat([[bb(z) for z in row] for row in cert['runs'][1]['scaled_input_Gram']]);GM=mp.matrix([[mm(af(GA[i,j])) for j in range(38)] for i in range(38)])
 L=mp.cholesky(GM);T=(L**-1).T;tf=[[mf(T[i,j]) for j in range(38)] for i in range(38)];TA=arb_mat([[aa(v) for v in row] for row in tf]);I=arb_mat(np.eye(38,dtype=int).tolist())
 e=rowbound(TA.transpose()*GA*TA-I);d=rowbound(TA.transpose()*(am(G)-GA)*TA);assert e<1
 rel=d/(1-e);assert rel<1
 exact_input={'precision_bits':640,'whitener_identity_defect':pack(e),'congruent_input_error':pack(d),'relative_quadratic_form_error_bound':pack(rel),'scope':'Exact source input-form comparison only; no output certificate.'}
 (E/'dyadic_whitener.json').write_text(json.dumps([[str(v) for v in row] for row in tf])+'\n')
 gp=mpfromfloat(G);bp=mpfromfloat(B);labels=[v[1] for v in new]
 rows_out={'all':section(gp,bp,mp.eye(38),labels,'all')}
 for name,ids in [('inner_pure',list(range(33))),('pure',list(range(7,33))),('outer',list(range(33,38)))]:
  q=mp.matrix(38,len(ids))
  for j,i in enumerate(ids):q[i,j]=1
  rows_out[name]=section(gp,bp,q,labels,name)
 constraints_path=ROOT/'proofs/240_s1j1_high_intersections/evidence/exact_constraints.json';assert sha(constraints_path)=='96f271d72ec6190011166d747dff391d783cedff8203b97eb31a87f49bc05344';con=json.loads(constraints_path.read_text())
 for name in ('high_input','high_graph'):
  q=mp.matrix([[mm(F(v)) for v in row] for row in con[name]['basis_columns']]).T
  assert q.rows==38 and q.cols==({'high_input':32,'high_graph':29}[name]);rows_out[name+'_in_LOW_norms']=section(gp,bp,q,labels,name)
 rows_out['all_exact_input_midpoint_FLOATING_output']=section(GM,bp,mp.eye(38),labels,'exact_mid')
 # The stored binary strain row is only a numerical c=0 constraint.
 cv=[F.from_float(float(v)) for v in meta['cvec']];pivot=max(range(38),key=lambda i:abs(cv[i]));inds=[i for i in range(38) if i!=pivot];q=mp.matrix(38,37)
 for j,i in enumerate(inds):q[i,j]=1;q[pivot,j]=mm(-cv[i]/cv[pivot])
 rows_out['stored_c0_FLOATING_constraint']=section(gp,bp,q,labels,'stored_c0')
 np.savez(E/'parts_matrices.npz',G=G,B=B,exact_input_midpoint=np.array(GM.tolist(),dtype=float))
 for path in [meta_path,logpath,RUN/'PRODUCER_SHA256.txt']+[RUN/n for n in cert['producer_sha256']]:shutil.copyfile(path,E/'source'/path.name)
 deps={str(certpath.relative_to(ROOT)):sha(certpath),str(constraints_path.relative_to(ROOT)):sha(constraints_path)}
 out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'ACCOUNTING_CONFIRMED_INPUT_COMPARISON_CERTIFIED_OUTPUT_FLOATING','proof_sha256':sha(TOP/'PROOF.md'),'parts':rows,'ignored_checkpoint_prefixes':ckpts,'cells':1569,'asymmetry_before_symmetrizing':asym,'sections':rows_out,'exact_input_comparison':exact_input,'original_trial_sha256':sha(src),'dependencies':deps,'script_sha256':sha(__file__),'matrix_file_sha256':sha(E/'parts_matrices.npz'),'dyadic_whitener_sha256':sha(E/'dyadic_whitener.json'),'source_files':{p.name:sha(p) for p in sorted((E/'source').iterdir()) if p.is_file()},'scope':'No exact output pairing, total quadrature/division bound, high operator norm, continuum singular value, injectivity or complement inverse. All section eigenvalues are floating diagnostics.','seconds':time.monotonic()-start}
 (E/'check.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'date':out['date'],'n':38,'cells':1569,'sections':{key:v['floating_singular_values'][:3] for key,v in rows_out.items()},'input_form_error':exact_input['relative_quadratic_form_error_bound']['ball'],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
