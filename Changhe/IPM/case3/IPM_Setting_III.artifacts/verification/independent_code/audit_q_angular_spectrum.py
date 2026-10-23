"""Result106. Direct quotient spectra; standard-library arithmetic, no inverse reuse.

This density-only diagnostic reads frozen exact JSON coefficients. It does not
load, import or execute the numerics lane's evaluator or its angular transform.
"""
from datetime import datetime, timezone
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidence/q_angular_spectrum'
OUT.mkdir(parents=True,exist_ok=True)
PROOF=ROOT/'research/q_angular_spectrum_audit/PROOF.md'
CHECKDIR=PROOF.parent/'verification'
checks=0
start=time.monotonic()


def require(condition, message=''):
    global checks
    if not condition:
        raise AssertionError(message)
    checks+=1


def dec(x):
    f=F(x)
    return D(f.numerator)/D(f.denominator)


def cheb_direct(coeff,x):
    out=coeff[0]
    if len(coeff)==1:
        return out
    prev=x*0+1
    now=x
    out+=coeff[1]*now
    for c in coeff[2:]:
        prev,now=now,2*x*now-prev
        out+=c*now
    return out


def cheb_clenshaw(coeff,x):
    b1=x*0
    b2=x*0
    for c in coeff[:0:-1]:
        b0=c+2*x*b1-b2
        b2,b1=b1,b0
    return coeff[0]+x*b1-b2


def logmap(s,kappa,L):
    return L.ln()+s.ln()/2-kappa*(2*(1-s)).ln()


def inverse_map(radius,kappa,L,precision):
    # Monotone bisection, independent of any producer or our Poisson inverses.
    r=D(radius)
    target=r.ln()
    lo=D(0)
    hi=D(1)
    for unused in range(4*precision+32):
        mid=(lo+hi)/2
        if mid==lo or mid==hi:
            break
        if logmap(mid,kappa,L)<target:
            lo=mid
        else:
            hi=mid
    s=(lo+hi)/2
    defect=abs(logmap(s,kappa,L)-target)
    require(defect<D(10)**(-precision+5),('inverse defect',radius,defect))
    return s,defect


# Independent rational Chebyshev forward recurrence against Clenshaw.
for size in range(1,21):
    coeff=[F((-1)**j*(j+3),j+1) for j in range(size)]
    for x in [F(-1),F(-7,9),F(-1,3),F(0),F(2,7),F(9,10),F(1)]:
        require(cheb_direct(coeff,x)==cheb_clenshaw(coeff,x),'Chebyshev identity')

# A separate midpoint cosine transform on a finite polynomial. This does not
# use Chebyshev evaluation and tests all recovered coefficients, including zeros.
finite_errors=[]
for J,M in [(16,9),(32,16),(64,48)]:
    coeff=[(-1)**j/(j+1)**2 for j in range(M)]
    angles=[math.pi*(i+.5)/(2*J) for i in range(J)]
    values=[sum(c*math.cos(2*j*th) for j,c in enumerate(coeff)) for th in angles]
    recovered=[sum(v*math.cos(2*j*th) for th,v in zip(angles,values))*(1 if j==0 else 2)/J for j in range(J)]
    err=max(abs(v-(coeff[j] if j<M else 0)) for j,v in enumerate(recovered))
    require(err<3e-14,('finite transform',J,err))
    finite_errors.append({'nodes':J,'nonzero_modes':M,'max_absolute_error':err})

# Rational normalized spectrum for sin(theta)^(7/4). Recurrence follows from
# integration by parts in the proof, not from quadrature or a fitted spectrum.
nu=F(7,4)
Ij=F(1)
normalized=[F(1)]
for j in range(1,2049):
    old=Ij
    Ij*= (2*j-2-nu)/(2*j+nu)
    require(2*(-j*Ij+(j-1)*old)==nu*(Ij+old),'integration-by-parts identity')
    normalized.append(2*Ij)

manufactured_errors=[]
for J in [512,2048,8192]:
    angles=[math.pi*(i+.5)/(2*J) for i in range(J)]
    values=[math.sin(th)**float(nu) for th in angles]
    mean=sum(values)/J
    rec=[2*sum(v*math.cos(2*j*th) for th,v in zip(angles,values))/(J*mean) for j in range(1,17)]
    err=max(abs(rec[j-1]-float(normalized[j])) for j in range(1,17))
    require(err<1e-7,('fractional transform',J,err))
    if manufactured_errors:
        require(err<manufactured_errors[-1]['max_absolute_normalized_error']/20,('quadrature refinement',J,err))
    manufactured_errors.append({'nodes':J,'max_absolute_normalized_error':err,'coefficients_j1_to_j16':rec})

with localcontext() as ctx:
    ctx.prec=80
    powers=[]
    for j in [16,32,64,128,256,512,1024]:
        power=(abs(dec(normalized[j]))/abs(dec(normalized[2*j]))).ln()/D(2).ln()
        require(abs(power-D(11)/4)<D(1)/j,('power',j,power))
        powers.append({'j':j,'two_j':2*j,'observed_power':str(power)})
    require(abs(D(powers[-1]['observed_power'])-D(11)/4)<D('0.00001'),'limiting power')

