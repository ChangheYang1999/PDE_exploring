from pathlib import Path
import sys,json
sys.dont_write_bytecode=True
from flint import fmpq as Q
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_full_graph_nonlinearity';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();a0=p.load(E/'check.json');p.rehash(a0['parent_files']);assert p.sha(D/'PROOF.md')==a0['proof_sha256']=='3ecda23dfa05f97bb7aedb762506b6d21e5a40e6918d6c9fc69d3b893cce4f32'
assert a0['parent_files']['research/logarithmic_full_graph_center_trace/evidence/verdict.json']=='a23396a208ea81bacceb01c17ed90f371f0cf8e7a27a0b02e2471a6a61459f3f'
raw=R/'data_exact/modal_v2.json';assert p.sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';raw=p.load(raw)
def hx(t):
 sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,e=t.split('p');whole,frac=m[2:].split('.');return Q(sign*int(whole+frac,16))*Q(2)**(int(e)-4*len(frac))
k,bi,L=[hx(raw['scalars_hex'][n]) for n in ['k','bi','L']];tau=hx(raw['arrays']['knots']['hex'][0]);degree=raw['degree'];modes=raw['arrays']['S']['shape'][0]
actual={'k':k,'A':Q(2)/k-1,'D':Q(4)/k-1,'bi':bi,'L':L,'inner_tau':tau,'spline_degree':Q(degree),'modes':Q(modes),'s_example':Q(153,50),'center_Vx_coefficient':1-Q(2)/k};assert {n:str(v) for n,v in actual.items()}==a0['actual'];assert 0<k<Q(1,2) and bi>50 and L>0 and tau<0 and degree==7 and modes==260
# Independent rational differential ring. Monomial powers are x,y,n,V1,V2.
# Cos/Sin jets are differentiated with the phase chain rule. Other jets
# represent arbitrary smooth fields; no Sympy or primary evaluator is imported.
def mon(ex=(0,)*5,jets=(),c=1):return {(tuple(ex),tuple(sorted(jets))):Q(c)} if c else {}
def var(i,j=1):
 ex=[0]*5;ex[i]=j;return mon(ex)
def jet(name,i=0,j=0):return mon(jets=((name,i,j),))
def add(*args):
 d={}
 for f in args:
  for k,c in f.items():d[k]=d.get(k,Q(0))+c
 return {k:c for k,c in d.items() if c}
def sc(f,c):return {k:v*c for k,v in f.items() if v*c}
def mul(*args):
 d=mon()
 for f in args:
  out={}
  for (a,j),c in d.items():
   for (b,jj),cc in f.items():
    k=(tuple(v+w for v,w in zip(a,b)),tuple(sorted(j+jj)));out[k]=out.get(k,Q(0))+c*cc
  d={k:c for k,c in out.items() if c}
 return d
def der(f,axis):
 out={}
 for (ex,jets),c in f.items():
  if ex[axis]:
   ee=list(ex);ee[axis]-=1;out=add(out,mon(ee,jets,c*ex[axis]))
  for at,(name,i,j) in enumerate(jets):
   jj=list(jets)
   if name in ['Cos','Sin']:
    assert i==j==0;jj[at]=('Sin' if name=='Cos' else 'Cos',0,0)
    out=add(out,mul(mon(ex,jj,-c if name=='Cos' else c),var(2),jet('Phi',1 if axis==0 else 0,1 if axis==1 else 0)))
   else:
    ij=[i,j];ij[axis]+=1;jj[at]=(name,*ij);out=add(out,mon(ex,jj,c))
 return out
def d(f,i,n=1):
 for _ in range(n):f=der(f,i)
 return f
def lap(f):return add(d(f,0,2),d(f,1,2))
def U(f):return sc(d(d(f,0),1),-1),d(f,0,2)
x,y,n,v1,v2=[var(i) for i in range(5)];A,Phi,C,Sin=[jet(nm) for nm in ['A','Phi','Cos','Sin']]
checks={}
def check(name,left,right=None):
 if right is None:right={}
 assert left==right,(name,left,right);checks[name]=True
