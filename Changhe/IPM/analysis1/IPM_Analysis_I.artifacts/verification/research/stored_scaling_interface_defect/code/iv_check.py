from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from mpmath import iv
import hashlib,json,re,sys
sys.dont_write_bytecode=True;iv.dps=220
R=Path(__file__).resolve().parents[3];D=R/'research/stored_scaling_interface_defect';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def hx(s):
 m=re.fullmatch(r'([+-]?)0x([0-9a-f]+)\.([0-9a-f]+)p([+-]?\d+)',s);assert m,s
 sign,whole,part,power=m.groups();return Q((-1 if sign=='-' else 1)*int(whole+part,16))*Q(2)**(int(power)-4*len(part))
def rat(s):
 z=s.split('/');assert 1<=len(z)<=2;return Q(int(z[0]),int(z[1]) if len(z)==2 else 1)
def dec(s):
 m=re.fullmatch(r'([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?',s);assert m
 sign,whole,part,power=m.groups();part=part or '';return Q((-1 if sign=='-' else 1)*int(whole+part))*Q(10)**(int(power or 0)-len(part))
def iq(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ends(z):
 def f(t):sign,mant,expo,bits=t;assert bits==mant.bit_length();return Q((-1 if sign else 1)*mant)*Q(2)**expo
 return {'lower_exact':str(f(z._mpi_[0])),'upper_exact':str(f(z._mpi_[1]))}
def convolution(a,b):
 out={}
 for j,x in a.items():
  for k,y in b.items():out[j+k]=out.get(j+k,Q(0))+x*y
 return {j:x for j,x in out.items() if x}
def project(v):
 # Laurent z=e^(i theta), all coefficients of cos^2(theta)sin(theta) are imaginary.
 cos={1:Q(1,2),-1:Q(1,2)};sin_over_i={1:Q(-1,2),-1:Q(1,2)};base=convolution(convolution(cos,cos),sin_over_i);res={}
 for m,z in enumerate(v):
  cp={0:Q(1)} if m==0 else {2*m:Q(1,2),-2*m:Q(1,2)}
  for n,a in convolution(base,cp).items():res[n]=res.get(n,Q(0))+a*z
 for n,z in res.items():assert res.get(-n,Q(0))==-z
 return {n:-2*z for n,z in res.items() if n>0 and z}
start=datetime.now(timezone.utc).isoformat();A=load(E/'arb.json');assert A['code_sha256']==sha(D/'code/arb_check.py');assert A['proof_sha256']==sha(D/'PROOF.md')
for key in ['npz','hex_json']:assert sha(R/A[key]['path'])==A[key]['sha256']
for n,z in A['source_snapshots'].items():assert sha(R/n)==z['sha256']
x=load(R/A['hex_json']['path']);assert x['source_npz_sha256']==A['npz']['sha256'];assert x['degree']==7
z=x['arrays'];assert z['S']['shape']==[260,1565] and z['knots']['shape']==[1573]
def get(name,i,j):
 shape=z[name]['shape'];assert len(shape)==2;return hx(z[name]['hex'][i*shape[1]+j])
a,b=hx(z['knots']['hex'][0]),hx(z['knots']['hex'][-1]);kn=[hx(t) for t in z['knots']['hex']];assert kn[:8]==[a]*8 and kn[-8:]==[b]*8;assert a<kn[8] and kn[-9]<b and all(t<=s for t,s in zip(kn,kn[1:]));assert a==rat(A['a_exact']) and b==rat(A['b_exact'])
Ji=[];Jo=[]
for m in range(260):
 Ji.append(sum([get('D',m,j) for j in reversed(range(7))],get('Ei',m,0)-get('S',m,0))+Q(m==0))
 Jo.append(sum([get('Aout',m,j) for j in reversed(range(10))],get('Eo',m,0)-get('S',m,1564)))
assert list(map(str,Ji))==A['join_inner_minus_spline'];assert list(map(str,Jo))==A['join_outer_minus_spline'];assert all(Ji) and all(Jo)
fi,fo=project(Ji),project(Jo);pi,po,ti,to=fi[3],fo[3],fi[1],fo[1];assert (pi,po,ti,to)==tuple(rat(A[n]) for n in ['P_inner','P_outer','F1_inner','F1_outer'])
# Different scalar form: square exp(a), exp(b), factor out exp(b)^2 in the cancellation.
ra=iv.exp(iq(a));rb=iv.exp(iq(b));e2a=ra*ra;e2b=rb*rb
V={'inner_strain_term':-iq(pi)*e2a,'outer_strain_term':iq(po)*e2b,'Sigma_K_pw':e2b*(iq(po)-iq(pi)*(ra/rb)**2),'Sigma_source_minus_canonical':(iq(ti+pi)*e2a-iq(to+po)*e2b)/4}
B={n:ends(t) for n,t in V.items()}
for n,t in B.items():
 ar=A['arb512'][n];assert max(rat(t['lower_exact']),rat(ar['lower_exact']))<=min(rat(t['upper_exact']),rat(ar['upper_exact']))
 assert rat(t['lower_exact'])*rat(t['upper_exact'])>0
windows={'Sigma_K_pw':['4.46796331677046e-18','4.46796331677047e-18'],'Sigma_source_minus_canonical':['-2.56259669151642e-17','-2.56259669151641e-17']}
for n,(l,u) in windows.items():
 for t in [A['arb512'][n],B[n]]:assert dec(l)<rat(t['lower_exact'])<=rat(t['upper_exact'])<dec(u)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_HEX_LAURENT_IV220_STORED_INTERFACE_DEFECT_REQUIRES_ACTUAL_REVIEW','code_sha256':sha(Path(__file__)),'arb_json_sha256':sha(E/'arb.json'),'exact_modal_jumps_checked':520,'nonzero_inner':260,'nonzero_outer':260,'full_angle_projection_modes':{'inner':len(fi),'outer':len(fo)},'iv220':B,'strict_decimal_windows':windows,'conclusions':{'literal_stored_rho_is_weak_H1_loc':'REFUTED','ordinary_stored_K_pw_has_zero_canonical_strain':'REFUTED','source_only_and_canonical_strain_are_identical':'REFUTED','exactly_joined_canonical_trial':'OUTSIDE_SCOPE'},'scope':'Literal dyadic stored function with knot joins; continuous exact repair excluded. Source-only comparison is ideal exact arithmetic, not an error bound on floating operations.'}
with (E/'iv.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','exact_modal_jumps_checked','full_angle_projection_modes','strict_decimal_windows']}))
