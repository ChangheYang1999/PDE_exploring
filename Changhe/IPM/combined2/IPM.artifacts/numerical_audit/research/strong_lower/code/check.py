"""Independent Cartesian point and Holder-pair lower bounds; no producer evaluation."""
from math import comb,factorial
from pathlib import Path
import argparse,importlib.util,json,time
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strong_lower'
spec=importlib.util.spec_from_file_location('own_jets',ROOT/'research/cartesian_jets/code/point_jets.py')
jets=importlib.util.module_from_spec(spec);spec.loader.exec_module(jets)


def component(p,order,ys):
    xs=order-ys
    return p[xs+jets.STRIDE*ys]*factorial(xs)*factorial(ys)


def norm(p,order):
    return sum((comb(order,b)*component(p,order,b)**2 for b in range(order+1)),arb(0)).sqrt()


def positive_record(v):
    assert v>0 and v.rel_accuracy_bits()>=128,v
    return jets.record(v)


def tensor_fixture():
    p=jets.jet({(1,1):1});assert (norm(p,2)**2).contains(arb(2))
    p=jets.jet({(2,1):1});assert (norm(p,3)**2).contains(arb(12))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--points',default='research/strong_lower/data/baseline_points_v01.json')
    parser.add_argument('--bits',type=int,default=1024);parser.add_argument('--tag',required=True)
    args=parser.parse_args();ctx.prec=args.bits;jets.calibrate();tensor_fixture()
    relative=Path(args.points);assert not relative.is_absolute() and '..' not in relative.parts
    assert args.tag and all(c.isalnum() or c in '_-' for c in args.tag)
    inputs=ROOT/relative;request=json.loads(inputs.read_text());source=json.loads(jets.CANONICAL.read_text())
    assert request['source_sha256']==source['source_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
    start=jets.stamp();tick=time.monotonic();c=Q(source['cl_exact']);raw=[]
    for point in request['points']:
        x,y=Q(point['x']),Q(point['y']);C,powers=jets.potential(source,x,y)
        _,_,_,F=jets.residual(C,x,y,c);raw.append((x,y,F,powers))
        print(jets.stamp(),'point assembled',point['name'],flush=True)
    weighted={};rows=[]
    for params in request['parameters']:
        alpha,delta,sigma=map(Q,[params['alpha'],params['delta'],params['sigma']])
        assert 0<alpha<1 and delta>alpha/(2*c-2)
        degree=1+alpha+delta;k=int(degree.numerator//degree.denominator);beta=degree-k
        assert 0<beta<1 and k<=2 and sigma<=5-4/c
        if sigma not in weighted:
            weighted[sigma]=[jets.weighted(F,powers,x*x+y*y,sigma) for x,y,F,powers in raw]
        values=weighted[sigma];point_rows=[];lower_s=[Q(0)]*(k+1)
        for index,g in enumerate(values):
            records={str(j):positive_record(norm(g,j)) for j in range(k+1)}
            for j in range(k+1):lower_s[j]=max(lower_s[j],Q(records[str(j)]['lower_exact']))
            point_rows.append({'index':index,'name':request['points'][index]['name'],'norms':records})
        pair_rows=[];lower_h=Q(0);best_pair=None
        for i in range(len(raw)):
            for h in range(i+1,len(raw)):
                dx,dy=raw[i][0]-raw[h][0],raw[i][1]-raw[h][1];distance2=dx*dx+dy*dy
                assert distance2>0
                numerator=norm(values[i]-values[h],k)
                quotient=numerator/(arb(distance2)**arb(beta/2))
                record=positive_record(quotient);lower=Q(record['lower_exact'])
                if lower>lower_h:lower_h=lower;best_pair=[i,h]
                pair_rows.append({'indices':[i,h],'squared_distance_exact':str(distance2),'quotient':record})
        row={**params,'order_exact':str(degree),'top_derivative':k,'holder_beta_exact':str(beta),
          'point_norms':point_rows,'pair_quotients':pair_rows,'S_lower_exact':{str(j):str(v) for j,v in enumerate(lower_s)},
          'Stop_lower_exact':str(lower_h),'best_pair':best_pair,'SF_lower_exact':str(sum(lower_s,Q(0))+lower_h)}
        rows.append(row)
        print(jets.stamp(),'parameters',params,'SF lower',arb(Q(row['SF_lower_exact'])).str(25),flush=True)
    result={'started_utc':start,'finished_utc':jets.stamp(),'elapsed_seconds':time.monotonic()-tick,
        'source_sha256':source['source_sha256'],'canonical_sha256':jets.digest(jets.CANONICAL),
        'point_request':str(relative),'point_request_sha256':jets.digest(inputs),'precision_bits':args.bits,
        'code_sha256':jets.digest(__file__),'cartesian_code_sha256':jets.digest(jets.__file__),
        'proof_sha256':jets.digest(BASE/'PROOF.md'),'points':request['points'],'rows':rows,
        'scope':'Outward point and pair lower endpoints for the registered global strong norm. No upper or inverse estimate.'}
    with (BASE/'verification'/f'{args.tag}.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')


if __name__=='__main__':main()
