"""Independent no-cap version of the gated witness. Diagnostics only."""
import json
from pathlib import Path
import mpmath as mp
from check_gated_reduction import lower
mp.mp.dps=60
k=1/mp.sqrt(2)
Q=(mp.mpf("0.5")+1/mp.sqrt(2))/mp.pi

def tail_scaled(s):
    """J(1/s)/s with a removable value at zero."""
    if s==0:
        return Q
    ell=(1-s)/2
    d0=ell**2+(ell+k)**2
    # d1-d0 = s, after division by t^2.
    val=mp.log1p(s/d0)/4
    val+=(mp.atan(k/(1-s+k))-mp.atan((k-s)/(1+k)))/2
    val+=mp.log1p(s/k)/2
    return val/(mp.pi*s)

def unbounded_lower(a):
    rem=mp.quad(lambda s:s**(-a)*(tail_scaled(s)-Q),[0,1])
    return lower(a)+a*Q/(1-a)+a*rem

if __name__=='__main__':
    rows=[]
    for txt in ['.001','.01','.02','.05','.1','.2','.25','.3','.4','.5','.6','.7','.75','.8','.9','.95','.99']:
        a=mp.mpf(txt); val=unbounded_lower(a)
        row={'alpha':txt,'lower_diagnostic':mp.nstr(val,45),'additive_over_2_pi_alpha':mp.nstr(val-2/(mp.pi*a),45)}
        rows.append(row);print(row,flush=True)
    Path('data/unbounded_gate_diagnostic.json').write_text(json.dumps({'status':'diagnostic, not certificate','alpha1_coefficient':mp.nstr(Q,50),'values':rows},indent=2)+'\n')
