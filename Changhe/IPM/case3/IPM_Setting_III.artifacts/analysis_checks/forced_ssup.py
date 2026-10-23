# Forced-source local exponent supremum (scal1 / verifier correction of I.7): DW(0)=diag(A-Delta,1+Delta).
# Rows of the numerics table (NUM_REPORT 4.4): c_l beta mu Delta a0 smin.
import re, numpy as np
rows=[]
for line in open('numerics/NUM_REPORT.md'):
    m=re.match(r'\s+(\d+\.\d\d)\s+(\d+\.\d\d)\s+([+-]\d+\.\d+)\s+([+-]\d+\.\d+)\s+(\d+\.\d+)\s+(\d+e-\d+)\s+(\S+)',line)
    if m: rows.append([float(m.group(i)) for i in range(1,7)])
def ssup(lx,ly,a):
    D=lx-ly
    if abs(D)<1e-12: return float('nan')
    d=np.linspace(1+1e-9,60,600001)
    k=(lx*d-1)/D; py=(a+1-ly*d)/D
    return np.max(np.minimum(np.minimum(d,k),py))
print(" c_l  beta    a0    Delta  lam_x  lam_y  ssup_unforced  ssup_forced   smin")
for cl,b,mu,De,a0,sm in rows:
    A=2*cl-1; B=A-1
    su=min(a0/B,(a0+1)/A)
    sf=ssup(A-De,1+De,a0)
    print(f"{cl:4.2f} {b:5.2f} {a0:7.3f} {De:6.3f} {A-De:6.3f} {1+De:6.3f} {su:9.3f} {sf:12.3f} {sm:9.0e}")
