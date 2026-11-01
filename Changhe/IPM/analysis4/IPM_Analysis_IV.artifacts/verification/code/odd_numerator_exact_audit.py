"""Independent exact Cartesian replay of the finite odd-numerator obstruction table."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
from math import isqrt
import json, re, sys, time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from rational_scan_audit import compute, first
ROOT=Path('research/195_odd_numerator_obstructions')

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
def valuation(q,p):
    assert q
    n,d=q.numerator,q.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v

def main():
    start=time.monotonic();source=Path('../a4-lead/code/oddnum/digits_sin1.out')
    raw=source.read_bytes();(ROOT/'sources/lead_digits_sin1.out').write_bytes(raw)
    expected={}
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'p=(\d+) a=(\d+) digits\(v=-4\.\.1\)=(\[.*\])',line)
        assert m,line
        p,a=map(int,m.group(1,2));expected[p,a]=json.loads(m.group(3))
    pairs=[(p,a) for p in range(5,24) if prime(p) for a in range(3,p,2)]
    assert len(pairs)==37 and set(pairs)==set(expected)
    rows=[]
    for p,a in pairs:
        delta=Fraction(a,p);n0,j0=first(delta);assert (n0,j0)==(2*p,a-1)
        result=compute(delta,{1:'1'},n0)
        result.pop('density_at_resonance')
        k=Fraction(result['kappa_exact']);forcing=Fraction(result['forcing_exact'])
        assert k and forcing==-2*(a-1)*k
        v=valuation(k,p);assert v in[-2,-1,0] and ((v==0)==((p,a)==(11,5)))
        cleared=k*p**4;modulus=p**6;assert cleared.denominator%p
        residue=(cleared.numerator*pow(cleared.denominator,-1,modulus))%modulus
        digits=[(residue//p**j)%p for j in range(6)]
        assert digits==expected[p,a],(p,a,digits,expected[p,a])
        result.update(p=p,a=a,p_adic_valuation=v,digits_minus4_through1=digits,reported_digits_match=True,checked_at_utc=stamp())
        name=f'p{p}_a{a}.json';(ROOT/'verification'/name).write_text(json.dumps(result,indent=2)+'\n')
        rows.append({key:value for key,value in result.items() if key not in ['kappa_exact','forcing_exact']})
        report=dict(checked_at_utc=stamp(),complete=len(rows)==len(pairs),expected_count=len(pairs),completed_count=len(rows),rows=rows,source=dict(path=str(source),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
        (ROOT/'verification/checks.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(p=p,a=a,valuation=v,digits_match=True,actual_elapsed_s=time.monotonic()-start)),flush=True)
    for name in ['odd_numerator_exact_audit.py','rational_scan_audit.py','laurent_log_audit.py']:
        (ROOT/'sources'/name).write_bytes((Path('code')/name).read_bytes())
    for name in ['kappa_odd.py','kappa_odd_digits.py']:
        (ROOT/'sources'/('lead_'+name)).write_bytes((Path('../a4-lead/code/oddnum')/name).read_bytes())
    print(json.dumps(dict(all_checks_pass=True,completed=len(rows),actual_elapsed_s=time.monotonic()-start)),flush=True)

if __name__=='__main__':main()
