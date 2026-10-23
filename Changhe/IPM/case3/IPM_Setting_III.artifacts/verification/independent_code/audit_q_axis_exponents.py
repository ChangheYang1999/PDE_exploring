"""Density-only MP axis exponent audit, with independent log-radius FD."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import argparse,json,hashlib,sys
import mpmath as mp
from q_checkpoint_reader import QCheckpoint
from q_high_precision_density import MPQDensity
from finite_angular_residual_projection import polynomial_and_derivative

ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);ap.add_argument('--digits',type=int,default=90);args=ap.parse_args()
q=QCheckpoint(args.snapshot);mp.mp.dps=args.digits+40
model=MPQDensity(q.coeff,q.L,q.kappa,q.cl)
a=mp.fsum(((-1)**k)*v for k,v in enumerate(model.coeff[0]));assert a

def qval(r,axis,analytic=False):
    s,w=model.coords(r);t=2*s-1 if s<mp.mpf('.5')else 1-2*w
    pairs=[polynomial_and_derivative(row,t)if analytic else model.clenshaw(row,t)for row in model.coeff]
    vs=[];ds=[]
    for j,(B,Bt)in enumerate(pairs):
        eps=1 if axis=='x'else (-1)**j
        vs.append(eps*s**j*B)
        ds.append(eps*((j*s**(j-1)*B if j else 0)+2*s**j*Bt))
    val=mp.fsum(vs);dot=2*s*w/(w+2*model.kappa*s)*(-val+w*mp.fsum(ds))/a
    return w*val/a,dot

def fd(r,axis,h):
    return (qval(r*mp.exp(-2*h),axis)[0]-8*qval(r*mp.exp(-h),axis)[0]+8*qval(r*mp.exp(h),axis)[0]-qval(r*mp.exp(2*h),axis)[0])/(12*h)

# Manufactured constant Chebyshev density has q=w and known local exponent.
saved=model.coeff;old_a=a;model.coeff=[[mp.mpf(3)]];a=mp.mpf(3);gate=[]
for radius in ('0.0001','0.02','0.3','1','5','100'):
    r=mp.mpf(radius);s,w=model.coords(r)
    for axis in ['x','y']:
        v,d=qval(r,axis,True);target=2*w/(w+2*model.kappa*s)
        error=abs(-d/(1-v)-target);assert error<mp.mpf('1e-100')
        h=mp.mpf('.00001');de=abs(fd(r,axis,h)-d);assert de<mp.mpf('1e-17')
        gate.append(dict(r=radius,axis=axis,analytic_error=mp.nstr(error,12),fd_error=mp.nstr(de,12)))
model.coeff=saved;a=old_a
bphys=None
for path in Path('evidence/q_exact_jets').glob('R1*/diagnostic.json'):
    for row in json.loads(path.read_text())['rows']:
        if row['metadata']['sha256']==q.meta['sha256']:
            b=F(row['exact']['b_core']['exact']);bphys=mp.mpf(b.numerator)/b.denominator*mp.power(2,2*model.kappa)/model.L**2
core=mp.sqrt(abs(a/bphys))if bphys else None
radii=[('physical',mp.power(10,-4+mp.mpf(5)*j/11))for j in range(12)]
if core:radii.extend(('core_scaled',core*mp.power(10,-3+mp.mpf(4)*j/11))for j in range(12))
rows=[]
for kind,r in radii:
    for axis in ['x','y']:
        val,dot=qval(r,axis,True);g=1-val;comparisons=[]
        for h in [mp.mpf('.0001'),mp.mpf('.00001')]:
            d=fd(r,axis,h);comparisons.append(dict(log_step=str(h),q_dot=mp.nstr(d,args.digits),absolute_error=mp.nstr(abs(d-dot),30),exponent_difference=mp.nstr(abs((d-dot)/g),30)if g else None))
        rows.append(dict(grid=kind,axis=axis,r=mp.nstr(r,args.digits),r_over_core=mp.nstr(r/core,args.digits)if core else None,q=mp.nstr(val,args.digits),one_minus_q=mp.nstr(g,args.digits),q_dot=mp.nstr(dot,args.digits),s_local=mp.nstr(-dot/g,args.digits)if g else None,FD=comparisons))
dest=Path('evidence/q_axis_exponents')/args.tag;dest.mkdir(parents=True,exist_ok=True)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='COMPUTED',source=args.snapshot,source_sha256=q.meta['sha256'],a=mp.nstr(a,args.digits),physical_b=mp.nstr(bphys,args.digits)if bphys else None,core=mp.nstr(core,args.digits)if core else None,working_digits=mp.mp.dps,rows=rows,manufactured_gate=gate,command=[sys.executable,*sys.argv],implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Finite axis samples and two log-radius FD comparisons. Does not establish a Holder exponent or a smooth limit. Saved binary coefficients are evaluated without normalization repair.')
(dest/'diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
lines=[f'# Axis exponents: {args.tag}','',out['utc'],'',out['scope'],'',f'Source SHA256 {q.meta["sha256"]}; a={mp.nstr(a,14)}; core={mp.nstr(core,14) if core else "undefined"}.','','| grid | axis | r | 1-q | s_local | FD exponent difference, h=1e-5 |','|---|---|---:|---:|---:|---:|']
for row in rows:lines.append('| '+row['grid']+' | '+row['axis']+' | '+' | '.join(mp.nstr(mp.mpf(row[k]),10)if row[k]is not None else'undefined'for k in ['r','one_minus_q','s_local'])+' | '+row['FD'][-1]['exponent_difference']+' |')
(dest/'TABLE.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'tag':args.tag,'rows':len(rows),'a':out['a'],'core':out['core'],'status':'COMPUTED'}))
