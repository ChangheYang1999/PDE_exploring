"""Certificate-level checks of noninteger zeros and an exactly zero sample."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
from gmpy2 import mpq
from flint import ctx
from pure_cartesian_ball import ball
from discrete_response_cover import cover
import json,time
ROOT=Path('research/232_discrete_response_cover')
class Example:
    h=2
    def __init__(self,zero):self.zero=F(zero)
    def compact(self,t):return t-ball(mpq(str(self.zero)))
def value_interval(data):
    m,e,r,re=data;middle=F(m)*F(2)**e;radius=F(r)*F(2)**re
    return middle-radius,middle+radius

def check():
    start=time.monotonic();old=ctx.prec;ctx.prec=256;receipts=[]
    for target in [F(1,100),F(1,2)]:
        result=cover(Example(F(1,8)),1,target);s=F(result['s']);assert 0<s<F(1,40)
        parts=[];statuses=set()
        for row in result['nodes']:
            a,b=F(row['a']),F(row['b']);address=row['address'];v=int(address,2) if address else 0
            assert (a,b)==(F(v,2**(len(address)+1)),F(v+1,2**(len(address)+1)))
            first=(1/b+2)/4;lo=max(1,-(-first.numerator//first.denominator));hi=None
            if a:
                last=(1/a+2)/4;hi=last.numerator//last.denominator
            assert (lo,hi)==(row['lower'],row['upper']);statuses.add(row['status'])
            if row['status']=='empty':assert hi is not None and hi<lo
            else:
                lower,upper=value_interval(row['enclosure']);assert lower>s or upper<-s
                if row['status']=='singleton':
                    assert lo==hi==row['k'];exact=F(1,4*lo-2)-F(1,8);assert lower<=exact<=upper
                else:
                    assert row['status']=='interval' and lower<=a-F(1,8) and b-F(1,8)<=upper
            parts.append((a,b))
        parts.sort();assert parts[0][0]==0 and parts[-1][1]==F(1,2) and all(a[1]==b[0] for a,b in zip(parts,parts[1:]))
        assert 'singleton' in statuses
        if target==F(1,2):assert result['adjustments']
        receipts.append(dict(initial_target=str(target),certificate=result,exact_infimum='1/40',all_leaf_checks_pass=True))
    rejected=False;reason=None
    try:cover(Example(F(1,6)),1,F(1,100))
    except AssertionError as exc:
        assert exc.args and isinstance(exc.args[0],tuple) and exc.args[0][0]=='unresolved_integer' and exc.args[0][1]==2
        rejected=True;reason=list(exc.args[0])
    assert rejected;ctx.prec=old
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,examples=receipts,exact_zero_rejected=rejected,rejection=reason,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    for name in ['discrete_cover_checks.py','discrete_response_cover.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in out.items() if k!='examples'}),flush=True)
    return out
if __name__=='__main__':check()
