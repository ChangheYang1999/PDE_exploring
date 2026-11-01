"""Compare long-run log columns with the exact maximal-degree cycle."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,time,math,sys
sys.dont_write_bytecode=True
import sympy as s
from flint import fmpq,arb,ctx
ctx.prec=512


def compile_rational(text,var):
    num,den=s.fraction(s.cancel(s.sympify(text,locals={'k':var})))
    nc=[fmpq(str(x)) for x in s.Poly(num,var).all_coeffs()]
    dc=[fmpq(str(x)) for x in s.Poly(den,var).all_coeffs()]
    def at(k):
        def horner(c):
            out=fmpq(0)
            for x in c:out=out*k+x
            return out
        return horner(nc)/horner(dc)
    return at


def main():
    start=time.monotonic();root=Path('research/48_top_log_numerical_audit');(root/'sources').mkdir(parents=True,exist_ok=True);(root/'verification').mkdir(exist_ok=True)
    symbolic=json.loads(Path('research/44_maximal_log_chain/verification/symbolic_chain.json').read_text())
    var=s.symbols('k',integer=True,positive=True)
    fs={int(r):{int(j):compile_rational(v,var) for j,v in values.items()} for r,values in symbolic['normalized_density'].items()}
    b={2:fmpq(symbolic['b2']),3:fmpq(symbolic['b3'])}
    ratio=compile_rational(symbolic['successive_ratio'],var)
    for k in range(3,111):b[k+1]=b[k]*ratio(k)
    truth={}
    for n in range(7,331):
        k=(n-1)//3;r=n-3*k;m=2*k-2;profile={}
        for shift,fun in fs[r].items():
            f=m+shift;v=b[k]*fun(k)
            if f<0:f=-f;v=-v
            if f:profile[f]=profile.get(f,fmpq(0))+v
        norm=sum(map(abs,profile.values()),fmpq(0))
        truth[n]=arb(norm).log()/arb(10).log()
    files=[('../a4-lead/logs/log_d2_3_amp5_N320.jsonl','lead_float',5),
           ('../a4-lead/logs/ld_d2_3_amp5_N290.jsonl','lead_longdouble',5),
           ('../a4-num/logs/log_sin1_c3_p512.regen.jsonl','num_arb_regen',1),
           ('../a4-num/logs/log_sin1_c3_p512.jsonl','num_arb_running',1)]
    sources={};result=[];indexed={}
    for src,tag,amp in files:
        raw=Path(src).read_bytes();(root/'sources'/(tag+'.jsonl')).write_bytes(raw);sources[tag]={'path':src,'sha256':sha256(raw).hexdigest()}
        rows=[]
        for line in raw.splitlines():
            try:row=json.loads(line)
            except json.JSONDecodeError:continue
            n=row.get('n',0)
            if n not in truth:continue
            col=row.get('col')
            if col is not None:
                if not col[-1]:continue
                observed=math.log10(col[-1])-n*math.log10(amp)
                normcol=[math.log10(v)-n*math.log10(amp) if v>0 else -math.inf for v in col]
            else:
                normcol=row.get('log10_col_l1')
                if not normcol:continue
                observed=normcol[-1]
            degree=len(normcol)-1
            expected_degree=max(0,(n-1)//3-1)
            assert degree==expected_degree,(tag,n,degree,expected_degree)
            error=observed-float(truth[n])
            bump=max(((lg+math.lgamma(k+1)/math.log(10)-normcol[0],k) for k,lg in enumerate(normcol) if k>0 and math.isfinite(lg)),default=(-math.inf,0))
            rows.append({'n':n,'top_degree':degree,'observed_log10_top_l1':observed,
                         'exact_log10_top_l1_ball':str(truth[n]),'log10_discrepancy':error,
                         'approx_relative_discrepancy':math.expm1(error*math.log(10)),
                         'max_factorial_relative_log10':bump[0],'max_factorial_relative_index':bump[1]})
            indexed.setdefault(tag,{})[n]=normcol
        if rows:
            maxrow=max(rows,key=lambda r:abs(r['approx_relative_discrepancy']))
            result.append({'tag':tag,'checked_orders':len(rows),'last_n':rows[-1]['n'],
                           'max_abs_relative_discrepancy':abs(maxrow['approx_relative_discrepancy']),
                           'max_error_n':maxrow['n'],'checks':rows})
    cross=[]
    if 'lead_float' in indexed and 'lead_longdouble' in indexed:
        for n in sorted(indexed['lead_float'].keys() & indexed['lead_longdouble'].keys()):
            a=indexed['lead_float'][n];bcol=indexed['lead_longdouble'][n]
            if n%10:continue
            diffs=[abs(x-y) for x,y in zip(a,bcol) if math.isfinite(x) and math.isfinite(y)]
            cross.append({'n':n,'max_absolute_log10_column_discrepancy':max(diffs),
                          'at_index':diffs.index(max(diffs))})
    out={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
         'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'sources':sources,'datasets':result,
         'float_longdouble_comparison':cross,'actual_elapsed_s':time.monotonic()-start,
         'scope':'Column-norm comparisons only. The exact maximal-degree cycle is not a proof of correctness of other log columns.'}
    (root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'datasets':[{k:v for k,v in row.items() if k!='checks'} for row in result],
                      'latest_cross':cross[-3:],'actual_elapsed_s':out['actual_elapsed_s']}),flush=True)

if __name__=='__main__':main()
