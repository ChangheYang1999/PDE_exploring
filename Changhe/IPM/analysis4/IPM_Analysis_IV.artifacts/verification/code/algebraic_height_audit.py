"""Exact Q(sqrt(2)) norm tests for the algebraic height extension."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from datetime import datetime,timezone
import json,time,sys
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from quantitative_divergence_audit import denominator_bound


def main():
    start=time.monotonic();source=Path('research/42_real_profile_prime_obstruction/verification/polynomial_checks.json');raw=source.read_bytes();data=json.loads(raw);rows=[]
    for row in data['results']:
        coeff=[Fraction(v) for v in row['kappa_coefficients']]
        A=sum((v*2**(k//2) for k,v in enumerate(coeff) if k%2==0),Fraction(0))
        Bcoef=sum((v*2**(k//2) for k,v in enumerate(coeff) if k%2),Fraction(0))
        # fixed_first: sin + sqrt(2) sin3 + 2 sin5; variable_first: sqrt(2) sin + sin3.
        bandwidth=6 if row['family']=='fixed_first' else 4
        p,a=row['prime'],row['a'];D,_,_=denominator_bound(p,a,bandwidth,1)
        assert D%A.denominator==0 and D%Bcoef.denominator==0
        intA=A*D;intB=Bcoef*D
        assert intA.denominator==intB.denominator==1
        norm=intA*intA-2*intB*intB
        assert norm.denominator==1 and norm
        # All sampled centers lie in [1/20,19/20]; all conjugate leading l1 norms < 5.
        assert Fraction(1,20)<=Fraction(a,p)<=Fraction(19,20)
        C=448*bandwidth*20*5
        assert abs(A)+2*abs(Bcoef)<=(C*p)**p
        rows.append(dict(prime=p,a=a,family=row['family'],field='Q(sqrt(2))',field_degree=2,
                         kappa_rational_part=str(A),kappa_sqrt2_part=str(Bcoef),
                         common_D_clears_coordinates=True,nonzero_integer_norm=True,
                         integer_norm_bit_length=abs(norm.numerator).bit_length(),
                         conjugate_upper_bound_C=C,conjugate_bound_verified=True))
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),source=str(source),source_sha256=sha256(raw).hexdigest(),
             cases=rows,actual_elapsed_s=time.monotonic()-start,
             scope='Finite exact algebraic norm checks, not a replacement for the general proof.')
    Path('research/49_algebraic_quantitative_divergence/verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'cases':len(rows),'elapsed_s':out['actual_elapsed_s']}),flush=True)

if __name__=='__main__':main()
