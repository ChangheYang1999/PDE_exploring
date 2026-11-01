"""Replay selected conditional evidence, exact index partitions and printed tables."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as Q
import gzip, json, pickle, sys, time, math
sys.dont_write_bytecode = True
from flint import arb, ctx
from stream_precision_audit import unpack
from unpack_dyadic4 import unpack as unpack4
BASE = Path('research/189_reset350_conditional_audit')
def main():
    start = time.monotonic(); ctx.prec = 1024; z = arb(0); logten = arb(10).log()
    m = json.loads((BASE/'verification/input_manifest.json').read_text())
    blob = (BASE/'verification/selected.pkl.gz').read_bytes()
    assert sha256(blob).hexdigest() == m['archive_sha256']
    raw = gzip.decompress(blob)
    assert len(raw) == m['selected_raw_bytes'] and sha256(raw).hexdigest() == m['selected_raw_sha256']
    state = pickle.loads(raw); del raw, blob
    checks = json.loads((BASE/'verification/checks.json').read_text())
    assert checks['all_checks_pass'] and state['source_sha256'] == checks['source_sha256'] == m['source_sha256']
    rows = {r['n']: r for r in checks['rows']}; selected = {}; norms = factorial = poisson = 0
    for n in [348,349,350]:
        arrays = {}
        for field in ['f','g']:
            arrays[field] = [[arb(*unpack(x)) for x in col] for col in state[field][n]]
            colnorm = [sum((abs(x) for x in col), z) for col in arrays[field]]
            total = sum(colnorm,z)
            assert total.overlaps(arb(*unpack4(rows[n]['fields'][field]['norm'])))
            assert (total.log()/logten).overlaps(arb(rows[n]['fields'][field]['log10_norm'])); norms += 1
            k = rows[n]['fields'][field]['factorial_maximizer']; peak = math.factorial(k)*colnorm[k]
            for j,a in enumerate(colnorm):
                if j != k: assert peak > math.factorial(j)*a; factorial += 1
        selected[n] = arrays
        # Rebuild the full polynomial residual by accumulating differential
        # operators, rather than testing the producer's pointwise formula.
        F,G = arrays['f'],arrays['g']; p = arb(2)-arb(2*n)/3
        nq = max(len(F),len(G)); nj = max(max(map(len,F)),max(map(len,G)))+1
        residual = [[z for j in range(nj)] for q in range(nq)]
        for q,col in enumerate(G):
            assert col[0].is_zero()
            for j,a in enumerate(col):
                residual[q][j] += (4*j*j-p*p)*a
                if q: residual[q-1][j] -= 2*p*q*a
                if q>=2: residual[q-2][j] -= q*(q-1)*a
        for q,col in enumerate(F):
            for j,a in enumerate(col):
                residual[q][j+1] -= (p-2*(j+1))*a/2
                if q: residual[q-1][j+1] -= q*a/2
                if j:
                    residual[q][j] -= (p+2*j)*a/2
                    if q: residual[q-1][j] -= q*a/2
        for col in residual:
            for v in col[1:]: assert v.contains(0); poisson += 1
    assert poisson == checks['poisson_coefficients']
    evaluations = {r['t']:r for r in checks['t_evaluations']}; table = {}
    for line in (BASE/'sources/tprofile_350.txt').read_text().splitlines()[1:]:
        words = line.split(); table[int(float(words[1]))] = words
    comparisons = 0
    for t,record in evaluations.items():
        for field in ['f','g']:
            cols = selected[350][field]; power = [arb(t)**q for q in range(len(cols))]
            values = [sum((col[j]*power[q] for q,col in enumerate(cols) if j<len(col)),z) for j in range(max(map(len,cols)))]
            norm = sum(map(abs,values),z)
            assert norm.overlaps(arb(*unpack4(record['fields'][field]['norm'])))
            lognorm = norm.log()/logten
            index = 2 if field=='f' else 6
            assert lognorm.overlaps(arb(table[t][index], '0.00005')); comparisons += 1
            absolute = sum((sum(map(abs,col),z)*abs(power[q]) for q,col in enumerate(cols)),z)
            cancel = (absolute/norm).log()/logten
            assert cancel.overlaps(arb(record['fields'][field]['cancellation_decades']))
            if field=='f':
                assert cancel.overlaps(arb(table[t][5],'0.005')); comparisons += 1
                col0 = sum(map(abs,cols[0]),z)
                assert (col0.log()/logten).overlaps(arb(table[t][4],'0.00005')); comparisons += 1
    bands = {r['q']:r for r in checks['bands350']}; bandvalues = 0
    lines = (BASE/'sources/bands_350.txt').read_text().splitlines()[2:]
    for line in lines:
        words = line.split('|'); q = int(words[0]); printed = [words[1].split(),words[2].split()[:3]]
        for field,offset,pnumbers in zip(['f','g'],[3,2],printed):
            # Physical frequency compared with n*delta-offset. F frequencies
            # are 2j+1 and G frequencies 2j.
            center = Q(700,3)-offset; col = selected[350][field][q]; parts = [z,z,z]
            for j,x in enumerate(col):
                frequency = 2*j+(field=='f'); distance = abs(Q(frequency)-center)
                threshold = Q(2) if q==0 else Q(q,4)
                bucket = 0 if distance<=threshold else (1 if q and distance<=q else 2)
                parts[bucket] += abs(x)
            total = sum(parts,z)
            for k,v in enumerate(parts):
                share = v/total
                assert share.overlaps(arb(bands[q]['fields'][field][k]))
                assert share.overlaps(arb(pnumbers[k],'0.0005')); bandvalues += 1
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
                  bits=1024,selected_orders=[348,349,350],norm_replays=norms,factorial_comparisons=factorial,
                  poisson_replays=poisson,printed_t_comparisons=comparisons,band_values=bandvalues,
                  archive_sha256=m['archive_sha256'],scope='Conditional finite arithmetic only; inherited input uncertainty remains OPEN.',
                  actual_elapsed_s=time.monotonic()-start)
    (BASE/'verification/replay.json').write_text(json.dumps(result,indent=2)+'\n')
    (BASE/'sources/replay_reset350_conditional.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(result),flush=True)
if __name__=='__main__': main()
