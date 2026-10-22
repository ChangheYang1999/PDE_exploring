"""Exact local rejection of ordinary two-shift stream states; packet118.

The production certificate uses closed rational center formulas. Its controls
use independent truncated polynomial arithmetic and differentiate the PDE.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json


def parse(data):
    beta = Q(data['beta'])
    if beta <= 2:
        raise ValueError('packet118 requires rational beta>2')
    ls = data['labels']
    if not isinstance(ls, list) or len(ls) != len(data['C']) or len(ls) != len(data['D']):
        raise ValueError('coefficient/label lengths differ')
    labels = []
    for label in ls:
        if len(label) != 3 or any(type(v) is not int for v in label):
            raise ValueError('labels must be integer triples')
        i, j, d = label
        if i < 0 or j < 0 or d not in (0, 1):
            raise ValueError('invalid basis index')
        labels.append((i, j, d))
    if len(set(labels)) != len(labels):
        raise ValueError('duplicate label')
    return beta, labels, list(map(Q, data['C'])), list(map(Q, data['D']))


def checks(data):
    beta, labels, C, D = parse(data)
    s = 1/beta
    a0 = a1 = c0 = c1 = b0 = b1 = Q(0)
    for (i, j, d), c, q in zip(labels, C, D):
        v = 0 if j % 2 else (-1)**(j//2)
        w = 0 if not j % 2 else j*(-1)**((j-1)//2)
        k = 1-s-d
        a0 += q*v
        a1 += q*w
        c0 += c*w
        c1 += c*(k-2*i*i*s-j*j)*v
        b0 -= c*(4*(k-2*i*i*s)-j*j)*v
        b1 += c*(-6*k+5+12*i*i*s+j*j)*w
    fs = {'f0': (beta-2*c0+2)*a0,
          'f1': (2*beta-c0+2)*a1-2*a0*c1,
          'g0': (beta-c0+1)*b0-2*a0,
          'g1': (2*beta+1)*b1-c1*b0-2*a1}
    moments = dict(a0=a0, a1=a1, c0=c0, c1=c1, b0=b0, b1=b1)
    monomials = {'f0': [2, 0], 'f1': [2, 1], 'g0': [1, 0], 'g1': [1, 1]}
    return {'beta': str(beta), 'moments': {k: str(v) for k, v in moments.items()},
            'residual_coefficients': {k: str(v) for k, v in fs.items()},
            'monomials': monomials, 'nonzero': {k: bool(v) for k, v in fs.items()},
            'center_strain_exact': c0 == 1+beta/2,
            'center_vorticity_exact': b0 == 4*a0/beta,
            'nontrivial_local_temperature': bool(a0),
            'verdict': 'REFUTED_AS_EXACT_FIELD' if any(fs.values()) else 'OPEN',
            'scope': 'Exact Taylor coefficient of this serialized field only; '
                     'no lower bound for nearby profiles and no global exclusion.'}


def make(path, out):
    cert = checks(json.loads(path.read_text()))
    cert.update(source_path=str(path.resolve()),
                source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                created_utc=datetime.now(timezone.utc).isoformat())
    out.write_text(json.dumps(cert, indent=2)+'\n')
    return cert


def verify(path, certificate):
    cert = json.loads(certificate.read_text())
    if cert['source_sha256'] != hashlib.sha256(path.read_bytes()).hexdigest():
        raise ValueError('input digest mismatch')
    for k, v in checks(json.loads(path.read_text())).items():
        if cert.get(k) != v:
            raise ValueError('certificate mismatch: '+k)
    return True


def archive(root):
    dest = root/'local_jet_certificates'
    dest.mkdir(exist_ok=True)
    rows = []
    for path in sorted(root.glob('*_state.json')):
        out = dest/(path.stem+'_certificate.json')
        cert = make(path, out)
        assert verify(path, out)
        rows.append({'state': path.name, 'source_sha256': cert['source_sha256'],
                     'beta': float(Q(cert['beta'])),
                     'residual_coefficients_float': {
                         k: float(Q(v)) for k, v in cert['residual_coefficients'].items()},
                     'nonzero': cert['nonzero'], 'verdict': cert['verdict'],
                     'certificate': str(out.relative_to(root))})
    (dest/'summary.json').write_text(json.dumps(rows, indent=2)+'\n')
    return rows


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['create', 'check', 'archive'])
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path, nargs='?')
    args = ap.parse_args()
    if args.mode == 'archive':
        rows = archive(args.input)
        print(json.dumps({'states': len(rows), 'rejected': sum(
            r['verdict'] == 'REFUTED_AS_EXACT_FIELD' for r in rows), 'rows': rows}, indent=2))
    elif args.mode == 'create':
        make(args.input, args.output)
    else:
        verify(args.input, args.output)
        print('CONFIRMED exact local coefficient certificate')
