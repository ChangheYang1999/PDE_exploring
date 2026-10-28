"""Replay a stored integer-flow local certificate and rebalance its residual.

No optimizer is called. Angular masses, every integer marginal and each used
transport cost are recomputed. The result is a local component, not an operator
bound. See local_disk_transport/balanced_residual/PROOF.md.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import argparse, hashlib, json, time
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / '08_improved_upper_bounds/local_disk_transport/balanced_residual/PROOF.md'
UNIT = 2 ** 44


def upper(x):
    assert x.is_finite()
    return arb(x.upper())


def record(x):
    assert x.is_finite()
    return dict(lower=str(x.lower().fmpq()), upper=str(x.upper().fmpq()),
                display=x.str(42, more=True))


def angular_enclosures(a, b, phase, n, pi):
    """Enclose each angular integral uniformly over the entire radial bin."""
    width = 2*pi/n
    starts = [phase/2+pi/4+width*j for j in range(n+1)]
    rot = acb(phase.cos(), phase.sin())
    radial = a.union(b)
    arcs, signs, lower_mass = [], [], []
    total_variation = arb(0)
    # Integral midpoint remainder: second theta derivative bound /24 * width^3.
    second = b**3*(1+2*b)/(pi*(1-b)**4)
    error = arb(0, upper(second*width**3/24))
    for j in range(n):
        theta = starts[j].union(starts[j+1])
        arc = acb(theta.cos(), theta.sin())
        midpoint = starts[j]+width/2
        mid = acb(midpoint.cos(), midpoint.sin())
        density = ((2*theta-phase).cos()
                   - (radial**2*rot/(1+radial*arc)**2).real)/(2*pi)
        own = ((2*starts[j+1]-phase).sin()
               - (2*starts[j]-phase).sin())/(4*pi)
        angular = own-width*(radial**2*rot/(1+radial*mid)**2).real/(2*pi)+error
        # The algebraically identical factorization has a different Arb
        # radius rounding. Intersect both valid bounds before checking
        # extraction quanta that can lie extremely near an endpoint.
        cross = (radial*radial*rot/(1+radial*mid)**2).real/(2*pi)
        angular2 = own-cross*width+error
        sign = 1 if density > 0 else (-1 if density < 0 else 0)
        if sign:
            positive, positive2 = sign*angular, sign*angular2
            lower_mass.append(arb.max(arb(0), arb.max(arb(positive.lower()), arb(positive2.lower()))))
            total_variation += arb.min(upper(positive), upper(positive2))
        else:
            lower_mass.append(arb(0))
            total_variation += width*upper(abs(density))
        signs.append(sign)
        arcs.append(arc)
    return signs, lower_mass, total_variation, arcs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    source, out = Path(args.input).resolve(), Path(args.out).resolve()
    assert out.is_relative_to(ROOT)
    raw = source.read_bytes()
    data = json.loads(raw)
    cfg = data['args']
    ctx.prec = 160
    alpha, delta = arb(cfg['alpha']), arb(cfg['delta'])
    n, nr, m = cfg['angles'], cfg['radial'], cfg['phases']
    jphase = data['phase_index']
    assert n >= 16 and n % 8 == 0 and nr > 0 and 0 <= jphase <= 2*m
    assert 0 < alpha < 1 and 0 < delta < arb(1)/2
    assert data['integer_unit'] == UNIT
    half = n*nr
    masses = data['masses']
    assert len(masses) == 2*half+2
    assert all(type(x) is int for x in masses)
    assert masses[half:2*half] == [-x for x in masses[:half]]
    assert masses[-2:] == [-UNIT//2, UNIT//2]
    flow_balance = [0]*len(masses)
    seen = set()
    for i, j, flow in data['plan']:
        assert all(type(v) is int for v in (i,j,flow)) and flow > 0
        assert 0 <= i < len(masses) and 0 <= j < len(masses)
        assert masses[i] > 0 and masses[j] < 0 and (i,j) not in seen
        seen.add((i,j)); flow_balance[i] += flow; flow_balance[j] -= flow
    assert flow_balance == masses
    pi = arb.pi(); phase = pi*jphase/(2*m)
    row_data, row_records = [], []
    old_residual, new_residual = arb(0), arb(0)
    started = time.monotonic()
    for row in range(nr):
        a = (delta.sqrt()+((arb(1)/2).sqrt()-delta.sqrt())*row/nr)**2
        b = (delta.sqrt()+((arb(1)/2).sqrt()-delta.sqrt())*(row+1)/nr)**2
        logr = (b/a).log()
        radial_average = (b**alpha-a**alpha)/(alpha*logr)
        signs, lower_mass, tv, arcs = angular_enclosures(a,b,phase,n,pi)
        current = masses[row*n:(row+1)*n]
        for k, mass in enumerate(current):
            if mass:
                assert signs[k] == (1 if mass > 0 else -1), (row,k,'sign')
                # Compare the stored exact extraction with an independent
                # enclosure of the true uniform angular mass times dr/r.
                assert arb(abs(mass))/UNIT <= lower_mass[k]*logr, (row,k,'mass')
        extracted = arb(sum(abs(x) for x in current))/UNIT
        signed_extracted = arb(sum(current))/UNIT
        Vhat = upper(tv*logr-extracted)
        assert Vhat >= 0
        signed_residual = -phase.cos()*(b*b-a*a)/2-signed_extracted
        Qhat = arb.min(Vhat, upper(abs(signed_residual)))
        diameter = (2*b)**alpha
        reflection = (1+2*b)**alpha
        old = Vhat*reflection
        new = Vhat*diameter+Qhat*(reflection-diameter)
        assert new >= 0 and (new <= old or (old-new).contains(0)), row
        old_residual += old; new_residual += new
        row_data.append((a,b,radial_average,arcs))
        row_records.append(dict(row=row,r0=record(a),r1=record(b),
                                signed_extraction=str(Fraction(sum(current),UNIT)),
                                residual_variation=record(Vhat),
                                residual_mass=record(signed_residual),
                                old_cost=record(old),new_cost=record(new)))
    chord = [(2*(pi*min(k+1,n//2)/n).sin())**alpha for k in range(n//2+1)]
    cost = arb(0); categories = {}
    for i,j,flow in data['plan']:
        ia,ja = i >= 2*half,j >= 2*half
        if ia and ja:
            edge,tag = arb(1),'atom_atom'
        elif not ia and not ja:
            ri,rj = (i % half)//n,(j % half)//n
            if ri != rj:
                edge,tag = arb(2)**alpha,'cross_row_repair'
            else:
                a,b,average,arcs = row_data[ri]
                ai,aj = i % n,j % n
                if i//half == j//half:
                    dist = min(abs(ai-aj),n-abs(ai-aj))
                    edge,tag = chord[dist]*average,'same_pole'
                else:
                    arc = arcs[ai]+arcs[aj]
                    edge = arb.max(upper(abs(1+a*arc)),upper(abs(1+b*arc)))**alpha
                    tag = 'opposite_pole'
        else:
            node,atom = (j,i) if ia else (i,j)
            a,b,average,arcs = row_data[(node % half)//n]
            if node//half == atom-2*half:
                edge,tag = average,'own_atom'
            else:
                arc = arcs[node % n]
                edge = arb.max(upper(abs(1+a*arc)),upper(abs(1+b*arc)))**alpha
                tag = 'other_atom'
        assert edge >= 0 and edge.is_finite()
        piece = arb(flow)/UNIT*edge
        cost += piece; categories[tag] = categories.get(tag,arb(0))+piece
    a2 = 2**(1+alpha/2)/(pi*(alpha+2))
    small = 2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(),
                  status='Local component only. Analytic cross-read pending.',
                  input_path=str(source),input_sha256=hashlib.sha256(raw).hexdigest(),
                  proof_sha256=hashlib.sha256(PROOF.read_bytes()).hexdigest(),
                  auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  precision_bits=ctx.prec,configuration=cfg,phase_index=jphase,
                  exact_marginals=True,extractions_checked=True,
                  transport=record(cost),old_residual=record(old_residual),
                  new_residual=record(new_residual),small_disk=record(small),
                  old_local_plus_small=record(cost+old_residual+small),
                  new_local_plus_small=record(cost+new_residual+small),
                  improvement=record(old_residual-new_residual),rows=row_records,
                  categories={k:record(v) for k,v in categories.items()},
                  elapsed_seconds=time.monotonic()-started)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('time_utc','transport','old_residual','new_residual',
                                          'new_local_plus_small','improvement','elapsed_seconds')},indent=2))

if __name__ == '__main__':
    main()
