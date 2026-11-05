#!/usr/bin/env python3
"""FLOAT evaluation of proved mean-zero derivative Fourier-moment bounds.

Input radial point evaluations and Gauss sums remain uncertified quadrature.
"""
import argparse,json,math
from pathlib import Path
import numpy as np

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('--output',type=Path,required=True)
    ar=ap.parse_args();d=json.loads(ar.input.read_text());n=d['nodes'];lo,hi=d['log_interval']
    zz,ww=np.polynomial.legendre.leggauss(n);ww=ww*(hi-lo)/2
    rs=np.array([p['r'] for p in d['points']]);den=np.array([p['energies'][0] for p in d['points']]);E=np.array(d['physical_energies'][0])
    total=np.array(d['integer_moment_totals']);frac=np.array(d['fractional_4p1_totals'])
    records=[]
    for ai,order in enumerate([0,1,1,2,2,2]):
        m=2+order;mass=np.sqrt(2*np.pi*rs*np.maximum(den[:,ai,m+2],0))*rs*ww
        best=None
        for lam in np.geomspace(1e-5,100,700):
            v=lam*rs;logweight=np.where(v<=2,v,2+2*np.log(np.maximum(v/2,1)))
            low=float(mass@logweight/(2*np.pi))
            for tau in np.geomspace(.01,100,50):
                t=tau*E[ai,m+1]/E[ai,m+2]
                high=float(np.sqrt((E[ai,m+1]+t*E[ai,m+2])*np.log1p(1/(t*lam*lam))/(4*np.pi)))
                val=low+high
                if best is None or val<best['bound']:
                    best={'bound':val,'lambda':float(lam),'t':float(t),'low':low,'high':high,'h_L1_screen':float(mass.sum())}
        total[ai,m]=min(total[ai,m],best['bound']);records.append(best)
        if order==2:frac[ai]=min(frac[ai],total[ai,4]**.9*total[ai,5]**.1)
    D=np.zeros((3,3));D[0,0]=2*(total[0,4]+frac[0])
    for i in range(2):D[i+1,0]=D[0,i+1]=2*(20*(total[0,3]+frac[0])+2*(total[i+1,4]+frac[i+1]))
    for i in range(2):
        for j in range(2):
            ij=3 if i==j==0 else 5 if i==j==1 else 4
            D[i+1,j+1]=4*(60*(total[0,2]+frac[0])+20*(total[i+1,3]+frac[i+1]+total[j+1,3]+frac[j+1])+2*(total[ij,4]+frac[ij]))
    out={'status':'FLOAT_PHYSICAL_CANCELLATION_SCREEN_NOT_A_CERTIFICATE','source':str(ar.input),
         'critical_moment_records':records,'integer_moment_totals':total.tolist(),'fractional_4p1_totals':frac.tolist(),
         'weighted_Schur_matrix':D.tolist(),'Schur_norm':float(np.linalg.norm(D,2)),'row_sum':float(max(D.sum(axis=1)))}
    ar.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
