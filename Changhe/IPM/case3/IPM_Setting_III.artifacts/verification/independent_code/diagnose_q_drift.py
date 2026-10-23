"""Strain-range diagnostics and independently integrated third angular mass.
Only this lane's scalar coefficient reader and retained inverse samples are used.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,hashlib,csv,math
import numpy as np
from numpy.polynomial.legendre import leggauss
from log_radius_inverse import LogRadiusQCheckpoint
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);ap.add_argument('--evaluation',action='append',default=[]);args=ap.parse_args()
c=LogRadiusQCheckpoint(args.snapshot);a=float(c.polynomial(0,-1.));D=c.cl-1
# Polynomial exactness of Gauss integration replaces the reader's adaptive t integration.
def primitive(sig,nq):
    nodes,weights=leggauss(nq);ss=np.asarray(sig,float);tt=ss[...,None]*(nodes+1)/2
    vals=(.25+(.5*c.kappa-.25)*tt)*(c.polynomial(1,2*tt-1)-tt*c.polynomial(2,2*tt-1))
    return ss*np.sum(vals*weights,axis=-1)/2
orders=[max(24,(c.N+4)//2),max(48,c.N+4),max(64,2*c.N+8)]
# Mapped Gauss measure is sigma/2; the physical strain integrand has coefficient 1/4.
totals=[float(primitive(1.,nq)) for nq in orders]
cc=-a/4+totals[-1];J=totals[-1]
assert max(abs(v-J) for v in totals)<2e-9*max(1.,abs(J)),totals
def coordinates_with_weight(log_r):
    log_r=np.asarray(log_r,float)
    tq,sigma=c.coordinates_log(log_r)
    # w=(L/r)^(1/kappa) sigma^(1/(2*kappa))/2.  Retain w even
    # when the double-precision sigma has rounded to one.
    w=np.exp(-math.log(2.)+(math.log(c.L)-log_r)/c.kappa+np.log(sigma)/(2*c.kappa))
    assert np.all(w>0) and np.all(w<=1+2e-13)
    return tq,sigma,w
logs=np.arange(-30.,300.0001,.25);tq,sig,w=coordinates_with_weight(logs*math.log(10.))
mass=w/2*(sig*c.polynomial(1,tq)-sig*sig*c.polynomial(2,tq))
cumulative=primitive(sig,orders[-1]);radial=[]
for l,ss,mm,jj in zip(logs,sig,mass,cumulative):
    radial.append({'log10_radius':float(l),'sigma':float(ss),'rho3_over_r':float(mm),'cumulative_rho3_over_r2':float(jj),'fraction_of_signed_total':float(jj/J) if J else None})
# A separate angular projection confirms rho3/r, without the two-coefficient formula.
theta=np.arange(256)*2*np.pi/256;cosines=np.cos(2*np.arange(c.M)[:,None]*theta)
proj=[]
for logr in [-12.,-2.,0.,8.,20.,40.,80.,160.,250.]:
    tt,sg,ww=coordinates_with_weight(np.array([logr*math.log(10.)]));vals=np.array([float(sg[0]**k*c.polynomial(k,tt)[0]) for k in range(c.M)])
    density_over_r=ww[0]*np.sin(theta)*(vals@cosines)
    numeric=float(2*np.mean(density_over_r*np.sin(3*theta)))
    formula=float(ww[0]/2*(sg[0]*c.polynomial(1,tt)[0]-sg[0]**2*c.polynomial(2,tt)[0]))
    assert abs(numeric-formula)<3e-12*max(1.,abs(formula))
    proj.append({'log10_radius':logr,'angular_projection':numeric,'two_coefficient_formula':formula})
# Existing full-plane velocity samples, with both actual and demanded strain denominators.
rows=[];sources=[]
for path in args.evaluation:
    src=Path(path);ev=json.loads(src.read_text());sources.append({'path':str(src.resolve()),'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
    assert ev['metadata']['N']==c.N and ev['metadata']['M']==c.M
    assert ev['metadata']['cl']==c.cl
    expected_c=ev['center_and_tail']['quadrature'][-1]['c']
    assert abs(cc-expected_c)<2e-9*max(1.,abs(expected_c)),(cc,expected_c)
    for row in ev['points']:
        x,y=row['x'],row['y']
        if not x or not y:continue
        r=row['radius'];ss=float(c.coordinates_log(np.array([math.log(r)]))[1][0]);masscum=float(primitive(ss,orders[1]))
        rows.append({'source':str(src),'x':x,'y':y,'r':r,'theta':math.atan2(y,x),'rho_over_a_y':row['rho']/(a*y),'U1_over_actual_minus_c_x':row['U'][0]/(-cc*x),'U2_over_actual_c_y':row['U'][1]/(cc*y),'U1_over_D_x':row['U'][0]/(D*x),'U2_over_minus_D_y':row['U'][1]/(-D*y),'R_Nf_FD8':row['residuals'][-1]['R_Nf'],'R_Nv_FD8':row['residuals'][-1]['R_Nv'],'cumulative_third_mass':masscum})
# Signed mass is not a probability. Report absolute mass window separately and do not infer a unique ring.
absnorm=float(np.sum((abs(mass[1:])+abs(mass[:-1]))/2*np.diff(logs)*math.log(10.)))
absacc=np.concatenate(([0.],np.cumsum((abs(mass[1:])+abs(mass[:-1]))/2*np.diff(logs)*math.log(10.))))
percentiles={}
for f in [.05,.25,.5,.75,.95]:percentiles[str(f)]=float(np.interp(f*absnorm,absacc,logs))
result={'utc':datetime.now(timezone.utc).isoformat(),'tag':args.tag,'metadata':c.meta,'a0':a,'canonical_c_polynomial_quadrature':cc,'D':D,'Delta':D+cc,'third_mass_integral_levels':dict(zip(map(str,orders),totals)),'required_total_c_plus_a_over4':cc+a/4,'angular_projection_checks':proj,'signed_mass_log_profile':radial,'absolute_mass_on_log_window':absnorm,'absolute_mass_log10_percentiles_on_window':percentiles,'inverse_samples':rows,'evaluation_sources':sources,'scope':'Pointwise full-plane inverse observations, separate polynomial radial integration and angular projection. Signed mass can cancel or occupy several radii; no unique ring, uniform asymptotic law in D, or continuum profile/nonexistence is inferred. Window percentiles are not global tail bounds. FD8 precision limits of the original samples remain.'}
out=Path('evidence/q_drift')/args.tag;out.mkdir(parents=True,exist_ok=True);(out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
if rows:
    with (out/'samples.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
with (out/'third_mass.csv').open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(radial[0]));writer.writeheader();writer.writerows(radial)
print(json.dumps({'utc':result['utc'],'tag':args.tag,'a0':a,'canonical_c':cc,'total_third_mass':J,'absolute_mass_log10_percentiles_on_window':percentiles,'samples':len(rows)}),flush=True)