# Saved states: exact binary inputs, two independent arithmetic precisions.
# Roots are cached by the exact map parameters, radius and working precision.
roots={}
state_results=[]
for N in [64,96,128,160,192]:
    path=ROOT/f'evidence/q_canonical_high_jets/R1C_CL3P0_N{N}/exact_input.json'
    raw=path.read_bytes()
    doc=json.loads(raw)
    coeffs=[[F(v) for v in row] for row in doc['coefficients']]
    M=len(coeffs)
    a=sum(c*(-1)**j for j,c in enumerate(coeffs[0]))
    require(a!=0,'nondegenerate stored formula')
    src=Path(doc['source'])
    require(hashlib.sha256(src.read_bytes()).hexdigest()==doc['source_sha256'],'binary source provenance')
    results={}
    for precision in [60,100]:
        with localcontext() as ctx:
            ctx.prec=precision
            cd=[[dec(v) for v in row] for row in coeffs]
            kappa=dec(doc['kappa'])
            L=dec(doc['L'])
            ad=dec(a)
            rows=[]
            for radius in ['0.01','0.03','0.1','0.3']:
                key=(doc['kappa'],doc['L'],radius,precision)
                if key not in roots:
                    roots[key]=inverse_map(radius,kappa,L,precision)
                s,defect=roots[key]
                t=2*s-1
                modes=[]
                spow=D(1)
                for j,row in enumerate(cd):
                    b=cheb_clenshaw(row,t)
                    forward=cheb_direct(row,t)
                    require(abs(b-forward)<D(10)**(-precision+7)*max(D(1),abs(b)),('saved Cheb cross-check',N,precision,radius,j))
                    modes.append((1-s)*spow*b/ad)
                    spow*=s
                rows.append({'r':radius,'s':str(s),'map_log_defect':str(defect),
                             'signed_coefficients':[str(v) for v in modes],
                             'absolute_coefficients_relative_to_c0':[str(abs(v/modes[0])) for v in modes],
                             'exact_zero_from_j':M})
            results[str(precision)]=rows
    comparisons=[]
    with localcontext() as ctx:
        ctx.prec=105
        for low,high in zip(results['60'],results['100']):
            lowc=[D(v) for v in low['signed_coefficients']]
            highc=[D(v) for v in high['signed_coefficients']]
            maxrel=max(abs(l-h)/max(abs(h),D('1e-300')) for l,h in zip(lowc,highc))
            maxabs=max(abs(l-h) for l,h in zip(lowc,highc))
            require(maxrel<D('1e-48'),('saved precision',N,low['r'],maxrel))
            comparisons.append({'r':low['r'],'max_relative_difference':str(maxrel),'max_absolute_difference':str(maxabs)})
    state_results.append({'N':N,'M':M,'a_exact':str(a),'source':doc['source'],'source_sha256':doc['source_sha256'],
                          'exact_input':str(path.relative_to(ROOT)), 'exact_input_sha256':hashlib.sha256(raw).hexdigest(),
                          'kappa_exact':doc['kappa'],'L_exact':doc['L'], 'precision_comparisons':comparisons,'evaluations':results})

record={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,
        'verdict':'PASS','checks':checks,'scope':'Density quotient coefficients only; no limiting regularity or inverse claim.',
        'proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'manufactured_nu_exact':str(nu),'manufactured_normalized_coefficients_j0_to_j32':[str(v) for v in normalized[:33]],
        'manufactured_doubling_powers':powers,'manufactured_quadrature':manufactured_errors,
        'finite_transform_tests':finite_errors,'states':state_results}
(OUT/'RESULTS.json').write_text(json.dumps(record,indent=2)+'\n')
(CHECKDIR/'checks.json').write_text(json.dumps({k:v for k,v in record.items() if k!='states'},indent=2)+'\n')
lines=['# Direct quotient angular spectrum audit','',f"UTC {record['utc']}. {checks} checks PASS. Elapsed {record['elapsed_seconds']:.3f} seconds.",'',
       'The exact saved formula has zero coefficients for j >= M. Values below a floating transform floor are evaluated directly here. These finite spectra do not determine the regularity of a limit. Both 60 and 100 decimal digit evaluations are stored.','','| N | M | r | c12/c0 | c16/c0 | c24/c0 | c32/c0 |','|---:|---:|---:|---:|---:|---:|---:|']
for state in state_results:
    for row in state['evaluations']['100']:
        with localcontext() as ctx:
            ctx.prec=8
            coeff=[D(v) for v in row['signed_coefficients']]
            values=[format(coeff[j]/coeff[0],'.5E') if j<len(coeff) else '0 (exact)' for j in [12,16,24,32]]
        lines.append('| '+str(state['N'])+' | '+str(state['M'])+' | '+row['r']+' | '+' | '.join(values)+' |')
lines+=['','The manufactured quotient sin(theta)^(7/4) has exact rational normalized cosine coefficients from the proved recurrence. Its tail has power 11/4. The measured doubling exponents approach this value:', '', '| j | exponent from j and 2j |','|---:|---:|']
for row in powers:
    lines.append('| '+str(row['j'])+' | '+row['observed_power'][:24]+' |')
lines+=['','A finite low-mode list does not bound a fractional endpoint coefficient without additional controlled hypotheses. The proof supplies a subtraction construction and states explicitly that it need not solve the frozen angular equation.']
(OUT/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'verdict':record['verdict'],'checks':checks,'elapsed_seconds':record['elapsed_seconds'],'output':str(OUT/'SUMMARY.md')},indent=2))
