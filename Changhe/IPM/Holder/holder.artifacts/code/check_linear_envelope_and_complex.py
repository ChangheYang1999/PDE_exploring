"""Small exact-constant checks, independent of the polar replay."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
ctx.prec=256

def record(v):
    assert v.is_finite()
    return dict(ball=v.str(45,more=True),lower=str(v.lower().fmpq()),upper=str(v.upper().fmpq()))

def main():
    pi=arb.pi(); ln2=arb(2).log();r=arb(1)/4;e=arb(1)/100
    E=-(1-r*r).log()/2;N=arb(1)/2-2*r.log()/pi
    L=arb.max(-(1-2*r).log(),(1+2*r)*(1+2*r).log())
    BC=r*r/(1-r)**2*(-r.log()+arb(3)/2-ln2/2)
    BD=3*r*r/(4*(1-r)**2)*(-r.log()+ln2+arb(2)/3)
    ellC=r.log()+ln2/2-arb(1)/2;ellD=r.log()+ln2-1
    Z=(N+E)*(arb(2)**e-1)/e+arb(2)**(e+1)/pi*(1/(1-e)+arb(1)/2-(arb(3)/2).log())
    KC=(ellC*ellC+arb(1)/4)/pi+Z+BC+E*L
    KD=(ellD*ellD+1-pi*pi/12)/pi+Z+BD+3*E*L
    assert KC<arb('2.85') and KD<arb(3)
    C0=arb(1)/2+(ln2-1)/pi
    upper0=1+ln2/2+(1+1/pi).log()
    lower0=1-ln2/2
    alpha=['1/1000','1/100','1/20','1/10','1/5','3/10','1/2','3/4','9/10','99/100']
    claims=['1001.6243','101.6358','21.6886','11.7588','6.9155','5.4345','4.6230','5.4987','9.4980','70.0268']
    rows=[]
    for text,claim in zip(alpha,claims):
        a=arb(text)
        # Qn are evaluated in logarithmic form, separate from the lead's script.
        logq2=ln2-((2-a).log())/2+(1-a)/2*((1-a).log()-(2-a).log())
        logq3=arb(6).log()-(3-a).log()+(1-a)/2*(arb(3).log()+(1-a).log()-arb(4).log()-(3-a).log())
        b1=((a-1)*ln2).exp();b2=((a-1)*ln2-logq2).exp();b3=((a-1)*ln2-logq3).exp()
        c=arb.min((b1+b3)/2,arb(2)**a/pi)
        s=((2*b3+(1-a)*c)/(2*b2))
        upper=2*b2*(a*s.log()).exp()/(a*(1-a))
        passed=upper<=arb(claim)
        rows.append(dict(alpha=text,upper=record(upper),claimed_upper=claim,claim_valid=bool(passed)))
    paths=['code/check_linear_envelope_and_complex.py','08_improved_upper_bounds/explicit_second_term/linear_envelope/PROOF.md',
           '16_beurling_complex_norm/upper_second_term/PROOF.md']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),rho='1/4',epsilon='1/100',KC=record(KC),KD=record(KD),
        C0=record(C0),complex_upper_second_term=record(upper0),complex_lower_second_term=record(lower0),rows=rows,
        source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    target=ROOT/'08_improved_upper_bounds/explicit_second_term/linear_envelope/verification/constants.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    (ROOT/'16_beurling_complex_norm/upper_second_term/verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
