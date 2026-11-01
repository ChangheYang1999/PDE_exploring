"""Exact finite checks of the two-index analytic Poisson estimates."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,time


def main():
    start=time.monotonic();count=0;worst={};skipped=0
    for delta in map(Q,['1/101','1/7','2/3','6/7','100/101']):
        cp=(1+1/delta)/2;lam=1+2*cp
        for n in range(1,36):
            nd=n*delta;nearest=2*round(nd/2);dn=abs(nd-nearest)
            if not dn:skipped+=1;continue
            for k in [0,1,2,5,10,30,100,1000,1000000]:
                w=n+k;mu=nd+2*k;p=2-mu
                center=int(abs(p))
                frequencies=set(range(1,32,2))|{a for a in range(max(1,center-5),center+6) if a%2}
                for a in frequencies:
                    channels=[(a+1,-1/(2*(a+1+p)))]
                    if a>=3:channels.append((a-1,1/(2*(a-1-p))))
                    norm=sum(abs(b) for m,b in channels)
                    deriv=sum(m*abs(b) for m,b in channels)
                    ratios={'stream':norm/(cp/dn),'angular_derivative':deriv/(lam*w/dn),'radial_factor':abs(p)*norm/(lam*w/dn)}
                    for name,ratio in ratios.items():
                        assert ratio<=1,(name,delta,n,k,a,ratio)
                        if name not in worst or ratio>worst[name][0]:worst[name]=(ratio,dict(delta=str(delta),n=n,k=k,input_frequency=a))
                    count+=1
    root=Path('research/62_analytic_multipoles');code=Path(__file__)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
        arithmetic='exact Fraction',coefficient_cases=count,resonant_density_indices_skipped=skipped,
        inequalities_per_case=3,all_inequalities_pass=True,
        worst_ratios={name:dict(ratio_exact=str(v[0]),**v[1]) for name,v in worst.items()},
        actual_elapsed_s=time.monotonic()-start,source_sha256=sha256(code.read_bytes()).hexdigest())
    (root/'verification'/'multiplier_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    (root/'sources'/'analytic_multipole_bounds.py.txt').write_bytes(code.read_bytes())
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
