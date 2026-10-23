#!/usr/bin/env python3
"""Hash-checked aggregation of completed whole-plane norm quadratures."""
import json,hashlib
from pathlib import Path
from decimal import Decimal,localcontext
from datetime import datetime,timezone
ROOT=Path('evidence/q_compact_derivative_norms')
KEYS=['rho_norm_squared','residual_norm_squared','rho_norm','residual_norm','eta']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def relative(a,b):
    a,b=Decimal(a),Decimal(b)
    return str(abs(a-b)/max(abs(a),abs(b))) if a or b else '0'

def main():
    result={'utc':datetime.now(timezone.utc).isoformat(),'states':[],
            'scope':'Numerical full-plane compact radial quadrature using positive exact finite angular identities and an independent canonical inverse. Resolution and precision agreement are empirical, not interval bounds. Finite-state derivative ratios give no limiting regularity theorem. Shell contributions use the global quadrature nodes and do not carry independent shell error bounds.'}
    lines=['# Independent canonical whole-plane derivative norms','',result['utc'],'',result['scope'],'',
           'The norm includes every ordered Cartesian derivative: sum_j binom(k,j) |partial_x^j partial_y^(k-j) f|^2. Both absolute norms and their scale-invariant ratio are reported.','',
           '| State | k | Quadrature nodes | ||D^k rho||_2 | ||D^k R||_2 | eta_k | Node-count relative change in eta |',
           '|---|---:|---:|---:|---:|---:|---:|']
    with localcontext() as ctx:
        ctx.prec=90
        for folder in sorted(ROOT.iterdir()):
            if not folder.is_dir():continue
            complete=[];pending=[]
            for p in folder.glob('nodes*_dps*.json'):
                r=json.loads(p.read_text())
                if r['status']!='COMPUTED':pending.append({'path':str(p),'status':r['status'],'completed_nodes':len(r['rows']),'nodes':r['nodes']});continue
                assert len(r['rows'])==r['nodes']
                assert sha(Path(r['input']))==r['input_sha256']
                raw=json.loads(Path(r['input']).read_text());assert raw['source_sha256']==r['source_sha256']
                complete.append((p,r))
            if not complete:continue
            complete.sort(key=lambda v:(v[1]['nodes'],v[1]['dps']))
            assert len({r['source_sha256'] for p,r in complete})==1
            state={'tag':folder.name,'source_sha256':complete[0][1]['source_sha256'],'input':complete[0][1]['input'],'pending':pending,
                   'quadratures':[{k:r[k] for k in ['nodes','dps','node_digits','inverse_working_dps','totals','sampled_radii','shells']}|{'path':str(p),'sha256':sha(p),'finished_utc':r['finished_utc']} for p,r in complete],
                   'node_comparisons':[],'precision_comparisons':[]}
            by_dps={}
            for p,r in complete:by_dps.setdefault(r['dps'],[]).append(r)
            for dps,rr in by_dps.items():
                for low,high in zip(rr,rr[1:]):
                    if low['nodes']==high['nodes']:continue
                    state['node_comparisons'].append({'dps':dps,'low_nodes':low['nodes'],'high_nodes':high['nodes'],
                        'relative_differences':{k:{f:relative(low['totals'][k][f],high['totals'][k][f]) for f in KEYS} for k in low['totals']}})
            for i,(_,low) in enumerate(complete):
                for _,high in complete[i+1:]:
                    if low['nodes']==high['nodes'] and low['dps']!=high['dps']:
                        state['precision_comparisons'].append({'nodes':low['nodes'],'low_dps':low['dps'],'high_dps':high['dps'],
                            'relative_differences':{k:{f:relative(low['totals'][k][f],high['totals'][k][f]) for f in KEYS} for k in low['totals']}})
            selected=complete[-1][1]
            comp=next((v for v in reversed(state['node_comparisons']) if v['dps']==selected['dps'] and v['high_nodes']==selected['nodes']),None)
            for k,row in selected['totals'].items():
                fmt=lambda v:format(Decimal(v),'.10g')
                diff=fmt(comp['relative_differences'][k]['eta']) if comp else 'pending'
                lines.append(f"| {folder.name} | {k} | {selected['nodes']} | {fmt(row['rho_norm'])} | {fmt(row['residual_norm'])} | {fmt(row['eta'])} | {diff} |")
            state['selected_nodes']=selected['nodes'];state['selected_dps']=selected['dps'];state['selected_totals']=selected['totals']
            result['states'].append(state)
        lines+=['','Full JSON contains source hashes, absolute squared norms, all completed node counts, precision settings, extreme sampled radii, and diagnostic shell contributions. The displayed row uses the largest completed node count, then the highest target precision at that count. Pending comparisons are not convergence results.','',
                'The earlier broad log-radius pilot was underresolved and is retained only as historical evidence. This table concerns the smooth exact finite Q density with its canonical inverse; it does not integrate the producer\'s separate stream interpolant.','']
        (ROOT/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n');(ROOT/'SUMMARY.md').write_text('\n'.join(lines))
        print(json.dumps({'utc':result['utc'],'states':[(s['tag'],s['selected_nodes'],len(s['node_comparisons'])) for s in result['states']]}))
if __name__=='__main__':main()
