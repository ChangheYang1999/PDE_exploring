"""Specialize the exact Cartesian arithmetic to QQ[b] at fixed integer indices."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import tuned_cartesian_exact as ce
import four_ninths_response_minima as audit
ROOT=Path('research/164_four_ninths_response_minima')


def main():
    start=time.monotonic()
    oldpath=ROOT/'verification/small_responses.json'
    oldraw=oldpath.read_bytes();old=json.loads(oldraw)
    oldvalues={int(row['k']):[F(x) for x in row['coefficients']] for row in old['rows']}
    (ROOT/'verification/small_responses_before_domain_change.json').write_bytes(oldraw)
    ce.K=QQ;ce.k=0;ce.R,ce.b=ring('b',QQ)
    ce.MOD=None
    ce.p=lambda n:QQ(1)-QQ(4)*n/9
    import ast
    def load(data):
        q=QQ.from_sympy(sp.sympify(data['radial_exponent']))
        terms={ast.literal_eval(m):ce.R.from_expr(sp.sympify(v)) for m,v in data['signed_laurent'].items()}
        assert all(a==0 for a,m in terms)
        return ce.F(q,terms)
    data=json.loads(Path('research/144_general_rational_response_limit/verification/h2_Q9.json').read_text())
    ff={int(n):load(v) for n,v in data['low_density'].items()}
    gg={int(n):load(v) for n,v in data['low_stream'].items()}
    rows=[]
    for k in range(1,10):
        begin=time.monotonic();value=audit.small_response(k,ff,gg)
        assert len(value)<=10
        matched=k in oldvalues
        if matched:assert value==oldvalues[k],('domain comparison',k)
        row=dict(k=k,coefficients=list(map(str,value)),matches_previous_exact_domain=matched,actual_elapsed_s=time.monotonic()-begin)
        rows.append(row)
        (ROOT/'verification/fast_small_responses.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n')
        print(json.dumps({key:row[key] for key in ['k','matches_previous_exact_domain','actual_elapsed_s']}),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,previous_sha256=sha256(oldraw).hexdigest(),previous_exact_indices=sorted(oldvalues),actual_elapsed_s=time.monotonic()-start,
        scope='Fixed integer response indices use QQ[b], with the same exact Cartesian operations. No approximation or interpolation is introduced.')
    (ROOT/'verification/fast_domain_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    oldpath.write_text(json.dumps(dict(rows=[dict(k=row['k'],coefficients=row['coefficients']) for row in rows]),indent=2)+'\n')
    (ROOT/'sources/four_ninths_exact_polynomial_fast.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

if __name__=='__main__':main()
