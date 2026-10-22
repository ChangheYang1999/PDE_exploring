"""Independent exact row coefficients, raw-payload identity and manufactured cases."""
import sys
sys.dont_write_bytecode=True
import check as c
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq
from datetime import datetime,timezone
import json,zipfile,struct,io,tempfile,hashlib,numpy as np
D=c.D;E=c.E;S=c.S;B=c.B

def payload(p,key):
 with zipfile.ZipFile(p) as z:b=z.read(key+'.npy')
 sz=2 if b[6:8]==b'\x01\x00' else 4;n=int.from_bytes(b[8:8+sz],'little');return b[8+sz+n:]
def pf(q):return F(str(q))
start=c.now();pins=json.loads((E/'checks.json').read_text())['files']
for n,h in pins.items():c.need(c.sha(B/n)==h,'unchanged complete check input')
ref=S/'KC_assembled_image_all260.npz';byte_checks=0
for p in [*S.glob('KC_m*_*.npz'),S/'KprojB2_M16_s16_NJ1_img.npz']:
 for key in ['t_eval','w_i']:c.need(payload(p,key)==payload(ref,key),'all raw grid payload bytes');byte_checks+=1
c.need(payload(ref,'img_direct')==payload(S/'KprojB2_M16_s16_NJ1_img.npz','img_K'),'direct image raw payload bytes');byte_checks+=1
with np.load(ref,allow_pickle=False) as z:t=[F.from_float(float(x)) for x in z['t_eval']];w=[F.from_float(float(x)) for x in z['w_i']]
_,_,tq=c.manual(ref,'t_eval');_,_,wq=c.manual(ref,'w_i');d=[b-a for a,b in zip(t,t[1:])];dq=[b-a for a,b in zip(tq,tq[1:])];om=[d[0]/2]+[(d[i-1]+d[i])/2 for i in range(1,len(t)-1)]+[d[-1]/2];oq=[dq[0]/2]+[(dq[i-1]+dq[i])/2 for i in range(1,len(t)-1)]+[dq[-1]/2];coeff=0
for i in range(len(t)):
 for a,b in [(w[i]**2,wq[i]**2),(om[i]*w[i]**2,oq[i]*wq[i]**2)]:c.need(c.fq(a)==b and a>0,'two exact positive nodal weights');coeff+=1
for i in range(len(d)):
 for power in [1,2]:a=(w[i]+w[i+1])**2/(4*d[i]**power);b=(wq[i]+wq[i+1])**2/(4*dq[i]**power);c.need(c.fq(a)==b and a>0,'two exact positive edge weights');coeff+=1
# Three nodes and two columns, deliberately nonuniform spacing and weights.
c.N=3;c.M=2;tt=list(map(F,[-1,0,2]));ww=list(map(F,[2,3,4]));vv=list(map(F,[1,-2,0,3,2,1]));ds=[F(1),F(2)];oms=[F(1,2),F(3,2),F(1)];expect=[F(0) for _ in c.ROWS]
for i in range(3):
 for n in range(2):
  value=ww[i]**2*vv[2*i+n]**2;a=1+(2*n+1)**2;expect[0]+=value;expect[1]+=oms[i]*value;expect[2]+=a*value;expect[3]+=a*oms[i]*value
for i in range(2):
 for n in range(2):
  edge=((ww[i]+ww[i+1])/2)**2*(vv[2*i+2+n]-vv[2*i+n])**2;expect[2]+=edge/ds[i]**2;expect[3]+=edge/ds[i]
A=c.arb_forms(vv,tt,ww);I=c.iv_forms(vv,tt,ww);manufact=[]
for label,a,b,e in zip(c.ROWS,A,I,expect,strict=True):
 ba=c.ab(a);bi=c.ib(b);c.need(ba[0]<=e<=ba[1] and bi[0]<=e<=bi[1],'manufactured exact form contained by both');manufact.append({'row':label,'exact_Q':str(e),'arb':c.ss(ba),'iv':c.ss(bi)})
# Exercise the actual manual parser on independent boundary and malformed files.
def member(arr):
 b=io.BytesIO();np.save(b,arr,allow_pickle=False);return b.getvalue()
def checkparse(root,label,buf,accept):
 p=root/(label+'.npz')
 with zipfile.ZipFile(p,'w') as z:z.writestr('x.npy',buf)
 try:out=c.manual(p,'x');ok=True
 except (ValueError,SyntaxError,KeyError,struct.error):ok=False;out=None
 c.need(ok is accept,'actual manual parser case '+label);return out
parser=[]
with tempfile.TemporaryDirectory(dir=E,prefix='parser_') as td:
 root=Path(td);arr=np.array([0.0,-0.0,np.nextafter(0.0,1.0),-np.nextafter(0.0,1.0),np.finfo(float).max,np.finfo(float).tiny,1.0,-2.0],dtype='<f8');out=checkparse(root,'boundary_f64',member(arr),True)
 c.need(out[2]==[c.fq(F.from_float(float(x))) for x in arr],'all eight IEEE boundary cases');parser.append('eight_exact_IEEE_boundaries')
 good=member(np.array([1.0],dtype='<f8'))
 bad=[('nan',member(np.array([np.nan],dtype='<f8'))),('inf',member(np.array([np.inf],dtype='<f8'))),('ninf',member(np.array([-np.inf],dtype='<f8'))),('f32',member(np.array([1],dtype='<f4'))),('bigendian',member(np.array([1],dtype='>f8'))),('truncated',good[:-1]),('extra_payload',good+b'x'),('badmagic',b'BADMAG'+good[6:]),('badversion',good[:6]+b'\x09\x00'+good[8:]),('fortran',member(np.asfortranarray(np.ones((2,2),dtype='<f8'))))]
 for label,buf in bad:checkparse(root,label,buf,False);parser.append(label)
# Independent exact range coverage by unit-mode multiplicities.
def tiling(rs):return all(type(a) is int and type(b) is int and 0<=a<b<=260 for a,b in rs) and all(sum(a<=m<b for a,b in rs)==1 for m in range(260))
ranges=json.loads((E/'checks.json').read_text())['ranges'];c.need(tiling(ranges),'independent coverage by multiplicities');bad_ranges=[ranges[:-1],ranges+[ranges[0]],[[0,259]],[[0,260],[5,5]],[[0,261]],[[0,130],[129,260]],[[0,130],[131,260]],[[0.0,260]]]
for rs in bad_ranges:c.need(not tiling(rs),'invalid range mutation rejected')
for p in [Path(__file__),E/'checks.json',D/'REVIEW_RESOLUTION.md',D/'SAVED_SUMMARY_DISCREPANCY.md']:pins[str(p.relative_to(B))]=c.sha(p)
for n,h in pins.items():c.need(c.sha(B/n)==h,'fixed supplement inputs')
res={'start_utc':start,'utc':c.now(),'status':'PASS_RAW_PAYLOAD_EXACT_COEFFICIENT_AND_MANUFACTURED_SUPPLEMENT','raw_payload_equalities':byte_checks,'two_exact_positive_coefficients':coeff,'manufactured_forms':manufact,'parser_cases':parser,'ieee_boundary_values':8,'independent_complete_modes':260,'invalid_range_mutations':len(bad_ranges),'files':dict(sorted(pins.items()))}
with (E/'supplement.json').open('x') as f:json.dump(res,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in res.items() if k not in ['files','manufactured_forms']},indent=2))
