"""Independent archive/de Boor/polynomial-identity checker, packet187.
Does not import the generator, Cox recursion or floating quadrature.
"""
from fractions import Fraction as Q
from pathlib import Path
from bisect import bisect_right
from datetime import datetime,timezone
import hashlib,io,json,sys,time,resource
import numpy as np
import modal_norm_power as iv
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def decode(x):
    p=Path(x['archive_path']);blob=p.read_bytes();assert hashlib.sha256(blob).hexdigest()==x['archive_sha256']
    with np.load(io.BytesIO(blob),allow_pickle=False)as a:
        d=int(a['deg']);N=int(a['Nt']);K=int(a['K']);grade=float(a['grade']);assert d==x['degree']and N==x['Nt']and K==x['K']
        assert str(a['rmap'].item())=='r2'and str(a['scheme'].item())=='mask'and int(a['mreg'])==2
        assert all(a[n].dtype==np.dtype('float64')for n in ['cG','beta','beta_basis','L','grade'])
        for field,name in [('basis_beta','beta_basis'),('beta','beta'),('L','L'),('grade','grade')]:assert Q.from_float(float(a[name]))==Q(x[field])
        # This intentionally reproduces the binary array, not ideal real-power knots.
        middle=np.power(np.linspace(0.,1.,N+1),grade);knots=np.r_[np.zeros(d),middle,np.ones(d)].astype('<f8')
        assert hashlib.sha256(knots.tobytes()).hexdigest()==x['knot_binary_little_endian_sha256']
        ts=list(map(Q,x['knots']));assert ts==[Q.from_float(float(t))for t in knots]
        assert ts.count(0)==d+1 and ts.count(1)==d+1 and all(t<=u for t,u in zip(ts,ts[1:]))
        assert all(ts.count(t)==1 for t in set(ts)if 0<t<1)
        assert a['cG'].shape in[(K*(N+d),),(K,N+d)]
        raw=a['cG'].reshape(K,N+d);cs=[]
        for k in range(K):
            row=[Q(0)if j<k//2 else Q.from_float(float(raw[k,j]))for j in range(N+d)]
            assert row==list(map(Q,x['coefficients'][k]));cs.append(row)
        declared=dict(v.split(':',1)for v in a['code_sha256'].tolist());assert declared['bq3core.py']==x['source_core_sha256']==digest(x['source_core_path'])
    assert Q(x['basis_beta'])>0 and Q(x['L'])>0
    return ts,cs,d

def deboor(ts,coeff,d,t):
    j=min(len(coeff)-1,bisect_right(ts,t)-1);assert d<=j<len(coeff)
    v=[coeff[j-d+i]for i in range(d+1)]
    for r in range(1,d+1):
        for i in range(d,r-1,-1):
            den=ts[i+1+j-r]-ts[i+j-d];alpha=(t-ts[i+j-d])/den if den else Q(0);v[i]=v[i-1]+alpha*(v[i]-v[i-1])
    return v[-1]
def horner(p,x):
    y=Q(0)
    for a in reversed(p):y=y*x+a
    return y

def normcell(family,lo,hi,b,d):
    # Independently assemble the four weighted polynomial coefficients, by
    # symmetric multiplication with doubled strictly off-diagonal products.
    base=[[Q(0)]*(2*d+1)for _ in range(2)];odd=[[Q(0)]*(2*d+1)for _ in range(2)]
    for k,p in enumerate(family):
        for i in range(d+1):
            for j in range(i,d+1):
                v=p[i]*p[j]*(1 if i==j else 2)
                base[0][i+j]+=v*(2 if k==0 else 1);base[1][i+j]+=v*k*k
                if k%2:odd[0][i+j]+=v;odd[1][i+j]+=v*k*k
    whole=int(2*b);a=2*b-whole;pr=[iv.power(lo,a),iv.power(hi,a)];vals=[]
    for deriv in range(2):
        result=(Q(0),Q(0))
        for j in range(2*d+1):
            rational=base[deriv][j]*(hi**(j+2)-lo**(j+2))/(j+2)
            interval=iv.sub(iv.mulq(pr[1],hi**(whole+j+2)),iv.mulq(pr[0],lo**(whole+j+2)))
            interval=iv.mulq(interval,-odd[deriv][j]/(2*b+j+2));result=iv.add(result,iv.add((rational,rational),interval))
        vals.append(iv.outward(result))
    return vals

def check(cert,xs,archives=True):
    assert cert['schema']=='full-modal-area-norm-v1'
    ds=[decode(x)for x in xs]if archives else[(list(map(Q,x['knots'])),[list(map(Q,c))for c in x['coefficients']],x['degree'])for x in xs]
    assert len(ds)==2 and ds[0][0]==ds[1][0]and ds[0][2]==ds[1][2]
    assert all(xs[0][k]==xs[1][k]for k in ['basis_beta','L','degree','knots'])
    b=Q(xs[0]['basis_beta']);assert cert['basis_beta']==str(b)and cert['L']==xs[0]['L'];ts=ds[0][0];d=ds[0][2];K=max(len(x[1])for x in ds)
    assert cert['degree']==d and cert['mode_count']==K
    assert cert['precision']=={'bits':iv.BITS,'log_terms':iv.NLOG,'exp_degree':iv.NEXP}
    spans=[j for j in range(d,len(ts)-d-1)if ts[j]<ts[j+1]];assert [c['span']for c in cert['cells']]==spans
    totals=[[(Q(0),Q(0)),(Q(0),Q(0))]for _ in range(3)];identities=0
    for cell,span in zip(cert['cells'],spans):
        A,B=ts[span:span+2];assert list(map(Q,cell['t_interval']))==[A,B]and list(map(Q,cell['z_interval']))==[1-B,1-A]
        assert len(cell['polynomials_z'])==2;families=[]
        for polynomials,(knots,coeffs,degree)in zip(cell['polynomials_z'],ds):
            assert len(polynomials)==K;polys=[list(map(Q,p))for p in polynomials]
            for k,p in enumerate(polys):
                assert len(p)==d+1
                for i in range(1,d+2):
                    t=A+(B-A)*Q(i,d+2);v=deboor(knots,coeffs[k],degree,t)if k<len(coeffs)else Q(0)
                    assert horner(p,1-t)==v,('identity',span,k,i);identities+=1
            families.append(polys)
        families.append([[a-b for a,b in zip(p,q)]for p,q in zip(*families)])
        expected=[]
        for i,f in enumerate(families):
            vals=normcell(f,1-B,1-A,b,d);expected.append(list(map(iv.serialize,vals)))
            for j in range(2):totals[i][j]=iv.add(totals[i][j],vals[j])
        assert expected==cell['integrals_I0_I1']
    totals=[[iv.outward((max(Q(0),v[0]),v[1]))for v in row]for row in totals]
    assert cert['norm_squared_over_pi_b_L2']==[[iv.serialize(v)for v in row]for row in totals]
    ratios=[]
    for j in range(2):
        D=totals[2][j];R=totals[1][j];assert R[0]>0 and D[1]>=D[0]>=0
        ratios.append(iv.serialize((iv.square_root(D[0]/R[1])[0],iv.square_root(D[1]/R[0])[1])))
    assert cert['relative_L2_to_second']==ratios
    return {'verdict':'CONFIRMED','identity_checks':identities,'cells':len(spans),'relative_L2_to_second':ratios,'relative_L2_float':[[float(Q(x))for x in a]for a in ratios],'norm_squared_over_pi_b_L2':cert['norm_squared_over_pi_b_L2']}
def main():
    path=Path(sys.argv[1]);t=time.monotonic();cert=json.loads(path.read_text());xs=[]
    for item in cert['inputs']:
        p=Path(item['path']);assert digest(p)==item['sha256'];xs.append(json.loads(p.read_text()))
    result=check(cert,xs);result.update(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t,certificate_sha256=digest(path),checker_sha256=digest(__file__))
    path.with_suffix('.check.json').write_text(json.dumps(result,indent=2)+'\n');print(result['utc'],'CHECKED',result['elapsed_seconds'],result['identity_checks'],result['relative_L2_float'],flush=True)
if __name__=='__main__':main()