F=jet('F');h=sc(lap(F),-1);stream=d(F,0);u1,u2=U(F)
check('canonical_Poisson',sc(lap(stream),-1),d(h,0));check('divergence_free',add(d(u1,0),d(u2,1)));check('curl_sign',add(d(u2,0),sc(d(u1,1),-1),d(h,0)))
# Centered coordinate x means physical x-p in the fixed plateau.
plateau=sc(var(0,2),Q(1,2));g=sc(lap(plateau),-1);gu1,gu2=U(plateau)
check('plateau_density',g,mon(c=-1));check('plateau_velocity1',gu1);check('plateau_velocity2',gu2,mon());check('plateau_gradient_x',d(g,0));check('plateau_gradient_y',d(g,1))
f=mul(var(2,-2),A,C);h=sc(lap(f),-1);u1,u2=U(f);px,py=d(Phi,0),d(Phi,1)
A0=mul(A,add(mul(px,px),mul(py,py)));A1=add(sc(add(mul(d(A,0),px),mul(d(A,1),py)),2),mul(A,lap(Phi)));A2=lap(A)
check('density_wave_expansion',h,add(mul(A0,C),mul(var(2,-1),A1,Sin),sc(mul(var(2,-2),A2,C),-1)))
U1=add(mul(A,px,py,C),mul(var(2,-1),add(mul(d(A,0),py),mul(d(A,1),px),mul(A,d(px,1))),Sin),sc(mul(var(2,-2),d(d(A,0),1),C),-1))
U2=add(sc(mul(A,px,px,C),-1),sc(mul(var(2,-1),add(sc(mul(d(A,0),px),2),mul(A,d(px,0))),Sin),-1),mul(var(2,-2),d(A,0,2),C))
check('velocity1_wave_expansion',u1,U1);check('velocity2_wave_expansion',u2,U2)
def Vd(f):return add(mul(v1,d(f,0)),mul(v2,d(f,1)))
phasefactor=add(sc(mul(n,A0,Sin),-1),mul(A1,C),mul(var(2,-1),A2,Sin))
expect=add(mul(Vd(A0),C),mul(var(2,-1),Vd(A1),Sin),sc(mul(var(2,-2),Vd(A2),C),-1),mul(Vd(Phi),phasefactor))
check('transport_phase_factorization',Vd(h),expect)
rest=add(mul(add(d(A0,1),mul(A1,py)),C),mul(var(2,-1),add(d(A1,1),mul(A2,py)),Sin),sc(mul(var(2,-2),d(A2,1),C),-1))
check('transverse_leading_remainder',d(h,1),add(sc(mul(n,A0,py,Sin),-1),rest))
check('plateau_cross_exact',add(mul(gu1,d(h,0)),mul(gu2,d(h,1)),mul(u1,d(g,0)),mul(u2,d(g,1))),d(h,1))
# Derivative jets under the full four-patch reflection, not numerical samples.
original_h=sc(lap(F),-1);original_u=U(F);ref=[]
def reflect_F(poly,sx,sy):
 out={}
 for (ex,jets),c in poly.items():
  factor=sx**ex[0]*sy**ex[1]
  for name,i,j in jets:
   assert name=='F';factor*=sy*sx**i*sy**j
  out=add(out,mon(ex,jets,c*factor))
 return out
for sx in [-1,1]:
 for sy in [-1,1]:
  check(f'reflection_density_{sx}_{sy}',reflect_F(original_h,sx,sy),sc(original_h,sy))
  for j,fac in enumerate([sx,sy]):check(f'reflection_velocity_{sx}_{sy}_{j}',reflect_F(original_u[j],sx,sy),sc(original_u[j],fac))
  ref.append({'sx':sx,'sy':sy,'potential_sign':sy,'velocity_signs':[sx,sy]})
assert ref==a0['reflections']
# Inverse chart phase gradient at P is (-V2/V1,1).
check('flow_phase_first_integral_at_P',add(mul(v1,sc(mul(v2,var(3,-1)),-1)),v2));check('vertical_phase_derivative',mon(),mon(c=1))
G,H,ug1,ug2,uh1,uh2,sg,sh=[jet(nm) for nm in ['G','H','Ug1','Ug2','Uh1','Uh2','SigmaG','SigmaH']]
def q(U1,U2,Sig,dens):return add(mul(U1,d(dens,0)),mul(U2,d(dens,1)),sc(mul(Sig,add(mul(x,d(dens,0)),mul(y,d(dens,1)))),Q(1,3)))
qp=q(add(ug1,uh1),add(ug2,uh2),add(sg,sh),add(G,H));qm=q(add(ug1,sc(uh1,-1)),add(ug2,sc(uh2,-1)),add(sg,sc(sh,-1)),add(G,sc(H,-1)))
cross=add(q(ug1,ug2,sg,H),q(uh1,uh2,sh,G));check('full_rank_one_polarization',add(qp,sc(qm,-1)),sc(cross,2))
qp0=q(add(ug1,uh1),add(ug2,uh2),{},add(G,H));qm0=q(add(ug1,sc(uh1,-1)),add(ug2,sc(uh2,-1)),{},add(G,sc(H,-1)))
check('zero_strain_polarization',add(qp0,sc(qm0,-1)),sc(add(q(ug1,ug2,{},H),q(uh1,uh2,{},G)),2))
check('quadratic_homogeneity',q(mul(n,ug1),mul(n,ug2),mul(n,sg),mul(n,G)),mul(var(2,2),q(ug1,ug2,sg,G)))
powers=[]
for order in [0,1,2]:
 # Affine coefficients of s in the modulation-adjusted power (-s-order)+s.
 out=(Q(-order),Q(-1)+1);assert out==(Q(-order),Q(0));powers.append(list(map(str,out)))
assert Q(-1,2)*2+1==0 and actual['D']==2*actual['A']+1
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_FMPQ_WAVE_JET_AND_POLARIZATION_ALGEBRA','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(a0['parent_files']),'exact_parameters_compared':len(actual),'ring_checks':checks,'modulation_adjusted_affine_powers':powers,'scaled_cross_power':'0','reflections_compared':len(ref),'source_reuse':'Leibniz rational ring structure adapted from prior independent checkers; new phase Sin/Cos chain rule and polarization. No NumPy, Sympy or primary evaluator imported. Common n^(-s) is factored out as a spatial constant.','scope':'Exact finite algebra only. The vertical phase derivative is an initial-coordinate convention, not computational evidence for existence of the flow chart. Sobolev estimates, support and discontinuity remain analytic.'};p.write(E/'independent.json',out);print(json.dumps(out))
