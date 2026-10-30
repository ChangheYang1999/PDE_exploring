"""Dense independent quadrature diagnostic, compared with the validated Beta result."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,math
import numpy as np
from scipy.special import roots_legendre
from flint import ctx,arb
from radial import Radial,ar,q
ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    ctx.prec=256;start=time.monotonic()
    model=Radial(ROOT/'research/baseline/data/state131_independent.json');C=model.residual_quotient()
    degree=max(n for h,n in C);harmonics=list(range(0,degree+1,2))
    ref=json.loads((ROOT/'research/radial_fourier/data/objective_reference.json').read_text())
    aref=float(q(ref['a_ref_exact']));results=[]
    for order in (16,32):
        nodes,weights=roots_legendre(order);total=0.;max_integrand=(0.,0.)
        for left in range(-12,40):
            for node,weight in zip(nodes,weights):
                s=left+(node+1)/2;r2=arb(repr(math.exp(2*s)));u=1/(1+r2);t=r2/(1+r2)
                up={h:u**ar((h+1)*model.delta/2) for h in range(8)}
                coeff={n:arb(0) for n in harmonics}
                for (h,n),P in C.items():coeff[n]+=up[h]*model.poly_arb(P,t,u)
                # Evaluate 257 angular nodes; no original evaluator or quadrature rule is imported.
                theta=np.linspace(0.,math.pi/2,257)
                values=sum(float(coeff[n])*np.cos(n*theta) for n in harmonics)
                integral=float(np.trapezoid(values*values,theta))/(math.pi*aref*aref)
                total+=weight*integral/2
                if integral>max_integrand[1]:max_integrand=(s,integral)
        rec={'log_r_interval':[-12,40],'log_r_panels':52,'gauss_order_per_panel':order,
             'angular_trapezoid_intervals':256,'product_nodes':52*order*257,
             'J_abs_finite_interval_float':total,'maximum_sampled_log_r_integrand':max_integrand,
             'elapsed_seconds':time.monotonic()-start}
        results.append(rec);print(rec,flush=True)
    exact=arb(json.loads((ROOT/'research/radial_fourier/verification/state131_J_768.json').read_text())['J_abs'])
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'label':'FLOAT',
         'scope':'Dense finite-log-radius quadrature; no tail or quadrature error certificate is asserted by this script.',
         'field_precision_bits':ctx.prec,'exact_objective_for_comparison':exact.str(30),'rules':results,
         'relative_error_last':abs(results[-1]['J_abs_finite_interval_float']/float(exact)-1)}
    (ROOT/'research/radial_fourier/verification/quadrature.json').write_text(json.dumps(out,indent=2)+'\n')
