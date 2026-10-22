from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_mellin_moment_bound';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='c40c8cc86a1228692a379011a2bdb772138bd2d1deba4d2330ff8dd34a7b4c70'
parent='research/logarithmic_frozen_range_inverse/evidence/verdict.json';v=p.load(R/parent);pins=dict(v['files']);p.pin(pins,parent,'a5cce5f36cf56efdd512eb8ef5274f0b8708151342f4a16ec93892006601c3d7');p.rehash(pins)
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(npz,allow_pickle=False) as z:k=F.from_float(float(z['k'].item()))
A=2/k-1;DD=4/k-1;a=F(0);s=F(153,50);c=-A*(a-F(1,2))-1;u=DD/2-c;v=s*DD-u;t=u/DD;w=v/DD
assert DD==2*A+1 and 0<t<1 and 2<w<3 and t+w==s
actual={n:str(x) for n,x in {'k':k,'A':A,'D':DD,'a':a,'s':s,'c':c,'u':u,'v':v,'t':t,'w':w}.items()}
def Q(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def ep(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def enclosure(x):return {'lower_exact':str(ep(x.lower())),'upper_exact':str(ep(x.upper()))}
def window(x):
 l,r=ep(x.lower()),ep(x.upper());den=10**12;lo=F(l.numerator*den//l.denominator,den);hi=F(r.numerator*den//r.denominator+1,den)
 if lo==l:lo-=F(1,den)
 assert lo<l<=r<hi
 return [str(lo),str(hi)]
# Positive Euler gamma integral identity proved in PROOF; no analytic continuation.
N=Q(t).gamma()*Q(w).gamma()/(2*Q(s).gamma());root=N.sqrt();assert N>0
out={'start_utc':start,'utc':p.now(),'status':'PASS_ACTUAL_GAMMA_BALL_CONSTANT','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':actual,'arb512':{'N':enclosure(N),'sqrtN':enclosure(root)},'strict_windows':{'N':window(N),'sqrtN':window(root)},'scope':'Gamma-ball evaluation of the positive beta identity and exact parameter checks. Functional analysis is proved in PROOF, not by scalar assertions.'};p.write(E/'check.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['parent_files','arb512']}))
