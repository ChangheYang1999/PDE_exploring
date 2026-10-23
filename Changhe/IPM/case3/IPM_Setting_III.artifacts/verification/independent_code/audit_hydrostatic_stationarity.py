"""Finite-dimensional counterexamples and frozen hydrostatic-log arithmetic."""
from pathlib import Path
import datetime, hashlib, json, math, re, time
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
V=ROOT/'research/hydrostatic_stationarity_audit/verification'
start=time.monotonic(); checks=[]
def check(name,passed,detail=None):checks.append(dict(name=name,passed=bool(passed),detail=detail))
def exact(name,z):
    if isinstance(z,s.MatrixBase): z=z.applyfunc(s.simplify); check(name,z==s.zeros(*z.shape),str(z))
    else: z=s.simplify(z);check(name,z==0,str(z))
inputs=json.loads((V/'INPUTS.json').read_text())
for name,row in inputs['inputs'].items():check('frozen '+name,hashlib.sha256((V/name).read_bytes()).hexdigest()==row['sha256'])
a,b,d,L=s.symbols('a b d L',real=True)
F=s.Matrix([a,b,d]); P=s.Matrix([a,0,0]); lin=F-L*P
exact('orthogonal residual decomposition',F.dot(F)-(a*a+b*b+d*d))
exact('linearized norm decrease',lin.dot(lin)-(F.dot(F)-(2*L-L*L)*P.dot(P)))
exact('half norm directional derivative',s.diff(lin.dot(lin)/2,L).subs(L,0)+P.dot(P))
exact('unit-step prediction',lin.dot(lin).subs(L,1)-(F.dot(F)-a*a))
e=s.symbols('epsilon',positive=True)
J=s.diag(1,e); FF=s.Matrix([0,1]); DD=s.Matrix([0,-1/e]); A=J
exact('dropped correction removes residual',J*DD+FF)
exact('dropped correction changes field by one', (A*DD).dot(A*DD)-1)
exact('nonzero discarded gradient',J.T*FF-s.Matrix([0,e]))
exact('coordinate rescaling changes spectrum',J*s.diag(1,1/e)-s.eye(2))
J2=s.Matrix([[1,1],[0,e]]); vv=s.Matrix([-1,1])/s.sqrt(2)
exact('visible restriction has unit norm',(J2*s.Matrix([1,0])).dot(J2*s.Matrix([1,0]))-1)
exact('small-J direction strongly sampled', (A*vv).dot(A*vv)-(1+e*e)/2)
exact('small-J direction action',(J2*vv).dot(J2*vv)-e*e/2)
t=s.symbols('t'); f=1+t+3*t*t
check('nonlinear full step increases actual residual',f.subs(t,-1)**2>f.subs(t,0)**2,str(f.subs(t,-1)**2))
exact('nonlinear initial GN descent derivative',s.diff(f*f/2,t).subs(t,0)*(-1)+1)
rows=[]
pat=re.compile(r'runs/(\S+)\.pt\s+(\d+)x(\d+)\s+c\s+([\d.]+).*?rho_1 = \|U_keep\^T F\|/\|F\| ([\deE+.-]+) \(all s: ([\deE+.-]+); visible subspace: ([\deE+.-]+)\).*?\|J\^T F\|/\(smax \|F\|\) ([\deE+.-]+)')
for line in (V/'stationarity_log.txt').read_text().splitlines():
    m=pat.search(line)
    if not m:continue
    tag,n,mm,c,k,all_,vis,grad=m.groups();k,all_,vis,grad=map(float,[k,all_,vis,grad])
    row=dict(tag=tag,N=int(n),M=int(mm),c=float(c),rho_keep=k,rho_all=all_,rho_visible=vis,gradient=grad,drop_norm=math.sqrt(max(0,all_*all_-k*k)),outside_norm=math.sqrt(max(0,1-all_*all_)),linearized_decrease_fraction=k*k,visible_difference=abs(k-vis))
    rows.append(row)
    check('projection arithmetic '+tag,0<=k<=all_<=1 and grad<=k*1.02,row)
check('all twelve stationarity rows parsed',len(rows)==12,len(rows))
by={q['tag']:q for q in rows}
check('A64 outside range exceeds half',by['hsA_c3.0_N64']['outside_norm']>.5)
check('D64 outside range exceeds half',by['hsD_c3.0_N64_keep']['outside_norm']>.5)
check('E2N96 visible discrepancy refutes1e-4',by['hsE_c2.0_N96_hr']['visible_difference']>1e-4)
check('C3N64 visible discrepancy refutes1e-4',by['hsC_c3.0_N64_fine']['visible_difference']>1e-4)
source=(V/'dilation_source.py').read_text()
for name,text in [('coefficient projection','Dk[:, k] @ m.Proj[k].T'),('per-mode relative cutoff','keep = S_ >= 1e-8 * S_[0]'),('unwhitened visible restriction','JV = JR @ V'),('Euclidean dilation norm','vn = v / v.norm()'),('row removal','JR = J[:-nrows_extra]')]:check(name,text in source)
station=(V/'stationarity_source.py').read_text()
for name,text in [('computed all-column projection','r_all = (U.T @ F).norm().item() / nF'),('computed kept projection','r_keep = (U[:, keep].T @ F).norm().item() / nF'),('computed coefficient gradient','g = J.T @ F')]:check(name,text in station)
dilate=[]; prev=None
vp=re.compile(r'visible subspace dim (\d+) of nu (\d+).*?s_min/smax ([\deE+.-]+).*?count s<1e-13 smax (\d+), <1e-8 (\d+), <1e-4 (\d+).*?overlap with v_smin ([\d.]+)')
for line in (V/'dilation_log.txt').read_text().splitlines():
    m=vp.search(line)
    if m:prev=m.groups();continue
    m=re.search(r'runs/(hsA_c3.0_N\d+)\.pt.*?\|J_h v\|/\(smax\|v\|\) ([\deE+.-]+).*?s<1e-13 smax \[(\d+)\].*?proj.defect ([\deE+.-]+)',line)
    if m and prev:
        tag,jv,n13,pdef=m.groups();dim,nu,smin,v13,v8,v4,overlap=prev
        dilate.append(dict(tag=tag,dim=int(dim),nu=int(nu),smin=float(smin),full13=int(n13),visible13=int(v13),visible8=int(v8),visible4=int(v4),overlap=float(overlap),projection_defect=float(pdef),Jv=float(jv)))
check('four c3 dilation logs parsed',len(dilate)==4,len(dilate))
check('full ratios1/27/247/679',[q['full13'] for q in dilate]==[1,27,247,679])
check('restricted ratios zero at cutoff',[q['visible13'] for q in dilate]==[0,0,0,0])
check('projection defect range',min(q['projection_defect'] for q in dilate)==6.5e-6 and max(q['projection_defect'] for q in dilate)==3.1e-5)
result=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,passed=all(z['passed'] for z in checks),count=len(checks),stationarity_rows=rows,dilation_rows=dilate,scope='Static source/log pairings and independent finite-dimensional algebra. New producer Jacobians and fields not recomputed.')
(V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['utc','elapsed_seconds','passed','count']}))
for z in checks:
    if not z['passed']: print('FAIL',z)
raise SystemExit(0 if result['passed'] else 1)
