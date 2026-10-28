"""Independent S1M4P accounting, floating sections and exact input-form comparison.
Run only once final parts exist. This never certifies output quadrature or an inverse.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import fsum
import json,hashlib,shutil,time
import numpy as np
from scipy.linalg import eigh,null_space
from flint import arb,arb_mat,ctx
ctx.prec=640;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];ROOT=TOP.parents[1];NUM=ROOT.parent/'s2-num';RUN=NUM/'work/runs/S1M4P';E=TOP/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator
def bb(d):
 lo,hi=[F(int(d[k][0]))*F(2)**int(d[k][1]) for k in ('lo_binary','hi_binary')];assert lo<=hi
 return aa((lo+hi)/2)+arb(0,aa((hi-lo)/2).upper())
def pack(x):
 def dy(v):n,e=v.mid().man_exp();return [str(n),int(e)]
 return {'ball':x.str(40),'lo_binary':dy(x.lower()),'hi_binary':dy(x.upper())}
def am(x):return arb_mat([[aa(F.from_float(float(v))) for v in row] for row in x])
def rowbound(x):return max(sum(abs(x[i,j]) for j in range(x.ncols())).upper() for i in range(x.nrows()))
def main():
 start=time.monotonic();parts=sorted(RUN.glob('part_*.npz'));assert len(parts)==4,'Final four parts not yet available. Do not audit checkpoints as a completed run.'
 assert not list(RUN.glob('base_*.npz')),'Resumed producer history requires manual method/provenance audit before this never-resumed procedure.'
 meta_path=RUN/'meta.json';meta=json.loads(meta_path.read_text());new=meta['new'];assert len(new)==78
 certpath=ROOT/'proofs/198_pure_spline_input_gram/evidence/gram_512_640.json';assert sha(certpath)=='bc7512502550c11fd5ba859d7b4630ae70b7d643ff2de6d6af5e329e9261d606'
 cert=json.loads(certpath.read_text());rec=cert['runs']['S1M4P'];assert sha(meta_path)==rec['metadata_sha256'],'Metadata changed: inspect scales and basis before continuing.'
 assert rec['selected_new_indices']==list(range(78))
 src=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz';assert sha(src)==cert['source_sha256']
 expected_json=json.loads((RUN/'cells_expected.json').read_text());expected=expected_json['cells_expected'];assert expected==list(range(1569));seen=set();rows=[];gm=[];bm=[]
 for path in parts:
  with np.load(path,allow_pickle=False) as z:
   ids=list(map(int,z['done']));diag=json.loads(str(z['diag']));assert len(ids)==len(set(ids));assert len(ids)==diag['cells'];assert not seen.intersection(ids);seen.update(ids)
   g=z['GZ'];b=z['BY'];assert g.shape==b.shape==(78,78);assert np.isfinite(g).all() and np.isfinite(b).all();gm.append(g.copy());bm.append(b.copy())
   wid=int(path.stem.split('_')[1]);assert ids==expected[wid::4],'Never-resumed round-robin assignment differs.'
  rows.append({'name':path.name,'sha256':sha(path),'cells':len(ids),'done':ids});shutil.copyfile(path,E/'source'/path.name)
 assert seen==set(expected)
 # fsum independently avoids reproducing the producer/assembler accumulation order.
 G=np.array([fsum(v) for v in zip(*(x.ravel() for x in gm))]).reshape(78,78);B=np.array([fsum(v) for v in zip(*(x.ravel() for x in bm))]).reshape(78,78)
 asym={'G':float(np.max(abs(G-G.T))),'B':float(np.max(abs(B-B.T)))};G=(G+G.T)/2;B=(B+B.T)/2
 ckpts=[]
 for path in sorted(RUN.glob('ckpt_*.npz')):
  with np.load(path,allow_pickle=False) as z:
   ids=list(map(int,z['done']));wid=int(path.name.split('_')[1]);assert ids==expected[wid::4][:len(ids)];assert set(ids)<=seen
  ckpts.append({'name':path.name,'sha256':sha(path),'duplicate_prefix_cells':len(ids)})
 logpath=NUM/'logs/s1m4p_prod.log';log=logpath.read_text();assert 'sampling: 1569 cells over 4 workers' in log;assert 'resume:' not in log
 for wid in range(4):assert f'worker {wid} done: {len(expected[wid::4])} cells' in log
 sel={'m1':[i for i,v in enumerate(new) if v[2]==1],'m2':[i for i,v in enumerate(new) if v[2]==2],'m3':[i for i,v in enumerate(new) if v[2]==3],'m12':[i for i,v in enumerate(new) if v[2]<=2],'all':list(range(78)),'high_graph_columns_in_LOW_norms':[i for i,v in enumerate(new) if 7<=int(v[1][2:])<=26]}
 assert len(sel['high_graph_columns_in_LOW_norms'])==60
 rows_out={};cv=np.array(meta['cvec'])
 for label,idx in sel.items():
  g=G[np.ix_(idx,idx)];b=B[np.ix_(idx,idx)];ev,v=eigh(b,g);assert ev[0]>0;diag=np.sqrt(np.diag(g));eg=np.linalg.eigvalsh(g/np.outer(diag,diag));x=v[:,0];x/=np.linalg.norm(x);top=np.argsort(-abs(x))[:12]
  c=cv[idx];Q=null_space(c[None,:]);ec=eigh(Q.T@b@Q,Q.T@g@Q,eigvals_only=True)
  rows_out[label]={'n':len(idx),'indices':idx,'floating_singular_values':np.sqrt(ev[:8]).tolist(),'floating_c0_values':np.sqrt(np.maximum(ec[:8],0)).tolist(),'normalized_input_condition':float(eg[-1]/eg[0]),'weakest_vector':x.tolist(),'weakest_coefficients':[[new[idx[j]],float(x[j])] for j in top],'rayleigh_squared':float(x@b@x/(x@g@x))}
 # Certify ONLY the exact-input-form comparison, including all dyadic rounding in T.
 GA=arb_mat([[bb(z) for z in row] for row in rec['exact_scaled_input_Gram']]);gmid=np.array([[float(GA[i,j].mid()) for j in range(78)] for i in range(78)])
 L=np.linalg.cholesky(gmid);T=np.linalg.solve(L.T,np.eye(78));TA=am(T);I=arb_mat(np.eye(78,dtype=int).tolist());e=rowbound(TA.transpose()*GA*TA-I);d=rowbound(TA.transpose()*(am(G)-GA)*TA);assert e<1
 exact_input={'precision_bits':640,'whitener_identity_defect':pack(e),'congruent_input_error':pack(d),'relative_quadratic_form_error_bound':pack(d/(1-e)),'scope':'Certified comparison of exact source-defined input Gram with exact binary fsum matrix only. No output Gram certificate.'}
 # Consistency with a separate old-padding M3 run, and finite images paired with exact input midpoints.
 older=ROOT/'proofs/183_s1m3_floating_audit/evidence/parts_matrices.npz';ometa=json.loads((ROOT/'proofs/198_pure_spline_input_gram/evidence/source/S1M3_meta.json').read_text());oi=[i for i,v in enumerate(ometa['new']) if v in [new[j] for j in sel['m12']]];ni=sel['m12'];assert [ometa['new'][i] for i in oi]==[new[i] for i in ni]
 with np.load(older,allow_pickle=False) as z:
  og=z['G'][np.ix_(oi,oi)];ob=z['B'][np.ix_(oi,oi)]
 compare={'n':52,'G_relative_frobenius':float(np.linalg.norm(G[np.ix_(ni,ni)]-og)/np.linalg.norm(og)),'B_relative_frobenius':float(np.linalg.norm(B[np.ix_(ni,ni)]-ob)/np.linalg.norm(ob))}
 exact_input_midpoint_sv=np.sqrt(eigh(B,gmid,eigvals_only=True)[:8]).tolist()
 np.savez(E/'parts_matrices.npz',G=G,B=B,T=T,exact_input_midpoint=gmid)
 for path in [meta_path,RUN/'cells_expected.json',logpath]:shutil.copyfile(path,E/'source'/path.name)
 producer=NUM/'work/fsec.py';shutil.copyfile(producer,E/'source/current_producer_NOT_original_running_code.py')
 out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'ACCOUNTING_CONFIRMED_FLOATING_OUTPUT_ONLY','parts':rows,'ignored_checkpoint_prefixes':ckpts,'cells':1569,'asymmetry_before_symmetrizing':asym,'selections':rows_out,'exact_input_comparison':exact_input,'M3_comparison':compare,'floating_values_using_exact_input_midpoint':exact_input_midpoint_sv,'original_trial_sha256':sha(src),'exact_input_certificate_sha256':sha(certpath),'script_sha256':sha(__file__),'matrix_file_sha256':sha(E/'parts_matrices.npz'),'source_files':{p.name:sha(p) for p in (E/'source').iterdir() if p.is_file()},'scope':'No exact output pairing, total division/quadrature error, continuum singular value, Sobolev high-norm comparison, injectivity or complement inverse. All displayed singular values are floating. High graph subset values still use the LOW norms of this computation.','seconds':time.monotonic()-start}
 (E/'check.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'date':out['date'],'n':78,'cells':1569,'sections':{key:v['floating_singular_values'][:3] for key,v in rows_out.items()},'input_form_error':exact_input['relative_quadratic_form_error_bound']['ball'],'M3_comparison':compare,'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
