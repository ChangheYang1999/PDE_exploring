"""Exact arithmetic for the rough-velocity inverse and conditional closure."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json
from flint import arb,ctx
ctx.prec=384
def A(q):
 q=Q(q); return arb(q.numerator)/q.denominator
s=Q(1,2**28); r=Q(1,2**27); b0=Q(20,21); eta=r/20
components={'c':2,'Du':6,'omega_D2u':24,'omega_D3u':160,'Drho':22,'omega_D2rho':32,'omega_D3rho':80,'omega_D4rho':2048}
M=sum(components.values()); assert M==2374 and M<4096
bg_table=Q(565)+Q(493,4)+6; assert bg_table<Q(1024)
safe_C=2**22; loss_bg=s*safe_C; sqrt_s=Q(1,2**14); loss_W=128*r/sqrt_s
rate=Q(1,10)-loss_bg-loss_W
assert loss_bg==loss_W==Q(1,64) and rate==Q(11,160) and rate>Q(1,20)
assert 20*eta==r
pi=arb.pi(); ratio_bound=5*arb(1).exp()
k1=pi.sqrt()*ratio_bound/2+4; k2=3*pi.sqrt()*ratio_bound/2+16
assert k1<17 and k2<54 and 1+4*pi<14
cs=1/(2*(pi*A(s)*(1+A(s))).sqrt()); assert cs* A(s).sqrt()<A(Q(3,10))
d=cs*A(r); KL=1/(A(Q(19,5))-d); contraction=KL*d
assert d<A(Q(1,2**13)) and KL<1 and contraction<A(Q(1,2**13))
rough_top=Q(4,5)*Q(3,10)+Q(3,10)*(1+142*Q(1,2))+Q(19,5)*(1+44*Q(1,2))
rough_total=rough_top+Q(13,10)+Q(3,10)+Q(1,2)
assert rough_top==Q(2731,25) and rough_total<Q(128)
delta=s/2; p=2**31; kappa=p+4; assert p*delta==4 and p*(1+delta)+2-kappa==2
src=json.loads((Path(__file__).resolve().parents[2]/'source_audit/state131_exact.json').read_text())
c=Q(src['exact_parameters']['cl']); lam=2*c-1; assert 3-lam>0
proof=Path(__file__).resolve().parents[1]/'PROOF.md'
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','precision_bits':ctx.prec,'component_sup_bounds':components,'Mstar_upper':M,'background_commutator_table_sum':str(bg_table),'C_bg_safe':safe_C,'s':str(s),'r':str(r),'eta':str(eta),'eta_decimal':A(eta).str(55),'rate_lower':str(rate),'inverse_upper':20,'kernel_moment_bounds':[k1.str(55),k2.str(55)],'rough_energy_constant_before_rounding':str(rough_total),'embedding_cs':cs.str(55),'velocity_gradient_upper':d.str(55),'low_inverse_upper':KL.str(55),'low_contraction_upper':contraction.str(55),'moment':{'delta':str(delta),'p':p,'kappa':kappa,'integrability_gap':2,'transport_gap':A(3-lam).str(55)},'scope':'Arithmetic and listed analytic constants only. Actual residual smallness is not asserted.'}
(Path(__file__).resolve().parent/'constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
