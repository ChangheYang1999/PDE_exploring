"""Supplement307: independent arithmetic and static provenance; no producer execution."""
import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
import ast,json,hashlib,re
import numpy as np,torch
from q_local_checkpoint import load_numeric
R=Path('research/spec62_and_n224_text_audit');V=R/'verification';checks=[];bindings={};tokens=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);v=sha(p);ck('binding '+str(p),h is None or h==v);bindings[str(p)]=v;return p
def rat(v):return F(float(v))if isinstance(v,(float,np.floating))else F(str(v))
def rounded(n,s,v,source):
 v=rat(v);q=F(Decimal(s));u=F(10)**Decimal(s).as_tuple().exponent;lo=q-u/2;hi=q+u/2
 ck('rounding '+n,lo<=v<hi);tokens.append(dict(label=n,printed=s,value=float(v),exact_value=str(v),lower=str(lo),upper=str(hi),source=source))
for p in [Path(__file__),R/'REVIEW_RESOLUTION_PROOF.md',V/'CHECKS.json',V/'SUPPLEMENT_INPUTS.json']:bind(p)
base=json.loads((V/'CHECKS.json').read_text());ck('initial102 complete',base['count']==102==len(base['checks'])and all(x['passed']for x in base['checks']))
for p,h in base['bindings'].items():bind(p,h)
for d in json.loads((V/'SUPPLEMENT_INPUTS.json').read_text())['files']:bind(d['frozen'],d['sha256']);ck('stable input '+d['frozen'],d['two_reads_equal'])
parents={}
for label,p in [('299','research/hydrostatic_224_function_difference/verification/FINAL_BINDINGS.json'),('304','research/hydrostatic_same_node_inverse_audit/verification/FINAL_BINDINGS.json'),('306','research/report83_installation_and84_prelim/verification/FINAL_BINDINGS.json')]:
 p=Path(p);parents[label]=json.loads(bind(p,base['bindings'][str(p)]).read_text())
p=Path('research/hydrostatic_224_function_difference/verification/RUN.json');run=json.loads(bind(p,parents['299']['bindings'][str(p)]).read_text());factors=[]
for convention,group in run['annulus_increase'].items():
 ck('three distinct metric keys '+convention,set(group)=={'field','gradient','pointwise_relative'})
 for metric,row in group.items():
  q=rat(row['current'])/rat(row['previous']);ck('exact saved finite increase '+convention+metric,q>1);ck('stored ratio agrees to double rounding '+convention+metric,abs(q-rat(row['ratio']))<F(1,10**14));factors.append(q)
ck('nine actual finite factors',len(factors)==9)
for metric,s in [('field','0.0312'),('gradient','0.0577'),('pointwise_relative','0.0287')]:rounded('SPEC299 '+metric,s,run['annulus_increase']['common_nominal'][metric]['current'],'299')
rounded('minimum finite factor','3.90',min(factors),'299 exact stored-data quotient');rounded('maximum finite factor','4.20',max(factors),'299 exact stored-data quotient')
p=Path('research/hydrostatic_same_node_inverse_audit/verification/CHECKS.json');d=json.loads(bind(p,parents['304']['bindings'][str(p)]).read_text());row=next(r for r in d['rows']if r['label']=='reconstructed_node')
for name,values in [('diagnostic',row['diagnostic_rule']['analytic']),('physical',row['physical'][-1])]:
 for key,s,value in [('V1','-34.637'if name=='diagnostic'else'-34.083',values['V'][0]),('V2','-0.774'if name=='diagnostic'else'0.542',values['V'][1]),('Rf','1.4e-9'if name=='diagnostic'else'5.0e-3',values['Rf'])]:rounded('SPEC304 '+name+key,s,value,'304')
