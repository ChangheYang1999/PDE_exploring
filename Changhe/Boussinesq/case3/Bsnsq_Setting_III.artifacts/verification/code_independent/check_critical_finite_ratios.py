"""Own finite-remainder audit for P231. No lead or numerics code is used."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import hashlib,json,time,shutil
root=Path(__file__).resolve().parents[1];v=root/'research/231_critical_finite_axis_ratios/verification'
start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks={};diffs={}
def eq(name,l,r=0):
 d=s.factor(s.cancel(s.expand(l-r)));checks[name]=d==0;diffs[name]=str(d)
def truth(name,z):checks[name]=bool(z)
k,y,x=s.symbols('k y x',real=True);a=s.Function('a')(y);V=s.Function('V')(k,y);E=s.Function('E')(k,y)
A0=s.symbols('A0',nonzero=True);B0,D0=s.symbols('B0 D0')
H=A0*k*k/2+B0*k**4/4+D0*k**6/6;S=H+k**8*E
Q=-a*V*s.diff(S,y)/s.diff(S,k)
eq('general_smooth_Q_quotient',Q/k**7,-a*V*s.diff(E,y)/(A0+B0*k*k+D0*k**4+k**6*(8*E+k*s.diff(E,k))))
eq('I2_constant_coefficient',s.diff(H,k,4).subs(k,0),6*B0)
eq('I3_constant_coefficient',s.diff(H,k,6).subs(k,0),120*D0)
# Direct physical differentiation on a rational, positive-scale fixture.
a=1+y+y*y;AA=y+y*y/2+y**3/3;c2=s.Rational(-3,7);c4=s.Rational(2,11);P=c2*k*k+c4*k**4;D=4*AA+P
def dx(f):return s.diff(f,k)/a
def dy(f):return s.diff(f,y)-k*s.diff(a,y)/a*s.diff(f,k)
def order(f):
 p=s.Poly(s.expand(f),k)
 return min(m[0] for m in p.monoms()) if not p.is_zero else 1000
vp2=D/a;vp1=k*s.diff(a,y)*vp2;g=1+2*y+y*y
eq('comparison_divergence',dx(vp1)+dy(vp2),4)
B=s.diff(a,y,2)/a-2*(s.diff(a,y)/a)**2
op=dy(vp1)-dx(vp2)
eq('physical_curl',op,4*k*s.diff(a,y)+k*D*B-(1+k*k*s.diff(a,y)**2)*s.diff(P,k)/a**2)
o1=4*s.diff(a,y)+4*AA*B-2*c2/a**2;o3=c2*B-4*c4/a**2-2*c2*s.diff(a,y)**2/a**2
St=2*k*k+s.Rational(3,4)*k**4+s.Rational(2,6)*k**6
rp=s.expand(a*(vp1*dx(op)+vp2*dy(op)+op-dx(St)))
eq('F1_direct',rp.coeff(k,1),4*AA*s.diff(o1,y)+a*o1-4)
eq('F3_direct',rp.coeff(k,3),4*AA*s.diff(o3,y)+c2*s.diff(o1,y)+a*o3-3)
records={}
for M in (6,4):
 dv2=k**M*g/a;dQ=-k**(M+1)*s.diff(g,y)/(M+1);dv1=dQ+k*s.diff(a,y)*dv2
 eq(f'M{M}_divergence',dx(dv1)+dy(dv2))
 od=dy(dv1)-dx(dv2)
 rdiff=s.expand(a*((vp1+dv1)*dx(op+od)+(vp2+dv2)*dy(op+od)+op+od-dx(St))-rp)
 truth(f'M{M}_curl_order',order(od)==M-1);truth(f'M{M}_residual_order',order(rdiff)==M-1)
 eq(f'M{M}_F1_protected',rdiff.coeff(k,1))
 if M==6:eq('M6_F3_protected',rdiff.coeff(k,3))
 else:truth('M4_cannot_protect_F3',s.factor(rdiff.coeff(k,3))!=0)
 records[str(M)]={'curl_order':order(od),'residual_order':order(rdiff),'cubic_change':str(s.factor(rdiff.coeff(k,3)))}
 print('orders',M,order(od),order(rdiff),flush=True)
# Finite ratios do not force neighbourhood separation.
Ss=St+y*k**8
Tphys=Ss.subs(k,x/a)
I2=s.cancel(s.diff(Tphys,x,4).subs(x,0)/s.diff(Tphys,x,2).subs(x,0)**2)
I3=s.cancel(s.diff(Tphys,x,6).subs(x,0)/s.diff(Tphys,x,2).subs(x,0)**3)
I4=s.cancel(s.diff(Tphys,x,8).subs(x,0)/s.diff(Tphys,x,2).subs(x,0)**4)
eq('finite_I2_constant',s.diff(I2,y));eq('finite_I3_constant',s.diff(I3,y));truth('eighth_ratio_varies',s.diff(I4,y)!=0)
# The finite elimination dependency is frozen and its exact certificates rechecked.
p227=root/'research/227_lead_separable_vorticity_audit/verification/checks.json';dep=json.loads(p227.read_text())
shutil.copyfile(p227,v/'P227_checks.json');shutil.copyfile(root/'research/227_lead_separable_vorticity_audit/PROOF.md',v/'P227_PROOF.md')
truth('dependency53checks',dep['all_passed'] and len(dep['checks'])==53)
t=s.symbols('t');pp=-130509*t*t+4496958*t+12320;qq=-405889875*t**3+30302578176*t*t+58633849676*t+1213256384
bp=s.sympify(dep['bezout_P'],locals={'t':t});bq=s.sympify(dep['bezout_Q'],locals={'t':t})
eq('P227_Bezout_certificate',bp*pp+bq*qq,1)
eq('resultant_recomputed',s.resultant(pp,qq,t),s.Integer(dep['resultant']))
r,c2,c4=s.symbols('r c2 c4');local={'r':r,'c2':c2,'c4':c4}
eq('r2_dependency',s.sympify(dep['jets']['r2'],locals=local),9*r*(2*r-c2)/40)
eq('r3_dependency',s.sympify(dep['jets']['r3'],locals=local),r*(128*r-51*c2)*(2*r-c2)/2160)
eq('r4_dependency',s.sympify(dep['jets']['r4'],locals=local),r*(2*r-c2)*(6375*c2*c2-60562*c2*r+44704*r*r)/4492800)
eq('r5_dependency',s.sympify(dep['jets']['r5'],locals=local),r*(2*r-c2)*(-70125*c2**3+2822036*c2*c2*r-2726484*c2*r*r+1392064*r**3)/1272960000)
eq('B0_dependency',s.sympify(dep['B0'],locals=local),-(c2*c2*r+78*c2*r*r+80*c4)/20)
eq('E3_y2_dependency',s.sympify(dep['E3_y2'],locals=local),-c2*r**3*(2*r-c2)*pp.subs(t,c2/r)/1123200)
eq('E3_y3_dependency',s.sympify(dep['E3_y3'],locals=local),c2*r**4*(2*r-c2)*qq.subs(t,c2/r)/15466464000)
n=s.symbols('n',integer=True,positive=True);m=n+1
eq('highest_recursion_coefficient',-16*m*(m-1)*(m-2)-36*m*(m-1)-4*m,-4*(n+1)**2*(4*n+1))
truth('proof_before_controls',json.loads((v/'proof_before_checks.json').read_text())['written_utc']<start)
end=datetime.now(timezone.utc).isoformat();out={'started_utc':start,'ended_utc':end,'elapsed_seconds':time.monotonic()-t0,'all_passed':all(checks.values()),'checks':checks,'differences':diffs,'fixtures':records,'proof_sha256':hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Own finite remainder controls plus exact frozen algebraic dependency; fixtures are not PDE solutions. No lead/numerics code used.'}
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({key:out[key] for key in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('checks',len(checks),'failed',[q for q,z in checks.items() if not z])
