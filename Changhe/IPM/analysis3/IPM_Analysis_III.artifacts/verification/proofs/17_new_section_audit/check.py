from pathlib import Path
from datetime import datetime,timezone
import json,sys,hashlib
from types import SimpleNamespace
from fractions import Fraction
import sympy as s
from flint import arb,fmpq,ctx
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P/'code_snapshot'))
from opimage import Cells,green_A_on_cell
from section import TestSplines
from exact_trial import ExpPoly,moment_minf
ctx.prec=160
T=SimpleNamespace(p=7,t_lo_q=fmpq(0),t_hi_q=fmpq(2),nc=2,tb_q=[fmpq(0),fmpq(1),fmpq(2)],tb=[arb(0),arb(1),arb(2)],h_q=[fmpq(1),fmpq(1)])
C=Cells(T,[fmpq(1)],[fmpq(1)])
B=TestSplines(T,C,1)
fi=min(B.pieces);la=max(B.pieces)
first=dict(B.pieces[fi])[0]
last=dict(B.pieces[la])[B.nb-1]
left=first[0]
h=C.cells[la]['h'];right=sum((v*h**j for j,v in enumerate(last)),arb(0))
assert left==1 and right==1
assert 0 not in B.pieces and C.n-1 not in B.pieces
f=ExpPoly([(fmpq(0),[arb(1)])])
A0=moment_minf(arb(6),0)
g=green_A_on_cell(f,1,A0,arb(1),'minf')
ghost=g.terms[fmpq(-2)][0]
assert ghost.contains(arb(0)) and ghost.rad()>0
ss=s.symbols('sigma',real=True)
assert s.simplify(s.diff(s.exp(4*ss)/6,ss)+2*s.exp(4*ss)/6-s.exp(4*ss))==0
k,ell,c,cp=s.symbols('k ell c cp',nonzero=True)
d=-k*c/(3*ell+k*cp)
assert s.cancel(k*c/3+d*(ell+k*cp/3))==0
assert s.simplify((3*k-1)/2-(2*k-1))==(1-k)/2
import numpy as np
src=Path('source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz')
z=np.load(src,allow_pickle=False)
# Name is taken from the original NPZ, not from the snapshot's TAU code.
a=Fraction(float(z['Aout'][-1,0]))/2
assert a==Fraction(-8059128652303703,20769187434139310514121985316880384)
out={'time_utc':datetime.now(timezone.utc).isoformat(),'test_endpoint_values':[str(left),str(right)],'test_infinite_cell_pieces':False,'ghost_coefficient':ghost.str(40),'ghost_radius':str(ghost.rad()),'omitted_TAU_coefficient':str(a),'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),'result':'PASS for the stated static and model checks'}
(P/'evidence'/'check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
