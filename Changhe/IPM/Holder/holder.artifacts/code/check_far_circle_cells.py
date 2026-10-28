"""Independent real-variable checks of certified circle masses.
Floating tests are diagnostics; the proof and Arb bounds give certification.
"""
from pathlib import Path
from datetime import datetime, timezone
from flint import arb, acb, ctx
import numpy as np
from scipy.integrate import quad
import json, hashlib
from certify_far_circles import cell_measures
from circle_transport_plan import best_plan
ctx.prec=160
PI=arb.pi(); ROOT=Path(__file__).resolve().parents[1]

def real_density(theta,q,phase):
    # Direct Cartesian formula for w/(pi*(w*w-1/4)^2), rescaled to radius one.
    x=np.cos(theta); y=np.sin(theta)
    ar=(1-q)*x; ai=(1+q)*y
    dr=ar*ar-ai*ai; di=2*ar*ai
    # e^(-i theta)/(e^(i theta)-q e^(-i theta))^2
    re=(x*dr-y*di)/(np.pi*(dr*dr+di*di))
    im=(-y*dr-x*di)/(np.pi*(dr*dr+di*di))
    return re*np.cos(phase)-im*np.sin(phase)

def main():
    cases=[]; total=0; min_gap=float('inf'); max_quad_error=0
    for n in [24,64,128]:
      width=2*PI/n; points=[]
      for j in range(n//2):
        t=2*PI*(arb(j)+arb(1)/2)/n;points.append(acb(t.cos(),t.sin()))
      for ql,qh in [(0,.0001),(.03,.04),(.20,.21),(.249,.25)]:
        q=arb(str(ql)).union(arb(str(qh))); Q=arb(q.upper())
        M1=3*(1+Q)/(PI*(1-Q)**3);M2=9*(1+4*Q+Q*Q)/(PI*(1-Q)**4)
        values=[z**(-3)/(PI*(1-q*z**(-2))**2) for z in points]
        for p in [0,1,5,8,11,16]:
          phi=PI*p/32;c=phi.cos();s=phi.sin()
          masses,tv=cell_measures(values,c,s,M1,M2,width,2**44)
          costs=[float((2*(PI*min(j+1,n//2)/n).sin())**arb('1/2')) for j in range(n//2+1)]
          plan,info=best_plan(masses,costs)
          # Recheck conservation without calling the imported check_plan.
          balances=[0]*n
          for (i,j),v in plan.items():balances[i]+=v;balances[j]-=v
          assert balances==masses
          for qv in [ql,(ql+qh)/2,qh]:
            tv_actual=0
            for j in range(n//2):
              left=2*np.pi*j/n;right=2*np.pi*(j+1)/n
              signed,e=quad(real_density,left,right,args=(qv,float(phi)),epsabs=2e-13,epsrel=2e-13)
              variation,e2=quad(lambda t:abs(real_density(t,qv,float(phi))),left,right,epsabs=2e-13,epsrel=2e-13,limit=100)
              max_quad_error=max(max_quad_error,e,e2);tv_actual+=variation
              model=masses[j]/2**44
              if model:
                assert signed*model>0
                gap=abs(signed)-abs(model);min_gap=min(min_gap,gap)
                assert gap>=-1e-12
                vals=real_density(np.linspace(left,right,17),qv,float(phi))
                assert np.all(vals*np.sign(model)>=-1e-12)
              # Pointwise oddness checked from the independent Cartesian formula.
              mid=(left+right)/2
              assert abs(real_density(mid+np.pi,qv,float(phi))+real_density(mid,qv,float(phi)))<2e-14
              total+=1
            assert tv_actual<=float(tv.upper())+1e-11
          cases.append(dict(angles=n,q_interval=[ql,qh],phase_index=p,plan=info,edges=len(plan)))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='Independent floating diagnostics passed; not a replacement for the interval proof',cell_checks=total,minimum_extracted_mass_gap=min_gap,maximum_quad_error=max_quad_error,cases=cases,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/'data/far_circle_cell_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k!='cases'})
if __name__=='__main__':main()
