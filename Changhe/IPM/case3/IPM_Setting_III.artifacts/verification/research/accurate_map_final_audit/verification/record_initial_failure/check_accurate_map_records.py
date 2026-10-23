"""Independent parsing of frozen records; no producer code is executed."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from decimal import Decimal
import os,sys,json,hashlib,ast,re,traceback,math
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
R=Path('research/accurate_map_final_audit');V=R/'verification';checks=[];bindings={};records=[]
def now():return datetime.now(timezone.utc).isoformat()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);hh=hashlib.sha256(p.read_bytes()).hexdigest();ck('binding '+str(p),(h is None or hh==h)and(str(p)not in bindings or bindings[str(p)]==hh));bindings[str(p)]=hh;return p
def load(p):
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):return QLocalCheckpoint(p)
def interval(tok,x):
 q=Decimal(tok);u=Decimal(10)**q.as_tuple().exponent/2;return q-u<=Decimal.from_float(float(x))<=q+u
def header(s):
 first=s.splitlines()[0];_,_,time,opt=first.split(' ',3);return datetime.fromisoformat(time.replace('Z','+00:00')),ast.literal_eval(opt)
try:
 for p in [__file__,'independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py',R/'PROOF.md',R/'RECORD_AUDIT_PROOF.md']:bind(p)
 for name in ['INPUTS.json','INPUTS_SUPPLEMENT.json','INPUTS_ADDITIONAL.json']:
  d=json.loads(bind(V/name).read_text())
  for z in d['files']:bind(z['frozen'],z['sha256'])
 d=json.loads(bind(V/'RECORD_DRAFT_INPUTS.json').read_text())
 for z in d['files']:bind(z['path'],z['sha256'])
 seq=[('A','hsQ_c2.0_N96_acc',96,24,80,None,False),('B','hsQ_c2.0_N128_acc',128,32,51,51,False),('C','hsQ_c2.0_N96_acc_fromG',96,24,23,23,False),('E','hsQ_c2.0_N96_acc_fine',96,24,10,10,True),('G80','hsQ_c2.0_N80_acc6_fine',80,20,12,12,True),('G96','hsQ_c2.0_N96_acc6_fine',96,24,10,10,True),('G112','hsQ_c2.0_N112_acc6_fine',112,28,13,13,True),('G128','hsQ_c2.0_N128_acc6_fine',128,32,8,8,True)]
 for tag,stem,N,M,steps,failed,fine in seq:
  text=bind(V/(stem+'.log')).read_text();start,opt=header(text);q=load(bind(V/(stem+'.pt')));rr=[json.loads(s[9:])for s in text.splitlines()if s.startswith('# RESULT ')];ck('one final JSON '+tag,len(rr)==1);d=rr[0];ck('checkpoint/log result identical '+tag,q.data['result']==d)
  ck('dimensions/header/state '+tag,int(opt['N'])==q.N==d['N']==N and int(opt['M'])==q.M==d['M']==M and q.cl==d['c']==float(opt['c'])==2 and q.kappa==2 and q.p==.5 and q.L==1)
  ck('finite stored basis '+tag,q.basis=='local'and q.meta['basis_nodes_source']=='stored'and np.isfinite(q.u).all()and len(q.u)==sum(N+1-k for k in range(M)))
  counts=re.findall(r'# model built \((\d+) collocation points, nu (\d+)\)',text);rows=N*M*(3 if fine else 1);ck('recorded dimensions '+tag,counts==[(str(rows),str(len(q.u)))])
  accepted=re.findall(r'^  it (\d+): \|F\|2 (\S+) \|F\|max (\S+) lam (\S+)',text,re.M);fail=re.findall(r'^  it (\d+): line search failed',text,re.M);ck('contiguous accepted updates '+tag,[int(z[0])for z in accepted]==list(range(steps)));ck('failure index '+tag,fail==([]if failed is None else[str(failed)]));ck('cap versus failure '+tag,steps==int(opt['maxit'])if failed is None else steps<int(opt['maxit']))
  ck('result formulation '+tag,d['fine']==fine and d['cfree']is False and d['centre']=='drop'and d['extra']==[]and d['wextra']=={}and d['hstep']=='r'and d['inner']=='log'and d['centre_row_defect']is None)
  quad=dict(n0=32,per_decade=6 if tag.startswith('G')else 10,ngl=12 if tag.startswith('G')else 16,n_tail=240 if tag.startswith('G')else 400,q=2);ck('three quadrature records '+tag,d['quad']==quad and all(int(opt[k])==v and q.data['inverse_options'][k]==v for k,v in quad.items()))
  io=q.data['inverse_options'];ck('saved options '+tag,io['fine']==fine and io['centre']=='drop'and io['hrel']==1e-5 and io['hstep']=='r'and io['fd_step']=='hrel (1 + sqrt(xi^2 + t^2))')
  ck('raw norm record '+tag,0<d['nodes_Fmax']<=d['nodes_F2']and math.isfinite(d['nodes_F2']));ck('final accepted print intervals '+tag,interval(accepted[-1][1],d['nodes_F2'])and interval(accepted[-1][2],d['nodes_Fmax']))
  ck('center metadata internal identity '+tag,d['c']+d['cH']-1==d['centre_defect_single'] and q.data['cH']==d['cH'] and q.data['centre_defect_single']==d['centre_defect_single']);ck('sample rows schema '+tag,len(d['sampled'])==4 and all(len(z)==5 and np.isfinite(z).all()and z[2]>=0 and z[3]>=0 and z[4]>0 for z in d['sampled']))
  raw=re.findall(r'^# raw state saved (\S+) (\S+)$',text,re.M);ck('one raw save '+tag,len(raw)==1);saved=datetime.fromisoformat(raw[0][1].replace('Z','+00:00'));done=start+timedelta(seconds=d['wall']);ck('recorded chronology '+tag,start<saved<done and math.isfinite(d['wall']))
  tm=(q.tk[-2]+q.tk[-1])/2;radius=math.sqrt((1+tm)/2)/(1-tm)**2;ck('positive midpoint exterior '+tag,radius>1e6)
  records.append(dict(tag=tag,state=str(q.path),N=N,M=M,coefficient_count=len(q.u),PDE_rows=rows,complete_residual_rows=rows+2,accepted_updates=steps,failure_index=failed,start_utc=start.isoformat(),raw_save_utc=saved.isoformat(),diagnostics_end_from_wall=done.isoformat(),midpoint_rmax=radius,result=d,quad=quad,scope='Saved record consistency only; current evaluator and historical execution are not authenticated by these checks.'))
 D=bind(V/'hsQ_c2.0_N128_acc_fromG.log').read_text();di=[int(x)for x in re.findall(r'^  it (\d+): \|F\|2',D,re.M)];ck('D31 logged updates no endpoint record',di==list(range(31))and '# RESULT 'not in D and '# raw state saved 'not in D);last=re.findall(r'^  it (\d+): \|F\|2 (\S+) \|F\|max (\S+)',D,re.M)[-1];ck('D final displayed values',last==('30','3.893e-02','8.938e-03'),last)
 Flog=bind(V/'hsQ_c2.0_N128_acc_fine.out').read_text();ck('F setup failure record',all(s in Flog for s in ['torch.OutOfMemoryError','Tried to allocate 20.79 GiB','65.74 GiB','79.25 GiB','HSModel(N, M, c'])and not re.search(r'^  it ',Flog,re.M))
 source=bind(V/'producer_hs_solve.py').read_text();tree=ast.parse(source);funcs={n.name:ast.unparse(n)for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))};run=funcs['run'];model=funcs['HSModel'];sample=funcs['sampled_table']
 for key,needle in [('singular threshold','keep = S > 1e-13 * S[0]'),('strict Armijo','if nFn < (1 - 0.0001 * lam) * nF:'),('raw residual maximum','nodes_Fmax=F.abs().max().item()'),('norm2','nF = F.norm().item()'),('center Gaussian','hs_axis_exact.centre_exact(hsm.m, u)')]:ck('current source '+key,needle in run,needle)
 ck('normalization row definitions',"F = torch.cat"in model and 'a0 - 1' in model and 'K - 1'in model);ck('current sampled q forwarded',"q=getattr(hsm, 'q', 3)"in sample);ck('sample whole-set panels',"ymax_dec=np.log10(max(Yf.max(), 10.0))"in sample)
 angle=ast.parse(bind(V/'producer_hs_angular_scan.py').read_text());asrc=ast.unparse(angle);ck('scan normalized interpolated field','q = R / Nf'in asrc and 'qc = np.interp(th_c, th, q)'in asrc and 'coef = np.linalg.lstsq(C, q, rcond=None)[0]'in asrc);ck('rounded scan rays','np.round(np.arctan2(hsm.Y, hsm.X), 10)'in asrc)
 coeff=bind(V/'producer_hs_axis_exact.py').read_text();ck('finite Gaussian primitive not rational arithmetic','leggauss(2 * N + 2)'in coeff and 'k ** 2 * sgn'in coeff and 'Fraction'not in coeff)
 ck('Fprime chronology correction',next(z for z in records if z['tag']=='G128')['raw_save_utc']=='2026-10-22T04:02:28+00:00')
 for p,h in bindings.items():ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
 out=dict(status='PASS_FROZEN_ACCURATE_MAP_RECORD_CONSISTENCY',utc=now(),count=len(checks),checks=checks,bindings=bindings,records=records,scope='Metadata, counts and static source only. Producer code not executed; no independent candidate inverse or exact center yet. D/F absence statement restricted to frozen records.')
 p=V/'RECORD_CHECKS.json';tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(p);print(out['status'],len(checks))
except Exception:
 p=V/('RECORD_FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json');p.write_text(json.dumps(dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
