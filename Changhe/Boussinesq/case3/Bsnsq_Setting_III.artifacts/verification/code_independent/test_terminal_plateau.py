"""Independent manufactured controls for the local plateau obstruction.
No claim of profile existence, full numerical proof, or limit from finite time.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import argparse,json,time
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

def main():
 parser=argparse.ArgumentParser();parser.add_argument('root');args=parser.parse_args();root=Path(args.root);root.mkdir(exist_ok=True,parents=True)
 start=time.monotonic();utc=datetime.now(timezone.utc).isoformat()
 inp={'rectangle_radius':'1','c_values':['-2','0','2'],'u_values':['-1/10','-1/25','0','1/25','1/10'],'v_values':['-1/4','-1/10','1/10','1/4'],'times':['0','-2','-10','-40'],'flat_exponent_scale':'1/100','d_lower_bound':'27/10','rtol':'2/10000000000000','atol':'1/100000000000000','max_step':'1/2'}
 (root/'inputs.json').write_text(json.dumps(inp,indent=2)+'\n');q=lambda x:float(Fraction(x))
 x,y=sp.symbols('x y',real=True);v=sp.Function('v')(x);F=sp.Function('F')(x)
 exact=[]
 def check(name,value):
  value=sp.simplify(value);exact.append({'name':name,'expression':str(value),'pass':value==0})
 # Direct curl/divergence controls in physical Cartesian coordinates.
 w1=sp.Function('w1')(x,y);w2=sp.Function('w2')(x,y);div=sp.diff(w1,x)+sp.diff(w2,y);curl=sp.diff(w2,x)-sp.diff(w1,y)
 check('laplacian_first_component',sp.diff(w1,x,2)+sp.diff(w1,y,2)-sp.diff(div,x)+sp.diff(curl,y))
 check('laplacian_second_component',sp.diff(w2,x,2)+sp.diff(w2,y,2)-sp.diff(div,y)-sp.diff(curl,x))
 W=sp.Matrix([v,(4-sp.diff(v,x))*y]);om=-(sp.diff(W[1],x)-sp.diff(W[0],y));res=sp.diff(om,x)*W[0]+sp.diff(om,y)*W[1]+om
 check('flat_outgoing_reference_divergence',sp.diff(W[0],x)+sp.diff(W[1],y)-4)
 check('flat_outgoing_reference_vorticity',om-y*sp.diff(v,x,2))
 check('flat_outgoing_reference_residual',res-y*(v*sp.diff(v,x,3)+(5-sp.diff(v,x))*sp.diff(v,x,2)))
 # Both PDEs can hold with a terminal plateau when there is no endpoint.
 W=sp.Matrix([0,4*y-F]);om=sp.diff(F,x)
 check('continued_zero_arc_divergence',sp.diff(W[0],x)+sp.diff(W[1],y)-4)
 check('continued_zero_arc_curl',-(sp.diff(W[1],x)-sp.diff(W[0],y))-om)
 check('continued_zero_arc_thermal',sum(W[i]*sp.diff(F,[x,y][i]) for i in range(2)))
 check('continued_zero_arc_vorticity',sum(W[i]*sp.diff(om,[x,y][i]) for i in range(2))+om-sp.diff(F,x))
 # Polynomial harmonic field with continued zero line, in a rotated Cartesian frame.
 c=sp.Rational(3,5);s=sp.Rational(4,5);normal=-s*x+c*y;W=4*normal*sp.Matrix([-s,c])
 check('rotated_analytic_zero_line_divergence',sp.diff(W[0],x)+sp.diff(W[1],y)-4)
 check('rotated_analytic_zero_line_curl',sp.diff(W[1],x)-sp.diff(W[0],y))
 check('rotated_analytic_zero_line_equilibria',W.subs({x:c*sp.Symbol('t'),y:s*sp.Symbol('t')})[0])
 flows=[];ts=np.array([q(t) for t in inp['times']]);scale=q(inp['flat_exponent_scale']);dmin=q(inp['d_lower_bound'])
 for cv in map(q,inp['c_values']):
  for u0 in map(q,inp['u_values']):
   for v0 in map(q,inp['v_values']):
    def rhs(t,z):
     u,v,l=z;g=np.exp(-scale/u**2) if u>0 else 0.;cc=cv*np.sin(u)*np.cos(v);dd=3+.3*np.sin(u*v)
     return [g+u*v*cc,v*dd,v*cc]
    sol=solve_ivp(rhs,(0.,ts[-1]),[u0,v0,0.],method='DOP853',t_eval=ts,rtol=q(inp['rtol']),atol=q(inp['atol']),max_step=q(inp['max_step']))
    assert sol.success
    us,vs,ls=sol.y;ws=us*np.exp(-ls);ub=abs(u0)*np.exp(abs(cv)*abs(v0)/dmin);vb=abs(v0)*np.exp(dmin*ts)
    # Absolute tolerances here concern finite flow samples, never PDE ratios.
    bounded=bool(np.max(abs(us))<=ub+2e-12 and np.all(abs(vs)<=vb+2e-12));inside=bool(np.max(abs(sol.y[:2]))<1)
    invariant=bool(np.max(abs(ws-ws[0]))<2e-12 if u0<0 else np.max(abs(us))<2e-12 if u0==0 else np.all(np.diff(ws)<=2e-12) and np.min(us)>0)
    flows.append({'c_parameter':cv,'u0':u0,'v0':v0,'times':ts.tolist(),'u':us.tolist(),'v':vs.tolist(),'integral_vc':ls.tolist(),'w':ws.tolist(),'proved_uniform_u_bound':ub,'max_observed_abs_u':float(np.max(abs(us))),'bound_pass':bounded,'inside_rectangle':inside,'integrating_factor_pass':invariant,'pass':bounded and inside and invariant})
 out={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact':exact,'flows':flows,'all_passed':all(e['pass'] for e in exact+flows),'scope':'Exact algebra and finite backward-flow controls only. No limit, neighborhood theorem, or B2 existence claim is inferred from samples.'}
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['exact','flows']},indent=2));print('exact',len(exact),'flows',len(flows),'failures',sum(not e['pass'] for e in exact+flows))
 if not out['all_passed']:raise SystemExit(1)
if __name__=='__main__':main()
