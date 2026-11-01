"""Independent exact replay of compact certificate coverage and dyadic radii."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx,fmpq
from general_rational_majorant import RationalMajorant
from general_component_radius import stringify
ctx.prec=1024

def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator

def main():
    start=time.monotonic();root=Path('research/150_four_ninths_radii');source=Path('research/149_compact_response_certificates/verification/checks.json');data=json.loads(source.read_text());assert data['all_checks_pass'] and len(data['rows'])==5;assert json.loads((source.parent/'exact_repack_checks.json').read_text())['all_checks_pass']
    rows=[]
    for row in data['rows']:
        index=row['root_index'];s=F(row['s']);coverpath=source.parent/('root'+str(index)+'_coverage_exact.json');cover=json.loads(coverpath.read_text());K=cover['starting_index'];top=F(1,4*K-2)
        leaves=[];accepted=empty=0
        for node in cover['nodes']:
            address=node['address'];den=2**len(address);num=int(address,2) if address else 0
            a,b=F(num,den)*top,F(num+1,den)*top
            assert F(node['a'])==a and F(node['b'])==b
            lower=max(K,ceil((1/b+2)/4));upper=None if not a else floor((1/a+2)/4)
            assert lower==node['lower'] and upper==node['upper']
            if node['status']=='empty':assert upper is not None and upper<lower;empty+=1
            else:
                assert node['status']=='accepted'
                # Exact dyadic endpoint test, independent of Arb display and parsing.
                m,e,r,re=node['response_exact_dyadic']
                mid=F(m)*F(2)**e;rad=F(r)*F(2)**re
                assert rad>=0 and abs(mid)-rad>s;accepted+=1
            leaves.append((a,b))
        leaves.sort();assert leaves[0][0]==0 and leaves[-1][1]==top
        assert all(left[1]==right[0] for left,right in zip(leaves,leaves[1:]))
        assert accepted==cover['accepted'] and empty==cover['empty'] and len(leaves)==cover['split']+1
        for item in row['finite']:assert abs(arb(item['sigma']))>arb(fmpq(str(s)))
        assert {v['k'] for v in row['finite']}==set(range(1,17))
        lo,hi=map(F,row['root_interval'])
        a=F(ceil((1+max(abs(lo),abs(hi)))*1000),1000)
        assert a>=1+abs(lo) and a>=1+abs(hi)
        m=RationalMajorant(2,9,4,a,s);box=[2*v for v in m.Y0]
        upper=1
        while any(v>b for v,b in zip(m.transformed(F(1,2**upper),box),box)):upper*=2
        lower=upper//2
        while upper-lower>1:
            q=(upper+lower)//2
            if all(v<=b for v,b in zip(m.transformed(F(1,2**q),box),box)):upper=q
            else:lower=q
        z=F(1,2**upper);image=m.transformed(z,box);assert all(v<b for v,b in zip(image,box))
        preceding=m.transformed(2*z,box);assert any(v>b for v,b in zip(preceding,box))
        record=dict(root_index=index,a=a,s=s,z0=z,z_power=upper,radius_power_of_two=F(9*upper,4),kappa=m.kappa,L=m.L,constant=m.constant,J=m.J,Y0=m.Y0,box=box,map_on_box=image,maximum_ratio=max(v/b for v,b in zip(image,box)),preceding_dyadic_fails=True,coverage_leaves=len(leaves),accepted_leaves=accepted,empty_leaves=empty,coverage_sha256=sha256(coverpath.read_bytes()).hexdigest())
        rows.append(record);print(json.dumps(dict(root=index,a=str(a),s=str(s),q=upper,radius_power=str(F(9*upper,4)),ratio=float(record['maximum_ratio']),coverage_leaves=len(leaves))),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,source_sha256=sha256(source.read_bytes()).hexdigest(),rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Exact certificate replay and rational supersolutions; the analytic theorem145 and response formula149 need independent review.')
    (root/'verification/checks.json').write_text(json.dumps(stringify(result),indent=2)+'\n')
    for name in ['check_compact_response_cover.py','general_rational_majorant.py','general_component_radius.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
if __name__=='__main__':
    try:main()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/150_four_ninths_radii/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
