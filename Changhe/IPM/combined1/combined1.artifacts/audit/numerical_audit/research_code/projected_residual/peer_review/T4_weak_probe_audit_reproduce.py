"""Independent weak-background pairing and polar vector norm integrals."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import argparse, hashlib, json, sys, time
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[1]
T = P([0, 1]); U = P([1, -1]); ZERO = P([])

def rat(x):
    v = Fraction(str(x))
    return Q(v.numerator, v.denominator)

def ar(x):
    return arb(x.numerator) / x.denominator

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(rows, j, n, value):
    if not value or n == 0:
        return
    if n < 0:
        n, value = -n, -value
    rows[j, n] = rows.get((j, n), ZERO) + value
    if not rows[j, n]:
        del rows[j, n]

def rad(value, p):
    return 2*p*T*value + 2*T*U*value.derivative()

def td(value, a, k):
    return (k-2*a*T)*value + 2*T*U*value.derivative()

def divide(value):
    assert value[0] == 0 and value[1] == 0
    return P(list(value)[2:])

def fields(data):
    c = rat(data['cl']); delta = 1-1/c
    pot = {}
    for (j,m,k), value in zip(data['order'], data['coefficients']):
        pot[j,2*m] = pot.get((j,2*m), ZERO)+rat(value)*T**k
    rho, stream = {}, {}
    for (j,n), value in pot.items():
        p = (3+1/c-j*delta)/2
        lap = rad(rad(value,p),p)-n*n*value
        drlap = rad(lap,p)-2*lap
        put(rho,j,n-1,(drlap+n*lap)/2)
        put(rho,j,n+1,-(drlap-n*lap)/2)
        plus = rad(value,p)-n*value
        plus = rad(plus,p)-(n+2)*plus
        minus = rad(value,p)+n*value
        minus = rad(minus,p)+(n-2)*minus
        put(stream,j,n+2,plus/4)
        put(stream,j,n-2,-minus/4)
    return c, delta, {k:divide(v) for k,v in rho.items()}, {k:divide(v) for k,v in stream.items()}

def square_groups(rows, delta, k):
    by_mode = {}
    for (j,n), value in rows.items():
        by_mode.setdefault(n,[]).append((j,value,td(value,(j+1)*delta/2,k)))
    groups = {}
    pairs = 0
    for n, entries in by_mode.items():
        for i,(j,v,dv) in enumerate(entries):
            for l in range(i,len(entries)):
                jj,w,dw = entries[l]
                value = (1 if i==l else 2)*(n*n*v*w+dv*dw)
                groups[j+jj] = groups.get(j+jj,ZERO)+value
                pairs += 1
    return groups, pairs

def integral(value,b):
    shifted = (T*value)(U)
    answer = arb(0)
    for l,v in enumerate(shifted):
        if v:
            assert b+l > -1, (str(b),l)
            answer += ar(v/(b+l+1))
    return answer

def run(name, ps, bits):
    start = time.monotonic(); ctx.prec = bits
    path = ROOT/f'data/{name}_canonical.json'
    c,delta,rho,stream = fields(json.loads(path.read_text()))
    bgroups,bpairs = square_groups(stream,delta,2)
    cgroups,cpairs = square_groups(rho,delta,1)
    print('constructed',len(rho),'density terms',len(stream),'stream terms',time.monotonic()-start,flush=True)
    boxes = [('FW-T-T4L2-sharp-v1',Q(1,7744),Q(147,200000),2**18),
             ('FW-T-T4L2-sharpw-v1',Q(1,5184),Q(1351,1000000),2**20),
             ('FW-T-T4L2-v1',Q(1,2**17),Q(1,2**14),2**18),
             ('FW-T-TB-sharp-v1',Q(1,8192),Q(43,50000),2**18),
             ('A2-D(b)',Q(1,2**18),Q(1,2**16),2**18)]
    out = {'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,
           'precision_bits':bits,'source_sha256':digest(path),'code_sha256':digest(Path(__file__)),
           'proof_sha256':digest(ROOT/'PROOF.md'),'method':'exact polar squares and background weak pairing; no cached residual',
           'B_pairs':bpairs,'C_pairs':cpairs,'probes':[]}
    pi = arb.pi()
    for p in ps:
        linear = sum((-pi/2*integral(value*((3*c+1)-2*c*p*T),(j+1)*delta/2+p-3)
                      for (j,n),value in rho.items() if n==1),arb(0))
        ngroups = {}
        for (j,m),ss in stream.items():
            ds = td(ss,(j+1)*delta/2,2)
            for (k,n),rr in rho.items():
                if abs(n-m) != 1:
                    continue
                sigma = 1 if n>m else -1
                value = rr*(sigma*m*ss*(1-2*p*T)-ds)
                ngroups[j+k] = ngroups.get(j+k,ZERO)+value
        nonlinear = pi/4*sum((integral(value,(j+2)*delta/2+p-3)
                               for j,value in ngroups.items()),arb(0))
        pairing = linear+nonlinear
        b2 = pi/2*sum((integral(value,2*p-3+(j+2)*delta/2) for j,value in bgroups.items()),arb(0))
        c2 = pi/2*sum((integral(value,2*p-3+(j+2)*delta/2) for j,value in cgroups.items()),arb(0))
        a2 = pi/2*integral(((3*c+1)-2*c*p*T)**2,Q(2*p-3))
        n2 = pi/(2*(2*p-1)*(2*p-2))
        assert min(b2,c2,a2,n2) > 0
        n,a,b,cc = [v.sqrt() for v in [n2,a2,b2,c2]]
        base = a+(1+2*p)*b+cc
        results=[]
        for fw,s,r,w2 in boxes:
            mass=ar(r)/arb(w2).sqrt()
            grad=ar(r)/(4*pi*ar(s)*(1+ar(s))).sqrt()
            denominator=base+grad*n
            upper=mass*denominator
            gap=abs(pairing)-upper
            results.append({'framework':fw,'necessary_upper':upper.str(90),'gap':gap.str(90),
                            'excluded':bool(gap>0),'L2_correction_lower_at_d':(abs(pairing)/denominator).str(90)})
        out['probes'].append({'p':p,'pairing':pairing.str(100),'linear_pairing':linear.str(90),
                              'nonlinear_pairing':nonlinear.str(90),'N':n.str(90),'A':a.str(90),'B':b.str(90),'C':cc.str(90),
                              'denominator_without_d':base.str(90),'boxes':results})
        out['elapsed_seconds']=time.monotonic()-start
        (ROOT/f'verification/{name}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
        print('p',p,'pairing',pairing.str(24),'base',base.str(16),'all_excluded',all(q['excluded'] for q in results),
              'seconds',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('candidate',default='d2',nargs='?')
    parser.add_argument('--p',type=int,nargs='+',default=[2,3,4])
    parser.add_argument('--bits',type=int,default=1024)
    args=parser.parse_args()
    assert all(p>=2 for p in args.p)
    run(args.candidate,args.p,args.bits)
