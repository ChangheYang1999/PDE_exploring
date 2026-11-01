"""Exact size bound for the extracted profile at the new irrational parameter."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from fractions import Fraction
import json


def main():
    source=Path('research/02_candidate007/data/leading_exact.json')
    data=json.loads(source.read_text())
    terms={int(m):Fraction(a) for m,a in data['density'].items()}
    T=sum((abs(a)*(2**((m-1)//2)) for m,a in terms.items()),Fraction())
    assert T<31
    assert 256*31<2**13
    assert 2**15*7*31<2**23
    assert Fraction(54)*Fraction(4,9)==24
    output={
        'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'input':source.as_posix(),'input_sha256':sha256(source.read_bytes()).hexdigest(),
        'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'The extracted density polynomial is reused at delta=1/sqrt(5), not at the stored rational parameter.',
        'sigma':'log(2)/2','weighted_norm':'sqrt(2)*T','T_exact':str(T),'T_lt_31':True,
        'M_lt':'2^13','A_lt':'2^23','R':'2^54',
        'weighted_density_tail_after_N':'2^14 * 2^(-N)',
        'conditional_on':'The all-order theorem in research/07_diophantine_convergence/PROOF.md',
    }
    target=Path('research/07_diophantine_convergence/verification/reference_constants.json')
    target.write_text(json.dumps(output,indent=2)+'\n')
    print('Exact extracted-profile norm factor T =',float(T),' < 31')


if __name__=='__main__':
    main()