p=Path('research/hydrostatic_same_node_inverse_audit/verification/earlier_solver_static.py');solver=bind(p,parents['306']['bindings'][str(p)]).read_text();t=ast.parse(solver);u=ast.unparse
sample=next(n for n in t.body if isinstance(n,ast.FunctionDef)and n.name=='sampled_table');sampletxt=u(sample)
expected=["tm = 0.5 * (tR[:-1] + tR[1:])","rm = m.rad.rmap_np(torch.tensor(tm)).numpy()","RR, TT = np.meshgrid(rm, thm, indexing='ij')","msk = (RR >= lo) & (RR < hi)","out.append((lo, hi, float(np.abs(R[msk]).max()), float((np.abs(R) / Nf)[msk].max()), float(Nf[msk].max())))","Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g)"]
for s in expected:ck('static sampled definition '+s,s in sampletxt)
ck('static sampled log branch',"getattr(hsm, 'inner', 'gauss') == 'log'"in sampletxt)
ck('static sampled log parameters',"hs_layer.hydro_V_log(ge, X, Y, n0=32, per_decade=10, ngl=16, n_tail=400, hrel=hsm.hrel)"in sampletxt)
# Bind each inheritance link and the radial map; inspect syntax only.
for name,child,parent in [('dr','DR','ipm3ql.IPM3QL'),('ipm3ql','IPM3QL','ipm3q.IPM3Q'),('ipm3q','IPM3Q','ipm3s.IPM3S')]:
 t=ast.parse((V/(name+'_static.py.txt')).read_text());c=next(n for n in t.body if isinstance(n,ast.ClassDef)and n.name==child);ck('inheritance '+child,[u(x)for x in c.bases]==[parent]);ck('superinit '+child,any(isinstance(n,ast.Call)and u(n.func)=='super().__init__'for n in ast.walk(c)))
