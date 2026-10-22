"""Independent source-field diagnostic. No producer imports; no rigor claim."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,pickle,hashlib,time,os
import numpy as np
from numpy.polynomial.legendre import leggauss
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/harmonic_projection_scope';S=D/'sources'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def stamp():return datetime.now(timezone.utc).isoformat()
def load(p):return json.loads(p.read_text())
def pval(pc,t):
 out=np.zeros_like(t);der=np.zeros_like(t)
 for a,b,al,c in pc:
  a,b,al=float(a),float(b),float(al);l=0 if np.isneginf(a) else np.searchsorted(t,a);r=len(t) if np.isposinf(b) else np.searchsorted(t,b)
  if r<=l:continue
  x=t[l:r]-(b if np.isneginf(a) else a);p=np.zeros_like(x);dp=np.zeros_like(x)
  for j,co in enumerate(c):
   p+=float(co)*x**j
   if j:dp+=j*float(co)*x**(j-1)
  ex=np.exp(al*x);out[l:r]+=ex*p;der[l:r]+=ex*(dp+al*p)
 return out,der
start=stamp();tick=time.monotonic();man=load(D/'data_exact/manifest.json');pins=dict(man['files'])
for n,h in pins.items():need(sha(B/n)==h,'captured input digest')
records=[]
for case in man['cases']:
 summ=load(B/case['summary']);prof=load(B/case['profile']);sec=summ['sections']['Fminus'];sh=sec['smallest5_shares'][0];pr=prof['shells'][0]
 with np.load(B/case['vector'],allow_pickle=False) as z:v={n:z[n] for n in z.files}
 meta=pickle.loads((B/case['columns']).read_bytes());cols=meta['cols'];nF=int(v['nF']);h=v['Fminus_h'][:,0];Mt=len(v['A0']);need(Mt==260 and len(v['Bm'])==261,'source angular count');need(len(cols)==nF and np.all(h[nF+2:]==0),'Fminus coordinates');need(str(v['mode'])=='H1m' and str(v['ROWS'])==case['rows'] and summ['rows_mode']==case['rows'] and summ['mode']=='H1m','same norm and row mode')
 need(float(v['Fminus_sigma'][0])==sh['sigma']==pr['sigma'] and float(v['Fminus_hGh'][0])==sh['hGh']==pr['hGh_saved'],'same saved vector order');need(all(int(m)==int(v['col_m'][i]) and str(lab)==str(v['col_label'][i]) for i,(m,pc,lab) in enumerate(cols)),'column metadata order')
 # Exact signed-frequency coefficients, independently from numerical quadrature.
 trans={}
 for m in range(Mt):
  for q in [1+2*m,1-2*m,3+2*m,3-2*m]:
   need(q%2==1 and q!=0,'odd frequency');key=(m,(abs(q)-1)//2);trans[key]=trans.get(key,F(0))+F(1 if q>0 else -1,8)
 need({j:c for (m,j),c in trans.items() if m==0 and c}=={0:F(1,4),1:F(1,4)},'exact Phi0')
 trunc=max(max(int(x[0]) for x in cols)+3,int(v['Mh'])+2);Mharm=max(j for m,j in trans)+1;tm=float(v['tmin']);t0=float(v['t0']);L=float(v['L']);k=float(v['k'])
 pieces=[p for m,p,l in cols]+[meta['kp_pieces'],meta['tau_pieces']]
 bps=set(np.linspace(tm-25,tm,51).tolist()+np.linspace(t0,t0+45,91).tolist())
 for pc in pieces:
  for a,b,al,c in pc:
   if np.isfinite(a):bps.add(float(a))
   if np.isfinite(b):bps.add(float(b))
 # Include all three unused reference joins to match the declared finite interval partition, not their zero fields.
 for a,b in v['ref_ta_tb']:bps.update([float(a),float(b)])
 bps=np.array(sorted(bps));runs=[]
 for ng in [20,32]:
  z,w=leggauss(ng);t=((bps[1:]-bps[:-1])[:,None]*z[None,:]/2+(bps[1:]+bps[:-1])[:,None]/2).ravel();wt=((bps[1:]-bps[:-1])[:,None]*w[None,:]/2).ravel();need(np.all(np.diff(t)>0) and np.all(wt>0),'positive sorted quadrature')
  bm=np.zeros((Mt,len(t)));bd=np.zeros_like(bm)
  for i,(m,pc,label) in enumerate(cols):
   if h[i]==0:continue
   p,dp=pval(pc,t);bm[int(m)]+=h[i]*p;bd[int(m)]+=h[i]*dp
  for i,(key,ak) in enumerate([('kp_pieces',v['A0']),('tau_pieces',v['Bm'][:Mt])]):
   p,dp=pval(meta[key],t);bm+=h[nF+i]*ak[:,None]*p[None,:];bd+=h[nF+i]*ak[:,None]*dp[None,:]
  ww=wt*L**6*np.exp(2*t)*(1+(np.exp(t)/L)**2)**(1.5-k);rr=[]
  for mm in [trunc,Mt]:
   c=np.zeros((Mharm,len(t)));cs=np.zeros_like(c)
   for (m,j),co in trans.items():
    if m<mm and co:c[j]+=float(co)*bm[m];cs[j]+=float(co)*(3*bm[m]+bd[m])
   q=2*np.arange(Mharm)+1;en=np.pi*np.sum(((1+q*q)[:,None]*c*c+cs*cs)*ww[None,:],axis=1);E=float(en.sum());fraction=float(en[:2].sum()/E);need(np.isfinite(E) and E>0 and 0<=fraction<=1,'finite positive energy')
   rr.append({'modes':mm,'energy':E,'low_harmonic_fraction':fraction,'saved_profile_fraction_difference':fraction-pr['harmonic_energy_fractions']['N=0..1'],'saved_hGh_difference':E-sh['hGh']})
  need(abs(rr[0]['low_harmonic_fraction']-pr['harmonic_energy_fractions']['N=0..1'])<1e-9,'independent finite quadrature fraction agrees');need(abs(rr[0]['energy']-pr['E_X'])<1e-8,'independent finite quadrature energy agrees')
  runs.append({'order':ng,'nodes':len(t),'profile_convention':rr[0],'full_gram_convention':rr[1]})
 rec={'family':case['family'],'rows':case['rows'],'sigma':sh['sigma'],'saved_projection_m0':sh['modes'][0],'saved_low_harmonic_fraction':pr['harmonic_energy_fractions']['N=0..1'],'exact_saved_projection_le_harmonic':F.from_float(sh['modes'][0])<=F.from_float(pr['harmonic_energy_fractions']['N=0..1']),'exact_saved_gap':str(F.from_float(pr['harmonic_energy_fractions']['N=0..1'])-F.from_float(sh['modes'][0])),'runs':runs};need(rec['exact_saved_projection_le_harmonic'],'saved nesting inequality');records.append(rec);print(json.dumps(rec),flush=True)
for p in [D/'data_exact/manifest.json',D/'SOURCE_SCOPE.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final captured input digest')
out={'start_utc':start,'utc':stamp(),'status':'PASS_SAVED_ARTIFACTS_AND_INDEPENDENT_FLOATING_HARMONIC_DIAGNOSTIC','records':records,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Exact finite-dimensional projection nesting proof is separate. Fresh field evaluation uses floating finite radial quadrature, including full source KP/TAU and the producer profile truncation, not rigorous physical energy enclosures or weak-H1 membership. Scalar JSON comparisons certify only saved artifact values; no inverse or IPM endpoint.'}
with (D/'evidence/check.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','seconds']}))
