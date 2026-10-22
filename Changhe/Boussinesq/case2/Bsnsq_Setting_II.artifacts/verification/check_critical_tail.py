"""Separate standard-library decoder and exact certificate checker.

Chebyshev coefficients use the closed factorial formula, independently of
recurrence-based generation. No certificate-generation code is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, isqrt
from datetime import datetime, timezone
import argparse, ast, hashlib, json, struct, time, zipfile

def load_array(archive, name):
    raw = archive.read(name + '.npy')
    assert raw[:6] == b'\x93NUMPY'
    n = 2 if raw[6] == 1 else 4
    length = int.from_bytes(raw[8:8+n], 'little')
    header = ast.literal_eval(raw[8+n:8+n+length].decode('latin1'))
    assert not header['fortran_order']
    body = raw[8+n+length:]
    kind = header['descr']
    if kind in ('<f8', '=f8'):
        values = [Q.from_float(v[0]) for v in struct.iter_unpack('<d', body)]
    elif kind.startswith('<U'):
        values = [body.decode('utf-32-le').rstrip('\x00')]
    else:
        raise ValueError(kind)
    return header['shape'], values

def polynomial(shape, values):
    mcount, ncount = shape
    coefficients = [Q(0)] * mcount
    for m in range(mcount):
        endpoint = sum((values[m*ncount+n] * (1 if n % 2 == 0 else -1)
                        for n in range(ncount)), Q(0))
        if m == 0:
            coefficients[0] += endpoint
            continue
        for k in range(m//2+1):
            j = m-2*k
            factor = Q(m * (-1)**k * factorial(m-k-1) * 2**j,
                       2 * factorial(k) * factorial(j))
            coefficients[j] += endpoint * factor
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients

def decode(rows):
    return [Q(int(row['n']), int(row['d'])) for row in rows]

def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n)+1))

def main():
    start=time.monotonic()
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',default='runs/critical_tail_certificate.json')
    parser.add_argument('--output',default='runs/critical_tail_independent_check.json')
    args=parser.parse_args()
    cert_path=Path(args.certificate)
    output_path=Path(args.output)
    assert output_path.resolve().is_relative_to(Path(__file__).resolve().parent.parent)
    cert=json.loads(cert_path.read_text())
    source=Path(cert['source'])
    assert hashlib.sha256(source.read_bytes()).hexdigest()==cert['source_sha256']
    with zipfile.ZipFile(source) as archive:
        Ash, Av=load_array(archive, 'ca')
        Csh, Cv=load_array(archive, 'cG')
        expected={'beta':Q(2),'L':Q(1),'beta_map':Q(2),
                  'sigma_a':Q(3,2),'sigma_G':Q(5,4),'mapname':'t'}
        for key,value in expected.items():
            shape,values=load_array(archive,key)
            assert shape==() and values==[value], (key,shape,values)
    A=polynomial(Ash,Av);C=polynomial(Csh,Cv)
    get=lambda j: A[j] if 0 <= j < len(A) else Q(0)
    F=[(2*j+1)*get(j-1)-get(j)-2*(j+1)*get(j+1) for j in range(len(A)+1)]
    assert A==decode(cert['A_power_coefficients'])
    assert C==decode(cert['C_power_coefficients'])
    assert F==decode(cert['F_power_coefficients'])
    assert A[-1] and C[-1] and F[-1]
    checks=[]
    for row in cert['modular_certificates']:
        p=row['prime'];assert is_prime(p)
        reduced=[]
        for poly,label in [(F,'F'),(C,'C')]:
            assert all(x.denominator % p for x in poly)
            rr=[x.numerator*pow(x.denominator,-1,p)%p for x in poly]
            assert rr==row[label] and rr[-1]!=0
            reduced.append(rr)
        length=max(len(row['bezout_F'])+len(F),len(row['bezout_C'])+len(C))-1
        product=[0]*length
        for bez,poly in [(row['bezout_F'],reduced[0]),(row['bezout_C'],reduced[1])]:
            for i,a in enumerate(bez):
                for j,b in enumerate(poly):
                    product[i+j]=(product[i+j]+a*b)%p
        assert product[0]==1 and all(x==0 for x in product[1:])
        checks.append({'prime':p,'prime_proved_by_trial_division':True,
                       'leading_degrees_preserved':True,'bezout_identity_exact':True})
    result={'timestamp':datetime.now(timezone.utc).isoformat(),
            'elapsed_seconds':time.monotonic()-start,
            'source_sha256':cert['source_sha256'],
            'certificate_sha256':hashlib.sha256(cert_path.read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'method':'Standard-library NPZ decoding, factorial Chebyshev formula, coefficientwise derivative identity, trial-division primality, direct modular Bezout convolution',
            'exact_rational_coefficients_match':True,'degrees':[len(A)-1,len(C)-1,len(F)-1],
            'checks':checks,'verdict':'PASS',
            'scope':'Exact literal-state incompatibility only; no nearby-state exclusion or numerical error threshold.'}
    output_path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':
    main()