st=(V/'ipm3s_static.py.txt').read_text();t=ast.parse(st);rad=next(n for n in t.body if isinstance(n,ast.ClassDef)and n.name=='Radial2');m=next(n for n in rad.body if isinstance(n,ast.FunctionDef)and n.name=='rmap_np');ret=[n for n in ast.walk(m)if isinstance(n,ast.Return)];ck('unique exact radial map',len(ret)==1 and u(ret[0].value)=='self.L * np.sqrt((1 + t) / 2) / (1 - t) ** self.p')
ck('radial class assigned','self.rad = Radial2(N, L, p, self.dev)'in st);ck('radial map exponent from gamma','p = 1.0 / (1.0 - gamma)'in st)
ck('DR gamma from c','gamma=1.0 / C'in(V/'dr_static.py.txt').read_text())
states={}
for N,p,h in [(224,Path('research/hydrostatic_c2_resolved_224_audit/verification/hsG_c2.0_N224_log.completed.pt'),'fd0bc052d8a5eb54d759cb4c29cbcaf2983d92c94e13eabc953503a131abc632'),(192,Path('research/hydrostatic_c2_resolved_192_audit/verification/hsG_c2.0_N192_log.pt'),'5177b5ae4c8a480353f7d855e27cfb735accab264c56f53c1f54881476d737a0')]:
 bind(p,h)
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):data=load_numeric(p)
 q=data['result'];states[N]=q;ck('source tag '+str(N),q['tag']==f'hsG_c2.0_N{N}_log'and q['N']==N and q['M']==N//4 and q['c']==2 and q['inner']=='log'and q['hstep']=='r');ck('sample rows '+str(N),len(q['sampled'])==4 and all(len(row)==5 for row in q['sampled'])and [tuple(row[:2])for row in q['sampled']]==[(0,.1),(.1,1),(1,100),(100,1e300)]);ck('source map parameters '+str(N),float(data['L'])==1 and float(data['p'])==2)
 if N==224:
  tk=np.asarray(data['tk']);ck('sorted tnodes',len(tk)==225 and np.all(np.diff(tk)>0)and -1<=tk[0]<tk[-1]<1);tm=(float(tk[-2])+float(tk[-1]))/2;rmax=((1+tm)/2)**.5/(1-tm)**2;rounded('declared outer midpoint','6.7e7',rmax,'static map and stored nodes')
for key,s in [('E','-0.442'),('B','-3.108'),('centre_defect_single','-4.56e-5')]:rounded('producer '+key,s,states[224][key],'224 numeric metadata')
rounded('producer192 annulus','4.4e-5',states[192]['sampled'][2][3],'192 numeric metadata');rounded('producer224 annulus','4.8e-5',states[224]['sampled'][2][3],'224 numeric metadata');ck('source reported annulus rise',states[224]['sampled'][2][3]>states[192]['sampled'][2][3])
harvest=(V/'harvest224.txt').read_text();delta=re.findall(r'D_exact\s+([-+0-9.e]+)',harvest);ck('unique harvest exactdelta',len(delta)==1);rounded('harvest delta','-4.56e-5',delta[0],'captured harvest224')
cpblock=harvest.split('== C_p\n')[1].split('== m_0')[0];cp=cpblock.strip().split()[-1];rounded('harvest CpTheta','5.75',cp,'captured harvest224 last extrapolation token')
s=json.loads(Path('research/hydrostatic_c2_resolved_224_audit/verification/SUMMARY.json').read_text())['states'][0];rounded('raw Cp also rounds','5.75',s['cusp']['Cp'],'289 raw Cp');ck('E normalisation stored arithmetic',abs(rat(s['e'])/rat(s['a'])-rat(s['E']))<F(1,10**15));fv=s['far']['values'];ck('r2 component recombination',abs(-F(fv['c2'])+2*F(fv['K'])*F(fv['Q'])-F(fv['r2']))<F(1,10**70));ck('Cp normalisation component recombination',abs(F(s['cusp']['Cp'])/F(fv['K'])-F(s['cusp']['Cp_K']))<F(1,10**70))
p=Path('research/report83_installation_and84_prelim/verification/prelim84.md');text=bind(p,parents['306']['targets']['preliminary84']).read_text();norm=lambda s:' '.join(s.split());txt=norm(text)
for s in ['largest absolute entry of the unweighted residual vector: R_h at the collocation points and the normalization rows','not divided by N_f','For these c = 2 states the node residuals are computed with the solver\'s own quadrature of the inverse rows','the residuals and coefficients of this sixth state are not reported in this version.']:
 ck('existing report context '+s,s in txt)
entry=(V/'own289_publication_excerpt.md').read_text();ck('actual289 verdict publication','2026-10-22T01:25:31.654611+00:00: result289 CONFIRMED'in entry);ck('publication same binding','8e57a5ceca2d4627f5428763339e54b06bd0436811e79bb491f536fb4f6c0eb4'in entry);ck('minute label justified',datetime.fromisoformat('2026-10-22T01:25:31.654611+00:00').strftime('%Y-%m-%dT%H:%MZ')=='2026-10-22T01:25Z')
review=V/'opus_review';meta=json.loads((review/'metadata.json').read_text());response=json.loads((review/'response.json').read_text());ck('actual reviewer',meta['returned_model']==response['model']=='claude-opus-5-5'and meta['stop_reason']==response['stop_reason']=='end_turn');bind(review/'request.txt',meta['request_sha256'])
for n in ['metadata.json','response.json','answer.md']:bind(review/n)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_WITH_REQUIRED_SPEC_REPAIR',count=len(checks),checks=checks,bindings=bindings,tokens=tokens,source_node_diagnostic='absolute unweighted F incl normalisation rows under own solver quadrature',nominal_rmax=rmax,producer_Cp=cp,scope='Completes missing finite arithmetic and declared source semantics of102check audit. Producer maxima remain testimony. Same E/B/delta/Cp means at printed precision. No historical array or producer run authenticated, no new inverse accuracy claimed; degree23 and primary OPEN.')
(V/'REVIEW_SUPPLEMENT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
