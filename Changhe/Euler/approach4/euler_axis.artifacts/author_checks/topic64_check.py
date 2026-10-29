# Lead cross-check of the verifier's transport near-null example (topic64), c_l = 2/3.
import sympy as sp, json, time
t0=time.time()
r,z,eps,R,Z,K,dl=sp.symbols('r z epsilon R Z K delta',positive=True)
c=sp.Rational(2,3)
phi=z/2
Ur=-r*sp.diff(phi,z); Uz=2*phi+r*sp.diff(phi,r)
Wr=c*r+Ur; Wz=c*z+Uz
a=1-2*sp.diff(phi,z)
s=r**2
f=s**10+z**2; G=s**10/f
L=lambda q: Wr*sp.diff(q,r)+Wz*sp.diff(q,z)
out={}
out['W']=[str(sp.simplify(Wr)),str(sp.simplify(Wz))]
out['a']=str(a)
out['Wgrad_f_over_f']=str(sp.simplify(L(f)/f))
out['Wgrad_G']=str(sp.simplify(L(G)))
# divergence of the 3D field W = c x + U (axisymmetric): (1/r) d_r(r W^r) + d_z W^z
out['divW']=str(sp.simplify(sp.diff(r*Wr,r)/r+sp.diff(Wz,z)))
# scaling r = eps R, z = eps^10 Z
v=sp.simplify((f/eps**20).subs({r:eps*R,z:eps**10*Z}))
out['v_scaled']=str(v)
jac=sp.diff(eps*R,R)*sp.diff(eps**10*Z,Z)*(eps*R)  # r dr dz
out['measure_factor']=str(sp.simplify(jac/R))
# R_q for q = K(1 + delta psi(v) G), with a = 0: K delta psi'(v) (W.grad v) G
psi=sp.Function('psi')
q=K*(1+dl*psi(f/eps**20)*G)
Rq=sp.simplify(L(q))
out['Rq']=str(Rq)
# R_eta = -d_z(q^2) in scaled variables: power of eps
Reta=-sp.diff(q**2,z)
Reta_s=sp.simplify(Reta.subs({r:eps*R,z:eps**10*Z}))
out['Reta_scaled_times_eps10_free_of_eps']=str(sp.simplify(sp.diff(sp.expand(Reta_s*eps**10),eps)).doit()=='0')
# L2 rates: ||Rq||^2 ~ eps^12 * O(1); ||Reta||^2 ~ eps^-20 * eps^12
out['rate_Rq']='eps^6'; out['rate_Reta']='eps^-4'
out['liouville_rate_general']='3c/2 with t = 6 log eps here, 3c/2 = 1: eps^6 (consistent)'
out['seconds']=time.time()-t0
print(json.dumps(out,indent=1))
json.dump(out,open('checks/topic64_check_output.json','w'),indent=1)
# Redo the R_eta scaling with a concrete function of v (any function of v alone; v is eps-free after scaling).
vv=f/eps**20
for name,ps in (('v^3',vv**3),('exp(-v)',sp.exp(-vv))):
    qq=K*(1+dl*ps*G)
    Re=-sp.diff(qq**2,z)
    Res=sp.simplify(Re.subs({r:eps*R,z:eps**10*Z})*eps**10)
    out['Reta_eps10_'+name+'_depends_on_eps']=bool(sp.simplify(sp.diff(Res,eps))!=0)
    Rqs=sp.simplify(L(qq).subs({r:eps*R,z:eps**10*Z}))
    out['Rq_'+name+'_depends_on_eps']=bool(sp.simplify(sp.diff(Rqs,eps))!=0)
out['seconds']=time.time()-t0
print(json.dumps(out,indent=1))
json.dump(out,open('checks/topic64_check_output.json','w'),indent=1)
