"""Exact regional assembly only. No independent-middle acceptance is implemented."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
from flint import arb, ctx
from mpmath import iv

BASE = Path(__file__).resolve().parents[3]
DEST = BASE/'research/global_residual_assembly/evidence'
K = F(1615536043799051,9007199254740992)
L = F(8614738245908811,1125899906842624)
D = str(F(1,2)-K)
ROOTS = {
 'research/inner_cells/evidence/verdict.json':'0e20d17cdf606d10a9dde40d7d3ca511e509321947aa97a97838c7a84ba70b21',
 'research/outer_cells/evidence/verdict.json':'9a3d6cdce158574bd532f44c27b83aecb5007c985bdefa35e4f95e4f81dac9d6',
 'research/middle_residual/evidence/primary_acceptance.json':'92a82a09a804845c0af399a1034ba07fc92afd42b319baf9883cdc541528e745',
}

def require(condition, detail):
    if not condition:
        raise ValueError(detail)

def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream,'sha256').hexdigest()

def strict_object(pairs):
    result = {}
    for k,v in pairs:
        require(k not in result, 'duplicate JSON key '+k)
        result[k] = v
    return result

def bad_constant(text):
    raise ValueError('nonfinite JSON constant '+text)

def loads(text):
    return json.loads(text, object_pairs_hook=strict_object, parse_constant=bad_constant)

class Inputs:
    def __init__(self):
        self.pins = {}
    def pin(self, name, expected=None):
        path = BASE/name
        require(path.resolve().is_relative_to(BASE), 'input outside lane')
        actual = sha(path)
        if expected is not None:
            require(actual == expected, 'hash mismatch '+name)
        if name in self.pins:
            require(self.pins[name] == actual, 'input changed '+name)
        self.pins[name] = actual
        return actual
    def read(self, name):
        self.pin(name)
        return loads((BASE/name).read_text())
    def mapping(self, pins):
        for name, expected in pins.items():
            self.pin(name, expected)
    def stable(self):
        for name, expected in self.pins.items():
            require(sha(BASE/name)==expected, 'input changed '+name)

def rational_hex(text):
    # float.fromhex exactly imports a finite binary64 hex representation.
    return F.from_float(float.fromhex(text))

def ceiling(value, digits=12):
    require(value >= 0, 'negative ceiling input')
    scale = 10**digits
    n = (value.numerator*scale)//value.denominator + 1
    bound = F(n,scale)
    require(value < bound, 'ceiling not strict')
    return {'strict_upper_exact':str(bound),
            'strict_upper_decimal':str(n//scale)+'.'+str(n%scale).zfill(digits)}

def dyadic(x):
    m,e=x.man_exp()
    return F(int(m))*F(2)**int(e)

def arb_ends(x):
    require(x.is_finite(), 'nonfinite Arb result')
    a,b=dyadic(x.lower()),dyadic(x.upper())
    require(0<=a<=b, 'invalid Arb interval')
    return a,b

def iv_ends(x):
    require(not iv.isnan(x) and not iv.isinf(x), 'nonfinite iv result')
    vals=[]
    for sign,m,e,bc in x._mpi_:
        require(bc>=0, 'nonfinite mpf endpoint')
        vals.append((-1 if sign else 1)*F(int(m))*F(2)**int(e))
    a,b=vals
    require(0<=a<=b, 'invalid iv interval')
    return a,b

def sqrt_three_methods(value, digits=12):
    require(value>=0, 'negative squared norm')
    ctx.prec=512;iv.dps=160
    a=arb_ends((arb(value.numerator)/value.denominator).sqrt())
    b=iv_ends(iv.sqrt(iv.mpf(value.numerator)/value.denominator))
    require(a[0]*a[0]<=value<=a[1]*a[1], 'Arb enclosure fails exact square comparison')
    require(b[0]*b[0]<=value<=b[1]*b[1], 'iv enclosure fails exact square comparison')
    require(max(a[0],b[0])<=min(a[1],b[1]), 'disjoint sqrt enclosures')
    scale=10**digits
    q=isqrt((value.numerator*scale*scale)//value.denominator)
    low,high=F(q,scale),F(q+1,scale)
    require(low*low<=value<high*high, 'integer sqrt ceiling failure')
    require(max(a[1],b[1])<high, 'decimal ceiling below analytic upper endpoint')
    return {'input_squared_exact':str(value),
            'arb512':list(map(str,a)), 'iv160':list(map(str,b)),
            'integer_lower_exact':str(low), 'strict_upper_exact':str(high),
            'strict_upper_decimal':str((q+1)//scale)+'.'+str((q+1)%scale).zfill(digits)}

def contiguous(intervals, left, right):
    require(len(intervals)>0, 'empty partition')
    cursor=left
    for a,b in intervals:
        require(a==cursor and a<b, 'gap, overlap, or reversed interval')
        cursor=b
    require(cursor==right, 'wrong final partition endpoint')

def main():
    start=time.monotonic(); require(sys.flags.optimize==0, 'optimization forbidden')
    inputs=Inputs(); require(0<K<F(1,2) and L>0, 'weight parameters')
    first=inputs.read('research/global_residual_assembly/evidence/first.json')
    proof='research/global_residual_assembly/PROOF.md'
    inputs.pin(proof,'9655732d019a97615f60da1e25766736e2f3302b72e43624395db1dc094199bd')
    inputs.pin(str(Path(__file__).relative_to(BASE)))
    roots=[]
    for name,expected in ROOTS.items():
        inputs.pin(name,expected);v=inputs.read(name)
        require(v['status']==('CONFIRMED_PRIMARY_ASSEMBLY' if 'primary_acceptance' in name else 'CONFIRMED'), 'unaccepted region')
        inputs.mapping(v['files']);roots.append(v)
    vin,vout,vmid=roots
    require([v['cells'] for v in roots]==[54,89,7809], 'regional counts')
    # These are explicitly cited dependency verdicts, not a recursive audit of every JSON file.
    for name in ['inner_majorant','outer_majorant','outer_leading_cancellation']:
        vp='research/'+name+'/evidence/verdict.json';v=inputs.read(vp)
        require(v['status']=='CONFIRMED', 'unaccepted analytic tail dependency')
        inputs.mapping(v['files'])
    raw=inputs.read('data_exact/modal_v2.json')
    require(raw['degree']==7 and raw['arrays']['knots']['shape']==[1573], 'raw spline convention')
    require(rational_hex(raw['scalars_hex']['k'])==K and rational_hex(raw['scalars_hex']['L'])==L, 'raw scalars')
    knots=list(map(rational_hex,raw['arrays']['knots']['hex']))
    require(len(knots)==1573 and all(a<=b for a,b in zip(knots,knots[1:])), 'invalid raw knots')
    parents=[(a,b) for a,b in zip(knots,knots[1:]) if a<b]
    require(len(parents)==1558, 'raw parent count')
    ta,tb=parents[0][0],parents[-1][1]
    innerco=inputs.read('research/inner_majorant/evidence/exact_inner_coefficients.json')
    outerco=inputs.read('research/outer_majorant/evidence/exact_outer_coefficients.json')
    modalhash=inputs.pins['data_exact/modal_v2.json']
    require(innerco['input_sha256']==outerco['input_sha256']==modalhash, 'different modal inputs')
    require(F(innerco['ta_exact'])==ta and F(outerco['tb_exact'])==tb, 'different region joins')
    squares={};bounds={};regions={}
    for name,count,v,side in [('inner',54,vin,'inner'),('outer',89,vout,'exterior')]:
        prefix='research/'+name+'_cells/evidence/full_q16'
        man=inputs.read(prefix+'_manifest.json');s=inputs.read(prefix+'_summary.json');a=inputs.read(prefix+'_audit.json')
        inputs.mapping(man['pins']);inputs.mapping(s['pins']);inputs.mapping(a['pins'])
        require(man['status']=='PREPARED_EXACT_PARTITION' and man['Q']==16, 'regional manifest')
        require(s['status']=='COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT' and a['status']=='PASS_COMPLETE_REQUIRES_FINAL_REVIEW', 'regional audit status')
        require(s['cells_complete']==s['cells_required']==a['cells_checked']==len(man['cells'])==count, 'regional incomplete')
        intervals=[tuple(map(F,row)) for row in man['cells']]
        contiguous(intervals,F(-7) if name=='inner' else F(0),F(0) if name=='inner' else F(17))
        stream=prefix+'_cells.jsonl';streamsha=inputs.pin(stream)
        require(s['cell_file_sha256']==a['cell_file_sha256']==streamsha, 'regional stream binding')
        require(s['manifest_sha256']==a['manifest_sha256']==inputs.pins[prefix+'_manifest.json'], 'regional manifest binding')
        require(a['summary_sha256']==inputs.pins[prefix+'_summary.json'], 'regional summary binding')
        rowcount=0;E=F(0)
        with (BASE/stream).open() as handle:
            for ci,line in enumerate(handle):
                row=loads(line);require(row['cell']==ci and ci<count, 'regional cell index')
                require((F(row['left_exact']),F(row['right_exact']))==intervals[ci], 'regional row coverage')
                val=F(row['joint_upper_exact']['L2_squared']);require(val>=0, 'negative regional L2')
                E+=val;rowcount+=1
        require(rowcount==count, 'regional row count')
        require(E==F(s['finite_'+side+'_L2_squared_upper_exact']), 'regional exact integral sum')
        suffix='_tail.json' if name=='inner' else '_tail_l2.json'
        tail=inputs.read(prefix+suffix)
        require(F(tail['T_exact'])==(7 if name=='inner' else 17), 'tail join gap')
        require(tail['status']=='PASS_REQUIRES_SOURCE_REVIEW', 'tail status')
        if name=='inner':
            require(F(tail['ta_exact'])==ta and F(tail['k_exact'])==K and F(tail['L_exact'])==L, 'inner tail scalars')
            require(F(tail['B5_upper_exact'])>0 and F(tail['base_majorant_T_exact'])<=7, 'origin hypothesis')
            Etail=F(tail['values']['L2_squared']['upper_exact'])
            require(Etail==F(s['tail_L2_squared_upper_exact']), 'inner tail norm mismatch')
            require(s['tail_sha256']==a['tail_sha256']==inputs.pins[prefix+suffix], 'inner tail binding')
        else:
            upper=F(tail['published_upper_exact']);require(upper>=0, 'negative outer tail norm')
            require(upper==F(s['tail_L2_upper_exact']), 'outer tail norm mismatch');Etail=upper*upper
            require(s['tail_l2_sha256']==a['tail_l2_sha256']==inputs.pins[prefix+suffix], 'outer tail binding')
        E+=Etail
        require(E==F(s['full_'+side+'_L2_squared_upper_exact'])==F(a['full_'+side+'_L2_squared_upper_exact'])==F(v['L2_join_squared_upper_exact']), 'full regional squared norm mismatch')
        require(E<F(v['public_bounds']['L2']['strict_upper_decimal'])**2, 'published regional norm ceiling')
        squares[name]=E;bounds[name]={}
        for key,rec in v['public_bounds'].items():
            if key=='L2':continue
            value=F(rec['authoritative_upper_exact']);require(0<=value<F(rec['strict_upper_decimal']), 'published regional sup ceiling')
            bounds[name][key]=value
        require(bounds[name]['weighted_0']==bounds[name]['W_over_m'], 'zero weight identity')
        regions[name]={'cells':count,'tau_first':str(intervals[0][0]),'tau_last':str(intervals[-1][1]),'full_tail':True,'squared_norm_exact':str(E),'region_join_log_radius_exact':str(ta if name=='inner' else tb)}
    prefix='research/middle_residual/evidence/'
    partition=inputs.read(prefix+'partition_exact.json');s=inputs.read(prefix+'full_q16_summary.json');a=inputs.read(prefix+'full_q16_output_audit.json')
    require(partition['cells']==7809 and len(partition['spans'])==1558, 'middle partition counts')
    require(partition['input_sha256']==modalhash, 'middle input')
    expected=[]
    for j,(span,(p,q)) in enumerate(zip(partition['spans'],parents)):
        require(span['span']==j and span['first_cell']==len(expected), 'parent indexing')
        require(F(span['a_exact'])==p and F(span['b_exact'])==q, 'raw parent mismatch')
        n=span['count'];require(type(n) is int and n>0, 'subdivision count')
        expected.extend((j,p+(q-p)*i/n,p+(q-p)*(i+1)/n) for i in range(n))
    require(len(expected)==7809, 'middle child count')
    contiguous([(p,q) for _,p,q in expected],ta,tb)
    stream=prefix+'full_q16_cells.jsonl';streamsha=inputs.pin(stream)
    require(s['status']=='COMPUTED_REQUIRES_INDEPENDENT_OUTPUT_AUDIT' and s['source_footer_read'] is True, 'middle source footer status')
    require(s['cells_complete']==s['cells_required']==a['cells_audited']==7809 and a['status']=='PASS', 'middle complete audit')
    require(s['output_sha256']==a['completed_output_sha256']==streamsha, 'middle output binding')
    require(a['summary_sha256']==inputs.pins[prefix+'full_q16_summary.json'], 'middle summary binding')
    km=inputs.read(prefix+'knot_manifest.json');ka=inputs.read(prefix+'knot_audit.json');archive=prefix+'original_knots.jsonl.gz';inputs.pin(archive)
    require(ka['status']=='PASS' and ka['footer_read'] is True and ka['spans']==1558 and ka['cells']==7809, 'archive completion audit')
    require(ka['archive_sha256']==km['output_sha256']==s['input_sha256']==inputs.pins[archive], 'archive hash binding')
    require(ka['manifest_sha256']==inputs.pins[prefix+'knot_manifest.json'] and ka['partition_sha256']==inputs.pins[prefix+'partition_exact.json'], 'archive metadata binding')
    bkeys=list(vmid['public_strict_bounds']);maxima={key:(F(-1),None) for key in bkeys};rowcount=0
    with (BASE/stream).open() as handle:
        head=loads(next(handle));require(head==s['run_header']==a['run_header'], 'middle header binding')
        require(head['type']=='header' and head['cells_required']==7809 and head['degree']==16, 'middle header')
        require(F(head['k_exact'])==K and F(head['L_exact'])==L and head['modal_input_sha256']==modalhash, 'middle scalar binding')
        for ci,line in enumerate(handle):
            row=loads(line);require(ci<7809 and row['type']=='cell' and row['cell']==ci, 'middle row index')
            j,p,q=expected[ci];require(row['parent_span']==j and (F(row['left_exact']),F(row['right_exact']))==(p,q), 'middle row interval')
            for key in bkeys:
                value=F(row[key]);require(value>=0, 'negative middle bound')
                if value>maxima[key][0]:maxima[key]=(value,ci)
            rowcount+=1
    require(rowcount==7809, 'middle row count')
    for key,(value,ci) in maxima.items():
        require(value==F(a['maxima'][key]['upper']) and ci==a['maxima'][key]['cell'], 'middle audit maximum')
        require(value==F(s['maxima'][key]['bound_exact']) and ci==s['maxima'][key]['cell'], 'middle summary maximum')
        require(value<F(vmid['public_strict_bounds'][key]), 'middle public bound ceiling')
    squares['middle']=F(a['L2_squared_upper_exact']);require(0<squares['middle']<F(vmid['L2_strict_upper_exact'])**2, 'middle L2 ceiling')
    bounds['middle']={'W':maxima['W_upper_exact'][0], 'W_over_m':maxima['W_over_m_upper_exact'][0], 'weighted_0':maxima['W_over_m_upper_exact'][0], 'weighted_1/2':maxima['Wm_times_one_plus_u_power_half_upper_exact'][0], 'weighted_'+D:maxima['Wm_times_one_plus_u_power_half_minus_k_upper_exact'][0]}
    regions['middle']={'cells':7809,'parents':1558,'first_log_radius_exact':str(ta),'last_log_radius_exact':str(tb),'source_footer_bound_to_accepted_audit':True,'squared_norm_exact':str(squares['middle']),'evidence_level':'PRIMARY_ONLY'}
    outer=inputs.read('research/outer_majorant/evidence/outer_result.json')
    require(F(outer['scalars_exact']['k'])==K and F(outer['scalars_exact']['L'])==L and F(outer['tb_exact'])==tb, 'outer analytic scalars')
    nterms=0;rates=[]
    for rec in outer['majorant']:
        gamma=F(rec['gamma_exact']);require(gamma<=2*K-1, 'nondecaying exterior rate');rates.append(gamma)
        for power,coeff in enumerate(rec['coefficients']):
            require(0<=F(coeff['lower_exact'])<=F(coeff['upper_exact']), 'negative exterior coefficient')
            for delta in [F(0),F(1,2),F(1,2)-K]:require(gamma-K+delta<0, 'weighted exterior nondecay')
            nterms+=1
    require(len(rates)==1864 and nterms==3508, 'exterior majorant counts')
    global_bounds={}
    for key in bounds['middle']:
        values={name:rec[key] for name,rec in bounds.items()};owner=max(values,key=values.get);value=values[owner]
        global_bounds[key]={'authoritative_upper_exact':str(value),'largest_upper_bound_region':owner,'regional_upper_exact':{name:str(v) for name,v in values.items()},**ceiling(value)}
    total=sum(squares.values(),F(0));root=sqrt_three_methods(total)
    inputs.stable()
    result={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_PRIMARY_REGIONAL_ASSEMBLY_REQUIRES_REVIEW','k_exact':str(K),'L_exact':str(L),'joins_exact':[str(ta),str(tb)],'regions':regions,'global_suprema':global_bounds,'global_N2':root,'decay_checks':{'exponent_groups':len(rates),'nonnegative_monomials':nterms,'largest_exponent_exact':str(max(rates))},'files':inputs.pins,'seconds':time.monotonic()-start,'scope':'Exact aggregation of accepted inner45, outer43 and PRIMARY middle31 bounds. No regional coefficient recomputation or independent topic46 application. Canonical archive closure and full PDE endpoint remain OPEN.'}
    (DEST/'primary_assembly.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'utc':result['utc'],'status':result['status'],'pins':len(inputs.pins),'suprema':{k:v['strict_upper_decimal'] for k,v in global_bounds.items()},'N2':root['strict_upper_decimal'],'seconds':result['seconds']}),flush=True)

if __name__=='__main__':
    main()
