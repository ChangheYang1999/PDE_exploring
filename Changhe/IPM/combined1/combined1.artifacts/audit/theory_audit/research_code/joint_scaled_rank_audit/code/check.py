"""Exact abstract shape and two-pole witnesses; no peer code execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import comb
import json,hashlib,sys,time
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
start=time.monotonic()
read=lambda p:json.loads(p.read_text())
old=read(B/'data/old_basis.json');own=read(B/'source/T4_single_scale.json')
peer=read(B/'source/N4_result.json');abstract=read(B/'source/N4_shapes.json')
shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
oldshapes=list(map(shape,old['generators']))
assert len(oldshapes)==len(set(oldshapes))==1922
new=[(j,m,('legqs',0,N,4,R)) for R in [25,50] for j in [1,2,3] for m in range(9,16) for N in range(12)]
allshapes=oldshapes+new
assert len(new)==504 and len(set(allshapes))==2426 and set(allshapes)==set(map(shape,abstract['generators']))
c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma
ps=[(3+gamma-j*delta)/2 for j in range(8)]
assert all(p.denominator!=1 for p in ps)
diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
assert all(p.denominator!=1 for p in diffs)
assert list(map(str,ps))==peer['branch_exponents']==own['p_j']
assert list(map(str,diffs))==peer['noninteger_differences']
assert 3+gamma<4 and gamma-1<0
witnesses=[];cross=[]
peerw={(x['scale'],x['m'],x['N']):x for x in peer['Laurent_witnesses']}
for R,Rother in [(25,50),(50,25)]:
    a=Q(R*R-1);v=-1/a;t=1-v;other=1-Q(Rother*Rother-1)/a
    assert other!=0;cross.append({'scale':R,'other_denominator':str(other)})
    row=next(x for x in own['rows'] if x['scale']==R)
    ow={(x['m'],x['N']):x for x in row['witnesses']}
    for m in range(9,16):
        for N in range(12):
            value=R**8*v**4*comb(2*N,N)*t**(m+N)/a**(4+N)
            assert value!=0 and value==Q(ow[m,N]['coefficient'])==Q(peerw[R,m,N]['Laurent_coefficient'])
            witnesses.append({'scale':R,'m':m,'N':N,'coefficient':str(value),'nonzero':True})
inputs=[B/'PROOF.md',Path(__file__),B/'data/old_basis.json',*sorted((B/'source').iterdir())]
result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in inputs},'potential_dimension':2426,'density_dimension':2426,'shape_list_matches':True,'witness_count':len(witnesses),'cross_poles':cross,'witnesses':witnesses,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-274 abstract two-scale rank and density injectivity','actual_candidate_shape_match':None}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(result['utc'],result['witness_count'],result['elapsed_seconds'])
